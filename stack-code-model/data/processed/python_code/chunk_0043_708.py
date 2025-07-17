package Bezel.GCFW 
{
	/**
	 * ...
	 * @author piepie62
	 */
	
	import Bezel.Bezel;
	import Bezel.Utils.Keybind;
	import Bezel.bezel_internal;
	import Bezel.Events.EventTypes;
	import Bezel.Events.IngameClickOnSceneEvent;
	import Bezel.Events.IngameGemInfoPanelFormedEvent;
	import Bezel.Events.IngameKeyDownEvent;
	import Bezel.Events.IngameNewSceneEvent;
	import Bezel.Events.IngamePreRenderInfoPanelEvent;
	import Bezel.Events.IngameRightClickOnSceneEvent;
	import Bezel.Events.LoadSaveEvent;
	import Bezel.Events.Persistence.IngameClickOnSceneEventArgs;
	import Bezel.Events.Persistence.IngameGemInfoPanelFormedEventArgs;
	import Bezel.Events.Persistence.IngameKeyDownEventArgs;
	import Bezel.Events.Persistence.IngamePreRenderInfoPanelEventArgs;
	import Bezel.Events.SaveSaveEvent;
	import Bezel.Logger;
	import Bezel.MainLoader;

	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.utils.getDefinitionByName;
	import flash.utils.getTimer;
	
	use namespace bezel_internal;

	public class GCFWBezel implements MainLoader
	{
		// Shortcuts to gameObjects
		private var _main:Object;/*Main*/
		private var GV:Object;/*GV*/
		private var SB:Object;/*SB*/
		private var prefs:Object;/*Prefs*/
		
		private var logger:Logger;
		private var bezel:Bezel;
		
		private static const defaultHotkeys:Object = createDefaultKeyConfiguration();
		
		public function get MOD_NAME():String { return "GCFW Bezel"; }
		public function get VERSION():String { return Bezel.Bezel.VERSION; }
		public function get BEZEL_VERSION():String { return Bezel.Bezel.VERSION; }
		
		public function bind(b:Bezel, o:Object):void
		{
			for (var hotkey:String in defaultHotkeys)
			{
				b.keybindManager.registerHotkey(hotkey, defaultHotkeys[hotkey]);
			}
			
			b.keybindManager.registerHotkey("GCFW Bezel: Reload all mods", new Keybind("ctrl+alt+shift+home"));
		}
		public function unload():void {}
		
		public function GCFWBezel()
		{
		}
		
		public function get coremodInfo(): Object
		{
			return {"name": "GCFW_BEZEL_MOD_LOADER", "version": GCFWCoreMod.VERSION, "load": GCFWCoreMod.installHooks};
		}
		
		public function loaderBind(bezel:Bezel, mainGame:Object, gameObjects:Object): void
		{
			this.logger = bezel.getLogger("GCFW Bezel");
			this.bezel = bezel;
			
			this.GV = getDefinitionByName("com.giab.games.gcfw.GV") as Class;
			this.SB = getDefinitionByName("com.giab.games.gcfw.SB") as Class;
			this.prefs = getDefinitionByName("com.giab.games.gcfw.Prefs") as Class;
			gameObjects.main = mainGame;
			gameObjects.core = this.GV.ingameCore;
			gameObjects.GV = this.GV;
			gameObjects.SB = this.SB;
			gameObjects.prefs = this.prefs;

			gameObjects.mods = getDefinitionByName("com.giab.games.gcfw.Mods");
			gameObjects.constants = new Object();
			gameObjects.constants.achievementIngameStatus = getDefinitionByName("com.giab.games.gcfw.constants.AchievementIngameStatus");
			gameObjects.constants.actionStatus = getDefinitionByName("com.giab.games.gcfw.constants.ActionStatus");
			gameObjects.constants.battleMode = getDefinitionByName("com.giab.games.gcfw.constants.BattleMode");
			gameObjects.constants.battleOutcome = getDefinitionByName("com.giab.games.gcfw.constants.BattleOutcome");
			gameObjects.constants.battleTraitId = getDefinitionByName("com.giab.games.gcfw.constants.BattleTraitId");
			gameObjects.constants.beaconType = getDefinitionByName("com.giab.games.gcfw.constants.BeaconType");
			gameObjects.constants.buildingType = getDefinitionByName("com.giab.games.gcfw.constants.BuildingType");
			gameObjects.constants.dropType = getDefinitionByName("com.giab.games.gcfw.constants.DropType");
			gameObjects.constants.epicCreatureType = getDefinitionByName("com.giab.games.gcfw.constants.EpicCreatureType");
			gameObjects.constants.gameMode = getDefinitionByName("com.giab.games.gcfw.constants.GameMode");
			gameObjects.constants.gemComponentType = getDefinitionByName("com.giab.games.gcfw.constants.GemComponentType");
			gameObjects.constants.gemEnhancementId = getDefinitionByName("com.giab.games.gcfw.constants.GemEnhancementId");
			gameObjects.constants.ingameStatus = getDefinitionByName("com.giab.games.gcfw.constants.IngameStatus");
			gameObjects.constants.monsterBodyPartType = getDefinitionByName("com.giab.games.gcfw.constants.MonsterBodyPartType");
			gameObjects.constants.monsterBuffId = getDefinitionByName("com.giab.games.gcfw.constants.MonsterBuffId");
			gameObjects.constants.monsterType = getDefinitionByName("com.giab.games.gcfw.constants.MonsterType");
			gameObjects.constants.pauseType = getDefinitionByName("com.giab.games.gcfw.constants.PauseType");
			gameObjects.constants.screenId = getDefinitionByName("com.giab.games.gcfw.constants.ScreenId");
			gameObjects.constants.selectorScreenStatus = getDefinitionByName("com.giab.games.gcfw.constants.SelectorScreenStatus");
			gameObjects.constants.skillId = getDefinitionByName("com.giab.games.gcfw.constants.SkillId");
			gameObjects.constants.skillType = getDefinitionByName("com.giab.games.gcfw.constants.SkillType");
			gameObjects.constants.stageType = getDefinitionByName("com.giab.games.gcfw.constants.StageType");
			gameObjects.constants.statId = getDefinitionByName("com.giab.games.gcfw.constants.StatId");
			gameObjects.constants.strikeSpellId = getDefinitionByName("com.giab.games.gcfw.constants.StrikeSpellId");
			gameObjects.constants.talismanFragmentType = getDefinitionByName("com.giab.games.gcfw.constants.TalismanFragmentType");
			gameObjects.constants.talismanPropertyId = getDefinitionByName("com.giab.games.gcfw.constants.TalismanPropertyId");
			gameObjects.constants.targetPriorityId = getDefinitionByName("com.giab.games.gcfw.constants.TargetPriorityId");
			gameObjects.constants.tutorialId = getDefinitionByName("com.giab.games.gcfw.constants.TutorialId");
			gameObjects.constants.url = getDefinitionByName("com.giab.games.gcfw.constants.Url");
			gameObjects.constants.waveFormation = getDefinitionByName("com.giab.games.gcfw.constants.WaveFormation");
			gameObjects.constants.wizLockType = getDefinitionByName("com.giab.games.gcfw.constants.WizLockType");
			gameObjects.constants.wizStashStatus = getDefinitionByName("com.giab.games.gcfw.constants.WizStashStatus");

			var version:String = GV.main.scrMainMenu.mc.mcBottomTexts.tfDateStamp.text;
			version = version.slice(0, version.search(' ') + 1) + Bezel.Bezel.prettyVersion();
			GV.main.scrMainMenu.mc.mcBottomTexts.tfDateStamp.text = version;
			//checkForUpdates();

			GV.main.stage.addEventListener(KeyboardEvent.KEY_DOWN, stageKeyDown);

			this.logger.log("GCFW Bezel", "GCFW Bezel bound to game's objects!");
		}

		// Called after the gem's info panel has been formed but before it's returned to the game for rendering
		bezel_internal function ingameGemInfoPanelFormed(infoPanel:Object, gem:Object, numberFormatter:Object): void
		{
			bezel.dispatchEvent(new IngameGemInfoPanelFormedEvent(EventTypes.INGAME_GEM_INFO_PANEL_FORMED, new IngameGemInfoPanelFormedEventArgs(infoPanel, gem, numberFormatter)));
		}

		// Called before any of the game's logic runs when starting to form an infopanel
		// This method is called before infoPanelFormed (which should be renamed to ingameGemInfoPanelFormed)
		bezel_internal function ingamePreRenderInfoPanel(): Boolean
		{
			var eventArgs:IngamePreRenderInfoPanelEventArgs = new IngamePreRenderInfoPanelEventArgs(true);
			bezel.dispatchEvent(new IngamePreRenderInfoPanelEvent(EventTypes.INGAME_PRE_RENDER_INFO_PANEL, eventArgs));
			//logger.log("ingamePreRenderInfoPanel", "Dispatched event!");
			return eventArgs.continueDefault;
		}

		// Called immediately as a click event is fired by the base game
		// set continueDefault to false to prevent the base game's handler from running
		bezel_internal function ingameClickOnScene(event:MouseEvent, mouseX:Number, mouseY:Number, buildingX:Number, buildingY:Number): Boolean
		{
			var eventArgs:IngameClickOnSceneEventArgs = new IngameClickOnSceneEventArgs(true, event, mouseX, mouseY, buildingX, buildingY);
			bezel.dispatchEvent(new IngameClickOnSceneEvent(EventTypes.INGAME_CLICK_ON_SCENE, eventArgs));
			return eventArgs.continueDefault;
		}

		// Called immediately as a right click event is fired by the base game
		// set continueDefault to false to prevent the base game's handler from running
		bezel_internal function ingameRightClickOnScene(event:MouseEvent, mouseX:Number, mouseY:Number, buildingX:Number, buildingY:Number): Boolean
		{
			var eventArgs:IngameClickOnSceneEventArgs = new IngameClickOnSceneEventArgs(true, event, mouseX, mouseY, buildingX, buildingY);
			bezel.dispatchEvent(new IngameRightClickOnSceneEvent(EventTypes.INGAME_RIGHT_CLICK_ON_SCENE, eventArgs));
			return eventArgs.continueDefault;
		}

		// Called after the game checks that a key should be handled, but before any of the actual handling logic
		// Set continueDefault to false to prevent the base game's handler from running
		bezel_internal function ingameKeyDown(e:KeyboardEvent): Boolean
		{
			var eventArgs:IngameKeyDownEventArgs = new IngameKeyDownEventArgs(e, true);
			var keyDownEvent:IngameKeyDownEvent = new IngameKeyDownEvent(EventTypes.INGAME_KEY_DOWN, eventArgs);
			bezel.dispatchEvent(keyDownEvent);
			doHotkeyTransformation(keyDownEvent);
			return eventArgs.continueDefault;
		}

		bezel_internal function stageKeyDown(e: KeyboardEvent): void
		{
			if (this.bezel.keybindManager.getHotkeyValue("GCFW Bezel: Reload all mods").matches(e))
			{
				if (bezel.modsReloadedTimestamp + 10*1000 > getTimer())
				{
					GV.vfxEngine.createFloatingText4(GV.main.mouseX,GV.main.mouseY < 60?Number(GV.main.mouseY + 30):Number(GV.main.mouseY - 20),"Please wait 10 secods!",16768392,14,"center",Math.random() * 3 - 1.5,-4 - Math.random() * 3,0,0.55,12,0,1000);
					return;
				}
				SB.playSound("sndalert");
				GV.vfxEngine.createFloatingText4(GV.main.mouseX,GV.main.mouseY < 60?Number(GV.main.mouseY + 30):Number(GV.main.mouseY - 20),"Reloading mods!",16768392,14,"center",Math.random() * 3 - 1.5,-4 - Math.random() * 3,0,0.55,12,0,1000);
				bezel.reloadAllMods();
			}
		}

		// Called after the game is done loading its data
		bezel_internal function loadSave(): void
		{
			bezel.dispatchEvent(new LoadSaveEvent(GV.ppd, EventTypes.LOAD_SAVE));
		}

		// Called after the game is done saving its data
		bezel_internal function saveSave(): void
		{
			bezel.dispatchEvent(new SaveSaveEvent(GV.ppd, EventTypes.SAVE_SAVE));
		}

		// Called when a level is loaded or reloaded
		bezel_internal function ingameNewScene(): void
		{
			bezel.dispatchEvent(new IngameNewSceneEvent(EventTypes.INGAME_NEW_SCENE));
		}
		
		private static function createDefaultKeyConfiguration():Object
		{
			var config:Object = new Object();
			config["Throw gem bombs"] = new Keybind("b");
			config["Build tower"] = new Keybind("t");
			config["Build lantern"] = new Keybind("l");
			config["Build pylon"] = new Keybind("p");
			config["Build trap"] = new Keybind("r");
			config["Build wall"] = new Keybind("w");
			config["Combine gems"] = new Keybind("g");
			config["Switch time speed"] = new Keybind("q");
			config["Pause time"] = new Keybind("space");
			config["Start next wave"] = new Keybind("n");
			config["Destroy gem for mana"] = new Keybind("x");
			config["Drop gem to inventory"] = new Keybind("tab");
			config["Duplicate gem"] = new Keybind("d");
			config["Upgrade gem"] = new Keybind("u");
			config["Show/hide info panels"] = new Keybind("period");
			config["Cast freeze strike spell"] = new Keybind("number_1");
			config["Cast whiteout strike spell"] = new Keybind("number_2");
			config["Cast ice shards strike spell"] = new Keybind("number_3");
			config["Cast bolt enhancement spell"] = new Keybind("number_4");
			config["Cast beam enhancement spell"] = new Keybind("number_5");
			config["Cast barrage enhancement spell"] = new Keybind("number_6");
			config["Create Critical Hit gem"] = new Keybind("numpad_4");
			config["Create Mana Leeching gem"] = new Keybind("numpad_5");
			config["Create Bleeding gem"] = new Keybind("numpad_6");
			config["Create Armor Tearing gem"] = new Keybind("numpad_1");
			config["Create Poison gem"] = new Keybind("numpad_2");
			config["Create Slowing gem"] = new Keybind("numpad_3");
			config["Up arrow function"] = new Keybind("up");
			config["Down arrow function"] = new Keybind("down");
			config["Left arrow function"] = new Keybind("left");
			config["Right arrow function"] = new Keybind("right");

			return config;
		}
		
		private function doHotkeyTransformation(e:IngameKeyDownEvent):void
		{
			var origDefault:Boolean = e.eventArgs.continueDefault;
			for(var name:String in defaultHotkeys)
			{
				if(this.bezel.keybindManager.getHotkeyValue(name).matches(e))
				{
					e.eventArgs.event.keyCode = defaultHotkeys[name].key;
					e.eventArgs.event.altKey = defaultHotkeys[name].alt;
					e.eventArgs.event.ctrlKey = defaultHotkeys[name].ctrl;
					e.eventArgs.event.shiftKey = defaultHotkeys[name].shift;
					e.eventArgs.continueDefault = origDefault;
					return;
				}
				else if (defaultHotkeys[name].matches(e))
				{
					e.eventArgs.continueDefault = false;
				}
			}
		}
	}

}