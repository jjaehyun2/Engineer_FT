/**Created by the LayaAirIDE,do not modify.*/
package ui.sddzGame.ddzPart {
	import laya.ui.*;
	import laya.display.*; 

	public class PlayerCtlPartUI extends View {
		public var jiaofenBox:Box;
		public var fen1Btn:Button;
		public var fen0Btn:Button;
		public var fen2Btn:Button;
		public var fen3Btn:Button;
		public var jiabeiBox:Box;
		public var jiabeiBtn:Button;
		public var bujiaBtn:Button;
		public var jiaogqiangBox:Box;
		public var qiangdizhuBtn:Button;
		public var jiaodizhuBtn:Button;
		public var bujiaoBtn:Button;
		public var buqiangBtn:Button;
		public var ctlBox:Box;
		public var mingpaiBtn:Button;
		public var buchuBtn:Button;
		public var tishiBtn:Button;
		public var chupaiBtn:Button;
		public var buqiBtn:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Box","props":{"y":0,"x":0,"var":"jiaofenBox"},"child":[{"type":"Button","props":{"x":203,"width":183,"var":"fen1Btn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"1分","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":0,"width":183,"var":"fen0Btn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"不叫","sizeGrid":"0,29,0,27"}},{"type":"Button","props":{"y":0,"x":406,"width":183,"var":"fen2Btn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"2分","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"y":0,"x":608,"width":183,"var":"fen3Btn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"3分","sizeGrid":"0,29,0,28"}}]},{"type":"Box","props":{"var":"jiabeiBox"},"child":[{"type":"Button","props":{"y":0,"x":0,"width":183,"var":"jiabeiBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"加倍","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":203,"width":183,"var":"bujiaBtn","stateNum":1,"skin":"common/buttonHong.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"不加倍","sizeGrid":"0,30,0,28"}}]},{"type":"Box","props":{"y":0,"var":"jiaogqiangBox"},"child":[{"type":"Button","props":{"width":183,"var":"qiangdizhuBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":35,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"抢地主","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":0,"width":183,"var":"jiaodizhuBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"叫地主","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"y":0,"x":203,"width":183,"var":"bujiaoBtn","stateNum":1,"skin":"common/buttonHong.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":35,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"不叫","sizeGrid":"0,30,0,28"}},{"type":"Button","props":{"y":0,"x":203,"width":183,"var":"buqiangBtn","stateNum":1,"skin":"common/buttonHong.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"不抢","sizeGrid":"0,30,0,28"}}]},{"type":"Box","props":{"y":0,"var":"ctlBox"},"child":[{"type":"Button","props":{"width":183,"var":"mingpaiBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"明牌","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":203,"width":183,"var":"buchuBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"不出","sizeGrid":"0,29,0,27"}},{"type":"Button","props":{"x":406,"width":183,"var":"tishiBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"提示","sizeGrid":"0,29,0,27"}},{"type":"Button","props":{"y":0,"x":609,"width":183,"var":"chupaiBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"出牌","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":812,"width":183,"var":"buqiBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"要不起","sizeGrid":"0,29,0,28"}}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}