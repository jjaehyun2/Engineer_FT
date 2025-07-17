/**Created by the LayaAirIDE,do not modify.*/
package ui.gameCommon {
	import laya.ui.*;
	import laya.display.*; 

	public class UserInfoUI extends View {
		public var clickBg:Image;
		public var idTf:Label;
		public var diamondTf:Label;
		public var diamond:Image;
		public var nickName:Label;
		public var giftList:List;
		public var imgPhoto:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":1038},"child":[{"type":"Image","props":{"y":0,"x":0,"width":1038,"visible":true,"var":"clickBg","height":1038,"alpha":0.01}},{"type":"Box","props":{"y":259.5,"x":310.5},"child":[{"type":"Image","props":{"y":0,"x":0,"width":417,"skin":"common/gameBg.png","sizeGrid":"34,32,34,34","height":519}},{"type":"Image","props":{"y":26,"x":13,"width":391,"skin":"common/commonTitBg.png","height":97,"sizeGrid":"10,10,8,14"}},{"type":"Label","props":{"y":45,"x":266,"width":133,"var":"idTf","text":"ID:1234567","overflow":"hidden","height":24,"fontSize":24,"color":"#c7edfb","alpha":0.88}},{"type":"Label","props":{"y":83,"x":143,"width":230,"var":"diamondTf","text":"10000","overflow":"hidden","height":24,"fontSize":24,"color":"#c7edfb","alpha":0.88}},{"type":"Image","props":{"y":82,"x":108,"width":28,"var":"diamond","skin":"gameCommon/icon_diamond.png","height":26}},{"type":"Label","props":{"y":45,"x":105,"wordWrap":false,"width":147,"var":"nickName","text":"玩家名字对对对","overflow":"scroll","height":34,"fontSize":24,"font":"Arial","color":"#c7edfb","align":"left"}},{"type":"Image","props":{"y":130,"x":13,"width":391,"skin":"common/commonTitBg.png","height":354,"sizeGrid":"10,10,8,14"}},{"type":"List","props":{"y":148,"x":20,"width":372,"var":"giftList","repeatX":4,"height":324}},{"type":"Box","props":{"y":34,"x":21},"child":[{"type":"Box","props":{"y":4,"x":4,"width":74,"visible":true,"height":74,"anchorY":0,"anchorX":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":74,"visible":true,"var":"imgPhoto","skin":"common/morentouxiang.png","height":74,"anchorY":0}},{"type":"Box","props":{"y":0,"x":0,"width":74,"visible":true,"renderType":"mask","height":74},"child":[{"type":"Image","props":{"width":74,"visible":true,"skin":"common/touxMask.png","height":74,"sizeGrid":"13,13,12,14"}}]}]},{"type":"Image","props":{"width":82,"visible":true,"skin":"common/touxBg.png","height":82,"sizeGrid":"15,15,19,18"}}]}]}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}