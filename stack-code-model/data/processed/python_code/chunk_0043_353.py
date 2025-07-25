package com.company.assembleegameclient.game {
import kabam.rotmg.game.signals.UpdateGiftStatusDisplaySignal;

public class GiftStatusModel {

    public function GiftStatusModel() {
        super();
    }
    [Inject]
    public var updateGiftStatusDisplay:UpdateGiftStatusDisplaySignal;
    public var hasGift:Boolean;

    public function setHasGift(param1:Boolean):void {
        this.hasGift = param1;
        this.updateGiftStatusDisplay.dispatch();
    }
}
}