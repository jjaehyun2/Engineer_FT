package kitaec.view {

import kitaec.controller.Controller;
import kitaec.model.Model;

import mx.events.FlexEvent;

import spark.components.BorderContainer;
import spark.layouts.VerticalLayout;

public class BaseView extends BorderContainer {

    [Bindable]
    protected var model:Model = Model.getInstance();
    [Bindable]
    protected var controller:Controller = Controller.getInstance();

    public function BaseView():void {
        var vlayout:VerticalLayout = new VerticalLayout();
        vlayout.paddingBottom = 10;
        vlayout.paddingLeft = 10;
        vlayout.paddingRight = 10;
        vlayout.paddingTop = 10;
        layout = vlayout;

        addEventListener(FlexEvent.ADD, onShow);
    }

    protected function onShow(event:FlexEvent):void {

    }
}
}