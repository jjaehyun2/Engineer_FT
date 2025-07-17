/**Created by the LayaAirIDE,do not modify.*/
package ui.niuniuGame {
	import laya.ui.*;
	import laya.display.*; 

	public class TableInfoPageUI extends View {
		public var chatBtn:Button;
		public var roomNumTf:Label;
		public var roundCountTf:Label;
		public var playTypeTf:Label;
		public var option:Button;
		public var voiceTip:Box;
		public var _time:Label;
		public var voiceIntercomBtn:Box;
		public var voicePlay:Image;
		public var voiceDis:Image;
		public var scoreList:Button;
		public var infoListBtn:Button;
		public var infoSImg:Image;
		public var weikaishiBox:Box;
		public var ruleTimeTf:Label;
		public var payType:Label;
		public var leftDissolveTf:Label;
		public var kaijuTf:Label;
		public var helpBtn:Button;
		public var setBtn:Button;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":640},"child":[{"type":"Button","props":{"y":445,"x":820,"var":"chatBtn","stateNum":1,"skin":"gameCommon/chat.png","scaleY":0.8,"scaleX":0.8}},{"type":"Image","props":{"y":4,"x":886,"width":211,"skin":"gameCommon/img_jinbi-di.png","sizeGrid":"18,27,19,30","scaleY":0.7,"scaleX":0.7,"height":125}},{"type":"Box","props":{"y":13,"x":899},"child":[{"type":"Label","props":{"y":23,"x":60,"wordWrap":false,"visible":true,"var":"roomNumTf","valign":"middle","text":"123456","overflow":"scroll","fontSize":20,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Label","props":{"y":23,"x":0,"wordWrap":false,"visible":true,"valign":"middle","text":"房号：","overflow":"scroll","fontSize":20,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Label","props":{"y":47,"x":60,"wordWrap":false,"visible":true,"var":"roundCountTf","valign":"middle","text":"1/6","overflow":"scroll","fontSize":20,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Label","props":{"y":47,"x":0,"wordWrap":false,"visible":true,"valign":"middle","text":"局数：","overflow":"scroll","fontSize":20,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Label","props":{"y":0,"x":0,"wordWrap":false,"width":92,"visible":true,"var":"playTypeTf","valign":"middle","text":"明牌抢庄","overflow":"scroll","height":20,"fontSize":20,"font":"SimHei","color":"#ffffff","align":"left"}}]},{"type":"Button","props":{"y":4,"x":4,"width":60,"var":"option","height":60},"child":[{"type":"Image","props":{"y":13,"x":10,"skin":"gameCommon/function_Option.png","scaleY":1.3,"scaleX":1.3}},{"type":"Image","props":{"y":0,"x":0,"width":60,"skin":"gameCommon/img_jinbi-di.png","sizeGrid":"18,27,19,30","height":60}}]},{"type":"Box","props":{"y":341,"x":934,"mouseThrough":true},"child":[{"type":"Box","props":{"y":-21,"x":-5,"visible":false,"var":"voiceTip","mouseThrough":true},"child":[{"type":"Image","props":{"y":0,"x":0,"width":91,"skin":"gameCommon/voice/voiceTip.png","sizeGrid":"6,5,19,8","mouseEnabled":false,"height":115}},{"type":"Label","props":{"y":14,"x":6,"width":78,"text":"点击发送","height":20,"fontSize":20,"font":"SimHei","color":"#fbfbfb","align":"center"}},{"type":"Label","props":{"y":41,"x":6,"width":79,"text":"上滑取消","height":20,"fontSize":20,"font":"SimHei","color":"#fbfbfb","align":"center"}},{"type":"Label","props":{"y":69,"x":6,"width":79,"var":"_time","text":"15'","height":20,"fontSize":20,"font":"SimHei","color":"#fbfbfb","align":"center"}}]},{"type":"Box","props":{"y":105.5,"x":6.5,"var":"voiceIntercomBtn"},"child":[{"type":"Button","props":{"y":-1,"x":-1,"stateNum":1,"skin":"gameCommon/duijiangji.png","scaleY":0.8,"scaleX":0.8}},{"type":"Image","props":{"y":33,"x":35,"visible":false,"var":"voicePlay","skin":"gameCommon/voice/voicePlay1.png","scaleY":0.8,"scaleX":0.8,"rotation":0,"mouseThrough":false,"anchorY":0.5,"anchorX":0.5}},{"type":"Image","props":{"y":-2,"x":-3,"visible":false,"var":"voiceDis","skin":"gameCommon/voice/voiceDis.png","scaleY":1.15,"scaleX":1.15,"disabled":true}}]}]},{"type":"Button","props":{"y":451,"x":679,"visible":false,"var":"scoreList","stateNum":1,"skin":"common/xinxiliebiaoBtn.png"},"child":[{"type":"Image","props":{"y":-1,"x":-12,"width":103,"skin":"common/xinxiliebiaoBtn.png","height":101,"alpha":0}}]},{"type":"Box","props":{"y":451,"x":739,"visible":false,"mouseThrough":true},"child":[{"type":"Button","props":{"x":4,"var":"infoListBtn","stateNum":1,"skin":"gameCommon/btnHorn.png"},"child":[{"type":"Button","props":{"y":11,"x":-4,"width":85,"stateNum":1,"skin":"gameCommon/btnHorn.png","height":82,"alpha":0}}]},{"type":"Image","props":{"y":0,"x":41,"var":"infoSImg","skin":"common/xiaohongdian.png","scaleY":1.2,"scaleX":1.2}}]},{"type":"Box","props":{"y":325,"x":410,"width":271,"var":"weikaishiBox","scaleY":0.8,"scaleX":0.8,"height":135},"child":[{"type":"Image","props":{"y":-29,"x":73.5,"skin":"gameCommon/dengdaikaiju.png"}},{"type":"Label","props":{"y":75,"x":0,"width":278,"visible":true,"var":"ruleTimeTf","valign":"middle","text":"本局时长：15分钟","height":27,"fontSize":24,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Label","props":{"y":41,"x":0,"width":278,"visible":true,"var":"payType","valign":"middle","text":"付费方式：房主付费","height":27,"fontSize":24,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Box","props":{"y":108,"x":0,"width":313,"height":27},"child":[{"type":"Label","props":{"y":0,"x":48,"width":262,"visible":true,"valign":"middle","text":"后未开局将解散","height":27,"fontSize":24,"font":"SimHei","color":"#ffffff","align":"center"}},{"type":"Label","props":{"y":0,"x":0,"width":96,"visible":true,"var":"leftDissolveTf","valign":"middle","text":"00:00 ","height":27,"fontSize":24,"font":"SimHei","color":"#ffffff","align":"center"}}]},{"type":"Label","props":{"y":8,"x":0,"width":278,"visible":true,"var":"kaijuTf","valign":"middle","text":"开局人：小嘟嘟呀呀","height":27,"fontSize":24,"font":"SimHei","color":"#ffffff","align":"center"}}]},{"type":"Button","props":{"y":4,"x":829,"width":50,"var":"helpBtn","labelSize":50,"labelPadding":"0,0,0,9","labelColors":"#ffffff,#ffffff,#ffffff","height":50},"child":[{"type":"Image","props":{"y":0,"x":0,"width":50,"skin":"gameCommon/img_jinbi-di.png","sizeGrid":"18,20,19,19","height":50}},{"type":"Label","props":{"y":1,"x":15,"visible":true,"valign":"middle","text":"?","fontSize":40,"font":"SimHei","color":"#ffffff","align":"center"}}]},{"type":"Button","props":{"y":75,"x":4,"width":55,"var":"setBtn","stateNum":1,"skin":"gameCommon/set.png","height":55}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}