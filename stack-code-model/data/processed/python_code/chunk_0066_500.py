package kitaec.view {

import flash.display.DisplayObject;
import flash.events.KeyboardEvent;
import flash.events.MouseEvent;
import flash.ui.Keyboard;

import kitaec.model.Model;

import mx.core.FlexGlobals;
import mx.managers.PopUpManager;

import spark.components.TitleWindow;

public class BasePopup extends TitleWindow {

    [Bindable]
    protected var model:Model = Model.getInstance();

    private var _showCloseButton:Boolean = true;
    private var closeButtonVisibleChanged:Boolean;

    public function BasePopup():void {
    }

    public function show(modal:Boolean = true):void {
        PopUpManager.addPopUp(this, FlexGlobals.topLevelApplication as DisplayObject, modal);
        PopUpManager.centerPopUp(this);
    }

    public function hide():void {
        PopUpManager.removePopUp(this);
    }

    override protected function keyDownHandler(event:KeyboardEvent):void {
        super.keyDownHandler(event);
        if(event.keyCode == Keyboard.ESCAPE) {
            hide();
        }
    }

    override protected function closeButton_clickHandler(event:MouseEvent):void {
        super.closeButton_clickHandler(event);
        hide();
    }

    public function set showCloseButton(value:Boolean):void {
        _showCloseButton = value;
        closeButtonVisibleChanged = true;
        invalidateProperties();
    }

    override protected function commitProperties():void {
        super.commitProperties();

        if(closeButtonVisibleChanged && closeButton) {
            closeButtonVisibleChanged = false;
            closeButton.visible = closeButton.includeInLayout = _showCloseButton;
        }
    }
}
}