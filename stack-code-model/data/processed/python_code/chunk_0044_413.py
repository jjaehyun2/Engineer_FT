/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.majiangParts {
	import laya.ui.*;
	import laya.display.*; 
	import ui.mainGame.Items.RightHandleItemUI;

	public class RightHandlePartUI extends View {
		public var card13:RightHandleItemUI;
		public var card12:RightHandleItemUI;
		public var card11:RightHandleItemUI;
		public var card10:RightHandleItemUI;
		public var card9:RightHandleItemUI;
		public var card8:RightHandleItemUI;
		public var card7:RightHandleItemUI;
		public var card6:RightHandleItemUI;
		public var card5:RightHandleItemUI;
		public var card4:RightHandleItemUI;
		public var card3:RightHandleItemUI;
		public var card2:RightHandleItemUI;
		public var card1:RightHandleItemUI;
		public var card0:RightHandleItemUI;
		public var tingImg:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{},"child":[{"type":"RightHandleItem","props":{"y":0,"x":0,"width":53,"var":"card13","height":41,"runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":54,"x":0,"var":"card12","height":41,"runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":94,"x":0,"var":"card11","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":134,"x":0,"var":"card10","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":174,"x":0,"var":"card9","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":214,"x":0,"var":"card8","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":254,"x":0,"var":"card7","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":294,"x":0,"var":"card6","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":334,"x":0,"var":"card5","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":374,"x":0,"var":"card4","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":414,"x":0,"var":"card3","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":454,"x":0,"var":"card2","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":494,"x":0,"var":"card1","runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"RightHandleItem","props":{"y":534,"x":0,"var":"card0","height":41,"runtime":"ui.mainGame.Items.RightHandleItemUI"}},{"type":"Image","props":{"y":-170,"x":-124,"width":245,"visible":true,"var":"tingImg","height":809}}]};
		override protected function createChildren():void {
			View.regComponent("ui.mainGame.Items.RightHandleItemUI",RightHandleItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}