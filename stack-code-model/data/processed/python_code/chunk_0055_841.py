package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.utils.getDefinitionByName;
	public class LevelSelect extends MovieClip
	{
		var map:MovieClip;
		var drag:Boolean;
		var background:MovieClip;
		public static var weaponSelect:MovieClip;
		public var planet:MovieClip;
		public var backGround2:MovieClip;
		public var bigPlanet:MovieClip;
		public var animPlanet:MovieClip;
		public function LevelSelect()
		{
			
			background = new BackGround1();
			background.x = 250;
			background.y = 190;
			addChild(background);
			drag = false;
			SpawnMap();
			addEventListener(Event.ENTER_FRAME,onEnterFrame);
			addEventListener(MouseEvent.MOUSE_DOWN,onMouseDown);
			addEventListener(MouseEvent.MOUSE_UP,onMouseUp);
			setChildIndex(Score,numChildren - 1);
			setChildIndex(options,numChildren - 1);
			options.addEventListener(MouseEvent.MOUSE_DOWN,optionClick);
			options.buttonMode = true;
			Main.Score = 0;
			for(var i in Main.LevelScore)
			{
				
				Main.Score += Main.LevelScore[i];
			}
			Score.text = "Score: " + Main.Score;
		}
		function optionClick(e:Event)
		{
			var optionsScreen = new OptionsScreen();
			addChild(optionsScreen);
			removeEventListener(Event.ENTER_FRAME,onEnterFrame);
			removeEventListener(MouseEvent.MOUSE_DOWN,onMouseDown);
			removeEventListener(MouseEvent.MOUSE_UP,onMouseUp);
		}
		public function SpawnMap()
		{
			map = new LevelSelectMap();
			addChild(map);
			map.x=-map["planet"+Main.level].x+250;
			map.y=-map["planet"+Main.level].y+300;
		}
		public function spawnWeaponSelect()
		{
			
			
			weaponSelect = new WeaponSelect();
			addChild(weaponSelect);
			removeEventListener(Event.ENTER_FRAME,onEnterFrame);
			removeEventListener(MouseEvent.MOUSE_DOWN,onMouseDown);
			removeEventListener(MouseEvent.MOUSE_UP,onMouseUp);
		}
		public function resume()
		{
			addEventListener(Event.ENTER_FRAME,onEnterFrame);
			addEventListener(MouseEvent.MOUSE_DOWN,onMouseDown);
			addEventListener(MouseEvent.MOUSE_UP,onMouseUp);
		}
		public function onEnterFrame(e:Event)
		{
			background.x = 250 + map.x / 10;
			background.y = 190 + map.y / 10;
			/*if(drag == false)
			{
				if(stage.mouseX > 450)
				{
					map.x -= 5
				}
				if(stage.mouseX < 50)
				{
					map.x += 5
				}
				if(stage.mouseY < 50)
				{
					map.y += 5
				}if(stage.mouseY > 550)
				{
					map.y -= 5
				}
			}*/
			if(map.x > 800)map.x = 800;

			if(map.x < -500)map.x = -500;

			if(map.y > 1100)map.y=1100;
			if(map.y < -200)map.y=-200;

		}
		public function StartAnimation()
		{
			addEventListener(Event.ENTER_FRAME,Animation);
		}
		public function Animation(e:Event)
		{
			
			if(backGround2 == null)
			{
				backGround2 = new BackGround2();
				backGround2.scaleX = 0.8;
				backGround2.scaleY = 0.8;
				backGround2.alpha = 0;
				addChild(backGround2);
				setChildIndex(map,numChildren - 1);
				
			}
			backGround2.alpha += 0.02
			if(animPlanet == null)
			{
				var planetClass = getDefinitionByName(String(["p"+(planet.currentFrame-1)])) as Class;
				animPlanet = new planetClass();
				animPlanet.x = planet.x+map.x;
				animPlanet.y = planet.y+map.y;;
				animPlanet.alpha = 1;
				addChild(animPlanet);				
			}
			if(bigPlanet == null)
			{
				bigPlanet = new BigPlanet();
				bigPlanet.y = 600;
				bigPlanet.x = 250;
				bigPlanet.alpha = 0;
				bigPlanet.gotoAndStop(planet.currentFrame-1);
				bigPlanet.hitTest.alpha = 0;
				addChild(bigPlanet);				
			}
			if(map!= null)
			{
				removeChild(map);
				map = null;
			}
			with(animPlanet)
			{
				
				if(height < 600)
				{
					height *=1.13;
					width *=1.13;
				}
				else if(height < 900)
				{
					height *=1.11;
					width *=1.11;
				}
				else if(height < 1800)
				{
					height *=1.07;
					width *=1.07;
				}
				var dx = 250-parent.x - x;
				var dy = 580-parent.y - y+850;
				var length = Math.sqrt( dx*dx + dy*dy );
				
				dx /= length; dy /= length;
				x += dx/25*length
				y += dy/25*length
			}
			if(length < 80)
			{
				animPlanet.alpha -= 0.03;
				bigPlanet.alpha += 0.03;
			}
			if(length < 20)
			{
				
				var main = Main.main;
				main.NewGame(Main.level);
				removeEventListener(Event.ENTER_FRAME,Animation);
				remove();
			}
		}
		public function onMouseDown(e:MouseEvent)
		{
			drag = true;
			map.startDrag();
			
		}
		public function remove()
		{
			options.removeEventListener(MouseEvent.MOUSE_DOWN,optionClick);
			removeEventListener(Event.ENTER_FRAME,onEnterFrame);
			removeEventListener(MouseEvent.MOUSE_DOWN,onMouseDown);
			removeEventListener(MouseEvent.MOUSE_UP,onMouseUp);
			removeChild(background);
			parent.removeChild(this);
		}
		public function onMouseUp(e:MouseEvent)
		{
			drag = false;
			map.stopDrag();
		}
	}
}