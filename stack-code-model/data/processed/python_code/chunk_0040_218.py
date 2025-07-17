package com.grantech.utils
{
  import starling.extensions.ColorArgb;

  public class Utils
  {
    static public function colorToHEX(red:Number, green:Number, blue:Number, alpha:Number):String
    {
      var redStr:String = int(red*255).toString(16).length == 2 ? int(red*255).toString(16) : "0" + int(red*255).toString(16);  
      var greenStr:String = int(green*255).toString(16).length == 2 ? int(green*255).toString(16) : "0" + int(green*255).toString(16);  
      var blueStr:String = int(blue*255).toString(16).length == 2 ? int(blue*255).toString(16) : "0" + int(blue*255).toString(16);  
      var alphaStr:String = int(alpha*255).toString(16).length == 2 ? int(alpha*255).toString(16) : "0" + int(alpha*255).toString(16);  
      return redStr + greenStr + blueStr + alphaStr;
    }

    static public function normalizeHEX(text:String):String
		{
			var len:int = 6 - text.length;
			for( var i:int = 0; i < len; i++ )
				text = "0" + text;
			len = 8 - text.length;
			for( i = 0; i < len; i++ )
				text = text + "f";
			return text;
		}
		
		static public function hexToARGB(text:String):ColorArgb
		{
			var color:ColorArgb = new ColorArgb();
			color.red		= parseInt(text.slice(0,2), 16) / 255;
			color.green	= parseInt(text.slice(2,4), 16) / 255;
			color.blue	= parseInt(text.slice(4,6), 16) / 255;
			color.alpha	= parseInt(text.slice(6,8), 16) / 255;
			return color;
		}

  }
}