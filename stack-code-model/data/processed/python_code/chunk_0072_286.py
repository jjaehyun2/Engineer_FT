/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.Items {
	import laya.ui.*;
	import laya.display.*; 

	public class RightHandleItemUI extends View {
		public var LiangEff:Image;
		public var backImg:Image;
		public var downImg:Image;
		public var valueImg:Image;
		public var frontImg:Image;
		public var huEffImg:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"visible":true},"child":[{"type":"Image","props":{"y":0,"x":-119,"var":"LiangEff","skin":"gametable/liang0001.png"}},{"type":"Image","props":{"y":28,"x":-66,"visible":false,"var":"backImg","skin":"gametable/mahjongpai/koupaiheng.png"}},{"type":"Image","props":{"y":28,"x":-66,"visible":false,"var":"downImg","skin":"gametable/mahjongpai/paihengtang.png"}},{"type":"Image","props":{"y":68,"x":-63,"width":108,"var":"valueImg","skin":"gametable/mahjongpai/tong9.png","scaleY":0.46,"scaleX":0.38,"rotation":-90,"height":128}},{"type":"Image","props":{"y":0,"x":-15,"visible":true,"var":"frontImg","skin":"gametable/mahjongpai/paifushilimian.png","scaleY":-1,"rotation":180,"height":88}},{"type":"Image","props":{"y":0,"x":-104,"var":"huEffImg","skin":"gametable/huanraohuoyan0001.png","scaleY":1.2,"scaleX":1.2}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}