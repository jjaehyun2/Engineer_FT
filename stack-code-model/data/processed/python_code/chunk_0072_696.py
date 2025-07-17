package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	public class EnergyBar extends MovieClip
	{
		public var energyBox:MovieClip
		public function EnergyBar()
		{
			addEventListener(Event.ENTER_FRAME,enterFrame);
			gotoAndStop(1);
		}
		public function enterFrame(e:Event)
		{
			if(Game.energy == Game.maxEnergy)
			{
				gotoAndStop(2);
			}else{
				gotoAndStop(1);
			}
			energy.text = Game.energy.toString();
			num.text = Math.round(((Game.maxEnergy + Game.energy) / Game.maxEnergy-1) * 100) + "%"
			energyBox.scaleY = 1-(Game.maxEnergy - Game.energy) / Game.maxEnergy
		}
	}
}