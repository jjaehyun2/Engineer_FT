package {
	
	import constants.ResourceType;
	import flash.display.BitmapData;
	import flash.display.MovieClip;
	import flash.events.EventDispatcher;
	import flash.system.ApplicationDomain;
	
	public class ResourceManager extends EventDispatcher {
		
		private static var explosion1Bitmapdatas:Vector.<BitmapData> = new Vector.<BitmapData>();
		private static var explosion2Bitmapdatas:Vector.<BitmapData> = new Vector.<BitmapData>();
		
		private static var groundBitmapdata:BitmapData;
		private static var garbageBitmapdata:BitmapData;
		private static var crater1Bitmapdata:BitmapData;
		private static var crater2Bitmapdata:BitmapData;
		
		public static function parse(appDomain:ApplicationDomain):void {
			groundBitmapdata = makeBitmapdataByName(appDomain, "Ground");
			//trace(groundBitmapdata, makeBitmapdataByName(appDomain, "Ground"));
			garbageBitmapdata = makeBitmapdataByName(appDomain, "Musor");
			crater1Bitmapdata = makeBitmapdataByName(appDomain, "Garbage1");
			crater2Bitmapdata = makeBitmapdataByName(appDomain, "Garbage2");
			
			explosion1Bitmapdatas = drawMovieClipToBitmapdatas(appDomain, "Explosion1");
			explosion2Bitmapdatas = drawMovieClipToBitmapdatas(appDomain, "Explosion2");
		}
		
		private static function makeBitmapdataByName(appDomain:ApplicationDomain, className:String):BitmapData {
			var BdataClass:Class = appDomain.getDefinition(className) as Class;
			var mc:MovieClip = new BdataClass() as MovieClip;
			var bitmapData:BitmapData = new BitmapData(mc.width, mc.height, true, 0x0);
			bitmapData.draw(mc);
			return bitmapData;
		}
		
		private static function drawMovieClipToBitmapdatas(appDomain:ApplicationDomain, className:String):Vector.<BitmapData> {
			var MovieClipClass:Class = appDomain.getDefinition(className) as Class;
			var movieClip:MovieClip = new MovieClipClass() as MovieClip;
			movieClip.stop();
			
			var vector:Vector.<BitmapData> = new Vector.<BitmapData>();
			for (var i:int = 1; i < movieClip.totalFrames+1; i++) {
				movieClip.gotoAndStop(i);
				var bitmapData:BitmapData = new BitmapData(movieClip.width, movieClip.height, true, 0x0);
				bitmapData.draw(movieClip);
				vector.push(bitmapData);
			}
			return vector;
		}
		
		public static function getBitmapData(type:uint):BitmapData {
			var bitmapData:BitmapData;
			switch (type) {
				case ResourceType.GROUND:
					bitmapData = groundBitmapdata;
				break;
				
				case ResourceType.GARBAGE:
					bitmapData = garbageBitmapdata;
				break;
				
				case ResourceType.CRATER1:
					bitmapData = crater1Bitmapdata;
				break;
				
				case ResourceType.CRATER2:
					bitmapData = crater2Bitmapdata;
				break;
				
				default: throw new Error("Incorrect resource type: " + type);
			}
			return bitmapData;
		}
		
		public static function getBitmapdatasVector(type:uint):Vector.<BitmapData> {
			var vector:Vector.<BitmapData>;
			switch (type) {
				
				case ResourceType.EXPLOSION1:
					vector = explosion1Bitmapdatas;
				break;
				
				case ResourceType.EXPLOSION2:
					vector = explosion2Bitmapdatas;
				break;
				
				default:throw new Error("Incorrect resource type: " + type);
			}
			return vector;
		}
		
	}
}