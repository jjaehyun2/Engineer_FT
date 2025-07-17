/**Created by the LayaAirIDE,do not modify.*/
package ui.niuniuGame.niuniuPart {
	import laya.ui.*;
	import laya.display.*; 

	public class PlayerCtlPartUI extends View {
		public var qiangBox:Box;
		public var bei0:Button;
		public var bei1:Button;
		public var bei2:Button;
		public var bei3:Button;
		public var bei4:Button;
		public var fenBox:Box;
		public var fen4:Button;
		public var fen2:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{},"child":[{"type":"Box","props":{"y":0,"x":0,"var":"qiangBox"},"child":[{"type":"Button","props":{"width":130,"var":"bei0","stateNum":1,"skin":"common/buttonLan.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"不抢","sizeGrid":"0,30,0,30"}},{"type":"Button","props":{"x":107,"width":130,"var":"bei1","stateNum":1,"skin":"common/buttonHuang.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"1倍","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":214,"width":130,"var":"bei2","stateNum":1,"skin":"common/buttonHuang.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"2倍","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":321,"width":130,"var":"bei3","stateNum":1,"skin":"common/buttonHuang.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"3倍","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"x":428,"width":130,"var":"bei4","stateNum":1,"skin":"common/buttonHuang.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"4倍","sizeGrid":"0,29,0,28"}}]},{"type":"Box","props":{"y":0,"x":160,"var":"fenBox"},"child":[{"type":"Button","props":{"y":2,"x":107,"width":130,"var":"fen4","stateNum":1,"skin":"common/buttonHuang.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"4分","sizeGrid":"0,29,0,28"}},{"type":"Button","props":{"width":130,"var":"fen2","stateNum":1,"skin":"common/buttonHuang.png","scaleY":0.8,"scaleX":0.8,"labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"2分","sizeGrid":"0,29,0,28"}}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}