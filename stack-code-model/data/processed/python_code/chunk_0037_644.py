package game.element
{
	public class MapElement extends BaseElement
	{
		public var x:int = 0;
		public var y:int = 0;
		public var map_type:int = 0;
		public function MapElement(x:int,y:int,map_type:int = 0)
		{
			super();
			this.x = x;
			this.y = y;
			this.map_type = map_type;
		}
	}
}