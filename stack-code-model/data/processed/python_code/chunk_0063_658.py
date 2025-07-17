package  
{
	import com.greensock.TweenLite;
	import flash.display.MovieClip;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.utils.setTimeout;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class UpgradeWindow extends Window 
	{
		public var toContinue:TextField = new TextField();
		
		public var moduleList:TextField = new TextField();
		public var moduleDescription:TextField = new TextField();
		public var dropsDisplay:TextField = new TextField();
		public var upgradeCountList:Vector.<MovieClip> = new Vector.<MovieClip>();
		
		public var attractorUpgrade:UpgradeBox = new UpgradeBox();
		public var recyclingUpgrade:UpgradeBox = new UpgradeBox();
		public var cooldownUpgrade:UpgradeBox = new UpgradeBox();
		public var enginesUpgrade:UpgradeBox = new UpgradeBox();
		public var gunnersUpgrade:UpgradeBox = new UpgradeBox();
		public var detonatorUpgrade:UpgradeBox = new UpgradeBox();
		
		public var upgradeList:Array = [];
		
		public function UpgradeWindow(width:int = 448, height:int = 336, windowTitle:String = "Upgrade Your Modules") 
		{
			super(width, height, windowTitle);
			
			moduleList.defaultTextFormat = new TextFormat("_typewriter", 16, 0xFFFFFF, true, null, null, null, null, "right");
			moduleList.text =	  "Attractor:\n\n"
								+ "Recycling:\n\n"
								+ "Cool-Down:\n\n"
								+ "Engines:\n\n"
								+ "Gunners:\n\n"
								+ "Detonator:";
			moduleList.x = -width/2 + 5;
			moduleList.width = width / 2 - 40;
			moduleList.height = 210;
			moduleList.y = -height/3;
			moduleList.selectable = false;
			//moduleList.border = true;
			//moduleList.borderColor = 0xFFFFFF
			addChild(moduleList);
			
			moduleDescription.defaultTextFormat = new TextFormat("_typewriter", 14, 0xFFFFFF, true, null, null, null, null, "center");
			moduleDescription.text = "Haters are hating";
			moduleDescription.wordWrap = true;
			moduleDescription.x = 30;
			moduleDescription.width = width / 2 - 35;
			moduleDescription.height = 210;
			moduleDescription.y = -height/3;
			moduleDescription.selectable = false;
			//moduleDescription.border = true;
			//moduleDescription.borderColor = 0xFFFFFF
			moduleDescription.filters = [GlowData.WindowModuleDescriptionTextGlow];
			addChild(moduleDescription);
			
			dropsDisplay.defaultTextFormat = new TextFormat("_typewriter", 24, 0xFFFFFF, true, null, null, null, null, "center");
			dropsDisplay.text = "Module Points: " + Module.dropsCollected;
			dropsDisplay.x = -width/2 + 5;
			dropsDisplay.width = width - 10;
			dropsDisplay.height = 35;
			dropsDisplay.y = height/3 - 5;
			dropsDisplay.selectable = false;
			//dropsDisplay.border = true;
			//dropsDisplay.borderColor = 0xFFFFFF
			dropsDisplay.filters = [GlowData.WindowModuleDescriptionTextGlow];
			addChild(dropsDisplay);
			
			
			attractorUpgrade.x = recyclingUpgrade.x = cooldownUpgrade.x = enginesUpgrade.x = gunnersUpgrade.x = detonatorUpgrade.x = attractorUpgrade.width / 2 - 30;
			
			var deltaY:Number = 36;
			attractorUpgrade.y = -102;
			recyclingUpgrade.y = attractorUpgrade.y + deltaY;
			cooldownUpgrade.y = recyclingUpgrade.y + deltaY;
			enginesUpgrade.y = cooldownUpgrade.y + deltaY;
			gunnersUpgrade.y = enginesUpgrade.y + deltaY;
			detonatorUpgrade.y = gunnersUpgrade.y + deltaY;
			
			upgradeList.push(attractorUpgrade, recyclingUpgrade, cooldownUpgrade, enginesUpgrade, gunnersUpgrade, detonatorUpgrade);
			attractorUpgrade.name = "attractor";
			recyclingUpgrade.name = "recycling";
			cooldownUpgrade.name = "cooldown";
			enginesUpgrade.name = "engines";
			gunnersUpgrade.name = "gunners";
			detonatorUpgrade.name = "detonator";
			
			for (var i:int = 0; i < upgradeList.length; i++)
			{
				addChild(upgradeList[i]);
				upgradeList[i].gotoAndStop(1);
				upgradeList[i].addEventListener(MouseEvent.ROLL_OVER, highlightUpgradeBox);
				upgradeList[i].addEventListener(MouseEvent.ROLL_OUT, unhighlightUpgradeBox);
				upgradeList[i].addEventListener(MouseEvent.CLICK, purchase);
			}
			
			
			toContinue.defaultTextFormat = new TextFormat("_typewriter", 14, 0xFFFFFF, true, null, null, null, null, "center");
			toContinue.text = "SPACE to Continue";
			toContinue.x = -width/2 + 5;
			toContinue.width = width - 10
			toContinue.height = 16;
			toContinue.y = height/2 - toContinue.height - 5;
			toContinue.selectable = false;
			//toContinue.border = true;
			//toContinue.borderColor = 0xFFFFFF
			addChild(toContinue);
		}
		
		override public function fadeIn():void 
		{
			super.fadeIn();
			hookSpaceListener();
		}
		
		private function purchase(e:MouseEvent):void 
		{
			if (Module.canPurchase(e.currentTarget as UpgradeBox))
			{
				Module.purchase(e.currentTarget as UpgradeBox);
				moduleDescription.text = Module.getDescription(e.currentTarget as UpgradeBox);
				dropsDisplay.text = "Module Points: " + Module.dropsCollected;
			}
		}
		
		private function unhighlightUpgradeBox(e:MouseEvent):void 
		{
			TweenLite.to(e.currentTarget, 2, { glowFilter: { color:0xFFFFFF, blurX:8, blurY:8, strength:2, alpha:0, remove:true }} );
			moduleDescription.text = "";
		}
		
		private function highlightUpgradeBox(e:MouseEvent):void 
		{
			TweenLite.to(e.currentTarget, 0.25, { glowFilter : { color:0xFFFFFF, blurX:8, blurY:8, strength:2, alpha:1 }} );
			moduleDescription.text = Module.getDescription(e.currentTarget as UpgradeBox);
		}
		
		override public function die():void 
		{			
			super.die();
			PlayState.StartNextWaveAndUnpause();
		}
		
	}

}