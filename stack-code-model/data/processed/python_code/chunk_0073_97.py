﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.account.web.commands.WebLoginCommand

package kabam.rotmg.account.web.commands
{
    import kabam.rotmg.account.web.model.AccountData;
    import kabam.rotmg.account.core.services.LoginTask;
    import kabam.lib.tasks.TaskMonitor;
    import kabam.rotmg.dialogs.control.CloseDialogsSignal;
    import kabam.rotmg.core.signals.TaskErrorSignal;
    import kabam.rotmg.account.core.signals.UpdateAccountInfoSignal;
    import kabam.rotmg.core.signals.InvalidateDataSignal;
    import kabam.rotmg.core.signals.SetScreenWithValidDataSignal;
    import kabam.rotmg.core.model.ScreenModel;
    import kabam.rotmg.packages.services.GetPackagesTask;
    import kabam.rotmg.mysterybox.services.GetMysteryBoxesTask;
    import io.decagames.rotmg.seasonalEvent.data.SeasonalEventModel;
    import kabam.lib.tasks.DispatchSignalTask;
    import kabam.lib.tasks.BranchingTask;
    import kabam.lib.tasks.TaskSequence;
    import com.company.assembleegameclient.game.GameSprite;
    import com.company.assembleegameclient.screens.CharacterTypeSelectionScreen;
    import com.company.assembleegameclient.screens.CharacterSelectionAndNewsScreen;
    import flash.display.Sprite;

    public class WebLoginCommand 
    {

        [Inject]
        public var data:AccountData;
        [Inject]
        public var loginTask:LoginTask;
        [Inject]
        public var monitor:TaskMonitor;
        [Inject]
        public var closeDialogs:CloseDialogsSignal;
        [Inject]
        public var loginError:TaskErrorSignal;
        [Inject]
        public var updateLogin:UpdateAccountInfoSignal;
        [Inject]
        public var invalidate:InvalidateDataSignal;
        [Inject]
        public var setScreenWithValidData:SetScreenWithValidDataSignal;
        [Inject]
        public var screenModel:ScreenModel;
        [Inject]
        public var getPackageTask:GetPackagesTask;
        [Inject]
        public var mysteryBoxTask:GetMysteryBoxesTask;
        [Inject]
        public var seasonalEventModel:SeasonalEventModel;
        private var setScreenTask:DispatchSignalTask;


        public function execute():void
        {
            var _local_1:BranchingTask = new BranchingTask(this.loginTask, this.makeSuccessTask(), this.makeFailureTask());
            this.monitor.add(_local_1);
            _local_1.start();
        }

        private function makeSuccessTask():TaskSequence
        {
            this.setScreenTask = new DispatchSignalTask(this.setScreenWithValidData, this.getTargetScreen());
            var _local_1:TaskSequence = new TaskSequence();
            _local_1.add(new DispatchSignalTask(this.closeDialogs));
            _local_1.add(new DispatchSignalTask(this.updateLogin));
            _local_1.add(new DispatchSignalTask(this.invalidate));
            _local_1.add(this.getPackageTask);
            _local_1.add(this.mysteryBoxTask);
            _local_1.add(this.setScreenTask);
            return (_local_1);
        }

        private function makeFailureTask():TaskSequence
        {
            var _local_1:TaskSequence = new TaskSequence();
            _local_1.add(new DispatchSignalTask(this.loginError, this.loginTask));
            return (_local_1);
        }

        private function getTargetScreen():Sprite
        {
            var _local_1:Class = this.screenModel.getCurrentScreenType();
            if (((_local_1 == null) || (_local_1 == GameSprite)))
            {
                _local_1 = ((Boolean(this.seasonalEventModel.isSeasonalMode)) ? CharacterTypeSelectionScreen : CharacterSelectionAndNewsScreen);
            }
            return (new (_local_1)());
        }



    }
}//package kabam.rotmg.account.web.commands