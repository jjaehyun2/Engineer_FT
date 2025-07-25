﻿package kabam.rotmg.ui.view {
import com.company.assembleegameclient.objects.Player;
import com.company.assembleegameclient.parameters.Parameters;
import com.company.assembleegameclient.ui.ExperienceBoostTimerPopup;
import com.company.assembleegameclient.ui.StatusBar;

import flash.display.Sprite;
import flash.events.Event;

import kabam.rotmg.text.model.TextKey;

public class StatMetersView extends Sprite {

    private var expBar_:StatusBar;
    private var fameBar_:StatusBar;
    private var hpBar_:StatusBar;
    private var mpBar_:StatusBar;
    private var expBarBackground_:StatusBar;
    private var fameBarBackground_:StatusBar;
    private var hpBarBackground_:StatusBar;
    private var mpBarBackground_:StatusBar;
    private var areTempXpListenersAdded:Boolean;
    private var curXPBoost:int;
    private var expTimer:ExperienceBoostTimerPopup;

    public function StatMetersView() {
        this.expBarBackground_ = new StatusBar(176, 16, 0x545454, 0x545454, null);
        this.expBar_ = new StatusBar(176, 16, 5931045, 0x545454, TextKey.EXP_BAR_LEVEL);
        this.fameBarBackground_ = new StatusBar(176, 16, 0x545454, 0x545454, null);
        this.fameBar_ = new StatusBar(176, 16, 0xE25F00, 0x545454, TextKey.CURRENCY_FAME);
        this.hpBarBackground_ = new StatusBar(176, 16, 0x545454, 0x545454, null);
        this.hpBar_ = new StatusBar(176, 16, 14693428, 0x545454, TextKey.STATUS_BAR_HEALTH_POINTS);
        this.mpBarBackground_ = new StatusBar(176, 16, 0x545454, 0x545454, null);
        this.mpBar_ = new StatusBar(176, 16, 6325472, 0x545454, TextKey.STATUS_BAR_MANA_POINTS);
        this.hpBar_.y = this.hpBarBackground_.y = 24;
        this.mpBar_.y = this.mpBarBackground_.y = 48;
        this.expBarBackground_.visible = true;
        this.expBar_.visible = true;
        this.fameBarBackground_.visible = false;
        this.fameBar_.visible = false;
        addChild(this.expBarBackground_);
        addChild(this.expBar_);
        addChild(this.fameBarBackground_);
        addChild(this.fameBar_);
        addChild(this.hpBarBackground_);
        addChild(this.hpBar_);
        addChild(this.mpBarBackground_);
        addChild(this.mpBar_);
    }

    public function update(_arg1:Player):void {
        this.expBar_.setLabelText(TextKey.EXP_BAR_LEVEL, {"level": _arg1.level_});
        if (_arg1.level_ < 20) {
            if (this.expTimer) {
                this.expTimer.update(_arg1.xpTimer);
            }
            if (!this.expBar_.visible) {
                this.expBarBackground_.visible = true;
                this.expBar_.visible = true;
                this.fameBarBackground_.visible = false;
                this.fameBar_.visible = false;
            }
            this.expBarBackground_.draw(1, 1, 0, 1);
            this.expBar_.draw(_arg1.exp_, _arg1.nextLevelExp_, 0);
            if (this.curXPBoost != _arg1.xpBoost_) {
                this.curXPBoost = _arg1.xpBoost_;
                if (this.curXPBoost) {
                    this.expBar_.showMultiplierText();
                }
                else {
                    this.expBar_.hideMultiplierText();
                }
            }
            if (_arg1.xpTimer) {
                if (!this.areTempXpListenersAdded) {
                    this.expBar_.addEventListener("MULTIPLIER_OVER", this.onExpBarOver);
                    this.expBar_.addEventListener("MULTIPLIER_OUT", this.onExpBarOut);
                    this.areTempXpListenersAdded = true;
                }
            }
            else {
                if (this.areTempXpListenersAdded) {
                    this.expBar_.removeEventListener("MULTIPLIER_OVER", this.onExpBarOver);
                    this.expBar_.removeEventListener("MULTIPLIER_OUT", this.onExpBarOut);
                    this.areTempXpListenersAdded = false;
                }
                if (((this.expTimer) && (this.expTimer.parent))) {
                    removeChild(this.expTimer);
                    this.expTimer = null;
                }
            }
        } else {
            if (!this.fameBar_.visible) {
                this.fameBarBackground_.visible = true;
                this.fameBar_.visible = true;
                this.expBarBackground_.visible = false;
                this.expBar_.visible = false;
            }
            this.fameBarBackground_.draw(1, 1, 0, 1);
            this.fameBar_.draw(_arg1.currFame_, _arg1.nextClassQuestFame_, 0);
        }
        this.hpBarBackground_.draw(1, 1, 0, 1);
        this.hpBar_.draw(_arg1.hp_, _arg1.maxHP_, Parameters.parse(_arg1.maxHPBoost_), _arg1.maxHPMax_, _arg1.level_);
        this.mpBarBackground_.draw(1, 1, 0, 1);
        this.mpBar_.draw(_arg1.mp_, _arg1.maxMP_, Parameters.parse(_arg1.maxMPBoost_), _arg1.maxMPMax_, _arg1.level_);
    }

    private function onExpBarOver(_arg1:Event):void {
        addChild((this.expTimer = new ExperienceBoostTimerPopup()));
    }

    private function onExpBarOut(_arg1:Event):void {
        if (((this.expTimer) && (this.expTimer.parent))) {
            removeChild(this.expTimer);
            this.expTimer = null;
        }
    }


}
}