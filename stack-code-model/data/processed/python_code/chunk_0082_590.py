package com.profusiongames.beings 
{
	import flash.geom.Rectangle;
	import starling.display.Quad;
	import starling.display.Sprite;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Being extends Sprite
	{
		private var _isDead:Boolean = false;
		protected var _numLives:int = 1;
		protected var _widthShrink:int = 0;
		protected var _heightShrink:int = 0;
		private var _drew:Boolean = false;
		public function Being() 
		{
			
		}
		
		//every frame
		public function frame():void
		{
			
		}
		public function get isDead():Boolean 
		{
			return _isDead;
		}
		
		public function die():void
		{
			_numLives--;
			if (_numLives == 0)
				_isDead = true;
		}
		
		public function resurrect():void
		{
			_isDead = false;
		}
		
		public function getBoundsShrunk(s:Sprite):Rectangle
		{
			var rect:Rectangle = super.getBounds(s);
			rect.x += _widthShrink;
			rect.width -= _widthShrink*2;
			rect.y += _heightShrink;
			rect.height -= _heightShrink*2;
			if (!_drew)
			{
				/*var q:Quad = new Quad(rect.width, rect.height);
				q.x = _widthShrink;
				q.y = _heightShrink;
				addChild(q);
				setChildIndex(q, 0);*/
				_drew = false;
			}
			return rect;
		}
		
	}

}