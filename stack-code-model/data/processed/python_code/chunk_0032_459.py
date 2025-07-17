package com.syamgot.as3.util
{
	import flash.geom.Point;

	public class MathUtil
	{
		/**
		 * 新しい MathUtil() コンストラクタを呼び出すと、ArgumentError 例外がスローされます。
		 * @throws ArgumentError #2012: MathUtil クラスをインスタンス化することはできません。
		 */
		public function MathUtil()
		{
			new ArgumentError('#2012: StringUtil クラスをインスタンス化することはできません。');
		}
		
		/**
		 * ラジアンを角度に直します.
		 * 
		 * @param radian
		 * @return 
		 */
		public static function radian2angle(radian:Number):Number 
		{
			return radian * 180 / Math.PI;
		}
		
		/**
		 * 角度をラジアンに直します.
		 * @param angle
		 * @return 
		 */
		public static function angle2radian(angle:Number):Number
		{
			return angle * Math.PI / 180;
		}
		
		/**
		 * ラジアンを角度(360度計算)に直します.
		 * 
		 * @param angle
		 * @return 
		 */
		public static function radian2angle360(radian:Number):Number
		{
			var angle:Number = MathUtil.radian2angle(radian);
			return 360 + angle >= 360 ? angle : 360 + angle;
		}
		
		/**
		 * 角度を360度計算に直します.
		 * 
		 * @param angle
		 * @return 
		 */
		public static function angle360(angle:Number):Number
		{
			return 360 + angle >= 360 ? angle : 360 + angle;
		}
		
		/**
		 * 2点間の距離を計算します.
		 * 
		 * @param angle
		 * @return 
		 */
		public static function distP2P(p1:Point, p2:Point):Number
		{	
			var dx:Number = p1.x - p2.x;
			var dy:Number = p2.y - p1.y;
			return Math.sqrt(dx * dx + dy * dy);
		}
		
		/**
		 * 指定範囲内のランダムな数値を返します.
		 * 
		 * @param min
		 * @param max
		 * @return 
		 * 
		 */
		public static function randomByRange(min:Number, max:Number):Number
		{
			return Math.floor(Math.random()*(max-min+1))+min;
		}
		
	}
}