/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.Items {
	import laya.ui.*;
	import laya.display.*; 
	import ui.mainGame.Items.OutputRightItemUI;
	import ui.mainGame.Items.OutputTopItemUI;

	public class RightPengGangItemUI extends View {
		public var card2:OutputRightItemUI;
		public var card1:OutputRightItemUI;
		public var card0:OutputRightItemUI;
		public var card3:OutputTopItemUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{},"child":[{"type":"OutputRightItem","props":{"y":0,"x":0,"var":"card2","height":51,"runtime":"ui.mainGame.Items.OutputRightItemUI"}},{"type":"OutputRightItem","props":{"y":41,"x":0,"var":"card1","height":51,"runtime":"ui.mainGame.Items.OutputRightItemUI"}},{"type":"OutputRightItem","props":{"y":82,"x":0,"var":"card0","height":51,"runtime":"ui.mainGame.Items.OutputRightItemUI"}},{"type":"OutputTopItem","props":{"y":17,"x":9,"var":"card3","scaleY":0.55,"scaleX":0.55,"runtime":"ui.mainGame.Items.OutputTopItemUI"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.mainGame.Items.OutputRightItemUI",OutputRightItemUI);
			View.regComponent("ui.mainGame.Items.OutputTopItemUI",OutputTopItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}