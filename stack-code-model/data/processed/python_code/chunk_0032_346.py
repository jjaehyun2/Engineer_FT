package com.illuzor.otherside.graphics.screens.extra {
	
	import com.illuzor.otherside.tools.Assets;
	import com.illuzor.otherside.tools.ResizeManager;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class LoadingScreen extends Sprite {
		
		public function LoadingScreen() {
			var image:Image = new Image(Texture.fromBitmapData(Assets.loadingBitmapData, false));
			addChild(image);
			
			image.x = (ResizeManager.stageWidth - image.width) >> 1;
			image.y = (ResizeManager.stageHeight - image.height) >> 1;
		}
		
	}
}