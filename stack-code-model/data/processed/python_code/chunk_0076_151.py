/**
 * @author Peter Hansen
 * @author Daniel Wilken
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Game.View
{	
	import flash.display.Sprite;
	
	import de.p3337.zzznake.Game.Model.GameModel;
	import de.p3337.zzznake.Game.Model.Field.PlayingField;
	import de.p3337.zzznake.Main.Zzznake;
	import de.p3337.zzznake.Util.DefaultButton;
	
	/**
	 * The GameView draws the playing field grid, all parts of the snake, and snakes as layers onto each other.
	 * Furthermore an infobox is showing the current game stats and a button closes the game and redirects to the main menu.
	 */
	public class GameView {
		public static const GRID_COLOR:uint = 0xCCCCCC;
		
		private var model:GameModel;
		
		private var width:uint;
		private var height:uint;
		private var playingField:PlayingField;
		
		private var _view:Sprite;
		private var gridBackground:Sprite;
		private var container:Sprite;
		
		private var snakeView:SnakeView;
		private var snackView:SnackView;
		
		private var _infoBox:GameInfoBox;
		private var _backButton:DefaultButton;
		
		public function GameView(gameModel:GameModel) {
			model = gameModel;
			playingField = model.playingField;
			width = playingField.numberOfColumns;
			height = playingField.numberOfRows;
			
			draw();
		}
		
		private function draw():void {
			_view = new Sprite()
			
			container = new Sprite();
			container.x = Zzznake.ZZZNAKE_PADDING;
			container.mouseChildren = false;
			drawBackground();
			
			gridBackground = new Sprite();
			gridBackground.y = Zzznake.ZZZNAKE_PADDING;
			drawGridBackground();
			container.addChild(gridBackground);
			
			snakeView = new SnakeView(model.snakeModel);
			snakeView.view.y = Zzznake.ZZZNAKE_PADDING;
			container.addChild(snakeView.view);
			
			snackView = new SnackView(model);
			snackView.view.y = Zzznake.ZZZNAKE_PADDING;
			container.addChild(snackView.view);
			
			_view.addChild(container);
			
			_infoBox = new GameInfoBox(model);
			_infoBox.x = Zzznake.ZZZNAKE_PADDING;
			_infoBox.y = gridBackground.height + gridBackground.y + Zzznake.ZZZNAKE_PADDING;
			_view.addChild(_infoBox);
			
			_backButton = new DefaultButton("Main menu");
			_backButton.x = Zzznake.ZZZNAKE_PADDING;
			_backButton.y = Zzznake.ZZZNAKE_HEIGHT - _backButton._height - Zzznake.ZZZNAKE_PADDING;
			_view.addChild(backButton);	
		}
		
		public function update():void {
			snackView.update();
			snakeView.update();
			infoBox.update();
		}
		
		private function drawBackground():void {
			container.graphics.beginFill(0xFFFFFF);
			container.graphics.drawRect(0, 0, Zzznake.ZZZNAKE_WIDTH, Zzznake.ZZZNAKE_HEIGHT);
			container.graphics.endFill();
		}
		
		private function drawGridBackground():void {
			gridBackground.graphics.clear();
			gridBackground.graphics.lineStyle(1, GRID_COLOR);
			
			for (var col:Number = 0; col < this.width + 1; col++) {
				for (var row:Number = 0; row < this.height + 1; row++) {
					gridBackground.graphics.moveTo(col * GameModel.SQUARE_SIZE, 0);
					gridBackground.graphics.lineTo(col * GameModel.SQUARE_SIZE, GameModel.SQUARE_SIZE * this.height);
					gridBackground.graphics.moveTo(0, row * GameModel.SQUARE_SIZE);
					gridBackground.graphics.lineTo(GameModel.SQUARE_SIZE * this.width, row * GameModel.SQUARE_SIZE);
				}
			}
		}

		public function get view():Sprite {
			return _view;
		}

		public function get infoBox():GameInfoBox {
			return _infoBox;
		}

		public function get backButton():DefaultButton {
			return _backButton;
		}

		public function set backButton(value:DefaultButton):void {
			_backButton = value;
		}
	}
}