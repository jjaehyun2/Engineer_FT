/**Created by the LayaAirIDE,do not modify.*/
package ui.hall.replay {
	import laya.ui.*;
	import laya.display.*; 
	import ui.hall.HallBgUI;

	public class BattleDetailListPageUI extends View {
		public var recordList:List;
		public var roomTypeTf:Label;
		public var roomNumTf:Label;
		public var roomidTf:Label;
		public var backBtn:Button;
		public var viewDetailBtn:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":640,"height":1038},"child":[{"type":"Box","props":{"y":1,"x":-1,"width":642,"rotation":0,"height":1038},"child":[{"type":"HallBg","props":{"runtime":"ui.hall.HallBgUI"}},{"type":"Image","props":{"y":0,"x":5,"width":630,"skin":"common/diwenju.png","mouseThrough":true,"mouseEnabled":true,"height":1032,"sizeGrid":"28,16,30,20"}},{"type":"Image","props":{"y":0,"x":5,"width":630,"skin":"common/biaoti.png","height":86,"sizeGrid":"0,41,0,43"}},{"type":"Image","props":{"y":19,"x":227.5,"skin":"hall/duijuxq.png"}},{"type":"Image","props":{"y":98,"x":20,"width":600,"skin":"common/diwen.png","height":791,"sizeGrid":"18,20,18,19"}}]},{"type":"List","props":{"y":151,"x":33,"width":575,"var":"recordList","spaceY":3,"repeatX":1,"height":637}},{"type":"Label","props":{"y":107,"x":40,"width":180,"var":"roomTypeTf","valign":"middle","text":"西周麻将","height":35,"fontSize":22,"font":"SimHei","color":"#a8e3f9","align":"left"}},{"type":"Label","props":{"y":107,"x":224,"width":103,"valign":"middle","text":"房号：","height":35,"fontSize":22,"font":"SimHei","color":"#a8e3f9","align":"right"}},{"type":"Label","props":{"y":107,"x":568,"width":31,"var":"roomNumTf","valign":"middle","text":"55","height":35,"fontSize":22,"font":"SimHei","color":"#a8e3f9","align":"right"}},{"type":"Label","props":{"y":107,"x":316,"width":96,"var":"roomidTf","valign":"middle","text":"458789","height":35,"fontSize":22,"font":"SimHei","color":"#a8e3f9","align":"center"}},{"type":"Label","props":{"y":107,"x":471,"width":103,"valign":"middle","text":"总牌局：","height":35,"fontSize":22,"font":"SimHei","color":"#a8e3f9","align":"right"}},{"type":"Box","props":{"y":817,"x":84},"child":[{"type":"Button","props":{"width":250,"var":"backBtn","stateNum":1,"skin":"common/buttonHuang.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"返回","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":273,"width":250,"var":"viewDetailBtn","stateNum":1,"skin":"common/buttonLv.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"总战绩","sizeGrid":"0,29,0,27"}}]}]};
		override protected function createChildren():void {
			View.regComponent("ui.hall.HallBgUI",HallBgUI);
			super.createChildren();
			createView(uiView);

		}

	}
}