/**
 * Created by newkrok on 20/10/16.
 */
package net.fpp.pandastory.game.vo
{
	import flash.geom.Rectangle;

	public class TerrainVO
	{
		public var type:String;
		public var rectangle:Rectangle;

		public function TerrainVO( type:String, rectangle:Rectangle )
		{
			this.type = type;
			this.rectangle = rectangle;
		}
	}
}