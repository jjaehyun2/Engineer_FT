package as3lib.helper.map
{
	import flash.geom.Point;
	import as3lib.helper.math.MathHelper;
	
	/**
	 * 计算地球上任意两点的球面距离。假定地球是一个标准的圆球。
	 */
	public class MapHelper
	{
		/**
		 * 以英里为单位的地球半径
		 */
		public static const R_MILES:Number = 3963.1;
		/**
		 * 以海里为单位的地球半径
		 */
		public static const R_NAUTICAL_MILES:Number = 3443.9;
		/**
		 * 以公里为单位的地球半径
		 */
		public static const R_KM:Number = 6378;
//		public static const R_KM:Number = 6378.137;
		/**
		 * 以米为单位的地球半径
		 */
		public static const R_METERS:Number = 6378000;
//		public static const R_METERS:Number = 6378137;
		
		/** 
		 * 计算给定的两点间的距离。可以指定不同的地球半径，实现返回指定单位的距离计算结果
		 * 默认值为 R_METERS(6,378,000米)，推荐的半径值包括:
		 * R_MILES(3963.1英里)
		 * R_NAUTICAL_MILES(3443.9海里)
		 * R_KM(6378公里)
		 * @return 给定两点间的距离
		 * @see http://jan.ucc.nau.edu/~cvm/latlon_formula.html
		 * */
		public static function approxDistance(start:Point, end:Point, r:Number= MapHelper.R_METERS):Number 
		{
			
			var d:Number;
			var a1:Number = MathHelper.radians(start.y);
			var b1:Number = MathHelper.radians(start.x);
			var a2:Number = MathHelper.radians(end.y);
			var b2:Number = MathHelper.radians(end.x);
			with(Math) {
				d = acos(cos(a1)*cos(b1)*cos(a2)*cos(b2) + cos(a1)*sin(b1)*cos(a2)*sin(b2) + sin(a1)*sin(a2)) * r;
			}
			return d;
		}
		/** 
		 * 算法有别于approxDistance方法。<br/>
		 * 计算给定的两点间的距离。可以指定不同的地球半径，实现返回指定单位的距离计算结果
		 * 默认值为 R_METERS(6,378,000米)，推荐的半径值包括:
		 * R_MILES(3963.1英里)
		 * R_NAUTICAL_MILES(3443.9海里)
		 * R_KM(6378公里)
		 * @return 给定两点间的距离
		 */
		private static function GetDistance(start:Point, end:Point, r:Number= MapHelper.R_METERS):Number
		{
			//经纬度本身就是一个度的单位，地图两点并非直线而类似弧线
			var d:Number;
			var y1:Number = MathHelper.radians(start.y);
			var y2:Number = MathHelper.radians(end.y);
			var x1:Number = MathHelper.radians(start.x);
			var x2:Number = MathHelper.radians(end.x)
			
			var a:Number = y1 - y2;
			var b:Number = x1-  x2;
			with(Math) 
			{
				d = 2 * asin(sqrt(pow(sin(a/2),2) + cos(y1) * cos(y2)* pow(sin(b/2),2))) * r;
			}
			return d;
		}
	}
}