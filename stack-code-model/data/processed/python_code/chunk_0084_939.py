/**Created by the LayaAirIDE,do not modify.*/
package ui.gameCommon.items {
	import laya.ui.*;
	import laya.display.*; 
	import ui.gameCommon.VoiceShowUI;
	import laya.display.Text;

	public class NNPlayerInfoItemRightUI extends View {
		public var haveBox:Box;
		public var headImg:Image;
		public var offline:Image;
		public var gangEff:Image;
		public var readyImg:Label;
		public var zhuangImg:Image;
		public var nameTf:Label;
		public var chairPos:Label;
		public var offLineSp:Image;
		public var offlineTf:Label;
		public var tirenBtn:Button;
		public var recordTf:Label;
		public var voice:VoiceShowUI;
		public var express:Image;
		public var qiangImg:Image;
		public var zhuBox:Box;
		public var zhuTf:Text;
		public var fenshuTf:Label;
		public var jinbiAni:Animation;
		public var zhuangAni:Animation;
		public var sitdownBtn:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":0,"visible":true,"height":0},"child":[{"type":"Box","props":{"y":-4,"x":-36,"var":"haveBox"},"child":[{"type":"Image","props":{"y":79,"x":33,"width":111,"skin":"gameCommon/img_jinbi-di.png","sizeGrid":"0,27,0,30","scaleY":0.7,"scaleX":0.7,"height":39}},{"type":"Image","props":{"y":17,"x":45,"width":60,"skin":"gameCommon/img_wanjiatouxiang-di.png","sizeGrid":"16,16,19,16","height":60}},{"type":"Box","props":{"y":19,"x":47},"child":[{"type":"Image","props":{"width":56,"var":"headImg","skin":"common/morentouxiang.png","height":56}},{"type":"Image","props":{"y":0,"x":0,"width":56,"skin":"gameCommon/img_wanjiatouxiang-di.png","renderType":"mask","height":56}}]},{"type":"Image","props":{"y":20,"x":47,"width":56,"var":"offline","skin":"gameCommon/duanxian.png","height":56}},{"type":"Image","props":{"y":49,"x":9,"var":"gangEff","skin":"gameCommon/star0001.png"}},{"type":"Label","props":{"y":36,"x":46,"wordWrap":false,"width":56,"visible":true,"var":"readyImg","valign":"middle","text":"准备","strokeColor":"#381e07","stroke":2,"overflow":"hidden","height":30,"fontSize":22,"font":"SimHei","color":"#efef37","bold":true,"align":"center"}},{"type":"Image","props":{"y":12,"x":91,"width":25,"var":"zhuangImg","skin":"gameCommon/zhuang.png","height":25}},{"type":"Label","props":{"y":-5,"x":42,"wordWrap":false,"width":66,"visible":true,"var":"nameTf","valign":"middle","text":"玩家名字对对对","overflow":"scroll","height":24,"fontSize":16,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Label","props":{"y":22,"x":39,"wordWrap":false,"width":87,"visible":true,"var":"chairPos","valign":"middle","text":"座位号：0","overflow":"hidden","height":28,"fontSize":18,"font":"SimHei","color":"#ff0400","align":"center"}},{"type":"Image","props":{"y":33,"x":46,"width":57,"var":"offLineSp","skin":"common/heixedi.png","height":32,"alpha":0.4}},{"type":"Label","props":{"y":31,"x":42,"wordWrap":false,"width":64,"visible":true,"var":"offlineTf","valign":"middle","text":180,"strokeColor":"#000000","stroke":5,"height":37,"fontSize":35,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Button","props":{"y":31,"x":43,"var":"tirenBtn","stateNum":1,"skin":"gameCommon/tiren.png","labelSize":26,"labelPadding":0,"labelFont":"SimHei","labelColors":"#eeeeee,#eeeeee,#eeeeee","labelBold":false,"labelAlign":"center"}},{"type":"Label","props":{"y":81,"x":38,"width":68,"visible":true,"var":"recordTf","text":-1000,"height":19,"fontSize":22,"font":"SimHei","color":"#fadc00","align":"center"}},{"type":"VoiceShow","props":{"y":19,"x":111,"visible":true,"var":"voice","scaleY":0.8,"scaleX":-0.8,"runtime":"ui.gameCommon.VoiceShowUI"}},{"type":"Image","props":{"y":30,"x":60,"width":136,"visible":true,"var":"express","skin":"faceexpress/face01.png","height":138}},{"type":"Image","props":{"y":9,"x":-14,"var":"qiangImg","skin":"gameCommon/qiangx4.png"}},{"type":"Box","props":{"y":36,"x":-13,"var":"zhuBox"},"child":[{"type":"Image","props":{"y":1,"x":1,"width":52,"skin":"common/jinbidiwen.png","height":28,"alpha":0.3}},{"type":"Image","props":{"skin":"common/jinbi.png"}},{"type":"Text","props":{"y":1,"x":33,"var":"zhuTf","text":"8","fontSize":25,"color":"#ffff6f","bold":true}}]},{"type":"Label","props":{"y":82,"x":-15,"var":"fenshuTf","text":"+55","stroke":3,"fontSize":40,"font":"SimHei","color":"#00ff00","bold":true,"align":"center"}},{"type":"Animation","props":{"y":53,"x":75,"var":"jinbiAni","source":"gameCommon/JinbiAni.ani"}},{"type":"Animation","props":{"y":52,"x":75,"var":"zhuangAni","source":"gameCommon/ZhuangAni.ani","scaleY":0.8,"scaleX":0.8}}]},{"type":"Button","props":{"y":13,"x":9,"width":60,"var":"sitdownBtn","stateNum":1,"skin":"gameCommon/zuoxia.png","labelSize":28,"labelFont":"SimHei","labelColors":"#ffffff,#ffffff,#ffffff","height":60}}]};
		override protected function createChildren():void {
			View.regComponent("ui.gameCommon.VoiceShowUI",VoiceShowUI);
			View.regComponent("Text",Text);
			super.createChildren();
			createView(uiView);

		}

	}
}