/**Created by the LayaAirIDE,do not modify.*/
package ui.hall.item {
	import laya.ui.*;
	import laya.display.*; 

	public class GiveLogViewUI extends View {
		public var titleTf:Label;
		public var beginTimeTf:TextInput;
		public var endTimeTf:TextInput;
		public var searchBtn:Button;
		public var logList:List;
		public var closeBtn:Button;
		public var conditionRadio:RadioGroup;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":640,"height":1038},"child":[{"type":"Image","props":{"y":0,"x":0,"width":640,"skin":"common/popBg.png","height":1038,"sizeGrid":"20,20,20,20"}},{"type":"Image","props":{"y":253,"x":24,"width":592,"skin":"common/diwen.png","height":759,"sizeGrid":"18,20,18,19"}},{"type":"Box","props":{"y":15,"x":55},"child":[{"type":"Image","props":{"y":0,"x":0,"width":529,"skin":"common/diwen.png","height":66,"sizeGrid":"18,20,18,19"}},{"type":"Label","props":{"y":0,"x":4,"width":525,"var":"titleTf","valign":"middle","text":"赠送明细[ID:1166 小嘟嘟嘟]","overflow":"hidden","height":65,"fontSize":34,"font":"SimHei","color":"#c7edfb","align":"center"}}]},{"type":"TextInput","props":{"y":92,"x":192,"width":225,"var":"beginTimeTf","type":"date","skin":"common/touxMask.png","height":47,"fontSize":30,"font":"Helvetica","sizeGrid":"13,13,12,14"}},{"type":"TextInput","props":{"y":150,"x":192,"width":225,"var":"endTimeTf","type":"date","skin":"common/touxMask.png","height":47,"fontSize":30,"font":"Helvetica","sizeGrid":"13,13,12,14"}},{"type":"Label","props":{"y":98,"x":33,"width":146,"valign":"middle","text":"起始日期：","fontSize":34,"font":"SimHei","color":"#c7edfb","align":"center"}},{"type":"Label","props":{"y":156,"x":33,"width":146,"valign":"middle","text":"结束日期：","fontSize":34,"font":"SimHei","color":"#c7edfb","align":"center"}},{"type":"Button","props":{"y":112,"x":478,"width":130,"var":"searchBtn","stateNum":1,"skin":"common/buttonLan.png","labelStrokeColor":"#450100","labelStroke":2,"labelSize":25,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","labelBold":true,"label":"查询","height":70,"sizeGrid":"0,30,0,30"}},{"type":"List","props":{"y":255,"x":33,"width":575,"var":"logList","height":742}},{"type":"Button","props":{"y":16,"x":589,"var":"closeBtn","stateNum":1,"skin":"common/cha.png"}},{"type":"RadioGroup","props":{"y":210,"x":34,"var":"conditionRadio","space":20,"skin":"common/111.png","selectedIndex":0,"labels":"所有,未付款,已付款","labelSize":26,"labelPadding":"-4,0,20,5","labelColors":"#c7edfb,#c7edfb,#c7edfb","direction":"horizontal"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}