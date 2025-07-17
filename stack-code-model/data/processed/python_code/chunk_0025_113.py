package
{
	import flash.display.MovieClip;
	import flash.events.KeyboardEvent;
	import flash.events.Event;
	public class Weapons extends MovieClip
	{
		public static var WeaponSlots:Array;
		public static var SpecialSlot1:String;
		public static var SpecialSlot2:String;
		public static var SpecialSlot3:String;
		public static var currentWeapon:int;
		public static var weaponNumber:int;
		public static var specialWeaponNumber:int;
		public static var weaponArray:Array = new Array();
		public static var specialWeaponArray:Array = new Array();

		public static var Weapon21Cost:int = Game.maxEnergy/2;
		public static var trashCan:MovieClip;
		public function Weapons()
		{
			reset();
		}
		public function reset()
		{
			WeaponSlots= Game.WeaponSlots
			SpecialSlot1 = "Battery";
			SpecialSlot2 = "SolarPanel";
			SpecialSlot3 = "Platform";
			weaponArray = [];
			specialWeaponArray = [];
			currentWeapon = 1;
			weaponNumber = 5;
			CreateWeaponIcons(weaponNumber);
			specialWeaponNumber = 3;
			CreateSpecialWeaponIcons(specialWeaponNumber);
			selectWeapon(currentWeapon);
			trashCan = new TrashCan()
			trashCan.x = 475;
			trashCan.y = 475;
			addChild(trashCan);
		}
		private function CreateWeaponIcons(index)
		{
			for(var i = 0;i < index; i++)
			{	
				if(WeaponSlots[i] != "Empty")
				{
					var Weapon:WeaponIcon = new WeaponIcon(i,WeaponSlots[i],true);
					weaponArray.push(Weapon);
					Weapon.x = -70+25 + 10 + i * (60+10);
					Weapon.y = 25+10;
					addChild(Weapon);
					Weapon = null;
				}else{
					weaponNumber --;
				}
			}
		}
		private function CreateSpecialWeaponIcons(index)
		{
			var exist = false;
			for(var i = 0;i < index; i++)
			{

				for(var o in Main.secondaryWeaponsUnlocked)
				{
					
					if(Main.secondaryWeaponsUnlocked[o] == Weapons["SpecialSlot"+(i+1)])
					{
						
						exist = true;
						break;
					}
				}

				var Weapon:WeaponIcon = new WeaponIcon(i+21,Weapons["SpecialSlot"+(i+1)],exist);
				specialWeaponArray.push(Weapon);
				Weapon.x = -70+25 + 10 + (i+1) * (60+10);
				Weapon.y = 25+10+ 70;
				addChild(Weapon);
				Weapon = null;
				exist = false;
			}
		}
		public static function selectWeapon(index)
		{
			if(index != 1)
			{
				
				Game.mainTextField.text = "Press space to cancel turret placement.";
			}else{
				Game.mainTextField.text = "";
			}
			for(var i in weaponArray)
			{
				weaponArray[i].select(false);
			}
			for(i in specialWeaponArray)
			{
				specialWeaponArray[i].select(false);
			}
			if(index <= 20)
			{
				weaponArray[index-1].select(true);
			}else{
				specialWeaponArray[index-22].select(true);
			}
			currentWeapon = index;
		}
		public static function ChangeEnergyBarCost()
		{
			specialWeaponArray[0].delay = Weapons.Weapon21Cost;
		}
		public function remove()
		{
			weaponArray = null;
			specialWeaponArray = null;
			Weapon21Cost = 0;
			parent.removeChild(this);
		}

	}
}