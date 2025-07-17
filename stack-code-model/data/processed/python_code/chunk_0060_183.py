/**Created by the LayaAirIDE,do not modify.*/
package ui.hall.creatRoom {
	import laya.ui.*;
	import laya.display.*; 

	public class joinItemUI extends View {
		public var headBox:Box;
		public var headImg:Image;
		public var joinBtn:Button;
		public var nvImg:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Box","props":{"y":38,"x":0,"width":76,"var":"headBox","height":76,"anchorY":0.5,"anchorX":0},"child":[{"type":"Box","props":{"y":-4,"x":-4,"alpha":0.3},"child":[{"type":"Circle","props":{"y":42,"x":42,"radius":42,"lineWidth":0,"lineColor":"#eeeeee","fillColor":"#eeeeee"}}]},{"type":"Box","props":{"y":1,"x":1,"width":74,"height":74,"anchorY":0,"anchorX":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":74,"var":"headImg","skin":"common/morentouxiang2.png","height":74}},{"type":"Box","props":{"y":0,"x":0,"width":74,"renderType":"mask","height":74},"child":[{"type":"Circle","props":{"y":37,"x":37,"radius":37,"lineWidth":1,"fillColor":"#ff0000"}}]}]}]},{"type":"Button","props":{"y":0,"x":0,"var":"joinBtn","stateNum":1,"skin":"common/playerBg.png"}},{"type":"Image","props":{"y":84,"x":12,"var":"nvImg","skin":"common/nv_0.png"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}