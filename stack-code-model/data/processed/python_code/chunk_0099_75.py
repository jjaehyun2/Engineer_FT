/**Created by the LayaAirIDE,do not modify.*/
package ui.srddzGame.ddzPart.item {
	import laya.ui.*;
	import laya.display.*; 

	public class PockerItemUI extends View {
		public var backImg:Image;
		public var valueImg:Image;
		public var dizhuImg:Image;
		public var shadowImg:Image;
		public var mingImg:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":120,"var":"backImg","skin":"poker/bg.png","height":162}},{"type":"Image","props":{"y":0,"x":0,"var":"valueImg","skin":"poker/fang_10.png"}},{"type":"Image","props":{"y":2,"x":40,"var":"dizhuImg","skin":"poker/dizhupaibiao.png"}},{"type":"Image","props":{"y":0,"x":0,"var":"shadowImg","skin":"poker/poke_shadow.png"}},{"type":"Image","props":{"y":123,"x":3,"var":"mingImg","skin":"poker/ming.png"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}