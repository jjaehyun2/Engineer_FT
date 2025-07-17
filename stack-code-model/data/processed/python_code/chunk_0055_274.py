package
{
	import flash.events.MouseEvent;
	import flash.display.MovieClip;
	public class TrashCan extends MovieClip
	{
		function TrashCan()
		{
			addEventListener(MouseEvent.CLICK,onClick);
			addEventListener(MouseEvent.MOUSE_UP,onUP);
		}
		public function Pause()
		{
		}
		public function Resume()
		{
		}
		public function remove()
		{
			parent.removeChild(this);
		}
		public function onClick(e:MouseEvent)
		{
			deleteCannon();
			Weapons.selectWeapon(1);
			Game.fakeCannon.gotoAndStop(1);
			
		}
		public function onUP(e:MouseEvent)
		{
			deleteCannon();
			Weapons.selectWeapon(1);
			Game.fakeCannon.gotoAndStop(1);
		}
		function deleteCannon()
		{
			if(FakeCannon.DragCannon!=null)
			{
				if(FakeCannon.DragCannon.type == "SolarPanel")
				{
					Game.energy += 50/3*2;
					Game.EnergyAmount -= 1;
				}
				if(FakeCannon.DragCannon.type == "Battery")
				{
					Game.energy += 50/3*2;
				}
				var Type = FakeCannon.DragCannon.type;
				FakeCannon.DragCannon.remove()
				FakeCannon.DragCannon  = null;
				Game.fakeCannon.WeaponSelect(0);
				FakeCannon.Drag = false;
				FakeCannon.DragCannon = null;
				for( var i in Game.WeaponCost[0])
				{
					if(Type == Game.WeaponCost[0][i])
					{
						Game.energy += Game.WeaponCost[1][i]/3*2;
					}
				}
				
			}
		}
	}
}