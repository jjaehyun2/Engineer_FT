﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.errors.ErrorConfig

package kabam.rotmg.errors
{
    import robotlegs.bender.framework.api.IConfig;
    import org.swiftsuspenders.Injector;
    import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
    import robotlegs.bender.extensions.signalCommandMap.api.ISignalCommandMap;
    import kabam.rotmg.application.api.ApplicationSetup;
    import kabam.rotmg.errors.view.ErrorMediator;
    import kabam.rotmg.errors.control.ErrorSignal;
    import kabam.rotmg.errors.control.ReportErrorToAppEngineCommand;
    import kabam.rotmg.errors.control.LogErrorCommand;

    public class ErrorConfig implements IConfig 
    {

        [Inject]
        public var injector:Injector;
        [Inject]
        public var mediatorMap:IMediatorMap;
        [Inject]
        public var commandMap:ISignalCommandMap;
        [Inject]
        public var setup:ApplicationSetup;


        public function configure():void
        {
            this.mediatorMap.map(WebMain).toMediator(ErrorMediator);
            this.mapErrorCommand();
        }

        private function mapErrorCommand():void
        {
            if (this.setup.areErrorsReported())
            {
                this.commandMap.map(ErrorSignal).toCommand(ReportErrorToAppEngineCommand);
            }
            else
            {
                this.commandMap.map(ErrorSignal).toCommand(LogErrorCommand);
            }
        }


    }
}//package kabam.rotmg.errors