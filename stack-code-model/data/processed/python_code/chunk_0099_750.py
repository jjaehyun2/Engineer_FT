package kabam.rotmg.game.commands {
import com.company.assembleegameclient.screens.CharacterSelectionAndNewsScreen;

import kabam.rotmg.core.model.PlayerModel;
import kabam.rotmg.core.signals.InvalidateDataSignal;
import kabam.rotmg.core.signals.SetScreenSignal;
import kabam.rotmg.core.signals.SetScreenWithValidDataSignal;
import kabam.rotmg.death.model.DeathModel;
import kabam.rotmg.fame.control.ShowFameViewSignal;
import kabam.rotmg.fame.model.FameVO;
import kabam.rotmg.fame.model.SimpleFameVO;
import kabam.rotmg.messaging.impl.incoming.Death;

public class TransitionFromGameToMenuCommand {


    public function TransitionFromGameToMenuCommand() {
        super();
    }
    [Inject]
    public var player:PlayerModel;
    [Inject]
    public var model:DeathModel;
    [Inject]
    public var invalidate:InvalidateDataSignal;
    [Inject]
    public var setScreen:SetScreenSignal;
    [Inject]
    public var setScreenWithValidData:SetScreenWithValidDataSignal;
    [Inject]
    public var showFameView:ShowFameViewSignal;

    public function execute():void {
        this.invalidate.dispatch();
        if (this.model.getIsDeathViewPending()) {
            this.showDeathView();
        } else {
            this.showCurrentCharacterScreen();
        }
    }

    private function showDeathView():void {
        var _local1:Death = this.model.getLastDeath();
        var _local2:FameVO = new SimpleFameVO(this.player.getAccountId(), _local1.charId_);
        this.showFameView.dispatch(_local2);
    }

    private function showCurrentCharacterScreen():void {
        this.setScreenWithValidData.dispatch(new CharacterSelectionAndNewsScreen());
    }
}
}