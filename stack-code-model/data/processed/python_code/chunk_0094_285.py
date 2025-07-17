package  
{
	import flash.display.Sprite;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Entity extends Sprite
	{
		private var _life:Number = 100;
		
		public function Entity() 
		{
			
		}
		
		public function applyDamage(num:Number):void
		{
			life -= num;
			updateDamageMeter();
			if (life <= 0)
			{
				trace("life: " + life + this);
				kill();
			}
		}
		
		public function frame():void
		{
			
		}
		
		public function get life():Number
		{
			return _life;
		}
		public function set life(num:Number):void
		{
			_life = num;
		}
		
		public function updateDamageMeter():void
		{
			//to be implemented later
		}
		public function collisionCheck(obj:Sprite):Boolean
		{
			return hitTestObject(obj);
		}
		public function kill():void
		{
			trace("die");
			parent.removeChild(this);
		}
		
	}

}