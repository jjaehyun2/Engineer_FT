/**Created by the LayaAirIDE,do not modify.*/
package ui.hall {
	import laya.ui.*;
	import laya.display.*; 
	import ui.hall.HallBgUI;

	public class RechargeViewUI extends View {
		public var rech_list:List;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"y":0,"x":0,"width":640,"height":1038},"child":[{"type":"Box","props":{"y":0,"x":0},"child":[{"type":"HallBg","props":{"runtime":"ui.hall.HallBgUI"}},{"type":"Image","props":{"y":0,"x":5,"width":630,"skin":"common/diwenju.png","mouseThrough":true,"mouseEnabled":true,"height":1032,"sizeGrid":"28,16,30,20"}}]},{"type":"Box","props":{"y":0,"x":0}},{"type":"Label","props":{"y":30,"x":32,"width":580,"valign":"middle","text":"充值","height":50,"fontSize":40,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Image","props":{"y":98,"x":20,"width":600,"skin":"common/diwen.png","height":791,"sizeGrid":"18,20,18,19"}},{"type":"List","props":{"y":113,"x":44,"width":549,"var":"rech_list","spaceY":7,"spaceX":10,"repeatX":2,"height":755},"child":[{"type":"Box","props":{"visible":true,"renderType":"render"},"child":[{"type":"Image","props":{"y":0,"x":0,"width":266,"visible":true,"skin":"common/diwen.png","height":250,"sizeGrid":"18,20,18,19"}},{"type":"Image","props":{"y":34.2,"x":236,"visible":true,"skin":"hall/icon_diamond.png","scaleY":0.4,"scaleX":0.4}},{"type":"Label","props":{"y":28,"x":121,"width":107,"visible":true,"valign":"middle","text":"1000","name":"Diamonds","height":34,"fontSize":34,"font":"SimHei","color":"#c7edfb","bold":true,"align":"right"}},{"type":"Label","props":{"y":136,"x":157,"width":103,"visible":true,"valign":"middle","text":"¥999元","name":"mon","height":24,"fontSize":24,"font":"SimHei","color":"#ffc757","align":"right"}},{"type":"Image","props":{"y":59,"x":1,"visible":true,"skin":"hall/type_3.png","name":"priceDis"}},{"type":"Button","props":{"y":171,"x":10,"width":250,"stateNum":1,"skin":"common/buttonLv.png","name":"recharge","labelStrokeColor":"#450100","labelStroke":2,"labelSize":42,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"购买","height":70,"sizeGrid":"0,29,0,27"}},{"type":"Image","props":{"y":-3,"x":-3,"skin":"common/top_line.png"}},{"type":"Image","props":{"y":2,"x":2,"skin":"common/tuijian.png"}},{"type":"Image","props":{"y":78,"x":113,"width":147,"skin":"common/wenziBg.png","height":34,"sizeGrid":"0,17,0,20"}},{"type":"Label","props":{"y":79,"x":154,"width":71,"visible":true,"valign":"middle","text":"50000","name":"dis","height":31,"fontSize":24,"font":"SimHei","color":"#c7edfb","align":"right"}},{"type":"Label","props":{"y":84.5,"x":118,"visible":true,"valign":"middle","text":"赠送","fontSize":20,"font":"SimHei","color":"#ff6431","align":"right"}},{"type":"Image","props":{"y":85,"x":230,"visible":true,"skin":"hall/icon_diamond.png","scaleY":0.4,"scaleX":0.4}},{"type":"Image","props":{"y":119,"x":114,"width":145,"visible":true,"skin":"common/fenge.png","height":2}}]}]},{"type":"Image","props":{"y":0,"x":5,"width":630,"skin":"common/biaoti.png","height":86,"sizeGrid":"0,41,0,43"}},{"type":"Image","props":{"y":19,"x":229.5,"skin":"hall/goumaibaoshi.png"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.hall.HallBgUI",HallBgUI);
			super.createChildren();
			createView(uiView);

		}

	}
}