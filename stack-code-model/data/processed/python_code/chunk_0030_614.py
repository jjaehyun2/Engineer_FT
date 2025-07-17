/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame.majiangParts {
	import laya.ui.*;
	import laya.display.*; 

	public class HandleBtnsPartUI extends View {
		public var tingBtn:Button;
		public var chiBtn:Button;
		public var cancelBtn:Button;
		public var pengBtn:Button;
		public var gangBtn:Button;
		public var huBtn:Button;
		public var kouBtn:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{},"child":[{"type":"Button","props":{"y":0,"x":873,"var":"tingBtn","stateNum":1,"skin":"gametable/zhuomianliang1.png"}},{"type":"Button","props":{"y":0,"x":0,"var":"chiBtn","stateNum":1,"skin":"gametable/zhuomianchi.png"}},{"type":"Button","props":{"y":0,"x":1048,"var":"cancelBtn","stateNum":1,"skin":"gametable/zhuomianquxiao.png"}},{"type":"Button","props":{"y":0,"x":175,"var":"pengBtn","stateNum":1,"skin":"gametable/zhuomianpeng.png"}},{"type":"Button","props":{"y":0,"x":349,"var":"gangBtn","stateNum":1,"skin":"gametable/zhuomiangang.png"}},{"type":"Button","props":{"y":0,"x":699,"var":"huBtn","stateNum":1,"skin":"gametable/zhuomianhu.png"}},{"type":"Button","props":{"y":32,"x":524,"width":130,"var":"kouBtn","stateNum":1,"skin":"common/btn_green.png","labelSize":25,"labelFont":"黑体","labelColors":"#ffffff;#ffffff;#ffffff","label":"选择完成","height":72,"sizeGrid":"0,27,0,31"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}