package com {
	import flash.system.Capabilities;

	public class CapabilitiesUtils {
		public function CapabilitiesUtils() {
			//trace("avHardwareDisable: " + Capabilities.avHardwareDisable);
			//trace("hasAccessibility: " + Capabilities.hasAccessibility);
			//trace("hasAudio: " + Capabilities.hasAudio);
			//trace("hasAudioEncoder: " + Capabilities.hasAudioEncoder);
			//trace("hasEmbeddedVideo: " + Capabilities.hasEmbeddedVideo);
			//trace("hasMP3: " + Capabilities.hasMP3);
			//trace("hasPrinting: " + Capabilities.hasPrinting);
			//trace("hasScreenBroadcast: " + Capabilities.hasScreenBroadcast);
			//trace("hasScreenPlayback: " + Capabilities.hasScreenPlayback);
			//trace("hasStreamingAudio: " + Capabilities.hasStreamingAudio);
			//trace("hasVideoEncoder: " + Capabilities.hasVideoEncoder);
			//trace("isDebugger: " + Capabilities.isDebugger);
			//trace("language: " + Capabilities.language);
			//trace("localFileReadDisable: " + Capabilities.localFileReadDisable);
			//trace("manufacturer: " + Capabilities.manufacturer);
			//trace("pixelAspectRatio: " + Capabilities.pixelAspectRatio);
			//trace("screenColor: " + Capabilities.screenColor);
			//trace("screenDPI: " + Capabilities.screenDPI);
			//trace("screenResolutionX: " + Capabilities.screenResolutionX);
			//trace("screenResolutionY: " + Capabilities.screenResolutionY);
			//trace("serverString: " + Capabilities.serverString);
			//trace("version: " + Capabilities.version);
		}
		
		public static function isPlayerAIR():Boolean {
			return Capabilities.playerType == 'Desktop';
		}
		
		public static function isOSWindows():Boolean {
			return Capabilities.os.toLowerCase().indexOf('windows') > -1;
		}

		public static function isOSMac():Boolean {
			return Capabilities.os.toLowerCase().indexOf('mac') > -1;
		}

		public static function isOSLinux():Boolean {
			return ( (CapabilitiesUtils.isOSWindows() == false) && (CapabilitiesUtils.isOSMac() == false) );
		}
	}
}