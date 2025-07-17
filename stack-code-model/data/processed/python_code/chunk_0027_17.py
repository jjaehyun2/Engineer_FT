/**Created by the LayaAirIDE,do not modify.*/
package ui.niuniuGame {
	import laya.ui.*;
	import laya.display.*; 
	import ui.niuniuGame.PlayerInfoPageUI;
	import ui.niuniuGame.TableInfoPageUI;
	import ui.gameCommon.shortCutChat.PopChatItemUI;
	import ui.gameCommon.ReplayControlViewUI;

	public class GameTableUI extends View {
		public var pokerContainer:Box;
		public var playerInfoPage:PlayerInfoPageUI;
		public var tableInfoPage:TableInfoPageUI;
		public var popChat0:PopChatItemUI;
		public var popChat9:PopChatItemUI;
		public var popChat8:PopChatItemUI;
		public var popChat7:PopChatItemUI;
		public var popChat3:PopChatItemUI;
		public var popChat2:PopChatItemUI;
		public var popChat1:PopChatItemUI;
		public var popChat6:PopChatItemUI;
		public var popChat5:PopChatItemUI;
		public var popChat4:PopChatItemUI;
		public var chatContainer:Box;
		public var replayControlView:ReplayControlViewUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":640},"child":[{"type":"Box","props":{"y":0,"x":0,"width":1038,"height":640},"child":[{"type":"Image","props":{"y":0,"x":0,"skin":"niuniuGame/bg.jpg"}},{"type":"Image","props":{"y":0,"x":1038,"skin":"niuniuGame/bg.jpg","scaleX":-1}}]},{"type":"Box","props":{"var":"pokerContainer","mouseThrough":true},"child":[{"type":"Image","props":{"width":1038,"height":640}}]},{"type":"PlayerInfoPage","props":{"y":0,"x":0,"var":"playerInfoPage","runtime":"ui.niuniuGame.PlayerInfoPageUI"}},{"type":"TableInfoPage","props":{"var":"tableInfoPage","runtime":"ui.niuniuGame.TableInfoPageUI"}},{"type":"PopChatItem","props":{"y":474,"x":9,"var":"popChat0","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":348,"x":81,"var":"popChat9","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":223,"x":114,"var":"popChat8","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":139,"x":248,"var":"popChat7","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":139,"x":551,"var":"popChat3","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":223,"x":678,"var":"popChat2","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":348,"x":710,"var":"popChat1","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":89,"x":382,"var":"popChat6","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":79,"x":538,"var":"popChat5","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":89,"x":420,"var":"popChat4","scaleY":0.6,"scaleX":0.6,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"Box","props":{"var":"chatContainer"}},{"type":"ReplayControlView","props":{"var":"replayControlView","runtime":"ui.gameCommon.ReplayControlViewUI"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.niuniuGame.PlayerInfoPageUI",PlayerInfoPageUI);
			View.regComponent("ui.niuniuGame.TableInfoPageUI",TableInfoPageUI);
			View.regComponent("ui.gameCommon.shortCutChat.PopChatItemUI",PopChatItemUI);
			View.regComponent("ui.gameCommon.ReplayControlViewUI",ReplayControlViewUI);
			super.createChildren();
			createView(uiView);

		}

	}
}