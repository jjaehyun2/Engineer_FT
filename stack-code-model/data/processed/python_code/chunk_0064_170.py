/**Created by the LayaAirIDE,do not modify.*/
package ui.gameCommon {
	import laya.ui.*;
	import laya.display.*; 

	public class VoiceShowUI extends View {
		public var ani:Animation;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":89,"height":60},"child":[{"type":"Image","props":{"y":0,"x":14,"skin":"gameCommon/voice/voiceBg.png"}},{"type":"Animation","props":{"y":31,"x":45,"var":"ani","source":"gameCommon/VoiceTipSelf.ani","name":"playLoop"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}