package  {


	import application.assetLibs.Shared;
	import application.utils.DeviceInfo;
	import application.utils.SendAndLoadData;
	import feathers.controls.Drawers;
	import feathers.controls.LayoutGroup;
	import flash.text.engine.FontLookup;
	import flash.text.engine.Kerning;
	import flash.text.engine.RenderingMode;
	import flash.text.engine.TextRotation;
	import flash.text.AntiAliasType;
	import flash.text.TextFieldAutoSize;
	import screens.Splash;
	import screens.TopFooter;
	import starling.core.Starling;
	import starling.display.DisplayObject;
	
	/*import fl.text.TLFTextField;
	import flashx.textLayout.formats.TextLayoutFormat;
	import flashx.textLayout.elements.TextFlow;
	import flash.text.engine.FontLookup;
	import flash.text.engine.Kerning;
	import flash.text.engine.RenderingMode;
	import flash.text.engine.TextRotation;
	import flash.text.AntiAliasType;
	import flash.text.TextFieldAutoSize;
	import flashx.textLayout.formats.TextAlign;
	import flash.external.ExternalInterface;*/


	public class Settings {
		
		private static var __instance:Settings;
		private static var __allowInstantiation:Boolean = false;

		public static var _accessToken:String;
		public static var _userID:String = '0215587';
		
		public static var _lang:String;
		public static var _mui:Object;
		public static var _sharedObj:Shared;
		public static var _splash:Splash;
		public static var _topFooter:TopFooter;
		public static const LARI_SYMBOL:String = '¢';
		public static var _mapSettingsDrawer:Drawers;
		
		
		//ITEM LIBRARY
				
		//fonts...
		public static function get instance():Settings {
			if (! __instance) {
				__allowInstantiation=true;
				__instance=new Settings  ;
				__allowInstantiation=false;
			}
			return __instance;
		}
		
		public function Settings() {

			if (! __allowInstantiation) {
				throw new Error("используй  MainSettings.instance");
			}
		}

		public static function debugFullString(stringer:String):String {
			var myPattern:RegExp=/\r\n/g;
			return stringer.replace(myPattern,'');
		}
		
		
		public static function debugFullHTMLString(stringer:String):String {
			var myPattern:RegExp=/<3/g;
			return stringer.replace(myPattern,'♥');
		}
		
		
		public static function _getIntByDPI(exInt:int = 0):int {
			return int(exInt * (1/ Starling.current.contentScaleFactor));
		}
		
		public static function _moveByDPI(obj:DisplayObject,xPos:Number = undefined, yPos:Number=undefined):DisplayObject {
			if(!xPos) obj.x = int(xPos * DeviceInfo.dpiScaleMultiplier);
			if(!yPos) obj.y = int(yPos * DeviceInfo.dpiScaleMultiplier);
			
			return obj;
		}
		
		public static function _setSize(obj:DisplayObject, sizeX:Number = undefined, sizeY:Number = undefined, prop:Boolean = false, scale:Boolean = false):DisplayObject {
			
			if (scale) {
				if (!sizeX) {
					obj.scaleX = sizeX;
					if (prop) obj.scaleY = obj.scaleX;
				}
				
				if (!sizeY) {
					obj.scaleY = sizeY;
					if (prop) obj.scaleX = obj.scaleY;
				}
				
			}else {
				if (!sizeX) {
					obj.x = Settings._getIntByDPI(sizeX);
					if (prop) obj.scaleY = obj.scaleX;
				}
				
				if (!sizeY) {
					obj.y = Settings._getIntByDPI(sizeY);
					if (prop) obj.scaleX = obj.scaleY;
				}
				
			}
			
			return obj;
			
		}


		
		public static function callSandAndLoad(url:String, obj:Object, method:String, callBack:Function):void {
			var $send:SendAndLoadData = new SendAndLoadData(false);
			$send.initUser(url, obj, method);//MainSettings.instance.XMLgeneratePathRating  'xmlMuiPack/ratingAllXml.xml.xml'
			$send.addEventListener(AppEvent.XML_LOADED, callBack);
		}
	}
}