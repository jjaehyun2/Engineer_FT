package com.illuzor.otherside.graphics.bullets.player {
	
	import com.illuzor.otherside.graphics.characters.MovableObject;
	import starling.display.Sprite;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class BulletBase extends MovableObject {
		
		protected var _damage:uint;
		
		public function get damage():uint {
			return _damage;
		}
		
		/*override public function move():void {
			this.y -= speed;
		}*/
		
	}
}