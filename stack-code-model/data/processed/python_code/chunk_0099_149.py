/**Created by the LayaAirIDE,do not modify.*/
package ui.sddzGame.ddzPart {
	import laya.ui.*;
	import laya.display.*; 

	public class ClockPartUI extends View {
		public var cutdownTf:Label;
		public var pos1:Image;
		public var pos2:Image;
		public var pos0:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Box","props":{"y":0,"x":16,"width":114,"scaleY":0.7,"scaleX":0.7,"height":123},"child":[{"type":"Image","props":{"y":1,"x":4,"skin":"gameCommon/clock.png"}},{"type":"Label","props":{"y":32,"x":31.1923828125,"width":55.615234375,"var":"cutdownTf","valign":"middle","text":"09","strokeColor":"#000000","stroke":2,"height":50,"fontSize":40,"color":"#5a2e0f","align":"center"}}]},{"type":"Image","props":{"y":-42,"x":113,"var":"pos1","skin":"gameCommon/time-me.png","rotation":42}},{"type":"Image","props":{"y":-42,"x":1,"var":"pos2","skin":"gameCommon/time-me.png","scaleX":-1,"rotation":-42}},{"type":"Image","props":{"y":126,"x":73,"var":"pos0","skin":"gameCommon/time-me.png","rotation":180}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}