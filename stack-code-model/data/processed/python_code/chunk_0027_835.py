/**Created by the LayaAirIDE,do not modify.*/
package ui.niuniuGame.niuniuPart {
	import laya.ui.*;
	import laya.display.*; 

	public class ActTipUI extends View {
		public var tipTf:Label;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{},"child":[{"type":"Box","props":{},"child":[{"type":"Image","props":{"y":0,"x":0,"width":348,"skin":"niuniuGame/dikuang.png","height":47}},{"type":"Label","props":{"y":6,"x":0,"wordWrap":false,"width":348,"visible":true,"var":"tipTf","valign":"middle","text":"请准备","height":35,"fontSize":25,"font":"SimSun","color":"#ffffff","align":"center"}}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}