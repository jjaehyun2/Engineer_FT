/**Created by the LayaAirIDE,do not modify.*/
package ui.srddzGame {
	import laya.ui.*;
	import laya.display.*; 
	import ui.gameCommon.items.PlayerInfoLeftItemUI;
	import ui.gameCommon.items.PlayerInfoBaseItemUI;
	import ui.gameCommon.items.PlayerinfoTopItemUI;
	import ui.gameCommon.items.PlayerInfoBottomItemUI;
	import ui.gameCommon.PiaoSelePartUI;

	public class PlayerInfoPageUI extends View {
		public var playerInfo3:PlayerInfoLeftItemUI;
		public var playerInfo1:PlayerInfoBaseItemUI;
		public var playerInfo2:PlayerinfoTopItemUI;
		public var laba:Box;
		public var labaTip:Animation;
		public var playerInfo0:PlayerInfoBottomItemUI;
		public var piaoPart:PiaoSelePartUI;
		public var inviteBtn:Button;
		public var leaveBtn:Button;
		public var disbandBtn:Button;
		public var startBtn:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":640},"child":[{"type":"PlayerInfoLeftItem","props":{"y":100,"x":37,"visible":true,"var":"playerInfo3","runtime":"ui.gameCommon.items.PlayerInfoLeftItemUI"}},{"type":"PlayerInfoBaseItem","props":{"y":100,"x":919,"var":"playerInfo1","runtime":"ui.gameCommon.items.PlayerInfoBaseItemUI"}},{"type":"PlayerinfoTopItem","props":{"y":-19,"x":356,"var":"playerInfo2","runtime":"ui.gameCommon.items.PlayerinfoTopItemUI"}},{"type":"Box","props":{"y":7,"x":970,"visible":false,"var":"laba"},"child":[{"type":"Image","props":{"skin":"gameCommon/voice/voiceBg.png"}},{"type":"Animation","props":{"y":31,"x":29,"var":"labaTip","source":"gameCommon/VoiceTip.ani"}}]},{"type":"PlayerInfoBottomItem","props":{"y":565,"x":19,"var":"playerInfo0","runtime":"ui.gameCommon.items.PlayerInfoBottomItemUI"}},{"type":"PiaoSelePart","props":{"y":476,"x":332,"var":"piaoPart","runtime":"ui.gameCommon.PiaoSelePartUI"}},{"type":"Button","props":{"y":477,"x":908,"width":117,"var":"inviteBtn","stateNum":1,"skin":"gameCommon/img_jinbi-di.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":22,"labelPadding":"0,0,2,0","labelFont":"SimHei","labelColors":"#00edc2,#00edc2,#00edc2,#00edc2","labelBold":true,"label":"邀请好友","height":50}},{"type":"Button","props":{"y":5,"x":255,"width":117,"var":"leaveBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":24,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"离开房间","height":60,"sizeGrid":"0,29,0,27"}},{"type":"Button","props":{"y":5,"x":255,"width":117,"var":"disbandBtn","stateNum":1,"skin":"common/buttonHong.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":24,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"解散房间","height":60,"sizeGrid":"0,30,0,28"}},{"type":"Button","props":{"y":477,"x":444,"width":150,"var":"startBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":30,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"开始","height":73,"sizeGrid":"0,29,0,28"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.gameCommon.items.PlayerInfoLeftItemUI",PlayerInfoLeftItemUI);
			View.regComponent("ui.gameCommon.items.PlayerInfoBaseItemUI",PlayerInfoBaseItemUI);
			View.regComponent("ui.gameCommon.items.PlayerinfoTopItemUI",PlayerinfoTopItemUI);
			View.regComponent("ui.gameCommon.items.PlayerInfoBottomItemUI",PlayerInfoBottomItemUI);
			View.regComponent("ui.gameCommon.PiaoSelePartUI",PiaoSelePartUI);
			super.createChildren();
			createView(uiView);

		}

	}
}