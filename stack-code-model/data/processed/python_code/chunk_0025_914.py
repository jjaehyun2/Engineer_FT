package com.game.building
{
	import com.game.unit.core.FinderNull;
	
	import starling.display.Image;
	
	public class MainBase extends Building
	{
		public function MainBase(teamId:int=10)
		{
			super(teamId);
		}
		
		override protected function createFinder():void{
			finder = new FinderNull(this);
		}
		
		override protected function createRate():void{
//			rateBehavior = new RateNull();
		}
		
		override protected function draw():void{
			var battery:Image = new Image(Game.asset.getTexture("base"));
			battery.pivotX = battery.width>>1;
			battery.pivotY = battery.height>>1;
			addChild(battery);
		}
	}
}