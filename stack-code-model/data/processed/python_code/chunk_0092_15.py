﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.ui.view.ErrorDialogMediator

package kabam.rotmg.ui.view
{
    import robotlegs.bender.bundles.mvcs.Mediator;
    import com.company.assembleegameclient.ui.dialogs.ErrorDialog;
    import kabam.rotmg.core.signals.InvalidateDataSignal;
    import kabam.rotmg.core.signals.SetScreenWithValidDataSignal;
    import kabam.rotmg.dialogs.control.CloseDialogsSignal;
    import flash.events.Event;
    import com.company.assembleegameclient.screens.CharacterSelectionAndNewsScreen;

    public class ErrorDialogMediator extends Mediator 
    {

        [Inject]
        public var view:ErrorDialog;
        [Inject]
        public var invalidateData:InvalidateDataSignal;
        [Inject]
        public var setScreenWithValidData:SetScreenWithValidDataSignal;
        [Inject]
        public var close:CloseDialogsSignal;


        override public function initialize():void
        {
            addViewListener(Event.COMPLETE, this.onComplete);
            this.view.ok.addOnce(this.onClose);
        }

        override public function destroy():void
        {
            removeViewListener(Event.COMPLETE, this.onComplete);
        }

        public function onClose():void
        {
            this.close.dispatch();
        }

        private function onComplete(_arg_1:Event):void
        {
            this.invalidateData.dispatch();
            this.setScreenWithValidData.dispatch(new CharacterSelectionAndNewsScreen());
        }


    }
}//package kabam.rotmg.ui.view