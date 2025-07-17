/**
 * Created by newkrok on 29/12/15.
 */
package src.data
{
	import flash.geom.Point;

	public class LibraryElementVO
	{
		public var className:String;

		public var position:Point;

		public var scale:Number;

		public function LibraryElementVO( className:String, position:Point, scale:Number )
		{
			this.className = className;
			this.position = position;
			this.scale = scale;
		}
	}
}