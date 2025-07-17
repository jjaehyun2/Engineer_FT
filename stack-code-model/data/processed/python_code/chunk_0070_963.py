/**Created by the LayaAirIDE,do not modify.*/
package ui.hall.creatRoom {
	import laya.ui.*;
	import laya.display.*; 
	import ui.hall.creatRoom.joinItemUI;

	public class RoomListItemUI extends View {
		public var item0:joinItemUI;
		public var item1:joinItemUI;
		public var item2:joinItemUI;
		public var item3:joinItemUI;
		public var item4:joinItemUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"height":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":468,"skin":"hall/paoBg.png","height":120,"sizeGrid":"10,17,14,19"}},{"type":"joinItem","props":{"y":6,"x":13,"var":"item0","runtime":"ui.hall.creatRoom.joinItemUI"}},{"type":"joinItem","props":{"y":6,"x":105,"var":"item1","runtime":"ui.hall.creatRoom.joinItemUI"}},{"type":"joinItem","props":{"y":6,"x":196,"var":"item2","runtime":"ui.hall.creatRoom.joinItemUI"}},{"type":"joinItem","props":{"y":6,"x":288,"var":"item3","runtime":"ui.hall.creatRoom.joinItemUI"}},{"type":"joinItem","props":{"y":6,"x":379,"var":"item4","runtime":"ui.hall.creatRoom.joinItemUI"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.hall.creatRoom.joinItemUI",joinItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}