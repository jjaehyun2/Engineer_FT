/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.Items {
	import laya.ui.*;
	import laya.display.*; 

	public class HandleEffItemUI extends View {
		public var liangpaiImg:Image;
		public var pengImg:Image;
		public var gangImg:Image;
		public var huImg:Image;
		public var chiImg:Image;
		public var zimoImg:Image;
		public var dianpaoImg:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":300,"visible":false,"var":"liangpaiImg","skin":"22","height":300}},{"type":"Image","props":{"y":0,"x":0,"width":300,"visible":false,"var":"pengImg","height":300}},{"type":"Image","props":{"y":0,"x":0,"width":300,"visible":false,"var":"gangImg","height":300}},{"type":"Image","props":{"y":0,"x":0,"width":300,"visible":true,"var":"huImg","height":300}},{"type":"Image","props":{"y":0,"x":0,"width":300,"var":"chiImg","height":300}},{"type":"Image","props":{"y":0,"x":0,"width":300,"var":"zimoImg","height":300}},{"type":"Image","props":{"y":0,"x":0,"width":300,"var":"dianpaoImg","height":300}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}