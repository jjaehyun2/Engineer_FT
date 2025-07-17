/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Views.Screens.ScrollingStars
{
	import flash.display.BitmapData;
	import flash.filters.BlurFilter;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	
	import de.p3337.straightouttaspace.Utils.SizeEnum;
	
	public class StarBitmapData extends BitmapData
	{
		public function StarBitmapData(starSize:SizeEnum, bgColor:uint = 0x00000000, color:uint = 0xFFFFFFFF)
		{
			var bitmapSize:int = 3;
			var rectBegin:int = 1;
			var rectEnd:int = 1;
			switch(starSize) {
				case SizeEnum.SMALL:
					bitmapSize = 3;
					rectBegin = 1;
					rectEnd = 1;
					break;
				case SizeEnum.MEDIUM:
					bitmapSize = 4;
					rectBegin = 1;
					rectEnd = 2;
					break;
				case SizeEnum.LARGE:
					bitmapSize = 5;
					rectBegin = 1;
					rectEnd = 3;
					break;
			}
			
			super(bitmapSize, bitmapSize, true, bgColor);
			fillRect(new Rectangle(rectBegin, rectBegin, rectEnd, rectEnd), color);
			applyFilter(this, this.rect, new Point(), new BlurFilter(rectEnd, rectEnd));
		}
	}
}