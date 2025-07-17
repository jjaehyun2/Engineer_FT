/**Created by the LayaAirIDE,do not modify.*/
package ui.gameCommon {
	import laya.ui.*;
	import laya.display.*; 

	public class ReplayControlViewUI extends View {
		public var replayBox:Box;
		public var backBtn:Button;
		public var upBtn:Button;
		public var playBtn:Button;
		public var downBtn:Button;
		public var stopBtn:Button;
		public var skipBtn:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":640},"child":[{"type":"Image","props":{"y":0,"x":0,"width":1038,"skin":"common/baifengexian.png","mouseThrough":false,"height":640,"alpha":0.01}},{"type":"Box","props":{"y":559,"x":336,"var":"replayBox"},"child":[{"type":"Button","props":{"y":9,"x":-7,"var":"backBtn","stateNum":1,"skin":"gameCommon/huifanganniu1.png"}},{"type":"Button","props":{"y":9,"x":68,"var":"upBtn","stateNum":1,"skin":"gameCommon/huifanganniu2.png"}},{"type":"Button","props":{"y":9,"x":144,"var":"playBtn","stateNum":1,"skin":"gameCommon/huifanganniu3.png"}},{"type":"Button","props":{"y":9,"x":219,"var":"downBtn","stateNum":1,"skin":"gameCommon/huifanganniu4.png"}},{"type":"Button","props":{"y":9,"x":144,"var":"stopBtn","stateNum":1,"skin":"gameCommon/huifanganniu5.png"}},{"type":"Button","props":{"y":9,"x":294,"var":"skipBtn","stateNum":1,"skin":"gameCommon/huifanganniu6.png"}}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}