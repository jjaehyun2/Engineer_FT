package 
{
	import flash.display.BitmapData;
	import flash.display.Sprite;
	/**
	 * ...
	 * @author Stephen Birsa
	 */
	final internal class Player extends Sprite
	{
		private const _WIDTH:int = 20;
		private const _HEIGHT:int = 40;
		private const _ALPHA:int = 1;
		private const _COLOUR:int = 0x00FF00;
		
		internal var leftCol:Boolean = false;
		internal var rightCol:Boolean = false;
		internal var downCol:Boolean = false;
		internal var upCol:Boolean = false;
		internal const COLLISION:BitmapData = new BitmapData(1, 1, false, 0);
		internal var xSpeed:int = 0;
		internal var ySpeed:int = 0;
		internal const SPEED:int = 3;
		internal const JUMP_SPEED:int = -20;
		internal const FRICTION:Number = 0.9;
		internal const GRAVITY:Number = 1.5;
		internal const MAX_SPEED:int = 6;
		
		final public function Player() 
		{
			super();
			this.graphics.beginFill(_COLOUR, _ALPHA);
			this.graphics.drawRect(0, 0, _WIDTH, _HEIGHT);
			this.graphics.endFill();
		}
		
	}

}