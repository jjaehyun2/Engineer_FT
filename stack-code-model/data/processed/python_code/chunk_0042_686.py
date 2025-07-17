package com.profusiongames.items 
{
	import com.profusiongames.platforms.Platform;
	import starling.display.Sprite;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Item extends Sprite 
	{
		public var monetaryValue:int = 0;
		public var isCollectable:Boolean = false;
		
		private var _maxHeightAbovePlatform:int = 40;
		private var _minHeightAbovePlatform:int = 10;
		
		public function Item() 
		{
			
		}	
		
		public function floatAbovePlatform(p:Platform):void
		{
			x = int(p.x + int(Math.random() * p.width) - p.width / 2);
			y = int(p.y - (int(Math.random() * (_maxHeightAbovePlatform - _minHeightAbovePlatform)) + _minHeightAbovePlatform));
		}
	}

}