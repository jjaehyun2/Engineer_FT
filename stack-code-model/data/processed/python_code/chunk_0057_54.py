package org.bigbluebutton.air.voice {
	
	import org.bigbluebutton.air.voice.views.IMicButton;
	import org.bigbluebutton.air.voice.views.MicButtonMediator;
	import org.bigbluebutton.lib.voice.commands.MicrophoneMuteCommand;
	import org.bigbluebutton.lib.voice.commands.MicrophoneMuteSignal;
	
	import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
	import robotlegs.bender.extensions.signalCommandMap.api.ISignalCommandMap;
	import robotlegs.bender.framework.api.IConfig;
	
	public class VoiceConfig implements IConfig {
		
		[Inject]
		public var mediatorMap:IMediatorMap;
		
		[Inject]
		public var signalCommandMap:ISignalCommandMap;
		
		public function configure():void {
			mediators();
			signals();
		}
		
		/**
		 * Maps view mediators to views.
		 */
		private function mediators():void {
			mediatorMap.map(IMicButton).toMediator(MicButtonMediator);
		}
		
		/**
		 * Maps signals to commands using the signalCommandMap.
		 */
		private function signals():void {
			signalCommandMap.map(MicrophoneMuteSignal).toCommand(MicrophoneMuteCommand);
		}
	}
}