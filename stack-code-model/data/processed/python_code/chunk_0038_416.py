package
{
	import flash.display.MovieClip;
	import flash.events.MouseEvent;
	import flash.net.SharedObject;
	public class LoadMenu extends MovieClip
	{
		var reset:int;
		function LoadMenu()
		{
			confirmReset.y = load1.y;
			confirmReset.x = -200
			confirmReset.visible = false;
			confirmReset.Yes.buttonMode = true;
			confirmReset.No.buttonMode = true;
			confirmReset.Yes.addEventListener(MouseEvent.MOUSE_UP,YesButton)
			confirmReset.No.addEventListener(MouseEvent.MOUSE_UP,NoButton)
			back.addEventListener(MouseEvent.MOUSE_UP,goBack);
			back.buttonMode = true;
			for(var i = 0; i < 3; i++)
			{
				if(i == 0)
				{
					with(load1)
					{
						slot.text = "Slot1"
						loadSave.buttonMode = true;
						resetSave.buttonMode = true;
						loadSave.addEventListener(MouseEvent.MOUSE_UP,Load1);
						resetSave.addEventListener(MouseEvent.MOUSE_UP,Reset1);
					}
				}
				if(i == 1)
				{
					with(load2)
					{
						slot.text = "Slot2"
						loadSave.buttonMode = true;
						resetSave.buttonMode = true;
						loadSave.addEventListener(MouseEvent.MOUSE_UP,Load2);
						resetSave.addEventListener(MouseEvent.MOUSE_UP,Reset2);
					}
				}
				if(i == 2)
				{
					with(load3)
					{
						slot.text = "Slot3"
						loadSave.buttonMode = true;
						resetSave.buttonMode = true;
						loadSave.addEventListener(MouseEvent.MOUSE_UP,Load3)
						resetSave.addEventListener(MouseEvent.MOUSE_UP,Reset3);
					}
				}
			}
			var sharedObject:SharedObject
			var levelsComplete = 0;
			var levelScore = 0;
			for(i=1; i <4;i++)
			{
				if(i == 1)
				{
					sharedObject = SharedObject.getLocal( "PDS" );
				}
				if(i == 2)
				{
					sharedObject = SharedObject.getLocal( "PDS2" );
				}
				if(i == 3)
				{
					sharedObject = SharedObject.getLocal( "PDS3" );
				}
				if(sharedObject.data.LevelScore != undefined)
				{
					for(var o in sharedObject.data.LevelScore)
					{
						if(sharedObject.data.LevelScore[o] > 0)
						{
							levelsComplete ++;
							levelScore += sharedObject.data.LevelScore[o]
						}
					}
				}else{
					levelsComplete = 0;
					levelScore = 0;
				}
				this["load"+i].info.text = "Levels: "+levelsComplete+"/28\n\nScore: "+levelScore;
				levelsComplete = 0;
				levelScore = 0;
			}
			
			
		}
		function goBack(e:MouseEvent)
		{
			remove();
		}
		function remove()
		{
			back.removeEventListener(MouseEvent.MOUSE_UP,goBack);
			load1.loadSave.removeEventListener(MouseEvent.MOUSE_UP,Load1);
			load2.loadSave.removeEventListener(MouseEvent.MOUSE_UP,Load2);
			load3.loadSave.removeEventListener(MouseEvent.MOUSE_UP,Load3);
			load1.resetSave.removeEventListener(MouseEvent.MOUSE_UP,Reset1);
			load2.resetSave.removeEventListener(MouseEvent.MOUSE_UP,Reset2);
			load3.resetSave.removeEventListener(MouseEvent.MOUSE_UP,Reset3);
			confirmReset.Yes.removeEventListener(MouseEvent.MOUSE_UP,YesButton)
			confirmReset.No.removeEventListener(MouseEvent.MOUSE_UP,NoButton)
			parent.removeChild(this);
		}
		function NoButton(e:MouseEvent)
		{
			confirmReset.x = -200;
		}
		function YesButton(e:MouseEvent)
		{
			var main = Main.main;
			if(reset == 1)
			{
				main.Sobject("PDS")
				main.ResetData();
				load1.info.text = "Levels: 0/28\n\nScore: 0";
			}
			if(reset == 2)
			{
				main.Sobject("PDS2")
				main.ResetData();
				load2.info.text = "Levels: 0/28\n\nScore: 0";
			}
			if(reset == 3)
			{
				main.Sobject("PDS3")
				main.ResetData();
				load3.info.text = "Levels: 0/28\n\nScore: 0";
			}
			
			confirmReset.x = -200;
		}
		function Load1(e:MouseEvent)
		{
			var main = Main.main;
			main.Sobject("PDS")
			main.LoadData();
			main.SpawnLevelSelect();
			var menu = parent;
			remove();
			menu.remove();
			
		}
		function Load2(e:MouseEvent)
		{
			var main = Main.main;
			main.Sobject("PDS2")
			main.LoadData();
			main.SpawnLevelSelect();
			var menu = parent;
			remove();
			menu.remove();
		}
		function Load3(e:MouseEvent)
		{
			var main = Main.main;
			main.Sobject("PDS3")
			main.LoadData();
			main.SpawnLevelSelect();
			var menu = parent;
			remove();
			menu.remove();
		}
		function Reset1(e:MouseEvent)
		{
			confirmReset.visible = true;
			confirmReset.x = load1.x;
			reset = 1;
			/*var main = Main.main;
			main.Sobject("PDS")
			main.ResetData();
			load1.info.text = "Levels: 0/28\n\nScore: 0";*/
		}
		function Reset2(e:MouseEvent)
		{
			confirmReset.visible = true;
			confirmReset.x = load2.x;
			reset = 2;
		}
		function Reset3(e:MouseEvent)
		{
			confirmReset.visible = true;
			confirmReset.x = load3.x;
			reset = 3;
		}
	}
}