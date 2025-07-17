/**
 * @author Peter Hansen
 * @author Daniel Wilken
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Game.Controller
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.events.TouchEvent;
	import flash.ui.Keyboard;
	import flash.ui.Multitouch;
	import flash.utils.Timer;
	
	import de.p3337.zzznake.Enum.Direction;
	import de.p3337.zzznake.Enum.GameState;
	import de.p3337.zzznake.Enum.SoundFile;
	import de.p3337.zzznake.Game.GameEvent;
	import de.p3337.zzznake.Game.Model.GameModel;
	import de.p3337.zzznake.Game.View.GameView;
	import de.p3337.zzznake.Main.Zzznake;
	import de.p3337.zzznake.Menu.Command.ShowHighscoreNewEntryCommand;
	import de.p3337.zzznake.Menu.Command.ShowMenuCommand;
	import de.p3337.zzznake.Sound.Jukebox;
	import de.p3337.zzznake.Util.Helper;
	
	/**
	 * The GameController handles the user interactions like touch or key events to control the snake.
	 * Furthermore is handles the logic timer to continuesly move the snake forward and check for collisions.
	 */
	public class GameController extends EventDispatcher {
		
		private const SPEED_START_VALUE:uint = 480;
		private const SPEED_STEP_VALUE:uint = 30;
		private const SPEED_MINIMUM_VALUE:uint = 30;
		
		private var model:GameModel;
		private var view:GameView;
		private var logicTimer:Timer;
		
		public function GameController(model:GameModel) {
			this.model = model;
			
			this.view = new GameView(model); 
			
			this.view.backButton.addEventListener(MouseEvent.CLICK, function():void {
				Zzznake.getInstance().ExecuteCommand(new ShowMenuCommand());
			});
		}
		
		public function getView():Sprite {
			return view.view;
		}
		
		public function reset():void {
			model.reset();
		}
		
		public function startNewGame():void {
			model.addEventListener(GameEvent.GAME_START, onGameStart);
			
			Zzznake.getInstance().stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
			Zzznake.getInstance().stage.addEventListener(KeyboardEvent.KEY_UP, onKeyUp);
			
			if(Multitouch.supportsTouchEvents) {
				this.view.view.addEventListener(TouchEvent.TOUCH_TAP, onTapHandler);
			}
		}
		
		private function onGameStart(event:GameEvent):void {
			model.gameState = GameState.STARTED;
			model.removeEventListener(GameEvent.GAME_START, onGameStart);
			
			model.addEventListener(GameEvent.GAME_OVER, onGameOver);
			model.addEventListener(GameEvent.SNACK_CRUNCHED, onSnackCrunched);
			model.addEventListener(GameEvent.GAME_UPDATE, onGameUpdate);
			
			logicTimer = new Timer(this.SPEED_START_VALUE);
			logicTimer.addEventListener(TimerEvent.TIMER, onLogicTimer);
			
			logicTimer.start();
			view.update();
		}
		
		protected function onGameUpdate(event:Event):void {
			view.update();
		}
		
		protected function onLogicTimer(event:TimerEvent):void {
			updateDirection();
			model.snakeModel.moveForward();
			model.checkCollisions();
		}
		
		private function updateDirection():void {
			var lastDiection:Direction = model.snakeModel.head.direction;
			if(model.keys[Keyboard.RIGHT] && lastDiection !== Direction.LEFT) {
				model.snakeModel.head.changeDirection(Direction.RIGHT);
			} else if(model.keys[Keyboard.LEFT] && lastDiection !== Direction.RIGHT) {
				model.snakeModel.head.changeDirection(Direction.LEFT);
			} else if(model.keys[Keyboard.UP] && lastDiection !== Direction.DOWN) {
				model.snakeModel.head.changeDirection(Direction.UP);
			} else if(model.keys[Keyboard.DOWN] && lastDiection !== Direction.UP) {
				model.snakeModel.head.changeDirection(Direction.DOWN);
			}
		}
		
		protected function onSnackCrunched(event:GameEvent):void {
			Jukebox.getInstance().play(SoundFile.CRUNCH_FOOD);
			
			if(model.snakeModel.snackCrunchCount % 3 === 0) {
				model.incrementMovementSpeed();
				var newDelay:uint = this.SPEED_START_VALUE - (model.movementSpeed * this.SPEED_STEP_VALUE);
				if((logicTimer.delay >= this.SPEED_MINIMUM_VALUE + SPEED_STEP_VALUE) && newDelay < logicTimer.delay) {
					logicTimer.delay = newDelay;
				}
			}
		}
		
		protected function onGameOver(event:GameEvent):void {
			Jukebox.getInstance().play(SoundFile.GAME_OVER);
			
			Zzznake.getInstance().ExecuteCommand(new ShowHighscoreNewEntryCommand(
				model.snakeModel.fieldsMoved, model.snakeModel.snackCrunchCount, model.movementSpeed));
			
			removeGame();
		}
		
		public function removeGame():void {
			if(logicTimer) {
				logicTimer.reset();
				logicTimer.delay = this.SPEED_START_VALUE;
			}
			
			reset();
			
			var zzznake:Zzznake = Zzznake.getInstance();
			if(zzznake.stage.hasEventListener(KeyboardEvent.KEY_DOWN)) {
				zzznake.stage.removeEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
				zzznake.stage.removeEventListener(KeyboardEvent.KEY_UP, onKeyUp);
			}
			if(this.view.view.hasEventListener(TouchEvent.TOUCH_TAP)) {
				this.view.view.removeEventListener(TouchEvent.TOUCH_TAP, onTapHandler);
			}
			
			if(model.hasEventListener(GameEvent.SNACK_CRUNCHED)) {
				model.removeEventListener(GameEvent.SNACK_CRUNCHED, onSnackCrunched);
			}
			
			if(model.hasEventListener(GameEvent.GAME_START)) {
				model.removeEventListener(GameEvent.GAME_START, onGameStart);
			}
			
			if(model.hasEventListener(GameEvent.GAME_UPDATE)) {
				model.removeEventListener(GameEvent.GAME_UPDATE, onGameUpdate);
			}
			
			model.gameState = GameState.ENDED;
		}
		
		private function onTapHandler(evt:TouchEvent): void {
			var headCenterPadding:Number = Zzznake.ZZZNAKE_PADDING + (GameModel.SQUARE_SIZE / 2);
			var headX:uint = (model.snakeModel.head.getPosition().x * GameModel.SQUARE_SIZE) + headCenterPadding;
			var headY:uint = (model.snakeModel.head.getPosition().y * GameModel.SQUARE_SIZE) + headCenterPadding;
			
			var angle:Number = Helper.rad2Deg(Math.atan2(evt.stageY - headY, headX - evt.stageX));
			
			model.keys = new Array();
			if(angle <= 45 || angle > 315) {
				model.keys[37] = true;
			} else if(angle > 45 && angle <= 135) {
				model.keys[40] = true;
			} else if(angle > 135 && angle < 225) {
				model.keys[39] = true;
			} else {
				model.keys[38] = true;
			}
			
			if(model.gameState === GameState.INITIALIZED || model.gameState === GameState.ENDED) {
				model.dispatchEvent(new GameEvent(GameEvent.GAME_START));
			}
		}
		
		private function onKeyDown(e:KeyboardEvent):void {
			model.keys[e.keyCode] = true;
			if(model.gameState === GameState.INITIALIZED || model.gameState === GameState.ENDED) {
				model.dispatchEvent(new GameEvent(GameEvent.GAME_START));
			}
		}
		
		private function onKeyUp(e:KeyboardEvent):void {
			model.keys[e.keyCode] = false;
		}
	}
}