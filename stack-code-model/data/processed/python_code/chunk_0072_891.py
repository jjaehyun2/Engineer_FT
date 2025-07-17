/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.majiangParts {
	import laya.ui.*;
	import laya.display.*; 
	import ui.mainGame.Items.LeftHandleItemUI;

	public class LeftHandlePartUI extends View {
		public var card0:LeftHandleItemUI;
		public var card1:LeftHandleItemUI;
		public var card2:LeftHandleItemUI;
		public var card3:LeftHandleItemUI;
		public var card4:LeftHandleItemUI;
		public var card5:LeftHandleItemUI;
		public var card6:LeftHandleItemUI;
		public var card7:LeftHandleItemUI;
		public var card8:LeftHandleItemUI;
		public var card9:LeftHandleItemUI;
		public var card10:LeftHandleItemUI;
		public var card11:LeftHandleItemUI;
		public var card12:LeftHandleItemUI;
		public var card13:LeftHandleItemUI;
		public var tingImg:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{},"child":[{"type":"LeftHandleItem","props":{"y":0,"x":0,"var":"card0","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":40,"x":0,"var":"card1","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":80,"x":0,"var":"card2","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":120,"x":0,"var":"card3","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":160,"x":0,"var":"card4","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":200,"x":0,"var":"card5","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":240,"x":0,"var":"card6","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":280,"x":0,"var":"card7","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":320,"x":0,"var":"card8","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":360,"x":0,"var":"card9","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":400,"x":0,"var":"card10","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":440,"x":0,"var":"card11","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":480,"x":0,"var":"card12","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"LeftHandleItem","props":{"y":534,"x":0,"var":"card13","runtime":"ui.mainGame.Items.LeftHandleItemUI"}},{"type":"Image","props":{"y":642,"x":185,"width":245,"visible":false,"var":"tingImg","rotation":180,"height":812}}]};
		override protected function createChildren():void {
			View.regComponent("ui.mainGame.Items.LeftHandleItemUI",LeftHandleItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}