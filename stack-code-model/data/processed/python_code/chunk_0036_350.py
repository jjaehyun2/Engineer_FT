﻿package kabam.rotmg.account.core.view {
import kabam.rotmg.account.core.Account;
import kabam.rotmg.account.core.signals.UpdateAccountInfoSignal;
import kabam.rotmg.account.web.WebAccount;

import robotlegs.bender.bundles.mvcs.Mediator;

public class AccountInfoMediator extends Mediator {

    [Inject]
    public var account:Account;
    [Inject]
    public var view:AccountInfoView;
    [Inject]
    public var update:UpdateAccountInfoSignal;


    override public function initialize():void {
        this.view.setInfo(this.account.getUserName(), this.account.isRegistered());
        this.updateDisplayName();
        this.update.add(this.updateLogin);
    }

    private function updateDisplayName():void {
        var _local1:WebAccount;
        if ((this.account is WebAccount)) {
            _local1 = (this.account as WebAccount);
            if (((((!((_local1 == null))) && (!((_local1.userDisplayName == null))))) && ((_local1.userDisplayName.length > 0)))) {
                this.view.setInfo(_local1.userDisplayName, this.account.isRegistered());
            }
        }
    }

    override public function destroy():void {
        this.update.remove(this.updateLogin);
    }

    private function updateLogin():void {
        this.view.setInfo(this.account.getUserName(), this.account.isRegistered());
        this.updateDisplayName();
    }


}
}