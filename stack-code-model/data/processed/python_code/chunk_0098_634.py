/**Created by the LayaAirIDE,do not modify.*/
package ui.common {
	import laya.ui.*;
	import laya.display.*; 
	import laya.html.dom.HTMLDivElement;

	public class InfoListViewUI extends View {
		public var messageTf:HTMLDivElement;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":1038},"child":[{"type":"Box","props":{"y":228.5,"x":306.5,"height":581},"child":[{"type":"Image","props":{"y":0,"x":4,"width":421,"skin":"common/gameBg.png","sizeGrid":"34,32,34,34","height":578}},{"type":"Image","props":{"y":89,"x":24,"width":382,"skin":"common/commonTitBg.png","height":462,"sizeGrid":"10,10,8,14"}},{"type":"HTMLDivElement","props":{"y":102,"x":34,"width":363,"var":"messageTf","innerHTML":"55565565","height":431}},{"type":"Box","props":{"y":14,"x":28.5},"child":[{"type":"Image","props":{"width":372,"skin":"common/commonTitBg.png","height":66,"sizeGrid":"10,10,8,14"}},{"type":"Label","props":{"x":113,"width":146,"valign":"middle","text":"消息列表","height":65,"fontSize":34,"font":"SimHei","color":"#c7edfb","align":"center"}}]}]}]};
		override protected function createChildren():void {
			View.regComponent("HTMLDivElement",HTMLDivElement);
			super.createChildren();
			createView(uiView);

		}

	}
}