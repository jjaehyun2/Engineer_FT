package utils.css {
	import adobe.serialization.json.JSONEncoder;
	
	import flash.events.Event;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.text.StyleSheet;
	
	public class CSSUtils {
		public static var styleSheet:*;
		
		private static function _loadStyles(url:String,callback:Function,doneCallback:Function):void {
			var cssLoader:URLLoader = new URLLoader();
			var cssRequest:URLRequest = new URLRequest(url);
			var styles:StyleSheet = new StyleSheet();
			
			function cssLoadComplete(event:Event):void {
				var value:String = '';
				styles.parseCSS(cssLoader.data);
				if ( (callback is Function) && (callback != null) ) {
					value = callback(styles);
				}
				CSSUtils.styleSheet = styles;
				if ( (doneCallback is Function) && (doneCallback != null) ) {
					doneCallback(value);
				}
			}
			cssLoader.load(cssRequest);
			cssLoader.addEventListener(Event.COMPLETE, cssLoadComplete);
		}

		private static function stylesCallback(styles:*):* {
			var all_styles:Object = {};
			var names:* = styles.styleNames;
			var style:*;
			var aName:String;
			for (var i:String in names) {
				aName = names[i];
				style = styles.getStyle(aName);
				all_styles[aName] = style;
			}
			return all_styles;
		}
		
		private static function css2jsonCallback(styles:*):String {
			var all_styles:Object = CSSUtils.stylesCallback(styles);
			var je:JSONEncoder = new JSONEncoder(all_styles);
			var json:String = je.getString();
			return json;
		}
		
		public static function loadStyles(url:String,callback:Function):void {
			CSSUtils._loadStyles(url,CSSUtils.stylesCallback,callback);
		}

		public static function loadStylesAsJSON(url:String,callback:Function):void {
			CSSUtils._loadStyles(url,CSSUtils.css2jsonCallback,callback);
		}
	}
}