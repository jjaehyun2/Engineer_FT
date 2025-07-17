/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Views.Screens
{
	import flash.display.Bitmap;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.display.Stage;
	
	import de.p3337.straightouttaspace.Main.StraightOuttaSpace;

	public class StartScreen implements IScreen
	{
		private var _view:Sprite = new Sprite();
		private var stage:Stage;
		
		public function StartScreen(stage:Stage)
		{
			this.stage = stage;
			draw();
		}
		
		private function draw():void
		{
			// draw background image 
			[Embed(source='/de/p3337/straightouttaspace/resources/spaceshooter/Backgrounds/blue.png')]
			var BgImageClass:Class;
			var bgImage:Bitmap = new BgImageClass();
			_view.graphics.beginBitmapFill(bgImage.bitmapData);
			_view.graphics.drawRect(0, 0, this.stage.stageWidth, this.stage.stageHeight);
			_view.graphics.endFill();
			
			// add title image
			[Embed(source='/de/p3337/straightouttaspace/resources/title.jpg')]
			var TitleImageClass:Class;
			var titleImage:Bitmap = new TitleImageClass();
			var imageSize:int = this.stage.stageWidth - (StraightOuttaSpace.SOS_PADDING * 2);
			imageSize = imageSize > 500? 500 : imageSize;
			titleImage.width = imageSize;
			titleImage.height = imageSize + 8;
			titleImage.x = this.stage.stageWidth / 2 - imageSize / 2;
			titleImage.y = 100;
			_view.addChild(titleImage);
			
			// add start text
			[Embed(source='/de/p3337/straightouttaspace/resources/HitSpaceTextTween.swf')]
			var HitSpaceTextTweenClass:Class;
			var hitSpaceTextTweenAsset:MovieClip = new HitSpaceTextTweenClass();
			hitSpaceTextTweenAsset.x = stage.stageWidth / 2 - hitSpaceTextTweenAsset.width / 2;
			hitSpaceTextTweenAsset.y = titleImage.y + titleImage.height + StraightOuttaSpace.SOS_PADDING;
			hitSpaceTextTweenAsset.mouseChildren = false;
			_view.addChild(hitSpaceTextTweenAsset);
		}
		
		/**
		 * @inheritDoc
		 */
		public function update():void {}
		
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
		public function destroy():void {
			this._view.removeChildren();
			this.stage = null;
		}
	}
}