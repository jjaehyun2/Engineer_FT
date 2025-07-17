package com.illuzor.thegame.tools {
	
	import flash.display.BitmapData;
	import flash.system.ApplicationDomain;
	import flash.utils.Dictionary;
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	public class Assets {
		
		private static var domain:ApplicationDomain;
		private static var bitmapDatas:Dictionary = new Dictionary();

		public static function init(domain:ApplicationDomain):void {
			Assets.domain = domain;
		}
		
		public static function getImage(name:String):BitmapData{
			if (bitmapDatas[name] == undefined) {
				var BitmapdataClass:Class = domain.getDefinition("com.illuzor.thegame.bitmaps." + name) as Class;
				var bitmapData:BitmapData = new BitmapdataClass() as BitmapData;
				bitmapDatas[name] = bitmapData;
			}
			return bitmapDatas[name];
		}
		
	}
}