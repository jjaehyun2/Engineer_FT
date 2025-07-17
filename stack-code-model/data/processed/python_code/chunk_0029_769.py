/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.Items {
	import laya.ui.*;
	import laya.display.*; 

	public class OutputBottomItemUI extends View {
		public var downImg:Image;
		public var backImg:Image;
		public var valueImg:Image;
		public var huEffImg:Image;
		public var chiMark:Image;
		public var pengMark:Image;
		public var curIdxSimbol:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"visible":true},"child":[{"type":"Image","props":{"y":0,"x":0,"var":"downImg","skin":"gametable/mahjongpai/zhengmianfangdao.png"}},{"type":"Image","props":{"y":0,"x":0,"visible":false,"var":"backImg","skin":"gametable/mahjongpai/koupaishu.png"}},{"type":"Image","props":{"y":3,"x":0,"var":"valueImg","skin":"gametable/mahjongpai/tong9.png","scaleY":1.4,"scaleX":1.4}},{"type":"Image","props":{"y":-68,"x":-51,"var":"huEffImg","skin":"gametable/huanraohuoyan0001.png","scaleY":3,"scaleX":1.6}},{"type":"Image","props":{"y":74,"x":25,"visible":false,"var":"chiMark","skin":"gametable/chengbao/pengpaijiantou3_lan.png","scaleY":1.5,"scaleX":1.5,"rotation":0}},{"type":"Image","props":{"y":75,"x":27,"var":"pengMark","skin":"gametable/chengbao/pengpaijiantou1_lan.png","scaleY":1.5,"scaleX":1.5}},{"type":"Image","props":{"y":-28,"x":18,"visible":false,"var":"curIdxSimbol","skin":"gametable/xiaotuoluo.png","scaleY":1.6,"scaleX":1.6}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}