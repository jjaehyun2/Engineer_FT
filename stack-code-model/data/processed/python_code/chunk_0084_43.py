﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.account.web.commands.WebRegisterAccountCommand

package kabam.rotmg.account.web.commands
{
    import kabam.rotmg.account.core.services.RegisterAccountTask;
    import kabam.lib.tasks.TaskMonitor;
    import kabam.rotmg.core.signals.TaskErrorSignal;
    import kabam.rotmg.account.core.signals.UpdateAccountInfoSignal;
    import kabam.rotmg.dialogs.control.OpenDialogSignal;
    import kabam.rotmg.ui.signals.EnterGameSignal;
    import kabam.rotmg.ui.signals.PollVerifyEmailSignal;
    import kabam.lib.tasks.BranchingTask;
    import kabam.lib.tasks.TaskSequence;
    import kabam.lib.tasks.DispatchSignalTask;
    import kabam.rotmg.account.web.view.WebVerifyEmailDialog;
    import kabam.lib.tasks.Task;

    public class WebRegisterAccountCommand 
    {

        [Inject]
        public var task:RegisterAccountTask;
        [Inject]
        public var monitor:TaskMonitor;
        [Inject]
        public var taskError:TaskErrorSignal;
        [Inject]
        public var updateAccount:UpdateAccountInfoSignal;
        [Inject]
        public var openDialog:OpenDialogSignal;
        [Inject]
        public var enterGame:EnterGameSignal;
        [Inject]
        public var pollVerifyEmailSignal:PollVerifyEmailSignal;


        public function execute():void
        {
            var _local_1:BranchingTask = new BranchingTask(this.task, this.makeSuccess(), this.makeFailure());
            this.monitor.add(_local_1);
            _local_1.start();
        }

        private function makeSuccess():Task
        {
            var _local_1:TaskSequence = new TaskSequence();
            _local_1.add(new DispatchSignalTask(this.updateAccount));
            _local_1.add(new DispatchSignalTask(this.openDialog, new WebVerifyEmailDialog()));
            _local_1.add(new DispatchSignalTask(this.enterGame));
            _local_1.add(new DispatchSignalTask(this.pollVerifyEmailSignal));
            return (_local_1);
        }

        private function makeFailure():DispatchSignalTask
        {
            return (new DispatchSignalTask(this.taskError, this.task));
        }

    }
}//package kabam.rotmg.account.web.commands