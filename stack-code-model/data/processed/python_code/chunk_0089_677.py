/**Created by the LayaAirIDE,do not modify.*/
package ui.hall {
	import laya.ui.*;
	import laya.display.*; 
	import laya.display.Text;

	public class HallServiceViewUI extends View {
		public var closeService:Button;
		public var trueServiceBtn:Button;
		public var txt:Text;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":640,"height":1038},"child":[{"type":"Box","props":{"y":0,"x":0,"width":640,"height":1038},"child":[{"type":"Box","props":{"y":0,"x":0,"mouseThrough":true,"mouseEnabled":true,"alpha":0.5},"child":[{"type":"Rect","props":{"y":0,"x":0,"width":640,"lineWidth":0,"lineColor":"#000000","height":1038,"fillColor":"#000000"}}]},{"type":"Image","props":{"y":56,"x":30,"width":580,"skin":"common/popBg.png","height":946,"sizeGrid":"20,20,20,20"}},{"type":"Image","props":{"y":134,"x":59,"width":521,"skin":"common/baifengexian.png","height":1,"alpha":0.3}},{"type":"Image","props":{"y":150,"x":53,"width":534,"skin":"common/diwen.png","height":736,"sizeGrid":"18,20,18,19"}},{"type":"Label","props":{"y":79,"x":319,"width":519,"valign":"middle","text":"最终用户注册协议书","height":49,"fontSize":32,"font":"SimHei","color":"#c7edfb","anchorY":0,"anchorX":0.5,"align":"center"}},{"type":"Button","props":{"y":70,"x":568,"var":"closeService","stateNum":1,"skin":"common/cha.png","scaleY":0.7,"scaleX":0.7}},{"type":"Button","props":{"y":907,"x":219,"width":202,"var":"trueServiceBtn","stateNum":1,"skin":"common/buttonLv.png","labelSize":42,"labelPadding":"0,0,5,0","labelFont":"SimHei","labelColors":"#ffffff","labelAlign":"center","label":"确定","height":73,"sizeGrid":"0,29,0,27"}},{"type":"Text","props":{"y":166,"x":67,"wordWrap":true,"width":514,"var":"txt","text":"侯文杰侯文都是第三方第三方士的水电费水电费第三方第三方大夫杰猴大是大非当时发生的发生大幅度双方都是儿为而我房的说法但是","leading":10,"height":697,"fontSize":28,"font":"SimHei","color":"#c7edfb"}}]}]};
		override protected function createChildren():void {
			View.regComponent("Text",Text);
			super.createChildren();
			createView(uiView);

		}

	}
}