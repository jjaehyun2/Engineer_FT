/**
 * Created by Akira on 03/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.view {
    import com.bytesfromouterspace.stockbrokers.model.TransactionLogModel;
    import com.bytesfromouterspace.stockbrokers.ui.StringUtils;
    import com.bytesfromouterspace.stockbrokers.ui.components.BorderBackground;
    import com.bytesfromouterspace.stockbrokers.ui.components.ComponentBase;
    import com.bytesfromouterspace.stockbrokers.ui.components.Label;

    import flash.display.Bitmap;
    import flash.events.Event;

    public class TransactionLogView extends ComponentBase{
        private var background:BorderBackground;
        private var model:TransactionLogModel;
        private var _lblLog:Label;

        public function TransactionLogView(model:TransactionLogModel) {
            super(821, 28);
            this.model = model;
            model.addEventListener(Event.CHANGE, onModelChange);
            background = new BorderBackground(821, 28);
            background.backgroundColor = 0x017EC1;
            background.borderColor = 0x41C6F3;
            addChild(background);

            var lbl:Bitmap = theme.createBitmapLabel("Transaction Log", 10, 0xFFFFFF);
            lbl.x = 4;
            lbl.y = 6;

            addChild(lbl);
            _lblLog = new Label(700, 22, " ", 12, 0xFFFFFF, "visitor1");
            _lblLog.background.backgroundColor = 0x164259;
            _lblLog.background.borderColor = 0x12638D;
            _lblLog.x = lbl.width + 5;
            _lblLog.y = 2;
            addChild(_lblLog);
        }

        private function onModelChange(event:Event):void {
            _lblLog.text = model.lastMessage;
        }
    }
}