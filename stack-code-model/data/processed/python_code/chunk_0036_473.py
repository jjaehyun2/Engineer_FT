/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.Items {
	import laya.ui.*;
	import laya.display.*; 

	public class HuaLeftItemUI extends View {
		public var downImg:Image;
		public var valueImg:Image;
		public var valueNum:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Image","props":{"y":0,"x":0,"visible":true,"var":"downImg","skin":"gametable/mahjongpai/paihengtang.png"}},{"type":"Image","props":{"y":-1,"x":67,"width":41,"var":"valueImg","skin":"gametable/mahjongpai/hchun.png","rotation":90,"height":67}},{"type":"Image","props":{"y":13,"x":60,"visible":false,"var":"valueNum","skin":"gametable/huapart/hua1.png","rotation":90}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}