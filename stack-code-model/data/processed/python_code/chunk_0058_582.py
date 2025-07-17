package org.pong.mvcs.controller.bootstraps 
{
	import org.pong.mvcs.controller.commands.*;
	import org.pong.mvcs.view.signals.*;
	import org.pong.mvcs.service.signals.*;
	import org.pong.mvcs.service.signals.*;
	import robotlegs.bender.extensions.signalCommandMap.api.ISignalCommandMap;
	
	/**
	 * 
	 * Bootstrap dependency injector for all Commands.
	 * 
	 * @see org.pong.mvcs.AppConfig
	 * 
	 * @author mc
	 */
	
	public class BootstrapSignalCommandMap 
	{	
		public function BootstrapSignalCommandMap(signalCommandMap:ISignalCommandMap) 
		{
			signalCommandMap.map(TickSignal).toCommand(TickCommand);
			
			signalCommandMap.map(StartLoadingAssetsSignal).toCommand(StartLoadingAssetsCommand);
			signalCommandMap.map(AssetsLoadingCompleteSignal).toCommand(AssetsLoadingCompleteCommand);
			signalCommandMap.map(ScreenTransitionCompleteSignal).toCommand(ScreenTransitionCompleteCommand);
			
			signalCommandMap.map(BallAddedToStageSignal).toCommand(BallAdedToStageCommand);
			
			signalCommandMap.map(BallHitWallSignal).toCommand(BallHitWallCommand);
			signalCommandMap.map(BallHitPaddleSignal).toCommand(BallHitPaddleCommand);
			
			signalCommandMap.map(PlayerWonSignal).toCommand(PlayerWonCommand);
		}
	}

}