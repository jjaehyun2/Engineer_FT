package com.marioretana.checkersgame {
	import flash.display.BitmapData;
	import citrus.objects.CitrusSprite;

	import starling.display.DisplayObject;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;

	import flash.display.Bitmap;
	
	/**
	 * Represents one of the game chips.
	 * This class handles touch events for the chip, bitmap loading
	 * and reports to the game controller when a chip has been moved.
	 * @author Mario Retana <maretanar@gmail.com>
	 */
	public class Chip extends CitrusSprite {
		
		/**
		 * Enumerator for the chip's color.
		 * When a chip is instantiated, the color parameter should be one of these values.
		 */
		public static const CHIP_COLOR:Object =
		{
			BLACK : 0,
			RED : 1,
			WHITE : 2
		};
		
		public var chipSprite:DisplayObject;
		
		public function Chip(name : String, color:Number) {
			var bitmapData:BitmapData = getColorBitmapData(color);
			var params:Object =
			{
				x : 64,
				y : 32,
				width : 32,
				height : 32,
				touchable : true,
				view : new Bitmap(bitmapData)
			};
			super(name, params);
		}
		
		private function getColorBitmapData(color:Number):BitmapData
		{
			switch (color)
			{
				case CHIP_COLOR.BLACK:
					return EmbeddedSources.BLACK_CHIP_BITMAPDATA;
				case CHIP_COLOR.RED:
					return EmbeddedSources.RED_CHIP_BITMAPDATA;
				case CHIP_COLOR.WHITE:
					return EmbeddedSources.WHITE_CHIP_BITMAPDATA;
				default:
					return null;
			}
		}

		public function onTouch(event:TouchEvent):void
		{
		    var touch:Touch = event.getTouch(chipSprite);
		    if (touch && touch.phase === TouchPhase.MOVED)
		    {
				//var localPos:Point = touch.getLocation(displayObject);
				chipSprite.alpha = GlobalConfiguration.CHIP_USER_MOVED_ALPHA;
				x = touch.globalX - GlobalConfiguration.TILE_WIDTH / 2;
				y = touch.globalY - GlobalConfiguration.TILE_HEIGHT / 2;
		        Utils.logInfo("Touched object at position: " + touch.globalX + ', ' + touch.globalY);
		    }
			else if (touch && touch.phase === TouchPhase.ENDED)
			{
				chipSprite.alpha = 1;
				x = 64;
				y = 32;
			}
		}
		
	}
}