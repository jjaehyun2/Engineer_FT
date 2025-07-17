package com
{
	import entities.Colour;

	public class ColorNameSelector
	{
		// ActionScript file
		public function ColorNameSelector()
		{
			
		}
		
		private function presetColorArrary():void
		{
			//presetColor if not set yet
			if(AppPlusCache.Instance.colourDataArray[0].r == -1)
			{
				var color:String;
				var rgb:Array;
				var hsl:Array;
				for(var i:int = 0; i < AppPlusCache.Instance.colourDataArray.length; i++)
				{
					var colourItem:Colour = AppPlusCache.Instance.colourDataArray[i];
					
					color = "#" + colourItem.colorCode;
					rgb = getRGB(color);
					hsl = getHSL(color);
					colourItem.r = rgb[0];
					colourItem.g = rgb[1];
					colourItem.b = rgb[2];
					colourItem.h = hsl[0];
					colourItem.s = hsl[0];
					colourItem.l = hsl[0];
					
					AppPlusCache.Instance.colourDataArray[i] =  colourItem
				}
			}
		}
		
		public function getColorName(color:String):String 
		{
			//presetColor if not set yet
			if(AppPlusCache.Instance.colourDataArray)
			{
				presetColorArrary();
				
				color = color.toUpperCase();
				if(color.length < 3 || color.length > 7)
					return "";
				if(color.length % 3 == 0)
					color = "#" + color;
				if(color.length == 4)
					color = "#" + color.substr(1, 1) + color.substr(1, 1) + color.substr(2, 1) + color.substr(2, 1) + color.substr(3, 1) + color.substr(3, 1);
				
				var rgb:Array = getRGB(color);
				var r:int = rgb[0];
				var	g:int = rgb[1]; 
				var	b:int = rgb[2];
				
				var hsl:Array = getHSL(color);
				var h:int = hsl[0];
				var	s:int = hsl[1]; 
				var	l:int = hsl[2];
	
				var ndf1:int = 0; 
				var ndf2:int = 0; 
				var ndf:int = 0;
				var cl:int = -1;
				var df:int = -1;
				
				for(var i:int = 0; i < AppPlusCache.Instance.colourDataArray.length; i++)
				{
					if(color == "#" + AppPlusCache.Instance.colourDataArray[i].colorCode)
						return AppPlusCache.Instance.colourDataArray[i].name;
					
					ndf1 = Math.pow(r - AppPlusCache.Instance.colourDataArray[i].r, 2) + Math.pow(g - AppPlusCache.Instance.colourDataArray[i].g, 2) + Math.pow(b - AppPlusCache.Instance.colourDataArray[i].b, 2);
					ndf2 = Math.pow(h - AppPlusCache.Instance.colourDataArray[i].h, 2) + Math.pow(s - AppPlusCache.Instance.colourDataArray[i].s, 2) + Math.pow(l - AppPlusCache.Instance.colourDataArray[i].l, 2);
					ndf = ndf1 + ndf2 * 2;
					if(df < 0 || df > ndf)
					{
						df = ndf;
						cl = i;
					}
				}
				if(cl < 0 )
				{
					return "";
				}
				return AppPlusCache.Instance.colourDataArray[cl].name;
			}
			return "";
		}
		
		
		private function getHSL(color:String):Array {
			
			var rgb:Array = [parseInt('0x' + color.substring(1, 3)) / 255, parseInt('0x' + color.substring(3, 5)) / 255, parseInt('0x' + color.substring(5, 7)) / 255];
			var r:int = rgb[0];
			var	g:int = rgb[1]; 
			var	b:int = rgb[2];
			
			var min:int = Math.min(r, Math.min(g, b));
			var max:int = Math.max(r, Math.max(g, b));
			var delta:int = max - min;
			var l:int = (min + max) / 2;
			
			var s:int = 0;
			if(l > 0 && l < 1)
				s = delta / (l < 0.5 ? (2 * l) : (2 - 2 * l));
			
			var h:int = 0;
			if(delta > 0)
			{
				if (max == r && max != g) h += (g - b) / delta;
				if (max == g && max != b) h += (2 + (b - r) / delta);
				if (max == b && max != r) h += (4 + (r - g) / delta);
				h /= 6;
			}
			return [int(h * 255), int(s * 255), int(l * 255)];
		}
		
		private function getRGB(color:String):Array {
			return [int('0x' + color.substring(1, 3)), int('0x' + color.substring(3, 5)),  int('0x' + color.substring(5, 7))];
		}
		
	}
}