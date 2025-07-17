/**Created by the LayaAirIDE,do not modify.*/
package ui.niuniuGame.niuniuPart.item {
	import laya.ui.*;
	import laya.display.*; 

	public class PockerItemUI extends View {
		public var backImg:Image;
		public var valueImg:Image;
		public var shadowImg:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":120,"var":"backImg","skin":"poker/bg.png","height":162}},{"type":"Image","props":{"y":0,"x":0,"var":"valueImg","skin":"poker/fang_10.png"}},{"type":"Image","props":{"y":0,"x":0,"var":"shadowImg","skin":"poker/poke_shadow.png"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}