package kabam.rotmg.classes.view {
import com.company.assembleegameclient.screens.AccountScreen;
import com.company.assembleegameclient.screens.TitleMenuOption;
import com.company.rotmg.graphics.ScreenGraphic;

import flash.display.Shape;
import flash.display.Sprite;

import io.decagames.rotmg.seasonalEvent.data.SeasonalEventModel;
import io.decagames.rotmg.ui.defaults.DefaultLabelFormat;
import io.decagames.rotmg.ui.labels.UILabel;

import kabam.rotmg.core.StaticInjectorContext;
import kabam.rotmg.core.model.PlayerModel;
import kabam.rotmg.game.view.CreditDisplay;
import kabam.rotmg.ui.view.SignalWaiter;
import kabam.rotmg.ui.view.components.ScreenBase;

import org.osflash.signals.Signal;
import org.osflash.signals.natives.NativeMappedSignal;
import org.swiftsuspenders.Injector;

public class CharacterSkinView extends Sprite {


    public function CharacterSkinView() {
        super();
        this.init();
    }
    public var play:Signal;
    public var back:Signal;
    public var waiter:SignalWaiter;
    private var playBtn:TitleMenuOption;
    private var backBtn:TitleMenuOption;

    public function setPlayButtonEnabled(_arg_1:Boolean):void {
        if (!_arg_1) {
            this.playBtn.deactivate();
        }
    }

    private function init():void {
        this.makeScreenBase();
        this.makeAccountScreen();
        this.makeLines();
        this.makeCreditDisplay();
        this.makeScreenGraphic();
        this.playBtn = this.makePlayButton();
        this.backBtn = this.makeBackButton();
        this.makeListView();
        this.makeClassDetailView();
        this.waiter = this.makeSignalWaiter();
        this.play = new NativeMappedSignal(this.playBtn, "click");
        this.back = new NativeMappedSignal(this.backBtn, "click");
    }

    private function makeScreenBase():void {
        var _local1:ScreenBase = new ScreenBase();
        addChild(_local1);
    }

    private function makeAccountScreen():void {
        var _local1:AccountScreen = new AccountScreen();
        addChild(_local1);
    }

    private function makeCreditDisplay():void {
        var _local1:CreditDisplay = new CreditDisplay(null, true);
        var _local2:PlayerModel = StaticInjectorContext.getInjector().getInstance(PlayerModel);
        if (_local2 != null) {
            _local1.draw(_local2.getCredits(), _local2.getFame(), _local2.getTokens());
        }
        _local1.x = 800;
        _local1.y = 20;
        addChild(_local1);
    }

    private function makeLines():void {
        var _local1:Shape = new Shape();
        _local1.graphics.clear();
        _local1.graphics.lineStyle(2, 0x545454);
        _local1.graphics.moveTo(0, 105);
        _local1.graphics.lineTo(800, 105);
        _local1.graphics.moveTo(346, 105);
        _local1.graphics.lineTo(346, 526);
        addChild(_local1);
    }

    private function makeScreenGraphic():void {
        var _local1:ScreenGraphic = new ScreenGraphic();
        addChild(_local1);
    }

    private function makePlayButton():TitleMenuOption {
        var _local1:TitleMenuOption = new TitleMenuOption("Screens.play", 36, false);
        _local1.setAutoSize("center");
        _local1.setVerticalAlign("middle");
        _local1.x = 400 - _local1.width / 2;
        _local1.y = 550;
        addChild(_local1);
        return _local1;
    }

    private function makeBackButton():TitleMenuOption {
        var _local1:* = null;
        _local1 = new TitleMenuOption("Screens.back", 22, false);
        _local1.setVerticalAlign("middle");
        _local1.x = 30;
        _local1.y = 550;
        addChild(_local1);
        return _local1;
    }

    private function makeListView():void {
        var _local1:* = null;
        var _local3:* = null;
        var _local4:Injector = StaticInjectorContext.getInjector();
        var _local2:SeasonalEventModel = _local4.getInstance(SeasonalEventModel);
        if (_local2.isChallenger) {
            _local1 = new UILabel();
            DefaultLabelFormat.createLabelFormat(_local1, 18, 0xff0000, "center", true);
            _local1.width = 200;
            _local1.multiline = true;
            _local1.wordWrap = true;
            _local1.text = "Skins are not available in Rifts Mode";
            _local1.x = 600 - _local1.width / 2;
            _local1.y = (600 - _local1.height) / 2;
            addChild(_local1);
        } else {
            _local3 = new CharacterSkinListView();
            _local3.x = 351;
            _local3.y = 110;
            addChild(_local3);
        }
    }

    private function makeClassDetailView():void {
        var _local1:* = null;
        _local1 = new ClassDetailView();
        _local1.x = 5;
        _local1.y = 110;
        addChild(_local1);
    }

    private function makeSignalWaiter():SignalWaiter {
        var _local1:SignalWaiter = new SignalWaiter();
        _local1.push(this.playBtn.changed);
        _local1.complete.add(this.positionOptions);
        return _local1;
    }

    private function positionOptions():void {
        this.playBtn.x = stage.stageWidth / 2;
    }
}
}