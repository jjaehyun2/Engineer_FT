/**Created by the LayaAirIDE,do not modify.*/
package ui.hall.item {
	import laya.ui.*;
	import laya.display.*; 

	public class AgentItemUI extends View {
		public var playerName:Label;
		public var headImg:Image;
		public var levelImg:Image;
		public var cardNum:Label;
		public var detailBtn:Button;
		public var uidTf:Label;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":575,"visible":true,"skin":"common/diwen.png","height":100,"sizeGrid":"18,20,18,19"}},{"type":"Label","props":{"y":31,"x":99,"width":150,"visible":true,"var":"playerName","text":"哇哈哈-哇哈哈","overflow":"scroll","height":30,"fontSize":22,"font":"SimHei","color":"#c7edfb","align":"center"}},{"type":"Box","props":{"y":14,"x":20,"width":74,"visible":true,"height":74,"anchorY":0,"anchorX":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":74,"visible":true,"var":"headImg","skin":"common/morentouxiang.png","height":74,"anchorY":0}},{"type":"Box","props":{"y":0,"x":0,"width":74,"visible":true,"renderType":"mask","height":74},"child":[{"type":"Image","props":{"width":74,"visible":true,"skin":"common/touxMask.png","height":74,"sizeGrid":"13,13,12,14"}}]}]},{"type":"Image","props":{"y":10,"x":16,"width":82,"visible":true,"skin":"common/touxBg.png","height":82,"sizeGrid":"15,15,19,18"}},{"type":"Image","props":{"y":56,"x":119,"var":"levelImg","skin":"hall/level2.png"}},{"type":"Label","props":{"y":47,"x":268,"width":150,"visible":true,"var":"cardNum","text":"10000000张","overflow":"scroll","height":30,"fontSize":22,"font":"SimHei","color":"#c7edfb","align":"center"}},{"type":"Label","props":{"y":24,"x":268,"width":150,"visible":true,"text":"已赠送","overflow":"scroll","height":30,"fontSize":22,"font":"SimHei","color":"#c7edfb","align":"center"}},{"type":"Button","props":{"y":14,"x":423,"width":130,"var":"detailBtn","stateNum":1,"skin":"common/buttonLan.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":25,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"明细","height":70,"sizeGrid":"0,30,0,30"}},{"type":"Label","props":{"y":6,"x":99,"width":150,"visible":true,"var":"uidTf","text":"uid:1114","overflow":"scroll","height":30,"fontSize":22,"font":"SimHei","color":"#c7edfb","align":"center"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}