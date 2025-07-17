package com.maxpaynestory.arcadeshooter.core
{
	import flash.display.Sprite;
	import flash.events.Event;
	
	public class Bullet extends Sprite
	{
		public static var DIRECTION_UP:String="directionup";
		public static var DIRECTION_DOWN:String="directiondown";
		private var speed:Number;
		private var bulletDirection:String;
		private var sx:Number;
		private var sy:Number;
		public function Bullet(direction:String,startX:Number,startY:Number)
		{
			super();
			this.addEventListener(Event.ADDED_TO_STAGE,onBulletAddedToStage);
			/////// Incase if we want to make enemy fire bullets we can use the same Class with changed direction
			bulletDirection = direction;
			sx = startX;
			sy = startY;
			speed = 10; /// Speed of the bullet
		}
		
		protected function onBulletAddedToStage(event:Event):void
		{
			this.x = sx;
			this.y = sy;
			this.graphics.beginFill(0xFF794B);
			this.graphics.drawCircle(0, 0, 3);
			this.graphics.endFill();
		}
		
		public function uproachEnemy():void
		{
			switch(bulletDirection){
				case Bullet.DIRECTION_UP:
					this.y -= speed;
					break;
				
				case Bullet.DIRECTION_DOWN:
					this.y += speed;
					break;
			}
		}
		
		public function outOfScreen():Boolean
		{
			if(this.y >= stage.stageHeight || this.y <= 0){
				return true;
			}
			return false;
		}
		
		public function removeSelf():void
		{
			this.parent.removeChild(this);
		}
	}
}