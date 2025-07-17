/**Created by the LayaAirIDE,do not modify.*/
package ui.gameCommon.shortCutChat {
	import laya.ui.*;
	import laya.display.*; 

	public class PopChatItemUI extends View {
		public var backimg:Image;
		public var tf:Label;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Box","props":{"y":0,"x":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":423,"var":"backimg","skin":"chat/duihuakuang.png","sizeGrid":"0,51,0,50","alpha":0.8}},{"type":"Label","props":{"y":17,"x":12,"wordWrap":true,"width":392,"var":"tf","text":"快点吧，哥等的花儿都谢了发发个！","overflow":"visible","height":33,"fontSize":24,"font":"黑体","color":"#0d0c0c","bold":true,"align":"left"}}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}