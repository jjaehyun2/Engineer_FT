package cc.milkshape.grid.square
{	
	public class SquareFull extends SquareOwned
	{		
		private var _layers:Object;
		private var _neighbors:Object;
		public function SquareFull(x:int, y:int, url:String, size:int)
		{
			super(x, y, 0x393939, size);
			alpha = 0;
		}

		public function get neighbors():Object
		{
			return _neighbors;
		}

		public function set neighbors(v:Object):void
		{
			_neighbors = v;
		}

		public function get layers():Object
		{
			return _layers;
		}

		public function set layers(v:Object):void
		{
			_layers = v;
		}

	}
}