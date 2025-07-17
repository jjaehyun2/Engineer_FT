/**Created by the LayaAirIDE,do not modify.*/
package ui.niuniuGame {
	import laya.ui.*;
	import laya.display.*; 
	import ui.gameCommon.items.NNPlayerInfoItemSelfUI;
	import ui.gameCommon.items.NNPlayerInfoItemRightUI;

	public class PlayerInfoPageUI extends View {
		public var pos9:NNPlayerInfoItemSelfUI;
		public var pos8:NNPlayerInfoItemSelfUI;
		public var pos7:NNPlayerInfoItemSelfUI;
		public var pos6:NNPlayerInfoItemSelfUI;
		public var pos5:NNPlayerInfoItemSelfUI;
		public var pos0:NNPlayerInfoItemSelfUI;
		public var pos4:NNPlayerInfoItemRightUI;
		public var pos3:NNPlayerInfoItemRightUI;
		public var pos2:NNPlayerInfoItemRightUI;
		public var pos1:NNPlayerInfoItemRightUI;
		public var laba:Box;
		public var labaTip:Animation;
		public var leaveBtn:Button;
		public var disbandBtn:Button;
		public var inviteBtn:Button;
		public var startBtn:Button;
		public var readyBtn:Button;
		public var gameEndBtn:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":640},"child":[{"type":"NNPlayerInfoItemSelf","props":{"y":325,"x":4,"var":"pos9","runtime":"ui.gameCommon.items.NNPlayerInfoItemSelfUI"}},{"type":"NNPlayerInfoItemSelf","props":{"y":199,"x":39,"var":"pos8","runtime":"ui.gameCommon.items.NNPlayerInfoItemSelfUI"}},{"type":"NNPlayerInfoItemSelf","props":{"y":114,"x":172,"var":"pos7","runtime":"ui.gameCommon.items.NNPlayerInfoItemSelfUI"}},{"type":"NNPlayerInfoItemSelf","props":{"y":66,"x":306,"var":"pos6","runtime":"ui.gameCommon.items.NNPlayerInfoItemSelfUI"}},{"type":"NNPlayerInfoItemSelf","props":{"y":53,"x":465,"var":"pos5","runtime":"ui.gameCommon.items.NNPlayerInfoItemSelfUI"}},{"type":"NNPlayerInfoItemSelf","props":{"y":530,"x":6,"var":"pos0","runtime":"ui.gameCommon.items.NNPlayerInfoItemSelfUI"}},{"type":"NNPlayerInfoItemRight","props":{"y":66,"x":663,"var":"pos4","runtime":"ui.gameCommon.items.NNPlayerInfoItemRightUI"}},{"type":"NNPlayerInfoItemRight","props":{"y":114,"x":794,"var":"pos3","runtime":"ui.gameCommon.items.NNPlayerInfoItemRightUI"}},{"type":"NNPlayerInfoItemRight","props":{"y":199,"x":921,"var":"pos2","runtime":"ui.gameCommon.items.NNPlayerInfoItemRightUI"}},{"type":"NNPlayerInfoItemRight","props":{"y":326,"x":955,"var":"pos1","runtime":"ui.gameCommon.items.NNPlayerInfoItemRightUI"}},{"type":"Box","props":{"y":90,"x":971,"visible":false,"var":"laba"},"child":[{"type":"Image","props":{"skin":"gameCommon/voice/voiceBg.png"}},{"type":"Animation","props":{"y":31,"x":29,"var":"labaTip","source":"gameCommon/VoiceTip.ani"}}]},{"type":"Button","props":{"y":5,"x":80,"width":117,"var":"leaveBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#450100","labelStroke":1,"labelSize":24,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#ffffff,#ffffff,#ffffff,#ffffff","labelBold":true,"label":"离开房间","height":60,"sizeGrid":"0,29,0,27"}},{"type":"Button","props":{"y":5,"x":80,"width":117,"var":"disbandBtn","stateNum":1,"skin":"common/buttonHong.png","labelStrokeColor":"#450100","labelStroke":1,"labelSize":24,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#ffffff,#ffffff,#ffffff,#ffffff","labelBold":true,"label":"解散房间","height":60,"sizeGrid":"0,30,0,28"}},{"type":"Button","props":{"y":525,"x":925,"width":100,"var":"inviteBtn","stateNum":1,"skin":"gameCommon/img_jinbi-di.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":22,"labelPadding":"0,0,2,0","labelFont":"SimHei","labelColors":"#00edc2,#00edc2,#00edc2,#00edc2","labelBold":true,"label":"邀请好友","height":50}},{"type":"Button","props":{"y":445,"x":444,"width":150,"var":"startBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":30,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"开始","height":73,"sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"y":445,"x":444,"width":150,"var":"readyBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":30,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"准备","height":73,"sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"y":445,"x":395,"width":247,"var":"gameEndBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":30,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"游戏已经结束","height":73,"sizeGrid":"0,29,0,27"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.gameCommon.items.NNPlayerInfoItemSelfUI",NNPlayerInfoItemSelfUI);
			View.regComponent("ui.gameCommon.items.NNPlayerInfoItemRightUI",NNPlayerInfoItemRightUI);
			super.createChildren();
			createView(uiView);

		}

	}
}