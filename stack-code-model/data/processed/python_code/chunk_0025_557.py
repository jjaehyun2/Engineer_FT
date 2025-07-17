package com.game.buddle
{
	import com.calculation.Vector2D;
	
	import core.unit.behavior.IUnit;

	public class BuddleSkill extends Buddle
	{
		public function BuddleSkill(buddleString:String="boom_purple", boomString:String="bz_purple")
		{
			super(buddleString, boomString);
		}
		
		override protected function setProperty():void{
			maxSpeed = 15;
			mass = 4;
			
			var dx:Number = 15 - Math.random() * 20;
			var dy:Number = 10 - Math.random() * 20;
			
			velocity = new Vector2D(dx,dy);
		}
		
//		override public function set target(value:IUnit):void{
//			super.target = value;
//			var dx:Number = target.x - this.x;
//			var dy:Number = target.y - this.y;
//			
//			dy = 100;
//			if(Math.random() > 0.5){
//				dy = -dy;
//			}
//			
//			dy += int(Math.random() * 50);
//			
//			
//		}
		
//		private var gapY:int = -1;
//		private var gapX:int = 50;
//		
//		override protected function move():void{
//			if(gapY == -1){
//				gapY = 50 + Math.random() * 100;
//				if(Math.random() > 0.5){
//					gapY = -gapY;
//				}
//			}else{
//				if(Math.abs(gapY) > 10){
//					gapY/=2;
//				}
////				else{
////					gapY = 0;
////				}
//			}
//			
//			var dx:Number = target.x / gapX;
//			if(gapX > 1){
//				gapX--;
//			}
//			
//			seek(new Vector2D(target.x,target.y));
//		}
	}
}