/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.Items {
	import laya.ui.*;
	import laya.display.*; 
	import ui.mainGame.Items.OutputBottomItemUI;
	import ui.mainGame.Items.OutputRightItemUI;

	public class BottomPengGangItemUI extends View {
		public var card0:OutputBottomItemUI;
		public var card1:OutputBottomItemUI;
		public var card2:OutputBottomItemUI;
		public var card3:OutputRightItemUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"OutputBottomItem","props":{"y":0,"x":0,"var":"card0","runtime":"ui.mainGame.Items.OutputBottomItemUI"}},{"type":"OutputBottomItem","props":{"y":0,"x":90,"var":"card1","runtime":"ui.mainGame.Items.OutputBottomItemUI"}},{"type":"OutputBottomItem","props":{"y":0,"x":180,"var":"card2","runtime":"ui.mainGame.Items.OutputBottomItemUI"}},{"type":"OutputRightItem","props":{"y":-6,"x":79,"width":66,"visible":true,"var":"card3","scaleY":1.7,"scaleX":1.7,"height":56,"runtime":"ui.mainGame.Items.OutputRightItemUI"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.mainGame.Items.OutputBottomItemUI",OutputBottomItemUI);
			View.regComponent("ui.mainGame.Items.OutputRightItemUI",OutputRightItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}