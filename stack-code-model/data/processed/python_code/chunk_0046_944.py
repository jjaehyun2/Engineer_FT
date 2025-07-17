/**Created by the LayaAirIDE,do not modify.*/
package ui.common {
	import laya.ui.*;
	import laya.display.*; 
	import laya.html.dom.HTMLDivElement;

	public class HallNoticeInfoViewUI extends View {
		public var bg:Image;
		public var confirmBtn:Button;
		public var infoTf:HTMLDivElement;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":523,"var":"bg","skin":"common/gameBg.png","sizeGrid":"34,32,34,34","mouseThrough":true,"height":678}},{"type":"Image","props":{"y":79,"x":20.5,"width":482,"skin":"common/commonTitBg.png","height":510,"alpha":0.3,"sizeGrid":"10,10,8,14"}},{"type":"Button","props":{"y":600,"x":172.5,"width":178,"var":"confirmBtn","stateNum":1,"skin":"common/buttonLv.png","labelSize":30,"labelFont":"Helvetica","labelColors":"#ffffff,#ffffff,#ffffff","label":"确定","height":68,"sizeGrid":"0,29,0,27"}},{"type":"HTMLDivElement","props":{"y":80,"x":25,"width":474,"var":"infoTf","innerHTML":"htmlText","height":510}},{"type":"Label","props":{"y":11,"x":188.5,"width":146,"valign":"middle","text":"公告","height":65,"fontSize":34,"font":"SimHei","color":"#dbf4ee","align":"center"}}]};
		override protected function createChildren():void {
			View.regComponent("HTMLDivElement",HTMLDivElement);
			super.createChildren();
			createView(uiView);

		}

	}
}