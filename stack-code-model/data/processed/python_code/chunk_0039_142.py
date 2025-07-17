/**Created by the LayaAirIDE,do not modify.*/
package ui.hall {
	import laya.ui.*;
	import laya.display.*; 

	public class BottomBtnUI extends View {
		public var btnTab:Tab;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":640,"height":120},"child":[{"type":"Tab","props":{"y":0,"x":0,"var":"btnTab","space":2,"skin":"hall/hallDi.png","selectedIndex":2,"labels":"商城,排行榜,大厅,反馈,战绩","labelSize":36,"labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","direction":"horizontal","centerX":0,"bottom":0}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}