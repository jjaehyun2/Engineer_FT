/**Created by the LayaAirIDE,do not modify.*/
package ui.common {
	import laya.ui.*;
	import laya.display.*; 
	import laya.display.Text;

	public class VGameHelpUI extends View {
		public var close:Box;
		public var close1:Button;
		public var txt:Text;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":640,"height":1038},"child":[{"type":"Box","props":{"y":0,"x":0,"var":"close","mouseThrough":true,"alpha":0},"child":[{"type":"Rect","props":{"y":0,"x":0,"width":640,"lineWidth":0,"height":1038,"fillColor":"#000000"}}]},{"type":"Image","props":{"y":100,"x":34.5,"width":571,"skin":"common/gameBg.png","sizeGrid":"34,32,34,34","height":827}},{"type":"Image","props":{"y":169,"x":60.5,"width":518,"skin":"common/commonTitBg.png","height":731,"sizeGrid":"10,10,8,14"}},{"type":"Button","props":{"y":117,"x":564.5,"var":"close1","stateNum":1,"skin":"common/cha.png","scaleY":0.7,"scaleX":0.7}},{"type":"Label","props":{"y":121,"x":246.5,"width":147,"valign":"middle","text":"游戏规则","height":37,"fontSize":30,"font":"SimSun","color":"#c7edfb","bold":true,"align":"center"}},{"type":"Text","props":{"y":187,"x":77.5,"wordWrap":true,"width":493,"var":"txt","text":"侯文杰侯文杰猴大是大非当时发生的发生大幅度双方都是儿为而我房的说法但是","leading":10,"height":704,"fontSize":22,"font":"SimHei","color":"#c7edfb"}}]};
		override protected function createChildren():void {
			View.regComponent("Text",Text);
			super.createChildren();
			createView(uiView);

		}

	}
}