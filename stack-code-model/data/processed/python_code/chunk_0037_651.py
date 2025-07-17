package com.illuzor.otherside.graphics.characters {
	
	import com.illuzor.otherside.tools.ResizeManager;
	import starling.display.Image;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Ship1 extends ShipBase {
		
		private const SHIP_SPEED:Number = 1;
		
		public function Ship1(texture:Texture, config:Object=null) {
			super(config);
			var center:Image = new Image(texture);
			//center.scaleX = center.scaleY = ResizeManager.scale;
			addChild(center);
			pivotX = this.width >> 1;
		}
		
		override public function get speed():Number {
			return baseSpeed * SHIP_SPEED;
		}
		
	}
}