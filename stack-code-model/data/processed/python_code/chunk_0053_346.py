﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.account.kongregate.services.KongregateLoadApiTask

package kabam.rotmg.account.kongregate.services
{
    import kabam.lib.tasks.BaseTask;
    import kabam.rotmg.account.core.services.LoadApiTask;
    import flash.display.LoaderInfo;
    import kabam.rotmg.account.kongregate.view.KongregateApi;
    import kabam.rotmg.core.view.Layers;
    import kabam.rotmg.dialogs.control.OpenDialogSignal;
    import kabam.rotmg.dialogs.control.CloseDialogsSignal;
    import flash.system.Security;
    import flash.display.DisplayObject;

    public class KongregateLoadApiTask extends BaseTask implements LoadApiTask 
    {

        [Inject]
        public var info:LoaderInfo;
        [Inject]
        public var api:KongregateApi;
        [Inject]
        public var local:KongregateSharedObject;
        [Inject]
        public var layers:Layers;
        [Inject]
        public var openDialog:OpenDialogSignal;
        [Inject]
        public var closeDialog:CloseDialogsSignal;


        override protected function startTask():void
        {
            var _local_1:String = this.info.parameters.kongregate_api_path;
            Security.allowDomain(_local_1);
            this.layers.api.addChild((this.api as DisplayObject));
            this.api.loaded.addOnce(this.onApiLoaded);
            this.api.load(_local_1);
        }

        private function onApiLoaded():void
        {
            completeTask(true);
        }


    }
}//package kabam.rotmg.account.kongregate.services