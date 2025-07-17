package com.game.unit
{
	import com.game.buddle.Buddle;
	

	public class Plane2 extends Plane
	{
		public function Plane2(teamId:int=1)
		{
			super(teamId);
			maxSpeed = 2;
		}
		
		override public function renderTick(tick:int):void{
			if(armed){
				shoot();
				rateRender(tick);
			}else{
				findTarget();
				if(moveRate.isCool()){
					move();
					update();
					moveRate.coolDown();
				}
				moveRate.rateRender(tick);
			}
			renderTickEnd();
		}
		
		override protected function createBuddle():Buddle{
			var b:Buddle = super.createBuddle();
			b.mass = 10;
			return b;
		}
		
		override protected function get imageString():String{
			return "RedPlane";
		}
		
		override protected function get buddleString():String{
			return "missilered/bb";
		}
		
		override protected function get boomString():String{
			return "boomblue_a/boomblue_a";
		}
	}
}