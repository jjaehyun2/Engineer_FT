/**
 * @author Peter Hansen
 * @author Daniel Wilken
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Game.Model
{
	import flash.events.Event;
	import flash.events.EventDispatcher;
	
	import de.p3337.zzznake.Enum.GameState;
	import de.p3337.zzznake.Game.GameEvent;
	import de.p3337.zzznake.Game.Model.Collision.CollisionType;
	import de.p3337.zzznake.Game.Model.Field.Field;
	import de.p3337.zzznake.Game.Model.Field.PlayingField;
	import de.p3337.zzznake.Game.Model.Snack.PizzaElement;
	import de.p3337.zzznake.Game.Model.Snack.SnackElement;
	import de.p3337.zzznake.Game.Model.Snake.SnakeModel;

	/**
	 * The GameModel models a whole game with its components and their behavior.
	 */
	public class GameModel extends EventDispatcher {
		
		public static const SQUARE_SIZE:uint = 35;
		public static const FIELD_WIDTH:uint = 420;
		public static const FIELD_HEIGHT:uint = 300;
		
		private var _playingField:PlayingField;
		private var _snakeModel:SnakeModel;
		private var _snackElement:SnackElement;
		
		private var _gameState:GameState;
		private var _movementSpeed:uint;
		
		private var _keys:Array;
		
		public function GameModel() {
			var numberOfColumns:uint = uint(FIELD_WIDTH / SQUARE_SIZE);
			var numberOfRows:uint = uint(FIELD_HEIGHT / SQUARE_SIZE);
			
			_playingField = new PlayingField(numberOfColumns, numberOfRows);
			
			orderPizza();
			
			var startPosition:Field = playingField.getFreeRandomPosition();
			_snakeModel = new SnakeModel(startPosition, playingField);
			
			_snakeModel.addEventListener(GameEvent.GAME_UPDATE, notify);
			
			_movementSpeed = 0;
			_keys = new Array();
			
			_gameState = GameState.INITIALIZED;
		}
		
		public function reset():void {
			playingField.reset();
			
			orderPizza();
			
			var startPosition:Field = playingField.getFreeRandomPosition();
			_snakeModel.reset(startPosition);
			
			_movementSpeed = 0;
			_keys = new Array();
			
			notify(new GameEvent(GameEvent.GAME_UPDATE));
		}
		
		private function orderPizza():void {
			var snackPosition:Field = playingField.getFreeRandomPosition();
			if(snackElement !== null) snackElement.dispose();
			_snackElement = new PizzaElement(snackPosition);
			notify(new GameEvent(GameEvent.GAME_UPDATE));
		}
		
		/**
		 * Checks if the snakes head collided with either food or a part of the body and handles the collision.
		 */
		public function checkCollisions():void {
			var collisionType:CollisionType = playingField.checkCollisions(); 
			switch(collisionType) {
				case CollisionType.CRUNCH:
					snakeModel.eat();
					orderPizza();
					dispatchEvent(new GameEvent(GameEvent.SNACK_CRUNCHED));
					break;
				case CollisionType.OUCH:
					dispatchEvent(new GameEvent(GameEvent.GAME_OVER));
					break;
			}
		}
		
		public function notify(event:Event):void {
			dispatchEvent(event);
		}

		public function get gameState():GameState {
			return _gameState;
		}

		public function set gameState(value:GameState):void {
			_gameState = value;
		}

		public function get keys():Array {
			return _keys;
		}

		public function set keys(value:Array):void {
			_keys = value;
		}

		public function get movementSpeed():uint {
			return _movementSpeed;
		}
		
		public function incrementMovementSpeed():void {
			_movementSpeed++;
		}

		public function get snakeModel():SnakeModel {
			return _snakeModel;
		}

		public function get playingField():PlayingField {
			return _playingField;
		}

		public function get snackElement():SnackElement {
			return _snackElement;
		}
	}
}