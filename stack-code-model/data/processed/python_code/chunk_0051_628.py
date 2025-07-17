/**Created by the LayaAirIDE,do not modify.*/
package ui.hall {
	import laya.ui.*;
	import laya.display.*; 
	import ui.hall.HallBgUI;
	import laya.display.Text;

	public class HallViewUI extends View {
		public var handBtn:Box;
		public var handIMG:Image;
		public var nameTf:Label;
		public var coinTf:Label;
		public var creatXiZBtn:Button;
		public var creatSanDizhuBtn:Button;
		public var creatSiDizhuBtn:Button;
		public var creatXiSBtn:Button;
		public var creatPinshiBtn:Button;
		public var creatHHuaBtn:Button;
		public var joinRoomBtn:Button;
		public var gameTab:Tab;
		public var jinbiBtn:Button;
		public var noSimbol:Image;
		public var yuejuBtn:Button;
		public var Notice:Text;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"x":0,"width":640,"rotation":0,"renderType":"mask","height":1038,"color":"#fdfdfd"},"child":[{"type":"Box","props":{"y":0,"x":0},"child":[{"type":"HallBg","props":{"runtime":"ui.hall.HallBgUI"}},{"type":"Box","props":{"y":0,"x":0,"alpha":0.3},"child":[{"type":"Rect","props":{"width":640,"lineWidth":1,"height":110,"fillColor":"#000000"}}]},{"type":"Box","props":{"y":55,"x":15,"width":76,"var":"handBtn","height":76,"anchorY":0.5,"anchorX":0},"child":[{"type":"Box","props":{"y":-4,"x":-4,"alpha":0.3},"child":[{"type":"Circle","props":{"y":42,"x":42,"radius":42,"lineWidth":0,"lineColor":"#eeeeee","fillColor":"#eeeeee"}}]},{"type":"Box","props":{"y":1,"x":1,"width":74,"height":74,"anchorY":0,"anchorX":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":74,"var":"handIMG","skin":"common/morentouxiang2.png","height":74}},{"type":"Box","props":{"y":0,"x":0,"width":74,"renderType":"mask","height":74},"child":[{"type":"Circle","props":{"y":37,"x":37,"radius":37,"lineWidth":1,"fillColor":"#ff0000"}}]}]}]},{"type":"Label","props":{"y":15,"x":106,"width":177,"var":"nameTf","text":"哇哈哈*胡文松","overflow":"hidden","height":32,"fontSize":30,"font":"SimHei","color":"#ffffff","align":"left"}},{"type":"Image","props":{"y":32,"x":284,"width":46,"skin":"common/jinbi.png","height":46}},{"type":"Label","props":{"y":39,"x":331,"width":109,"var":"coinTf","valign":"middle","text":"100000","overflow":"hidden","height":31,"fontSize":36,"font":"SimHei","color":"#ffffff","align":"left"}},{"type":"Panel","props":{"y":192,"x":15.5,"width":611,"visible":false,"vScrollBarSkin":" ","height":684},"child":[{"type":"Button","props":{"y":170,"x":328,"width":288,"visible":true,"var":"creatXiZBtn","stateNum":1,"skin":"hall/danchengGame.png","height":156}},{"type":"Button","props":{"x":325,"var":"creatSanDizhuBtn","stateNum":1,"skin":"hall/sanrendoudizhu.png"}},{"type":"Button","props":{"var":"creatSiDizhuBtn","stateNum":1,"skin":"hall/sirendoudizhu.png"}},{"type":"Button","props":{"y":170,"x":0,"width":282,"visible":true,"var":"creatXiSBtn","stateNum":1,"skin":"hall/xizhoumajiang.png","height":158}},{"type":"Button","props":{"y":340,"x":8,"visible":false,"var":"creatPinshiBtn","stateNum":1,"skin":"hall/pinshiGame.png"}},{"type":"Button","props":{"y":340,"x":336,"visible":false,"var":"creatHHuaBtn","stateNum":1,"skin":"hall/huaihuamj.png"}}]},{"type":"Button","props":{"y":15,"x":444,"width":191,"var":"joinRoomBtn","stateNum":1,"skin":"hall/joinBtn.png","labelSize":36,"labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","label":"加入房间","height":80,"sizeGrid":"0,17,0,20"}},{"type":"Tab","props":{"y":174,"x":5,"var":"gameTab","space":5,"skin":"hall/gameBtn.png","selectedIndex":0,"labels":"三人斗地主,四人斗地主,拼十","labelSize":36,"labelPadding":"0,0,4,0","labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","direction":"vertical"}},{"type":"Button","props":{"y":174,"width":325,"var":"jinbiBtn","stateNum":1,"skin":"hall/jinbiBtn.png","right":30,"labelSize":36,"labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","label":"金币场","height":155,"sizeGrid":"17,18,19,19"},"child":[{"type":"Image","props":{"y":12,"x":184,"visible":false,"var":"noSimbol","skin":"hall/weikaifang.png"}}]},{"type":"Button","props":{"y":356,"width":325,"var":"yuejuBtn","stateNum":1,"skin":"hall/yuejuBtn.png","right":30,"labelSize":36,"labelFont":"SimHei","labelColors":"#e7fecb,#e7fecb,#e7fecb,#e7fecb","label":"约局场","height":155,"sizeGrid":"14,17,19,19"}},{"type":"Box","props":{"y":112,"x":0},"child":[{"type":"Image","props":{"y":0,"x":0,"width":640,"skin":"hall/paoBg.png","height":50,"alpha":0.3,"sizeGrid":"10,17,14,19"}},{"type":"Text","props":{"y":12,"x":11,"width":619,"var":"Notice","text":"文字文字y","height":33,"fontSize":24,"font":"SimHei","color":"#ffffff"}}]},{"type":"Image","props":{"y":56,"x":106,"skin":"common/nv_9.png","scaleY":1.5,"scaleX":1.5}}]}]};
		override protected function createChildren():void {
			View.regComponent("ui.hall.HallBgUI",HallBgUI);
			View.regComponent("Text",Text);
			super.createChildren();
			createView(uiView);

		}

	}
}