package com.illuzor.circles.ui.screens.menus {
	
	import com.illuzor.circles.Settings;
	import com.illuzor.circles.tools.Assets;
	import starling.display.Image;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class AboutMenu extends MenuBase {
		
		public function AboutMenu(text:String = "") {
			super(text);
		}
		
		override protected function start():void {
			var aboutImg:Image = new Image(Assets.atlas.getTexture("about_" + Settings.lang));
			addChild(aboutImg);
			if (aboutImg.width > stage.stageWidth * .7) {
				aboutImg.width = stage.stageWidth * .7;
				aboutImg.scaleY = aboutImg.scaleX;
			}
			aboutImg.x = (stage.stageWidth - aboutImg.width) >> 1;
			aboutImg.y = (stage.stageHeight - aboutImg.height) >> 1;
		}
		
	}
}