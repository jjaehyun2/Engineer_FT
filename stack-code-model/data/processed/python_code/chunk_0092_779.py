package kabam.rotmg.ui.commands {
import flash.display.DisplayObjectContainer;

import kabam.rotmg.ui.model.HUDModel;
import kabam.rotmg.ui.view.KeysView;

public class ShowHideKeyUICommand {


    public function ShowHideKeyUICommand() {
        super();
    }
    [Inject]
    public var contextView:DisplayObjectContainer;
    [Inject]
    public var hudModel:HUDModel;
    [Inject]
    public var isKeyUIToBeShown:Boolean;
    private var view:KeysView;

    public function execute():void {
        if (this.isKeyUIToBeShown) {
            this.view = new KeysView();
            this.view.x = 4;
            this.view.y = 4;
            this.contextView.addChild(this.view);
            this.hudModel.keysView = this.view;
        } else {
            this.view = this.hudModel.keysView;
            if (this.view && this.contextView.contains(this.view)) {
                this.contextView.removeChild(this.view);
                this.view = null;
                this.hudModel.keysView = null;
            }
        }
    }
}
}