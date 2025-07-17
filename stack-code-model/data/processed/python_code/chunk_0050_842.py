/**Created by the LayaAirIDE,do not modify.*/
package ui.gameCommon.items {
	import laya.ui.*;
	import laya.display.*; 

	public class DissolvePlayerItemUI extends View {
		public var nameTf:Label;
		public var toDealTf:Label;
		public var agreenImg:Image;
		public var opposeImg:Image;
		public var headImg:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":90,"height":160},"child":[{"type":"Image","props":{"y":34,"x":9,"width":70,"skin":"gameCommon/img_wanjiatouxiang-di.png","sizeGrid":"47,21,33,26","height":70}},{"type":"Label","props":{"y":0,"x":2,"wordWrap":false,"width":87,"visible":true,"var":"nameTf","valign":"middle","text":"玩家名字对对对","overflow":"hidden","height":28,"fontSize":18,"font":"SimHei","color":"#c7edfb","align":"center"}},{"type":"Label","props":{"y":122,"x":2,"wordWrap":false,"width":87,"visible":true,"var":"toDealTf","valign":"middle","text":"等待投票","overflow":"hidden","height":28,"fontSize":18,"font":"SimHei","color":"#c7edfb","align":"center"}},{"type":"Image","props":{"y":114,"x":23,"var":"agreenImg","skin":"common/gou.png"}},{"type":"Image","props":{"y":116,"x":27,"var":"opposeImg","skin":"common/cha.png"}},{"type":"Box","props":{"y":36,"x":11},"child":[{"type":"Image","props":{"y":0,"width":66,"var":"headImg","skin":"common/morentouxiang.png","height":66}},{"type":"Image","props":{"x":0,"width":66,"skin":"gameCommon/img_wanjiatouxiang-di.png","sizeGrid":"47,21,33,26","renderType":"mask","height":66}}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}