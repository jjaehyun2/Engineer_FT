package kabam.rotmg.arena.view {
import flash.events.MouseEvent;

import io.decagames.rotmg.pets.data.PetsModel;

import kabam.rotmg.account.core.Account;
import kabam.rotmg.dialogs.control.OpenDialogSignal;

import robotlegs.bender.bundles.mvcs.Mediator;

public class ArenaQueryPanelMediator extends Mediator {


    public function ArenaQueryPanelMediator() {
        super();
    }
    [Inject]
    public var view:ArenaQueryPanel;
    [Inject]
    public var openDialog:OpenDialogSignal;
    [Inject]
    public var petModel:PetsModel;
    [Inject]
    public var account:Account;

    override public function initialize():void {
        this.setEventListeners();
    }

    override public function destroy():void {
        super.destroy();
    }

    private function setEventListeners():void {
        if (this.view.enterButton) {
            this.view.enterButton.addEventListener("click", this.onButtonLeftClick);
            this.view.infoButton.addEventListener("click", this.onButtonRightClick);
        } else {
            this.view.infoButton.addEventListener("click", this.onButtonRightClick);
        }
    }

    protected function onButtonRightClick(_arg_1:MouseEvent):void {
        this.openDialog.dispatch(new HostQueryDialog());
    }

    protected function onButtonLeftClick(_arg_1:MouseEvent):void {
        this.openDialog.dispatch(new ArenaLeaderboard());
    }
}
}