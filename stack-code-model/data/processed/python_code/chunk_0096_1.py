package com.qcenzo.flake2d.core
{
	import flash.display.BitmapData;

	internal class Astar
	{
		private var _open:BinaryHeap;
		private var _nodes:Vector.<Node>;

		public function Astar()
		{
			_open = new BinaryHeap();
		}
		
		public function init(row:int, col:int, tileWidth:int, tileHeight:int, 
							 scaleFactor:Number, waypoint:BitmapData):void
		{
			_nodes.fixed = false;
			_nodes.splice(0, _nodes.length);
			for (var r:int = 0; r < row; r++)
				for (var c:int = 0; c < col; c++)
					_nodes.push(new Node(waypoint.getPixel(
						c * tileWidth * scaleFactor, r * tileHeight * scaleFactor)));
			_nodes.fixed = true;
		}
		
		public function findPath():void
		{
			
		}
	}
}

class Node
{
	public var g:int;
	public var h:int;
	public var walkable:Boolean;
	public var transparent:Boolean;
	public var closed:Boolean;
	public var parent:Node;
//	public var neighbors:Vector.<Node>;
	
	public function Node(color:uint)
	{
		if (color > 0)
		{
			this.walkable = true;
			transparent = color == 0xFF0000;
		}
	}
	
	public function get f():int
	{
		return g + h;
	}
}

class BinaryHeap
{
	private var _nodes:Vector.<Node>;
	
	public function BinaryHeap()
	{
		_nodes = new Vector.<Node>();
	}
	
	public function push(node:Node):void
	{
		
	}
	
	public function shift():Node
	{
		var root:Node = _nodes[1];
		_nodes[1] = _nodes.pop();
		while (true)
		{
			
		}
		return root;
	}
}