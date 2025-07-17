package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	public class FakeCannon extends MovieClip
	{
		private var collision:Boolean;
		public static var Drag:Boolean;
		public static var DragCannon:Object;
		public function FakeCannon()
		{
			
			reset();
			hitBox.visible = false;
			addEventListener(Event.ENTER_FRAME,enterFrame);
			addEventListener(MouseEvent.CLICK, onClick);
			addEventListener(MouseEvent.MOUSE_UP, onUP);
		}
		public function reset()
		{
			DragCannon = null;
			Drag = false;
			gotoAndStop(1);
		}
		function enterFrame(e:Event)
		{
			if(Key.isDown(32))
			{
				WeaponSelect(0);
			}
			if(Weapons.currentWeapon != 24)
			{
				collision = CheckCollision();
			}else{
				collision = PlatformCollision();
			}
			if(collision == true)
			{
				this.buttonMode = false;
				this.mouseEnabled = false;
				marker.gotoAndStop(2);
			}else{
				this.buttonMode = true;
				this.mouseEnabled = true;
				marker.gotoAndStop(1);
			}
			if(Drag == false)
			{
				for(var i = 1; i < Weapons.weaponNumber; i ++)
				{
					if(Key.isDown(48+i))
					{
						if(Weapons.weaponArray[i].Ready == true)
						{
							WeaponSelect(i);
						}
					}
				}
				for(i = 0; i < Weapons.specialWeaponNumber; i++)
				{
					if(i == 0)
					{
						if(Key.isDown(81))
						{
							if(Weapons.specialWeaponArray[i]!=null)
							{
								if(Weapons.specialWeaponArray[i].Ready == true)
								{
									for(var j in Main.secondaryWeaponsUnlocked)
									{
										if(Main.secondaryWeaponsUnlocked[j] == "Battery")
										{
											WeaponSelect(i+21);
											break;
										}
									}
									
								}
							}
						}
					}
					if(i == 1)
					{
						if(Key.isDown(87))
						{
							if(Weapons.specialWeaponArray[i]!=null)
							{
								if(Weapons.specialWeaponArray[i].Ready == true)
								{
									for(var k in Main.secondaryWeaponsUnlocked)
									{
										if(Main.secondaryWeaponsUnlocked[k] == "SolarPanel")
										{
											WeaponSelect(i+21);
											break;
										}
									}
								}
							}
						}
					}
					if(i == 2)
					{
						if(Key.isDown(69))
						{
							if(Weapons.specialWeaponArray[i]!=null)
							{
								
								if(Weapons.specialWeaponArray[i].Ready == true)
								{
									for(var l in Main.secondaryWeaponsUnlocked)
									{
										if(Main.secondaryWeaponsUnlocked[l] == "Platform")
										{
											WeaponSelect(i+21);
											break;
										}
									}
								}
							}
						}
					}
				}
				if(Weapons.currentWeapon != 1)
				{
					marker.visible = true;
				}else{
					marker.visible = false;
				}
			}else{
				if(Key.isDown(32))
				{
					WeaponSelect(0);
					DragCannon.GoOnline();
					Drag = false;
					DragCannon = null;
				}
				marker.visible = true;
			}
			x = stage.mouseX;
			y = stage.mouseY;
		}
		public function WeaponSelect(i)
		{
			
			Weapons.selectWeapon(i+1);
			if(i <= 20)
			{
				gotoAndStop(Weapons.WeaponSlots[Weapons.currentWeapon-1]);
			}else{
				
				gotoAndStop(Weapons["SpecialSlot"+(Weapons.currentWeapon-21)]);
			}
		}
		public function onClick(e:MouseEvent)
		{
			if(Weapons.currentWeapon != 24)
			{
				collision = CheckCollision();
			}else{
				collision = PlatformCollision();
			}
			SpawnCannon();
		}
		function onUP(e:MouseEvent)
		{
			if(Weapons.currentWeapon != 24)
			{
				collision = CheckCollision();
			}else{
				collision = PlatformCollision();
			}
			SpawnCannon();
		}
		function SpawnCannon()
		{
			if(collision == false)
			{
				if(Weapons.currentWeapon != 1)
				{
					
					if(Weapons.currentWeapon <= 20)
					{
						for( var v in Game.WeaponCost[0])
						{
							if(Weapons.WeaponSlots[Weapons.currentWeapon-1] == Game.WeaponCost[0][v])
							{
								Game.energy -= Game.WeaponCost[1][v];
								
							}
						}
						
						
						
						Game.NewCannon(stage.mouseX,stage.mouseY,Weapons.WeaponSlots[Weapons.currentWeapon-1]);
						Weapons.weaponArray[Weapons.currentWeapon-1].Offline();
					}else{
						if(Weapons.currentWeapon == 22)
						{
							Game.energy -= Game.maxEnergy/2;
							
						}
						if(Weapons.currentWeapon == 23)
						{
							
							Game.energy -= Game.SpecialWeapon2Cost;
							
						}
						if(Weapons.currentWeapon == 24)
						{
							
							Game.energy -= Game.SpecialWeapon3Cost;
							
						}

						Game.NewCannon(stage.mouseX,stage.mouseY,Weapons["SpecialSlot"+(Weapons.currentWeapon-21)]);
						Weapons.specialWeaponArray[Weapons.currentWeapon-22].Offline();
					}
					
					
					WeaponSelect(0);
				}
				if(Drag == true)
				{
					WeaponSelect(0);
					Drag = false
					DragCannon.x = stage.mouseX;
					DragCannon.y = stage.mouseY;
					DragCannon.GoOnline();
					DragCannon = null;
				}
			}
		}
		function CheckCollision():Boolean
		{
			
			var a:Array = [Game.bigPlanet.hitTest];
			for(var i in Game.platform)
			{
				a.push(Game.platform[i].hitTest);
			}
			for(i in a)
			{
				if(a[i].hitTestPoint(x,y,true))
				{
					for(var o in Game.cannons)
					{
						if(Game.cannons[o] !=DragCannon)
						{
							if(hitBox.hitTestObject(Game.cannons[o].hitBox))
							{
								return true;
								break;
							}
						}
					}
					return false;
				}
			}
			return true;
		}
		public function PlatformCollision()
		{
			if(y < 200)return true;
			if(Game.bigPlanet.hitTest.hitTestPoint(x,y,true))
			{
				return true;
			}else{
				for(var i in Game.platform)
				{
					if(Game.platform[i].hitTestObject(this.hitBox))
					{
						return true;
					}
				}
				return false;
			}
			return false;
		}
		public function remove()
		{
			removeChild(hitBox);
			hitBox = null;
			removeChild(marker);
			DragCannon = null;
			marker = null;
			removeEventListener(Event.ENTER_FRAME,enterFrame);
			removeEventListener(MouseEvent.CLICK, onClick);
			parent.removeChild(this);
		}
		public static function DragOn(cannon,type)
		{
			if(Drag == false)
			{
				if(Weapons.currentWeapon == 1)
				{
					DragCannon = cannon;
					Drag = true;
					Game.fakeCannon.gotoAndStop(type);
					Game.mainTextField.text = "Press space to cancel turret placement.";
					DragCannon.GoOffline();
				}
			}
		}
		public function Pause()
		{
			visible = false;
			removeEventListener(Event.ENTER_FRAME,enterFrame);
			removeEventListener(MouseEvent.CLICK, onClick);
		}
		public function Resume()
		{
			visible = true;
			addEventListener(Event.ENTER_FRAME,enterFrame);
			addEventListener(MouseEvent.CLICK, onClick);
		}
	}
	
}