package com.illuzor.otherside.graphics.game.ships {
	import starling.display.Image;
	import starling.textures.Texture;
	

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Ship2 extends ShipBase {
		
		public function Ship2(texture:Texture) {
			var image:Image = new Image(texture);
			addChild(image);
			speed = baseSpeed * 1.2;
			pivotX = this.width >> 1;
			pivotY = this.height;
		}
		
	}
}