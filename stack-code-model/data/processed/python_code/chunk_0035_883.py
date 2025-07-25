﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.promotions.commands.MakeBeginnersPackagePaymentCommand

package kabam.rotmg.promotions.commands
{
    import kabam.rotmg.account.core.PaymentData;
    import kabam.rotmg.account.core.services.MakePaymentTask;
    import kabam.lib.tasks.TaskMonitor;
    import kabam.rotmg.promotions.model.BeginnersPackageModel;
    import kabam.rotmg.packages.control.InitPackagesSignal;

    public class MakeBeginnersPackagePaymentCommand 
    {

        [Inject]
        public var data:PaymentData;
        [Inject]
        public var task:MakePaymentTask;
        [Inject]
        public var monitor:TaskMonitor;
        [Inject]
        public var model:BeginnersPackageModel;
        [Inject]
        public var init:InitPackagesSignal;


        public function execute():void
        {
            this.monitor.add(this.task);
            this.task.start();
            this.model.markAsPurchased();
            this.init.dispatch();
        }


    }
}//package kabam.rotmg.promotions.commands