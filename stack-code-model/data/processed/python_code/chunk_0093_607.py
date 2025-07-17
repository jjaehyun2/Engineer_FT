/**Created by the LayaAirIDE,do not modify.*/
package ui.sddzGame {
	import laya.ui.*;
	import laya.display.*; 
	import ui.sddzGame.ddzPart.handlePart.OtherHandlePartUI;
	import ui.sddzGame.ddzPart.handlePart.OwnerHandlePartUI;
	import ui.sddzGame.ddzPart.outputPart.OtherOutputPartUI;
	import ui.sddzGame.ddzPart.outputPart.OwnerOutputPartUI;
	import ui.sddzGame.ddzPart.ActTipUI;
	import ui.sddzGame.ddzPart.PlayerCtlPartUI;
	import ui.sddzGame.ddzPart.ClockPartUI;
	import ui.sddzGame.ddzPart.DipaiPartUI;

	public class PockerPageUI extends View {
		public var wenliImg:Image;
		public var handlePart2:OtherHandlePartUI;
		public var handlePart1:OtherHandlePartUI;
		public var handlePart0:OwnerHandlePartUI;
		public var outputPart2:OtherOutputPartUI;
		public var outputPart1:OtherOutputPartUI;
		public var outputPart0:OwnerOutputPartUI;
		public var actTip2:ActTipUI;
		public var actTip1:ActTipUI;
		public var ctlPart:PlayerCtlPartUI;
		public var clockPart:ClockPartUI;
		public var actTip0:ActTipUI;
		public var dipaiPart:DipaiPartUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":640,"height":1038},"child":[{"type":"Image","props":{"y":415,"x":150,"visible":false,"var":"wenliImg","skin":"sddzGame/wenli_sddz.png"}},{"type":"OtherHandlePart","props":{"y":332,"x":34,"var":"handlePart2","scaleY":0.6,"scaleX":0.6,"runtime":"ui.sddzGame.ddzPart.handlePart.OtherHandlePartUI"}},{"type":"OtherHandlePart","props":{"y":330,"x":533,"var":"handlePart1","scaleY":0.6,"scaleX":0.6,"runtime":"ui.sddzGame.ddzPart.handlePart.OtherHandlePartUI"}},{"type":"OwnerHandlePart","props":{"y":690,"x":43,"var":"handlePart0","scaleY":0.9,"scaleX":0.9,"runtime":"ui.sddzGame.ddzPart.handlePart.OwnerHandlePartUI"}},{"type":"OtherOutputPart","props":{"y":305,"x":130,"var":"outputPart2","scaleY":0.58,"scaleX":0.58,"runtime":"ui.sddzGame.ddzPart.outputPart.OtherOutputPartUI"}},{"type":"OtherOutputPart","props":{"y":305,"x":324,"var":"outputPart1","scaleY":0.58,"scaleX":0.58,"runtime":"ui.sddzGame.ddzPart.outputPart.OtherOutputPartUI"}},{"type":"OwnerOutputPart","props":{"y":560,"x":58,"var":"outputPart0","scaleY":0.6,"scaleX":0.6,"runtime":"ui.sddzGame.ddzPart.outputPart.OwnerOutputPartUI"}},{"type":"ActTip","props":{"y":323,"x":117,"var":"actTip2","runtime":"ui.sddzGame.ddzPart.ActTipUI"}},{"type":"ActTip","props":{"y":323,"x":376,"width":0,"var":"actTip1","height":0,"runtime":"ui.sddzGame.ddzPart.ActTipUI"}},{"type":"PlayerCtlPart","props":{"y":619,"x":76,"var":"ctlPart","scaleY":0.6,"scaleX":0.6,"runtime":"ui.sddzGame.ddzPart.PlayerCtlPartUI"}},{"type":"ClockPart","props":{"y":455,"x":259,"var":"clockPart","runtime":"ui.sddzGame.ddzPart.ClockPartUI"}},{"type":"ActTip","props":{"y":578,"x":243,"var":"actTip0","runtime":"ui.sddzGame.ddzPart.ActTipUI"}},{"type":"DipaiPart","props":{"y":121,"x":196,"var":"dipaiPart","scaleY":0.7,"scaleX":0.7,"runtime":"ui.sddzGame.ddzPart.DipaiPartUI"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.sddzGame.ddzPart.handlePart.OtherHandlePartUI",OtherHandlePartUI);
			View.regComponent("ui.sddzGame.ddzPart.handlePart.OwnerHandlePartUI",OwnerHandlePartUI);
			View.regComponent("ui.sddzGame.ddzPart.outputPart.OtherOutputPartUI",OtherOutputPartUI);
			View.regComponent("ui.sddzGame.ddzPart.outputPart.OwnerOutputPartUI",OwnerOutputPartUI);
			View.regComponent("ui.sddzGame.ddzPart.ActTipUI",ActTipUI);
			View.regComponent("ui.sddzGame.ddzPart.PlayerCtlPartUI",PlayerCtlPartUI);
			View.regComponent("ui.sddzGame.ddzPart.ClockPartUI",ClockPartUI);
			View.regComponent("ui.sddzGame.ddzPart.DipaiPartUI",DipaiPartUI);
			super.createChildren();
			createView(uiView);

		}

	}
}