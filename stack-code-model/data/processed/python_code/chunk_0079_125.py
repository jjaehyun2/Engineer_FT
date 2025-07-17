/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame {
	import laya.ui.*;
	import laya.display.*; 

	public class DeskBgPageUI extends View {

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":640},"child":[{"type":"Box","props":{"y":0,"x":0},"child":[{"type":"Rect","props":{"y":0,"x":0,"width":1038,"lineWidth":1,"height":640,"fillColor":"#007058"}}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}