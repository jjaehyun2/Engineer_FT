/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame {
	import laya.ui.*;
	import laya.display.*; 
	import ui.gameCommon.items.PlayerInfoLeftItemUI;
	import ui.gameCommon.items.PlayerInfoBaseItemUI;
	import ui.gameCommon.PiaoSelePartUI;
	import ui.gameCommon.items.PlayerinfoTopItemUI;

	public class PlayerInfoPageUI extends View {
		public var playerInfo3:PlayerInfoLeftItemUI;
		public var playerInfo0:PlayerInfoLeftItemUI;
		public var playerInfo1:PlayerInfoBaseItemUI;
		public var piaoPart:PiaoSelePartUI;
		public var playerInfo2:PlayerinfoTopItemUI;
		public var startBtn:Button;
		public var laba:Box;
		public var labaTip:Animation;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"visible":true,"sizeGrid":"38,22,24,28","height":640},"child":[{"type":"PlayerInfoLeftItem","props":{"y":150,"x":12,"visible":true,"var":"playerInfo3","runtime":"ui.gameCommon.items.PlayerInfoLeftItemUI"}},{"type":"PlayerInfoLeftItem","props":{"y":378,"x":12,"visible":true,"var":"playerInfo0","runtime":"ui.gameCommon.items.PlayerInfoLeftItemUI"}},{"type":"PlayerInfoBaseItem","props":{"y":131,"x":947,"var":"playerInfo1","runtime":"ui.gameCommon.items.PlayerInfoBaseItemUI"}},{"type":"PiaoSelePart","props":{"y":476,"x":332.5,"var":"piaoPart","runtime":"ui.gameCommon.PiaoSelePartUI"}},{"type":"PlayerinfoTopItem","props":{"y":-8,"x":74,"var":"playerInfo2","runtime":"ui.gameCommon.items.PlayerinfoTopItemUI"}},{"type":"Button","props":{"y":559,"x":429,"width":180,"var":"startBtn","stateNum":1,"skin":"common/btn_yellow.png","sizeGrid":"0,36,0,36","labelStrokeColor":"#000000","labelStroke":2,"labelSize":34,"labelFont":"SimHei","labelColors":"#ffffff,#ffffff,#ffffff","labelBold":true,"labelAlign":"center"},"child":[{"type":"Image","props":{"y":9,"x":43,"skin":"gameCommon/gameStart.png"}}]},{"type":"Box","props":{"y":3,"x":852,"visible":false,"var":"laba"},"child":[{"type":"Image","props":{"skin":"gameCommon/voice/voiceBg.png"}},{"type":"Animation","props":{"y":31,"x":29,"var":"labaTip","source":"gameCommon/VoiceTip.ani"}}]}]};
		override protected function createChildren():void {
			View.regComponent("ui.gameCommon.items.PlayerInfoLeftItemUI",PlayerInfoLeftItemUI);
			View.regComponent("ui.gameCommon.items.PlayerInfoBaseItemUI",PlayerInfoBaseItemUI);
			View.regComponent("ui.gameCommon.PiaoSelePartUI",PiaoSelePartUI);
			View.regComponent("ui.gameCommon.items.PlayerinfoTopItemUI",PlayerinfoTopItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}