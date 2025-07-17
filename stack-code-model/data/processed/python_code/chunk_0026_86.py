/**Created by the LayaAirIDE,do not modify.*/
package ui.gameCommon {
	import laya.ui.*;
	import laya.display.*; 
	import ui.gameCommon.items.DissolvePlayerItemUI;

	public class DissolvePageUI extends View {
		public var startTf:Label;
		public var player0:DissolvePlayerItemUI;
		public var player1:DissolvePlayerItemUI;
		public var player2:DissolvePlayerItemUI;
		public var player3:DissolvePlayerItemUI;
		public var player4:DissolvePlayerItemUI;
		public var leftTimeTf:Label;
		public var agreenBtn:Button;
		public var opposeBtn:Button;
		public var player5:DissolvePlayerItemUI;
		public var player6:DissolvePlayerItemUI;
		public var player7:DissolvePlayerItemUI;
		public var player8:DissolvePlayerItemUI;
		public var player9:DissolvePlayerItemUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":1038},"child":[{"type":"Image","props":{"y":0,"x":0,"width":1038,"skin":"common/heixedi.png","height":1038,"alpha":0.5}},{"type":"Box","props":{"y":228,"x":218},"child":[{"type":"Image","props":{"y":0,"x":0,"width":602,"skin":"common/popBg.png","height":502,"sizeGrid":"20,20,20,20"}},{"type":"Image","props":{"y":69,"x":22,"width":558,"skin":"common/wenzidi.png","sizeGrid":"13,14,13,15","height":381}},{"type":"Label","props":{"y":413,"x":41,"wordWrap":false,"width":520,"visible":true,"valign":"middle","text":"3人同意才会解散，解散后将按照目前得分进行最终排名","overflow":"hidden","height":28,"fontSize":22,"font":"SimHei","color":"#c7edfb","bold":true,"align":"left"}},{"type":"Label","props":{"y":15,"x":21.5,"wordWrap":false,"width":559,"visible":true,"var":"startTf","valign":"middle","text":"[玩家小嘟嘟]发起投票解散房间。","strokeColor":"#007151","stroke":3,"height":43,"fontSize":24,"font":"Microsoft YaHei","color":"#c7edfb","bold":true,"align":"center"}},{"type":"Box","props":{"y":78,"x":58},"child":[{"type":"DissolvePlayerItem","props":{"y":0,"x":0,"var":"player0","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}},{"type":"DissolvePlayerItem","props":{"y":3,"x":99,"var":"player1","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}},{"type":"DissolvePlayerItem","props":{"y":1,"x":198,"var":"player2","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}},{"type":"DissolvePlayerItem","props":{"y":4,"x":297,"var":"player3","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}},{"type":"DissolvePlayerItem","props":{"y":4,"x":396,"var":"player4","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}}]},{"type":"Box","props":{"y":456,"x":183},"child":[{"type":"Label","props":{"wordWrap":false,"width":127,"visible":true,"valign":"middle","text":"剩余时间：","overflow":"hidden","height":28,"fontSize":22,"font":"SimHei","color":"#c7edfb","bold":true,"align":"left"}},{"type":"Label","props":{"x":173,"wordWrap":false,"width":37,"visible":true,"var":"leftTimeTf","valign":"middle","text":1,"overflow":"hidden","height":28,"fontSize":22,"font":"SimHei","color":"#c7edfb","bold":true,"align":"center"}},{"type":"Label","props":{"x":205,"wordWrap":false,"width":31,"visible":true,"valign":"middle","text":"秒","overflow":"hidden","height":28,"fontSize":22,"font":"SimHei","color":"#c7edfb","bold":true,"align":"left"}}]},{"type":"Box","props":{"y":513,"x":79},"child":[{"type":"Button","props":{"width":200,"var":"agreenBtn","stateNum":1,"skin":"common/buttonLv.png","labelStrokeColor":"#000000","labelStroke":2,"labelSize":40,"labelFont":"黑体","labelColors":"#ffffff,#ffffff,#ffffff","height":68,"sizeGrid":"0,29,0,27"},"child":[{"type":"Image","props":{"y":9,"x":56,"skin":"common/tongyi.png"}}]},{"type":"Button","props":{"x":244,"width":200,"var":"opposeBtn","stateNum":1,"skin":"common/buttonHong.png","labelStrokeColor":"#000000","labelStroke":2,"labelSize":40,"labelFont":"黑体","labelColors":"#ffffff,#ffffff,#ffffff","height":68,"sizeGrid":"0,30,0,28"},"child":[{"type":"Image","props":{"y":10,"x":59,"skin":"common/fandui.png"}}]}]},{"type":"Box","props":{"y":249,"x":58},"child":[{"type":"DissolvePlayerItem","props":{"y":0,"x":0,"var":"player5","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}},{"type":"DissolvePlayerItem","props":{"y":3,"x":99,"var":"player6","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}},{"type":"DissolvePlayerItem","props":{"y":1,"x":198,"var":"player7","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}},{"type":"DissolvePlayerItem","props":{"y":4,"x":297,"var":"player8","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}},{"type":"DissolvePlayerItem","props":{"y":4,"x":396,"var":"player9","runtime":"ui.gameCommon.items.DissolvePlayerItemUI"}}]}]}]};
		override protected function createChildren():void {
			View.regComponent("ui.gameCommon.items.DissolvePlayerItemUI",DissolvePlayerItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}