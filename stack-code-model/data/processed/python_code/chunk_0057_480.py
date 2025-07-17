package com.illuzor.circles.ui {
	
	import com.greensock.TweenLite;
	import com.illuzor.circles.tools.Assets;
	import flash.geom.Point;
	import starling.display.Image;
	import starling.display.Sprite;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class PlayerCircle extends Sprite {
		
		private var _color:uint;
		private var image:Image;
		private var initSize:uint;
		private var centerPoint:Point;
		private var newColor:uint;
		private var line:Image;
		
		public function PlayerCircle(size:uint, centerPoint:Point) {
			this.centerPoint = centerPoint;
			initSize = size;
			image = new Image(Assets.circleTexture);
			image.width = initSize;
			image.height = initSize;
			addChild(image);
			
			var stroke:Image = new Image(Assets.atlas.getTexture("playerCircleStroke"));
			addChild(stroke);
			stroke.width = initSize;
			stroke.height = initSize;
			
			line = new Image(Assets.atlas.getTexture("playerCircleLine"));
			addChild(line);
			line.width = initSize;
			line.height = initSize;
			
			pivotX = image.width >> 1;
			pivotY = image.height >> 1;
		}
		
		public function hide(newColor:uint):void {
			this.newColor = newColor;
			_color = newColor;
			TweenLite.to(this, .3, { scaleX:0, scaleY:0, alpha:0, onComplete:show } );
		}
		
		public function show(imidiate:Boolean = false):void {
			this.x = centerPoint.x;
			this.y = centerPoint.y;
			image.color = newColor;
			line.color = newColor;
			if(!imidiate){
				TweenLite.to(this, .3, { scaleX:1, scaleY:1, alpha:1 } );
			} else {
				this.scaleX = this.scaleY = 1;
			}
		}
		
		public function get color():uint {
			return _color;
		}
		
		public function set color(value:uint):void {
			_color = value;
			image.color = _color;
			line.color = _color;
			newColor = _color;
		}
		
		public function set lineSize(size:Number):void {
			image.width = initSize * size;
			image.height = initSize * size;
			image.x = (initSize-image.width) / 2;
			image.y = (initSize-image.height) / 2;
		}
		
		public function get lineSize():Number {
			return image.width / 2;
		}
		
	}
}