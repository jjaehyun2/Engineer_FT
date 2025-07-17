/**
 * Created by Akira on 02/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.view {

    import com.bytesfromouterspace.stockbrokers.controller.KingpinController;
    import com.bytesfromouterspace.stockbrokers.event.KingpinEvent;
    import com.bytesfromouterspace.stockbrokers.model.KingpinModel;
    import com.bytesfromouterspace.stockbrokers.ui.StringUtils;
    import com.bytesfromouterspace.stockbrokers.ui.components.Button;
    import com.bytesfromouterspace.stockbrokers.ui.components.ComponentBase;

    import flash.display.Bitmap;
    import flash.events.Event;
    import flash.events.MouseEvent;

    public class KingpinView extends ComponentBase {

        private var _model:KingpinModel;
        private var _controller:KingpinController;
        private var _lblRequired:Bitmap;
        private var _lblConditions:Bitmap;
        private var _btnPay:Button;
        private var _btnAccept:Button;

        public function KingpinView(model:KingpinModel, controller:KingpinController) {
            super(332, 26);
            this._model = model;
            this._controller = controller;
            _model.addEventListener(KingpinEvent.CHANGE, update);
            graphics.lineStyle(1, 0x297C9D);
            graphics.beginFill(0x164259);
            graphics.drawRect(0,0,_width, _height);
            _lblRequired = theme.createBitmapLabel("Requires trust level " + model.minLevel, 14, 0xFFC926 , "victor_pixel");
            _lblRequired.x = 8;
            _lblRequired.y = 4;
            addChild(_lblRequired);

            _lblConditions = theme.createBitmapLabel(
                    "Loan of " + StringUtils.formatCurrency(model.amount) + " at " + model.rate * 100 + "% / turn",
                    17, 0xFFFFFF , "visitor2");
            _lblConditions.x = 8;
            _lblConditions.y = 5;
            addChild(_lblConditions);

            _btnAccept = new Button(60, 17);
            _btnAccept.buttonBackgroundNormal = 0x333333;
            _btnAccept.buttonBorderNormal = 0x666666;
            _btnAccept.drawBackground();
            _btnAccept.setLabel("Accept", 10, 0x666666, "visitor1");
            _btnAccept.x = 266;
            _btnAccept.y = 4;
            _btnAccept.addEventListener(MouseEvent.CLICK, onAcceptRequested);
            addChild(_btnAccept);

            _btnPay = new Button(60, 17);
            _btnPay.buttonBackgroundNormal = 0xFFCC00;
            _btnPay.buttonBorderNormal = 0x666666;
            _btnPay.drawBackground();
            _btnPay.setLabel("Pay", 10, 0x666666, "visitor1");
            _btnPay.x = 266;
            _btnPay.y = 4;
            _btnPay.addEventListener(MouseEvent.CLICK, onPayRequested);
            addChild(_btnPay);

            update(null);
        }

        private function setState(state:uint):void {
            switch(state) {
                case 0: // disabled
                    _lblRequired.visible = true;
                    _lblConditions.visible = false;
                    _btnAccept.visible = false;
                    _btnPay.visible = false;
                    break;

                case 1: // enabled not accepted
                    _lblRequired.visible = false;
                    _lblConditions.visible = true;
                    _btnAccept.visible = true;
                    _btnPay.visible = false;
                    break;

                case 2: // enabled accepted
                    _lblRequired.visible = false;
                    _lblConditions.visible = true;
                    _btnAccept.visible = false;
                    _btnPay.visible = true;
                    break;
            }
        }

        private function update(event:KingpinEvent):void {
            if(_model.enabled) {
                if(_model.accepted) {
                    setState(2);
                } else {
                    setState(1);
                }
            } else {
                if(_model.accepted && !_model.paid) {
                    setState(2);
                } else {
                    setState(0);
                }
            }
        }

        private function onPayRequested(event:MouseEvent):void {
            _controller.payLoan();
        }

        private function onAcceptRequested(event:MouseEvent):void {
            _controller.acceptLoan();
        }

        public function gameEnd():void {
            _btnAccept.enabled = false;
            _btnPay.enabled = false;
        }
    }
}