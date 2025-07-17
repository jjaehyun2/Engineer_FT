/**Created by the LayaAirIDE,do not modify.*/
package ui.common {
	import laya.ui.*;
	import laya.display.*; 

	public class PopBoxUI extends View {
		public var bg:Image;
		public var btnCLose:Button;
		public var txtTitle:Label;
		public var refuseBtn:Button;
		public var agreeBtn:Button;
		public var confirmBtn:Button;
		public var endViewReportBtn:Button;
		public var endToHallBtn:Button;
		public var txtBody:Label;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"sizeGrid":"29,24,23,26","height":1038},"child":[{"type":"Image","props":{"y":0,"x":0,"width":1038,"var":"bg","skin":"common/heixedi.png","height":1038,"alpha":0.5}},{"type":"Box","props":{"y":317,"x":205.5},"child":[{"type":"Image","props":{"y":0,"x":0,"width":627,"skin":"common/gameBg.png","sizeGrid":"34,32,34,34","height":319}},{"type":"Button","props":{"y":13,"x":578,"var":"btnCLose","stateNum":1,"skin":"common/cha.png"}},{"type":"Label","props":{"y":22,"x":76,"width":476,"var":"txtTitle","text":"提示","height":44,"fontSize":34,"color":"#c7edfb","bold":true,"align":"center"}},{"type":"Button","props":{"y":332,"x":91,"width":200,"var":"refuseBtn","stateNum":1,"skin":"common/buttonHong.png","labelStrokeColor":"#000000","labelStroke":2,"labelSize":40,"labelFont":"黑体","labelColors":"#ffffff,#ffffff,#ffffff","height":72,"sizeGrid":"0,30,0,28"},"child":[{"type":"Image","props":{"y":10,"x":57,"skin":"common/btnCancel.png"}}]},{"type":"Button","props":{"y":332,"x":342,"width":200,"var":"agreeBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#000000","labelStroke":2,"labelSize":40,"labelFont":"黑体","labelColors":"#ffffff,#ffffff,#ffffff","height":72,"sizeGrid":"0,29,0,27"},"child":[{"type":"Image","props":{"y":13,"x":54,"skin":"common/btnConfirm.png"}}]},{"type":"Button","props":{"y":332,"x":204.5,"width":200,"var":"confirmBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#000000","labelStroke":2,"labelSize":40,"labelPadding":"-2","labelFont":"黑体","labelColors":"#ffffff,#ffffff,#ffffff","label":"确定","height":72,"sizeGrid":"0,29,0,27"}},{"type":"Button","props":{"y":332,"x":41,"width":230,"var":"endViewReportBtn","stateNum":1,"skin":"common/buttonHuang.png","labelStrokeColor":"#000000","labelStroke":2,"labelSize":40,"labelFont":"黑体","labelColors":"#ffffff,#ffffff,#ffffff","height":72,"sizeGrid":"0,29,0,28"},"child":[{"type":"Image","props":{"y":6,"x":21,"skin":"common/btnLookRecode.png"}}]},{"type":"Button","props":{"y":332,"x":335,"width":230,"var":"endToHallBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#000000","labelStroke":2,"labelSize":40,"labelFont":"黑体","labelColors":"#ffffff,#ffffff,#ffffff","height":72,"sizeGrid":"0,29,0,27"},"child":[{"type":"Image","props":{"y":10,"x":24,"skin":"common/btnGotoHall.png"}}]},{"type":"Image","props":{"y":70,"x":24,"width":571,"skin":"common/commonTitBg.png","height":223,"sizeGrid":"10,10,8,14"}},{"type":"Label","props":{"y":80,"x":43,"wordWrap":true,"width":541,"var":"txtBody","valign":"top","text":"房间解散成功","overflow":"scroll","leading":9,"height":210,"fontSize":30,"color":"#c7edfb","align":"left"}}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}