package com.game.unit
{
	import com.calculation.Vector2D;
	

	public class Plane3 extends Plane
	{
		public function Plane3(teamId:int=1)
		{
			super(teamId);
			mass = 5;
		}
		
		override protected function get imageString():String{
			return "GodPlane";
		}
		
		override protected function get buddleString():String{
			return "wave_blue_a/wave_blue_a";
		}
		
		override protected function get boomString():String{
			return "ice_boom_blue/ice_boom_blue";
		}
		
		override protected function move():void{
			if(target){
				var ev:Vector2D = surround(targetVec,Math.PI/4);
			}else{
				seek(this.position.add(new Vector2D(5,0)));
			}
		}
	}
}