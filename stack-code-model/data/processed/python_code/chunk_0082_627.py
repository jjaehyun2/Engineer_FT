/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.Items {
	import laya.ui.*;
	import laya.display.*; 

	public class HuaBotttomItemUI extends View {
		public var downImg:Image;
		public var valueImg:Image;
		public var valueNum:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"visible":true},"child":[{"type":"Image","props":{"y":0,"x":0,"var":"downImg","skin":"gametable/mahjongpai/zhengmianfangdao.png"}},{"type":"Image","props":{"y":3,"x":4,"width":84,"var":"valueImg","skin":"gametable/mahjongpai/hmei.png","height":104}},{"type":"Image","props":{"y":7,"x":58,"visible":false,"var":"valueNum","skin":"gametable/huapart/hua1.png"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}