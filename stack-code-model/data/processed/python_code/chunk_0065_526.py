package kabam.rotmg.pets.view.components {
import kabam.rotmg.dialogs.control.CloseDialogsSignal;

import robotlegs.bender.bundles.mvcs.Mediator;

public class DialogCloseButtonMediator extends Mediator {


    public function DialogCloseButtonMediator() {
        super();
    }
    [Inject]
    public var view:DialogCloseButton;
    [Inject]
    public var closeDialogSignal:CloseDialogsSignal;

    override public function initialize():void {
        this.view.closeClicked.addOnce(this.closeDialog);
    }

    private function closeDialog():void {
        this.closeDialogSignal.dispatch();
    }
}
}