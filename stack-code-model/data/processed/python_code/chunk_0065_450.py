/**Created by the LayaAirIDE,do not modify.*/
package ui.sddzGame.ddzPart.outputPart {
	import laya.ui.*;
	import laya.display.*; 
	import ui.sddzGame.item.PockerItemUI;

	public class OwnerOutputPartUI extends View {
		public var box:Box;
		public var card0:PockerItemUI;
		public var card1:PockerItemUI;
		public var card2:PockerItemUI;
		public var card3:PockerItemUI;
		public var card4:PockerItemUI;
		public var card5:PockerItemUI;
		public var card6:PockerItemUI;
		public var card7:PockerItemUI;
		public var card8:PockerItemUI;
		public var card9:PockerItemUI;
		public var card10:PockerItemUI;
		public var card11:PockerItemUI;
		public var card12:PockerItemUI;
		public var card13:PockerItemUI;
		public var card14:PockerItemUI;
		public var card15:PockerItemUI;
		public var card16:PockerItemUI;
		public var card17:PockerItemUI;
		public var card18:PockerItemUI;
		public var card19:PockerItemUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"height":0},"child":[{"type":"Box","props":{"y":0,"x":0,"var":"box"},"child":[{"type":"PockerItem","props":{"y":0,"x":0,"var":"card0","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":40,"var":"card1","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":80,"var":"card2","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":120,"var":"card3","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":160,"var":"card4","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":200,"var":"card5","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":240,"var":"card6","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":280,"var":"card7","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":320,"var":"card8","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":360,"var":"card9","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":400,"var":"card10","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":440,"var":"card11","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":480,"var":"card12","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":520,"var":"card13","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":560,"var":"card14","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":600,"var":"card15","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":640,"var":"card16","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":680,"var":"card17","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":720,"var":"card18","runtime":"ui.sddzGame.item.PockerItemUI"}},{"type":"PockerItem","props":{"y":0,"x":760,"var":"card19","runtime":"ui.sddzGame.item.PockerItemUI"}}]}]};
		override protected function createChildren():void {
			View.regComponent("ui.sddzGame.item.PockerItemUI",PockerItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}