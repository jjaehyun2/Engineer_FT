/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Views.Screens
{
	import flash.display.Sprite;
	import flash.display.Stage;
	
	import de.p3337.straightouttaspace.Objects.Game;
	import de.p3337.straightouttaspace.Views.Objects.DrawableObjectView;
	import de.p3337.straightouttaspace.Views.Screens.HUD.HudScreen;
	import de.p3337.straightouttaspace.Views.Screens.ScrollingStars.ScrollingStarsScreen;
	
	public class PlayScreen implements IScreen
	{
		private var _view:Sprite = new Sprite();
		
		private var scrollingStarsScreen:ScrollingStarsScreen;
		private var hudScreen:HudScreen;
		private var boardView:Sprite;
		private var _stage:Stage;
		private var _game:Game;
		private var isRemoving:Boolean;
		
		public function PlayScreen(stage:Stage)
		{
			this._stage = stage;
			this.isRemoving = false;
			draw();
		}
		
		private function draw():void
		{	
			// add ScrollingStarsScreen as background animation
			scrollingStarsScreen = new ScrollingStarsScreen(this._stage, 80);
			_view.addChild(scrollingStarsScreen.view);
			
			// add HUD directly over background
			hudScreen = new HudScreen(this);
			_view.addChild(hudScreen.view);
			
			// add board view to add drawable items on screen
			boardView = new Sprite();
			_view.addChild(boardView);
		}
		
		/**
		 * @inheritDoc
		 */
		public function get view():Sprite
		{
			return _view;
		}
		
		/**
		 * @inheritDoc
		 */
		public function update():void
		{
			scrollingStarsScreen.update();
			if(!isRemoving)
			{
				var drawableObjectView:DrawableObjectView;
				for (var i:uint = 0; i < boardView.numChildren; i++)
				{
					drawableObjectView = (boardView.getChildAt(i) as DrawableObjectView);
					if(drawableObjectView.drawableObject == null || drawableObjectView.drawableObject.toBeDestroyed)
					{
						removeDrawableObjectView(drawableObjectView);
					}
					else
					{
						drawableObjectView.update();
					}
				}
			}
			
			hudScreen.update();
		}
		
		/**
		 * Adds visual objects like spaceships and weapons to the playScreen view.
		 * 
		 * @param object A DrawableObjectView object to add.
		 * @return True if the given DrawableObjectView was added
		 */
		public function addDrawableObjectView(object:DrawableObjectView):Boolean
		{
			var addedToBoard:Boolean = true;
			try {
				boardView.addChild(object);
			} catch(e:Error) {
				addedToBoard = false;
			}
			return addedToBoard;
		}
		
		/**
		 * Removes visual objects like spaceships and weapons from the playScreen view.
		 * 
		 * @param object A DrawableObjectView object to remove.
		 * @return True if the given DrawableObjectView was removed
		 */
		public function removeDrawableObjectView(object:DrawableObjectView):Boolean
		{
			this.isRemoving = true;
			var removedFromBoard:Boolean = true;
			try {
				object.destroy();
				boardView.removeChild(object);
			} catch(e:Error) {
				removedFromBoard = false;
			}
			this.isRemoving = false;
			return removedFromBoard;
		}
		
		public function set game(value:Game):void
		{
			_game = value;
		}
		
		public function get game():Game
		{
			return _game;
		}
		
		public function get stage():Stage
		{
			return _stage;
		}
		
		/**
		 * @inheritDoc
		 */
		public function destroy():void {
			this.scrollingStarsScreen.destroy();
			this.scrollingStarsScreen = null;
			
			this.hudScreen.destroy();
			this.hudScreen = null;
			
			for (var i:uint = 0; i < this.boardView.numChildren; i++)
			{
				(this.boardView.getChildAt(i) as DrawableObjectView).destroy();
			}
			this.boardView.removeChildren();
			this.boardView = null;
			
			this._view.removeChildren();
			
			this._stage = null;
		}
	}
}