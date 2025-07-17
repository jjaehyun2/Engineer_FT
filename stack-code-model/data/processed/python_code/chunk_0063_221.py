/**
 * Created by Administrator on 2015/8/13.
 */
package guiFlex.utils
{
	import flash.display.DisplayObject;
	import flash.filters.ColorMatrixFilter;

	public class ObjectUtils
	{
		public static const greyFilter:ColorMatrixFilter = new ColorMatrixFilter([0.3086, 0.6094, 0.082, 0, 0, 0.3086, 0.6094, 0.082, 0, 0, 0.3086, 0.6094, 0.082, 0, 0, 0, 0, 0, 1, 0]);

		public static function grey(obj:DisplayObject, isGrey:Boolean = true):void
		{
			if (isGrey)
			{
				obj.filters = [greyFilter];
			} else
			{
				obj.filters = null;
			}
		}
	}
}