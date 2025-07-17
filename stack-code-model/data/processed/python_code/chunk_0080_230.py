package com.illuzor.circles.ui.screens {
	
	import com.greensock.easing.Linear;
	import com.greensock.easing.Quart;
	import com.greensock.TweenLite;
	import com.illuzor.circles.constants.Colors;
	import com.illuzor.circles.constants.GameType;
	import com.illuzor.circles.constants.PauseType;
	import com.illuzor.circles.constants.ScreenType;
	import com.illuzor.circles.events.PauseEvent;
	import com.illuzor.circles.events.ScreenEvent;
	import com.illuzor.circles.interfaces.IController;
	import com.illuzor.circles.tools.AudioManager;
	import com.illuzor.circles.tools.ChallangeController;
	import com.illuzor.circles.tools.KeyboardManager;
	import com.illuzor.circles.tools.PlayManager;
	import com.illuzor.circles.tools.StorageManager;
	import com.illuzor.circles.tools.VibroManager;
	import com.illuzor.circles.ui.Lives;
	import com.illuzor.circles.ui.PauseButton;
	import com.illuzor.circles.ui.PlayerCircle;
	import com.illuzor.circles.ui.Score;
	import flash.geom.Point;
	import starling.display.Shape;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	//import com.illuzor.circles.tools.AdsManager;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class GameScreen extends Sprite {
		
		private var circleSize:uint;
		private var startDrag:Boolean;
		private var initDragX:int;
		private var initDragY:int;
		private var mainCircle:PlayerCircle;
		private var globalPosition:Point;
		private var controller:IController;
		private var centerPoint:Point;
		private var gameType:String;
		private var scores:uint = 0;
		private var scoreText:Score;
		private var lives:Lives;
		private var pauseScreen:PauseScreen;
		private var pauseButton:PauseButton;
		private var stageWidth:uint;
		private var stageHeight:uint;
		private var soundEnabled:Boolean;
		
		public function GameScreen(gameType:String) {
			this.gameType = gameType;
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			StorageManager.increasePlays();
			
			if (StorageManager.getInt("plays") == 100) {
				if (PlayManager.signedIn) {
					PlayManager.unlockAchievement(PlayManager.PLAY_100_TIMES);
				}
			}
			
			soundEnabled = StorageManager.getBool("sound");
			
			if (soundEnabled) AudioManager.playMusic();
			
			stageWidth = stage.stageWidth;
			stageHeight = stage.stageHeight;
			
			var initColor:uint = Colors.randomColor;
			centerPoint = new Point(stageWidth >> 1, stageHeight >> 1);
			circleSize = stageWidth / 5;
			
			controller = new ChallangeController(this, circleSize, gameType);
			
			controller.next();
			
			mainCircle = new PlayerCircle(circleSize, centerPoint);
			addChild(mainCircle);
			
			makeUI();
			
			var whiteScreen:Shape = new Shape();
			whiteScreen.graphics.beginFill(0xFFFFFF);
			whiteScreen.graphics.drawRect(0, 0, stageWidth, stageHeight);
			whiteScreen.graphics.endFill();
			addChild(whiteScreen);
			TweenLite.to(whiteScreen, .9, { alpha:0, onComplete:removeChild, ease:Linear.easeNone, onCompleteParams:[whiteScreen] } );
			
			pauseButton.addEventListener(Event.TRIGGERED, onPause)
			mainCircle.addEventListener(TouchEvent.TOUCH, onTouch);
			KeyboardManager.setFunction(onPause);
		}
		
		[Inline]
		private final function makeUI():void {
			var color:uint = controller.getColor();
			mainCircle.color = color;
			mainCircle.show(true);
			
			pauseButton = new PauseButton(color);
			addChild(pauseButton);
			pauseButton.width = pauseButton.height = 200;
			if (pauseButton.height > stageWidth / 5.6) {
				pauseButton.height = pauseButton.width = stageWidth / 5.6;
			}
			pauseButton.x = pauseButton.y = pauseButton.height / 5;
			
			lives = new Lives(color);
			addChild(lives);
			lives.width = stageWidth / 4;
			lives.scaleY = lives.scaleX;
			lives.x = (stageWidth - lives.width) >> 1;
			lives.y = stageHeight - lives.height * 2;
			
			scoreText = new Score("0000", color, stageWidth / 4);
			addChild(scoreText);
			scoreText.x = stageWidth - scoreText.width - pauseButton.x;
			scoreText.y = ((scoreText.bounds.height - lives.height) >> 1) + pauseButton.y;
		}
		
		private function onPause(e:Event = null):void {
			KeyboardManager.setFunction(continueGame);
			pause();
		}
		
		private function pause():void {
			if (!pauseScreen) {
				//AdsManager.showAds();
				controller.pause();
				pauseScreen = new PauseScreen(PauseType.PAUSE, mainCircle.color);
				addChild(pauseScreen);
				pauseScreen.addEventListener(PauseEvent.PLAY, onPauseEvent);
				pauseScreen.addEventListener(PauseEvent.MENU, onPauseEvent);
				pauseScreen.addEventListener(PauseEvent.REPLAY, onPauseEvent);
			}
		}
		
		private function onPauseEvent(e:PauseEvent):void {
			pauseScreen.removeEventListener(PauseEvent.PLAY, onPauseEvent);
			pauseScreen.removeEventListener(PauseEvent.MENU, onPauseEvent);
			pauseScreen.removeEventListener(PauseEvent.REPLAY, onPauseEvent);
			switch (e.type) {
				case PauseEvent.PLAY:
					continueGame();
				break;
				
				case PauseEvent.MENU:
					if (soundEnabled) AudioManager.stopMusic();
					dispatchEvent(new ScreenEvent(ScreenEvent.CHANGE_SCREEN, ScreenType.MAIN_MENU));
				break;
				
				case PauseEvent.REPLAY:
					scores = 0;
					scoreText.changeText(0);
					(controller as ChallangeController).replay();
					mainCircle.lineSize = 1;
					continueGame();
					lives.restart();
					mainCircle.x = stageWidth >> 1;
					mainCircle.y = stageHeight >> 1;
				break;
			}
		}
		
		private function continueGame():void {
			//AdsManager.hideAds();
			removeChild(pauseScreen);
			pauseScreen.dispose();
			pauseScreen = null
			controller.next();
			KeyboardManager.setFunction(onPause);
		}
		
		private function onTouch(e:TouchEvent):void {
			var globalTouch:Touch = e.getTouch(stage);
			globalPosition = globalTouch.getLocation(stage);
			switch (globalTouch.phase) {
				case TouchPhase.BEGAN:
					if (!startDrag) {
						addChild(mainCircle);
						var localTouch:Touch = e.getTouch(mainCircle);
						var localPosition:Point = localTouch.getLocation(mainCircle);
						initDragX = localPosition.x * mainCircle.scaleX;
						initDragY = localPosition.y * mainCircle.scaleY;
						startDrag = true;
					}
				break;
				case TouchPhase.MOVED:
					if(startDrag){
						addEventListener(Event.ENTER_FRAME, onMove);
					}
				break;
				case TouchPhase.ENDED:
					removeEventListener(Event.ENTER_FRAME, onMove);
					startDrag = false;
					var currentPoint:Point = new Point(mainCircle.x, mainCircle.y);
					var distancePoint:Point = controller.getCorrectPoint(mainCircle.color);
					
					var distanceSize:uint = circleSize / 2 + mainCircle.lineSize;
					if (Point.distance(currentPoint, distancePoint) < distanceSize) {
						if (soundEnabled) AudioManager.playSound(AudioManager.CORRECT_SOUND);
						if (gameType == GameType.SIZE || gameType == GameType.COMPLETE) {
							mainCircle.lineSize = (controller as ChallangeController).getSizeAspect();
						}
						controller.next();
						scores++;
						appendScore();
						if (PlayManager.signedIn) {
							checkAchievements();
						}
						var color:uint = controller.getColor();
						mainCircle.hide(color);
						scoreText.changeColor(color);
						lives.changeColor(color);
						pauseButton.changeColor(color);
					} else {
						if(soundEnabled) AudioManager.playSound(AudioManager.INCORRECT_SOUND);
						VibroManager.vibrate(220);
						lives.reduce();
						if (lives.gameOver) {
							endGame();
						} else {
							TweenLite.to(mainCircle, .4, { x:centerPoint.x, y:centerPoint.y, ease:Quart.easeOut } );
						}
					}
				break;
			}
		}
		
		private function checkAchievements():void {
			switch (gameType) {
				case GameType.SIZE:
					if (scores == 100) PlayManager.unlockAchievement(PlayManager.REACH_100_IN_SIZE);
				break;
				case GameType.TIME:
					if (scores == 100) PlayManager.unlockAchievement(PlayManager.REACH_100_IN_SPEED);
				break;
				case GameType.COMPLETE:
					if (scores == 50) PlayManager.unlockAchievement(PlayManager.REACH_50_IN_INSANE);
					if (scores == 100) PlayManager.unlockAchievement(PlayManager.REACH_100_IN_INSANE);
				break;
			}
		}
		
		private function endGame():void {
			if (!pauseScreen) {
				//AdsManager.showAds();
				pauseScreen = new PauseScreen(PauseType.GAME_OVER, mainCircle.color, scores, gameType);
				addChild(pauseScreen);
				controller.pause();
				pauseScreen.addEventListener(PauseEvent.PLAY, onPauseEvent);
				pauseScreen.addEventListener(PauseEvent.MENU, onPauseEvent);
				pauseScreen.addEventListener(PauseEvent.REPLAY, onPauseEvent);
				KeyboardManager.setFunction(gotoMainMenu);
			}
		}
		
		private function gotoMainMenu():void {
			pauseScreen.removeEventListener(PauseEvent.PLAY, onPauseEvent);
			pauseScreen.removeEventListener(PauseEvent.MENU, onPauseEvent);
			pauseScreen.removeEventListener(PauseEvent.REPLAY, onPauseEvent);
			dispatchEvent(new ScreenEvent(ScreenEvent.CHANGE_SCREEN, ScreenType.MAIN_MENU));
			if (soundEnabled) AudioManager.stopMusic();
		}
		
		private function appendScore():void {
			scoreText.changeText(scores);
		}
		
		private function onMove(e:Event):void {
			mainCircle.x = globalPosition.x - initDragX + circleSize / 2;
			mainCircle.y = globalPosition.y - initDragY + circleSize / 2;
		}
		
		override public function dispose():void {
			KeyboardManager.removeFunc();
			pauseButton.removeEventListener(Event.TRIGGERED, onPause)
			mainCircle.removeEventListener(TouchEvent.TOUCH, onTouch);
			removeEventListener(Event.ENTER_FRAME, onMove);
			controller.destroy();
			if (pauseScreen) pauseScreen.dispose();
			super.dispose();
		}
		
	}
}