package  
{
	import flash.display.Sprite;
	/**
	 * ...
	 * @author ...
	 */
	public class Util 
	{
		
		public static const UP:uint = 0;
		public static const RIGHT:uint = 1;
		public static const LEFT:uint = 3
		public static const DOWN:uint = 2;
		public static var terrain:Vector.<TerrainObject>;
		public static var mainSprite:Sprite;
		
		public static function init(sprite:Sprite):void {
			mainSprite = sprite;
			terrain =  new Vector.<TerrainObject>();
		}
	}

}