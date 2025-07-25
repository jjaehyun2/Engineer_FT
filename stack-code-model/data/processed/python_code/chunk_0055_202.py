package com.company.assembleegameclient.ui.options {
import com.company.assembleegameclient.game.GameSprite;
import com.company.assembleegameclient.objects.Player;
import com.company.assembleegameclient.parameters.Parameters;
import com.company.assembleegameclient.sound.Music;
import com.company.assembleegameclient.sound.SFX;
import com.company.assembleegameclient.ui.StatusBar;
import com.company.ui.SimpleText;
import com.company.util.AssetLibrary;

import flash.display.BitmapData;
import flash.display.Sprite;
import flash.display.StageQuality;
import flash.display.StageScaleMode;
import flash.events.Event;
import flash.events.KeyboardEvent;
import flash.events.MouseEvent;
import flash.filters.DropShadowFilter;
import flash.geom.Point;
import flash.system.Capabilities;
import flash.text.TextFieldAutoSize;
import flash.ui.Mouse;
import flash.ui.MouseCursor;
import flash.ui.MouseCursorData;

import io.decagames.rotmg.ui.buttons.SliceScalingButton;
import io.decagames.rotmg.ui.defaults.DefaultLabelFormat;
import io.decagames.rotmg.ui.sliceScaling.SliceScalingBitmap;
import io.decagames.rotmg.ui.texture.TextureParser;
import io.decagames.rotmg.utils.colors.GreyScale;

import kabam.rotmg.core.StaticInjectorContext;
import kabam.rotmg.messaging.impl.GameServerConnection;
import kabam.rotmg.ui.signals.ToggleShowTierTagSignal;
import kabam.rotmg.ui.view.components.MenuOptionsBar;

public class Options extends Sprite {

    private static const CONTROLS_TAB:String = "Controls";

    private static const HOTKEYS_TAB:String = "Hot Keys";

    private static const CHAT_TAB:String = "Chat";

    private static const GRAPHICS_TAB:String = "Graphics";

    private static const SOUND_TAB:String = "Sound";

    private static const MISC_TAB:String = "Misc";

    private static const LOOT:String = "Loot";

    private static const AIM:String = "Aim";

    private static const MISC:String = "Misc. Hacks";

    public static const CHAT_COMMAND:String = "chatCommand";

    public static const CHAT:String = "chat";

    public static const TELL:String = "tell";

    public static const GUILD_CHAT:String = "guildChat";

    public static const SCROLL_CHAT_UP:String = "scrollChatUp";

    public static const SCROLL_CHAT_DOWN:String = "scrollChatDown";

    private static const TABS:Vector.<String> = new <String>[CONTROLS_TAB, HOTKEYS_TAB, CHAT_TAB,
        GRAPHICS_TAB, SOUND_TAB, MISC_TAB, LOOT, AIM, MISC];

    private static var registeredCursors:Vector.<String> = new Vector.<String>(0);

    public static function setDefault(param1:SliceScalingButton, param2:String, param3:int = 100, param4:Boolean = true):void {
        param1.setLabel(param2, DefaultLabelFormat.defaultModalTitle);
        param1.x = 0;
        param1.y = 0;
        param1.width = param3;
        if (param4) {
            GreyScale.greyScaleToDisplayObject(param1, true);
        }
    }

    public static function refreshCursor():void {
        var _local1:MouseCursorData = null;
        var _local2:Vector.<BitmapData> = null;
        if (Parameters.data.cursorSelect != MouseCursor.AUTO && registeredCursors.indexOf(Parameters.data.cursorSelect) == -1) {
            _local1 = new MouseCursorData();
            _local1.hotSpot = new Point(15, 15);
            _local2 = new Vector.<BitmapData>(1, true);
            _local2[0] = AssetLibrary.getImageFromSet("cursorsEmbed", int(Parameters.data.cursorSelect));
            _local1.data = _local2;
            Mouse.registerCursor(Parameters.data.cursorSelect, _local1);
            registeredCursors.push(Parameters.data.cursorSelect);
        }
        Mouse.cursor = Parameters.data.cursorSelect;
    }

    public static function toggleQualityOption(_arg1:Boolean):void {
        if (WebMain.STAGE != null) {
            WebMain.STAGE.quality = !!_arg1 ? StageQuality.HIGH : StageQuality.LOW;
        }
    }

    private static function onToggleTierTag():void {
        StaticInjectorContext.getInjector().getInstance(ToggleShowTierTagSignal).dispatch(Parameters.data.showTierTag);
    }

    private static function onBarTextToggle():void {
        StatusBar.barTextSignal.dispatch(Parameters.data.toggleBarText);
    }

    public function Options(gs:GameSprite) {
        var tab:OptionsTabTitle = null;
        this.tabs_ = new Vector.<OptionsTabTitle>();
        this.options_ = new Vector.<Sprite>();
        super();
        this.gs_ = gs;
        graphics.clear();
        graphics.beginFill(2829099, 0.8);
        graphics.drawRect(0, 0, 800, 600);
        graphics.endFill();
        graphics.lineStyle(1, 6184542);
        graphics.moveTo(0, 100);
        graphics.lineTo(800, 100);
        graphics.lineStyle();
        this.title_ = new SimpleText(36, 16777215, false, 800, 0);
        this.title_.setBold(true);
        this.title_.htmlText = "<p align=\"center\">Options</p>";
        this.title_.autoSize = TextFieldAutoSize.CENTER;
        this.title_.filters = [new DropShadowFilter(0, 0, 0)];
        this.title_.updateMetrics();
        this.title_.x = 800 / 2 - this.title_.width / 2;
        this.title_.y = 8;
        addChild(this.title_);
        this.optionsBackground = TextureParser.instance.getSliceScalingBitmap("UI", "popup_header_title", 800);
        this.optionsBackground.y = 510;
        addChild(this.optionsBackground);
        this.continueButton_ = new SliceScalingButton(TextureParser.instance.getSliceScalingBitmap("UI", "generic_green_button"));
        setDefault(this.continueButton_, "continue", 100, false);
        this.continueButton_.addEventListener(MouseEvent.CLICK, this.onContinueClick);
        this.resetToDefaultsButton_ = new SliceScalingButton(TextureParser.instance.getSliceScalingBitmap("UI", "generic_green_button"));
        setDefault(this.resetToDefaultsButton_, "reset to default", 100, true);
        this.resetToDefaultsButton_.addEventListener(MouseEvent.CLICK, this.onResetToDefaultsClick);
        this.homeButton_ = new SliceScalingButton(TextureParser.instance.getSliceScalingBitmap("UI", "generic_green_button"));
        setDefault(this.homeButton_, "back to home", 100, true);
        this.menuOptionsBar = new MenuOptionsBar();
        this.menuOptionsBar.addButton(this.continueButton_, MenuOptionsBar.CENTER);
        this.menuOptionsBar.addButton(this.resetToDefaultsButton_, MenuOptionsBar.LEFT);
        this.menuOptionsBar.addButton(this.homeButton_, MenuOptionsBar.RIGHT);
        this.continueButton_.y = this.continueButton_.y + 7;
        this.resetToDefaultsButton_.x = this.resetToDefaultsButton_.x - 120;
        this.resetToDefaultsButton_.y = this.resetToDefaultsButton_.y + 7;
        this.homeButton_.x = this.homeButton_.x + 120;
        this.homeButton_.y = this.homeButton_.y + 7;
        this.homeButton_.addEventListener(MouseEvent.CLICK, this.onHomeClick);
        addChild(this.menuOptionsBar);
        var xOffset:int = 14;
        for (var i:int = 0; i < TABS.length; i++) {
            tab = new OptionsTabTitle(TABS[i]);
            tab.x = xOffset;
            tab.y = 70;
            addChild(tab);
            tab.addEventListener(MouseEvent.CLICK, this.onTabClick);
            this.tabs_.push(tab);
            xOffset = xOffset + 81;
        }
        addEventListener(Event.ADDED_TO_STAGE, this.onAddedToStage);
        addEventListener(Event.REMOVED_FROM_STAGE, this.onRemovedFromStage);
    }
    private var gs_:GameSprite;
    private var title_:SimpleText;
    private var continueButton_:SliceScalingButton;
    private var resetToDefaultsButton_:SliceScalingButton;
    private var homeButton_:SliceScalingButton;
    private var menuOptionsBar:MenuOptionsBar;
    private var optionsBackground:SliceScalingBitmap;
    private var tabs_:Vector.<OptionsTabTitle>;
    private var selected_:OptionsTabTitle = null;
    private var options_:Vector.<Sprite>;
    private var optionIndex_:int = 0;

    public function onUIQualityToggle():void {
        this.toggleQuality(Parameters.data.uiQuality);
    }

    public function toggleQuality(_arg1:Boolean):void {
        if (WebMain.STAGE != null) {
            WebMain.STAGE.quality = !!_arg1 ? StageQuality.HIGH : StageQuality.LOW;
        }
    }

    private function setSelected(tab:OptionsTabTitle):void {
        if (tab == this.selected_) {
            return;
        }
        if (this.selected_ != null) {
            this.selected_.setSelected(false);
        }
        this.selected_ = tab;
        this.selected_.setSelected(true);
        this.removeOptions();
        switch (this.selected_.text_) {
            case CONTROLS_TAB:
                this.addControlsOptions();
                break;
            case HOTKEYS_TAB:
                this.addHotKeysOptions();
                break;
            case CHAT_TAB:
                this.addChatOptions();
                break;
            case GRAPHICS_TAB:
                this.addGraphicsOptions();
                break;
            case SOUND_TAB:
                this.addSoundOptions();
                break;
            case MISC_TAB:
                this.addMiscOptions();
                break;
            case LOOT:
                this.addLootOptions();
                break;
            case AIM:
                this.addAimOptions();
                break;
            case MISC:
                this.addMiscHackOptions();
                break;
        }
    }

    private function close():void {
        stage.focus = null;
        parent.removeChild(this);
    }

    private function removeOptions():void {
        var option:Sprite = null;
        for each(option in this.options_) {
            removeChild(option);
        }
        this.options_.length = 0;
        this.optionIndex_ = 0;
    }

    private function addControlsOptions():void {
        this.addOption(new KeyMapper("moveUp", "Move Up", "Key to will move character up"));
        this.addOption(new KeyMapper("moveLeft", "Move Left", "Key to will move character to the left"));
        this.addOption(new KeyMapper("moveDown", "Move Down", "Key to will move character down"));
        this.addOption(new KeyMapper("moveRight", "Move Right", "Key to will move character to the right"));
        this.addOption(new ChoiceOption("allowRotation", new <String>["On", "Off"], [true, false], "Allow Camera Rotation", "Toggles whether to allow for camera rotation", this.onAllowRotationChange));
        this.addOption(new Sprite());
        this.addOption(new KeyMapper("rotateLeft", "Rotate Left", "Key to will rotate the camera to the left", !Parameters.data.allowRotation));
        this.addOption(new KeyMapper("rotateRight", "Rotate Right", "Key to will rotate the camera to the right", !Parameters.data.allowRotation));
        this.addOption(new KeyMapper("useSpecial", "Use Special Ability", "This key will activate your special ability"));
        this.addOption(new KeyMapper("autofireToggle", "Autofire Toggle", "This key will toggle autofire"));
        this.addOption(new KeyMapper("resetToDefaultCameraAngle", "Reset To Default Camera Angle", "This key will reset the camera angle to the default " + "position"));
        this.addOption(new KeyMapper("togglePerformanceStats", "Toggle Performance Stats", "This key will toggle a display of fps and memory usage"));
        this.addOption(new KeyMapper("toggleCentering", "Toggle Centering of Player", "This key will toggle the position between centered and " + "offset"));
        this.addOption(new KeyMapper("interact", "Interact/Buy", "This key will allow you to enter a portal or buy an item"));
        this.addOption(new ChoiceOption("contextualClick", new <String>["On", "Off"], [true, false], "Contextual Click", "Toggle the contextual click functionality", null));
    }

    private function onAllowRotationChange():void {
        var keyMapper:KeyMapper = null;
        for (var i:int = 0; i < this.options_.length; i++) {
            keyMapper = this.options_[i] as KeyMapper;
            if (keyMapper != null) {
                if (keyMapper.paramName_ == "rotateLeft" || keyMapper.paramName_ == "rotateRight") {
                    keyMapper.setDisabled(!Parameters.data.allowRotation);
                }
            }
        }
    }

    private function addHotKeysOptions():void {
        this.addOption(new KeyMapper("useHealthPotion", "Use/Buy Health Potion", "This key will use health potions if available, buy if unavailable"));
        this.addOption(new KeyMapper("useMagicPotion", "Use/Buy Magic Potion", "This key will use magic potions if available, buy if unavailable"));
        this.addOption(new KeyMapper("miniMapZoomIn", "Mini-Map Zoom In", "This key will zoom in the minimap"));
        this.addOption(new KeyMapper("miniMapZoomOut", "Mini-Map Zoom Out", "This key will zoom out the minimap"));
        this.addOption(new KeyMapper("escapeToNexus", "Escape To Nexus", "This key will instantly escape you to the Nexus"));
        this.addOption(new KeyMapper("options", "Show Options", "This key will bring up the options screen"));
        this.addOption(new KeyMapper("switchTabs", "Switch Tabs", "This key will switch from available tabs"));
        var key:String = Capabilities.os.split(" ")[0] == "Mac" ? "Command" : "Ctrl";
        this.addOption(new ChoiceOption("inventorySwap", new <String>["On", "Off"], [true, false], "Switch item to/from backpack.", "Hold the " + key + " key and click on an item to swap it between your inventory and your backpack.", null));
        this.addOption(new KeyMapper("reconGuildHall", "Recon Guild Hall", "Allows you to reconnect to the Guild Hall!"));
        this.addOption(new KeyMapper("reconCloth", "Recon Cloth Bazaar", "Allows you to reconnect to the Cloth Bazaar!"));
        this.addOption(new KeyMapper("reconVault", "Recon Vault", "Allows you to reconnect to Vault!"));
        this.addOption(new KeyMapper("reconRealm", "Recon Realm", "Allows you to reconnect to Realm!"));
        this.addOption(new KeyMapper("reconMarket", "Recon Market", "Allows you to reconnect to the Market!"));
        this.addOption(new KeyMapper("GPURenderToggle", "GPU Render Toggle", "Enable and Disable the Hardware Acceleration."));
        this.addOption(new KeyMapper("uiQualityToggle", "UI Quality Toggle", "Enable High/Low UI Quality."));
        this.addOption(new KeyMapper("partyInviteWorld","Invite World Party","Invite your members Party to your World!"));
        this.addOption(new KeyMapper("partyJoinWorld","Join World Party","Join to the World you were invited!"));
    }

    private function addChatOptions():void {
        this.addOption(new KeyMapper("chat", "Activate Chat", "This key will bring up the chat input box"));
        this.addOption(new KeyMapper("chatCommand", "Start Chat Command", "This key will bring up the chat with a \'/\' prepended to " + "allow for commands such as /who, /ignore, etc."));
        this.addOption(new KeyMapper("tell", "Begin Tell", "This key will bring up a tell (private message) in the chat" + " input box"));
        this.addOption(new KeyMapper("guildChat", "Begin Guild Chat", "This key will bring up a guild chat in the chat" + " input box"));
        this.addOption(new KeyMapper("partyChat","Begin Party Chat","This key will bring up a Party Chat in the chat" + " input box"));
        this.addOption(new KeyMapper("scrollChatUp", "Scroll Chat Up", "This key will scroll up to older messages in the chat " + "buffer"));
        this.addOption(new KeyMapper("scrollChatDown", "Scroll Chat Down", "This key will scroll down to newer messages in the chat " + "buffer"));
    }

    private function addGraphicsOptions():void {
        this.addOption(new ChoiceOption("defaultCameraAngle", new <String>["45°", "0°"], [7 * Math.PI / 4, 0], "Default Camera Angle", "This toggles the default camera angle", this.onDefaultCameraAngleChange));
        this.addOption(new ChoiceOption("centerOnPlayer", new <String>["On", "Off"], [true, false], "Center On Player", "This toggles whether the player is centered or offset", null));
        this.addOption(new ChoiceOption("showQuestPortraits", new <String>["On", "Off"], [true, false], "Show Quest Portraits", "This toggles whether quest portraits are displayed", this.onShowQuestPortraitsChange));
        this.addOption(new ChoiceOption("toggleBarText", new <String>["On", "Off"], [1, 0], "Toggle HP/MP Text", "Always show text value for remaining HP/MP", onBarTextToggle));
        this.addOption(new ChoiceOption("drawShadows", new <String>["On", "Off"], [true, false], "Draw Shadows", "This toggles whether to draw shadows", null));
        this.addOption(new ChoiceOption("textBubbles", new <String>["On", "Off"], [true, false], "Draw Text Bubbles", "This toggles whether to draw text bubbles", null));
        this.addOption(new ChoiceOption("showTradePopup", new <String>["On", "Off"], [true, false], "Show Trade Request Panel", "This toggles whether to show trade requests in the " + "lower-right panel or just in chat.", null));
        this.addOption(new ChoiceOption("showGuildInvitePopup", new <String>["On", "Off"], [true, false], "Show Guild Invite Panel", "This toggles whether to show guild invites in the " + "lower-right panel or just in chat.", null));
        this.addOption(new ChoiceOption("cursorSelect", new <String>["Off", "ProX", "X2", "X3", "X4", "Corner1", "Corner2", "Symb", "Alien", "Xhair", "Dystopia+"], [MouseCursor.AUTO, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], "Custom Cursor", "Click here to change the mouse cursor. May help with aiming.", refreshCursor));
        this.addOption(new ChoiceOption("GPURender", new <String>["On", "Off"], [true, false], "Hardware Acceleration", "Enables Hardware Acceleration if your system supports it", this.renderer));
        this.addOption(new ChoiceOption("customFPS", new <String>["15", "30", "60", "144", "240", "360", "1000"],[15, 30, 60,144,240,360,1000],"FPS Cap","This allows you to select the framerate cap",onFPSToggle));
        this.addOption(new ChoiceOption("vSync", new <String>["On", "Off"],[true,false],"Enable VSync","This toggles whether to enable Vertical Sync",onVSyncToggle));
    }

    private static function onVSyncToggle() : void {
        WebMain.STAGE.vsyncEnabled = Parameters.data.vSync;
    }

    private static function onFPSToggle() : void {
        WebMain.STAGE.frameRate = Parameters.data.customFPS;
    }

    private function addMiscOptions():void {
        this.addOption(new ChoiceOption("reduceParticles", new <String>["High", "Low", "NoParticles"], [2, 1, 0], "Change Particles Effect", "Reduce or Increase the Particles Effect!", null));
        this.addOption(new ChoiceOption("itemDataOutlines", new <String>["On", "Off"], [0, 1], "Change Item Data Outlines", "Change the outlines of the xml\'s!", null));
        this.addOption(new ChoiceOption("hpBars", new <String>["On", "Off"], [true, false], "Health Bars", "This toggles whether to health bars under entities (players & enemies).", null));
        this.addOption(new ChoiceOption("allyShots", new <String>["On", "Off"], [true, false], "Ally Shots", "This toggles whether to show and render ally shots. Disable this to improve performance.", null));
        this.addOption(new ChoiceOption("allyDamage", new <String>["On", "Off"], [true, false], "Ally Damage", "This toggles whether to show damage dealt to and by allies. Disable this to improve performance.", null));
        this.addOption(new ChoiceOption("allyNotifs", new <String>["On", "Off"], [true, false], "Ally Notifications", "This toggles whether to show notifications targeted at other players. Disable this to improve performance.", null));
        this.addOption(new ChoiceOption("dynamicHPcolor", new <String>["On", "Off"], [true, false], "Dynamic Damage Text Color", "Makes the damage text change color based on health", null));
        this.addOption(new ChoiceOption("smartProjectiles", new <String>["On", "Off"], [true, false], "Projectile Direction", "Makes projectiles face the direction they\'re going.", null));
        this.addOption(new ChoiceOption("projOutline", new <String>["On", "Off"], [true, false], "Projectile Outline", "Makes projectiles have an outline.", null));
        this.addOption(new ChoiceOption("sellMaxyPots", new <String>["On", "Off"], [true, false], "Sell Maxy Pots", "Sell Pots that you are Maxed.", null));
        this.addOption(new ChoiceOption("showTierTag", new <String>["On", "Off"], [true, false], "Show Tier Tag", "This toggles whether to show tier tags on your gear", onToggleTierTag));
        this.addOption(new ChoiceOption("HPBarcolors", new <String>["On", "Off"], [true, false], "HP Background Colors", "Make the background of HPBar and others have color.", null));
        this.addOption(new ChoiceOption("FS", new <String>["On", "Off"], [true, false], "Fullscreen", "Get a better view of the Game, but it cost a lot of performance. To use this, is recommended play it on Flash Player 18", this.fsv3));
        this.addOption(new ChoiceOption("hideList",new <String>["Off","Locked","Guild","Party","L/G/P"],[0,1,2,3,4],"Hide Players","Hide players on screen",null));
        this.addOption(new ChoiceOption("disableAllyParticles", new <String>["On", "Off"], [true, false], "Disable ally Particles", "Disable particles produces by shooting ally.", null));
        this.addOption(new ChoiceOption("uiQuality", new <String>["On", "Off"], [true, false], "UI Quality", "Enable High/Low UI Quality.", this.onUIQualityToggle));
        this.addOption(new ChoiceOption("disableAllParticles", new <String>["On", "Off"], [true, false], "Disable ALL Particles", "Enable/Disable ALL Particles.", null));
    }

    private function renderer():void {
        Parameters.root.dispatchEvent(new Event(Event.RESIZE));
    }

    private function fsv3():void {
        if (Parameters.data.FS) {
            stage.scaleMode = StageScaleMode.NO_SCALE;
        } else {
            stage.scaleMode = StageScaleMode.EXACT_FIT;
        }
        Parameters.root.dispatchEvent(new Event(Event.RESIZE));
    }

    private function addLootOptions():void {
        this.addOption(new ChoiceOption("lootPreview",new <String>["On", "Off"],[true,false],"Loot Preview","This toggles whether to show loot previews",null));
        this.addOption(new KeyMapper("autoDrinkKey","Auto Consume","Automatically consumes consumables when you walk near (3 tiles) a bag containing them"));
        this.addOption(new ChoiceOption("consumeNormal", new <String>["On", "Off"],[true,false],"Auto Consume Potions", "Toggles whether to consume potions with auto consume turned on", updateWanted))
        this.addOption(new ChoiceOption("LNAbility",new <String>["0","1","2","3","4","5","6"],[0,1,2,3,4,5,6],"Min Ability Tier","Minimum tier at which notifications and auto loot will function for ability items.",updateWanted));
        this.addOption(new ChoiceOption("autoLoot",new <String>["On", "Off"],[true,false],"Auto Loot","Items looted depend on min ability, ring, weapon, and armor tier settings.", null));
        this.addOption(new ChoiceOption("LNRing",new <String>["0","1","2","3","4","5","6"],[0,1,2,3,4,5,6],"Min Ring Tier","Minimum tier at which notifications and auto loot will function for rings.",updateWanted));
        this.addOption(new ChoiceOption("LNWeap",new <String>["0","1","2","3","4","5","6", "7", "8", "9", "10", "11", "12", "13"],[0,1,2,3,4,5,6,7,8,9,10,11,12, 13],"Min Weapon Tier","Minimum tier at which notifications and auto loot will function for weapons.",updateWanted));
        this.addOption(new ChoiceOption("LNArmor",new <String>["0","1","2","3","4","5","6", "7", "8", "9", "10", "11", "12", "13", "14"],[0,1,2,3,4,5,6,7,8,9,10,11,12,13, 14],"Min Armor Tier","Minimum tier at which notifications and auto loot will function for armor.",updateWanted));
        this.addOption(new ChoiceOption("potsMajor",new <String>["On", "Off"],[true,false],"Loot LIFE/MANA/ATT/DEF","High value potions.",updateWanted));
        this.addOption(new ChoiceOption("lootHP",new <String>["On", "Off"],[true,false],"Loot HP Potions to Inventory","Loots health potions from ground to inventory.",null));
        this.addOption(new ChoiceOption("potsMinor",new <String>["On", "Off"],[true,false],"Loot SPD/DEX/VIT/WIS","Low value potions.",updateWanted));
        this.addOption(new ChoiceOption("lootMP",new <String>["On", "Off"],[true,false],"Loot MP Potions to Inventory","Loots magic potions from ground to inventory.",null));
        this.addOption(new ChoiceOption("drinkPot",new <String>["On", "Off"],[true,false],"Drink Excess Potions","Drinks potions when an item is about to be looted on its slot.",null));
        this.addOption(new ChoiceOption("grandmaMode",new <String>["On", "Off"],[true,false],"Large Loot Bags and Chests","For those of you who are legally blind.",null));
        this.addOption(new KeyMapper("forgePotions","Potion Forge","Automatically forges potions together upon press"));
    }

    private function updateWanted() : void {
        Player.wantedList = null;
        gs_.map.player_.genWantedList();
    }

    private function onDefaultCameraAngleChange():void {
        Parameters.data.cameraAngle = Parameters.data.defaultCameraAngle;
        Parameters.save();
    }

    private function onShowQuestPortraitsChange():void {
        if (this.gs_ != null && this.gs_.map != null && this.gs_.map.partyOverlay_ != null && this.gs_.map.partyOverlay_.questArrow_ != null) {
            this.gs_.map.partyOverlay_.questArrow_.refreshToolTip();
        }
    }

    private function addSoundOptions():void {
        this.addOption(new ChoiceOption("playMusic", new <String>["On", "Off"], [true, false], "Play Music", "This toggles whether music is played", this.onPlayMusicChange));
        this.addOption(new Sprite());
        this.addOption(new ChoiceOption("playSFX", new <String>["On", "Off"], [true, false], "Play Sound Effects", "This toggles whether sound effects are played", this.onPlaySoundEffectsChange));
        this.addOption(new Sprite());
        this.addOption(new ChoiceOption("playPewPew", new <String>["On", "Off"], [true, false], "Play Weapon Sounds", "This toggles whether weapon sounds are played", null));
    }

    private function addAimOptions() : void {
        this.addOption(new KeyMapper("projNoClipKey","Toggle Projectile No-Clip","The key which toggles projectile no-clipping"));
        this.addOption(new ChoiceOption("noAAIgnore",new <String>["On", "Off"],[true,false],"Damage Ignored Enemies","This toggles whether to damage ignored (/aig [mobID]) enemies",null));
        this.addOption(new ChoiceOption("kaRangeSqr",
                new <String>["Infinite", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"],
                [-1, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256],
                "Kill Aura Range",
                "Sets the range for Kill Aura. Can also use /karange [integer]",null));
        this.addOption(new KeyMapper("AAHotkey","Toggle Aimbot","The key which toggles aimbot"));
        this.addOption(new KeyMapper("AAModeHotkey","Toggle Aimbot Mode","The key which toggles aimbot mode"));
        this.addOption(new KeyMapper("killAuraKey","Toggle Kill Aura","The key which toggles kill aura"));
        this.addOption(new ChoiceOption("AATargetLead",new <String>["On", "Off"],[true,false],"Target Lead","Enables leading of targets.",null));
        this.addOption(new ChoiceOption("AABoundingDist",
                new <String>["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "15", "20"],
                [1,2,3,4,5,6,7,8,9,10,15,20],"Bounding Distance","Restrict auto aim to see only as far as the bounding distance from the mouse cursor in closest to cursor aim mode.",null));

    }

    private function addMiscHackOptions() : void {
        this.addOption(new KeyMapper("godmodeKey","Toggle Godmode","The key which toggles godmode"));
        this.addOption(new ChoiceOption("noSink",new <String>["On", "Off"],[true,false],"No Sink","This toggles whether to disable the negative speed resulting from sinking",null));
        this.addOption(new ChoiceOption("autoGodmode",new <String>["On", "Off"],[true,false],"Restore Godmode","This toggles whether to automatically enable godmode when entering a new map",null));
        this.addOption(new ChoiceOption("autoSMult",new <String>["On", "Off"],[true,false],"Restore Speed Multiplier","This toggles whether to automatically restore the speed multiplier to its default value (/smult default [num]) when entering a new map",null));
        this.addOption(new KeyMapper("sMultKey","Speed Switch Key","The key which toggles between default speed mult (/smult default [num]) and switch mult (/smult switch [num])"));
        this.addOption(new ChoiceOption("panicSMult",new <String>["On", "Off"],[true,false],"Panic Mode","This toggles whether to restore the speed multiplier to default when a non-guild member enters your dungeon",null));
        this.addOption(new ChoiceOption("disableIdleWatcher",new <String>["On", "Off"],[true,false],"Disable AFK Checker","This disables the AFK checker",null));
        this.addOption(new ChoiceOption("disableDebuffs",new <String>["On", "Off"],[true,false],"Disable Debuffs","Disables client-side debuffs",null));
        this.addOption(new KeyMapper("tqKey","Teleport to Quest","The key which teleports you to quest. Make sure to also use /tppos [x] [y], where x and y are the coordinates obtained from /pos."));
        this.addOption(new KeyMapper("tqDeathKey","TQ on Death","Teleports to the current quest if it dies"));
        this.addOption(new KeyMapper("noClipKey","No Clip","Toggles whether to no clip"));
        this.addOption(new ChoiceOption("autoAcceptInv",new <String>["On", "Off"],[true,false],"Auto Accept Party","Auto accepts party invites",null));
        this.addOption(new KeyMapper("ROFKey","Toggle Rate of Fire","The key which toggles the Rate of Fire hack"));
    }

    private function onPlayMusicChange():void {
        Music.setPlayMusic(Parameters.data.playMusic);
    }

    private function onPlaySoundEffectsChange():void {
        SFX.setPlaySFX(Parameters.data.playSFX);
    }

    private function addOption(option:Sprite):void {
        option.x = this.optionIndex_ % 2 == 0 ? Number(Number(20)) : Number(Number(415));
        option.y = int(this.optionIndex_ / 2) * 44 + 122;
        addChild(option);
        option.addEventListener(Event.CHANGE, this.onChange);
        this.options_.push(option);
        this.optionIndex_++;
    }

    private function refresh():void {
        var option:Option = null;
        for (var i:int = 0; i < this.options_.length; i++) {
            option = this.options_[i] as Option;
            if (option != null) {
                option.refresh();
            }
        }
    }

    private function onContinueClick(event:MouseEvent):void {
        this.close();
    }

    private function onResetToDefaultsClick(event:MouseEvent):void {
        var option:Option = null;
        for (var i:int = 0; i < this.options_.length; i++) {
            option = this.options_[i] as Option;
            if (option != null) {
                delete Parameters.data[option.paramName_];
            }
        }
        Parameters.setDefaults();
        Parameters.save();
        this.refresh();
    }

    private function onHomeClick(event:MouseEvent):void {
        this.close();
        this.gs_.closed.dispatch();
    }

    private function onTabClick(event:MouseEvent):void {
        var tab:OptionsTabTitle = event.target as OptionsTabTitle;
        this.setSelected(tab);
    }

    private function onAddedToStage(event:Event):void {
        this.setSelected(this.tabs_[0]);
        stage.addEventListener(KeyboardEvent.KEY_DOWN, this.onKeyDown, false, 1);
        stage.addEventListener(KeyboardEvent.KEY_UP, this.onKeyUp, false, 1);
        GameServerConnection.instance.options();
    }

    private function onRemovedFromStage(event:Event):void {
        stage.removeEventListener(KeyboardEvent.KEY_DOWN, this.onKeyDown, false);
        stage.removeEventListener(KeyboardEvent.KEY_UP, this.onKeyUp, false);
        GameServerConnection.instance.options();
    }

    private function onKeyDown(event:KeyboardEvent):void {
        if (event.keyCode == Parameters.data.options) {
            this.close();
        }
        event.stopImmediatePropagation();
    }

    private function onKeyUp(event:KeyboardEvent):void {
        event.stopImmediatePropagation();
    }

    private function onChange(event:Event):void {
        this.refresh();
    }
}
}