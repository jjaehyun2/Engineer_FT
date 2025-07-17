package com.syamgot.as3.util {
	import flash.display.BitmapData;
	import flash.geom.Point;

	/**
	 * 
	 * @author syamgot
	 */
	public class BitmapDataUtil {
		public function BitmapDataUtil() {
		}


		/**
		 * 指定した色を透過させます.
		 * 
		 * カラーはアルファ値付きのカラー値を指定してください.
		 * 
		 * @param bmpd
		 * @param color
		 * @return 
		 */
		public static function transparent(bmpd:BitmapData, color:Number):BitmapData 
		{
			var tmp:BitmapData = new BitmapData(bmpd.width, bmpd.height, true, 0);
			tmp.threshold(bmpd, bmpd.rect, new Point(0, 0), "==", color, 0, 0xffffffff, true);
			bmpd.dispose();
			return tmp;
		}
	}
}