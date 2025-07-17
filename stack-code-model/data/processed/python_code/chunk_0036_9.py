package com.lowoui_as.utils
{
	import flash.external.ExternalInterface;

	public class PlaySound
	{
		public static var sounder:PlaySound = new PlaySound();

		public function PlaySound()
		{
			//UISoundTheme'MercuryUISound.UISoundTheme'
		}

		public function play(soundEventName:String,soundTheme:String)
		{
			/**
			 * soundEventName:
				 * "Btn_Hover"
				 * "Btn_Click_Common"
				 * "Btn_Click_Confirm"
				 *
			 */
			ExternalInterface.call("PlayUISound",soundEventName);

			/*if (soundTheme && soundEventName) {
				onPlaySound(soundEventName, soundTheme);
			}*/
		}

		/*private function onPlaySound(soundEventName:String, soundTheme:String):Void
		{
			if (!_global.gfxProcessSound) { return; }
			if (soundTheme == undefined) { soundTheme = "default"; }
			_global.gfxProcessSound(this, soundTheme, soundEventName);
		}*/
	}
}