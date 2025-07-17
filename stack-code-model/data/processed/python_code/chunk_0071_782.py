package com.illuzor.common {
	
	import flash.text.Font;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	internal class FontManager {
		
		public static var registred:Boolean;
		
		[Embed(source = "../../../../assets/Roboto-Regular.ttf", mimeType = "application/x-font-truetype", fontName = "RobotoRegular", unicodeRange = "U+0020-U+002F,U+0030-U+0039,U+003A-U+0040,U+0041-U+005A,U+005B-U+0060,U+0061-U+007A,U+007B-U+007E,U+02C6,U+02DC,U+2013-U+2014,U+2018-U+201A,U+201C-U+201E,U+2020-U+2022,U+2026,U+2030,U+2039-U+203A,U+20AC,U+2122,U+0401,U+0410-U+044F", embedAsCFF = "false")]
		private static const RobotoRegular:Class;
		
		public static function register():void {
			if (!registred) {
				registred = true;
				Font.registerFont(RobotoRegular);
			}
		}
		
	}
}