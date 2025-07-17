/**Created by the LayaAirIDE,do not modify.*/
package ui.srddzGame.ddzPart {
	import laya.ui.*;
	import laya.display.*; 
	import ui.srddzGame.ddzPart.item.PockerItemUI;

	public class DipaiPartUI extends View {
		public var card0:PockerItemUI;
		public var card1:PockerItemUI;
		public var card2:PockerItemUI;
		public var card3:PockerItemUI;
		public var card4:PockerItemUI;
		public var card5:PockerItemUI;
		public var card6:PockerItemUI;
		public var card7:PockerItemUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"PockerItem","props":{"y":0,"x":0,"var":"card0","scaleY":0.7,"scaleX":0.7,"runtime":"ui.srddzGame.ddzPart.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":30,"var":"card1","scaleY":0.7,"scaleX":0.7,"runtime":"ui.srddzGame.ddzPart.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":60,"var":"card2","scaleY":0.7,"scaleX":0.7,"runtime":"ui.srddzGame.ddzPart.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":90,"var":"card3","scaleY":0.7,"scaleX":0.7,"runtime":"ui.srddzGame.ddzPart.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":120,"var":"card4","scaleY":0.7,"scaleX":0.7,"runtime":"ui.srddzGame.ddzPart.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":151,"var":"card5","scaleY":0.7,"scaleX":0.7,"runtime":"ui.srddzGame.ddzPart.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":181,"var":"card6","scaleY":0.7,"scaleX":0.7,"runtime":"ui.srddzGame.ddzPart.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":211,"var":"card7","scaleY":0.7,"scaleX":0.7,"runtime":"ui.srddzGame.ddzPart.item.PockerItemUI"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.srddzGame.ddzPart.item.PockerItemUI",PockerItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}