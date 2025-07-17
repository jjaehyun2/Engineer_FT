/**Created by the LayaAirIDE,do not modify.*/
package ui.mainGame {
	import laya.ui.*;
	import laya.display.*; 
	import ui.mainGame.DeskBgPageUI;
	import ui.mainGame.TableInfoPageUI;
	import ui.mainGame.PlayerInfoPageUI;
	import ui.mainGame.NewCalculatePageUI;
	import ui.gameCommon.ReplayControlViewUI;
	import ui.gameCommon.shortCutChat.PopChatItemUI;

	public class GameTableUI extends View {
		public var main:Box;
		public var mjContainer:Box;
		public var tableInfoPage:TableInfoPageUI;
		public var playerInfoPage:PlayerInfoPageUI;
		public var calculatePart:NewCalculatePageUI;
		public var replayControlView:ReplayControlViewUI;
		public var leftPopChat:PopChatItemUI;
		public var bottomPopChat:PopChatItemUI;
		public var topPopChat:PopChatItemUI;
		public var rightPopChat:PopChatItemUI;
		public var chatContainer:Box;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":600,"visible":true,"height":400},"child":[{"type":"Box","props":{"y":-1,"x":-1,"var":"main"},"child":[{"type":"DeskBgPage","props":{"y":0,"x":0,"runtime":"ui.mainGame.DeskBgPageUI"}},{"type":"Box","props":{"var":"mjContainer"},"child":[{"type":"Image","props":{"width":1038,"height":640}}]},{"type":"TableInfoPage","props":{"visible":true,"var":"tableInfoPage","height":500,"runtime":"ui.mainGame.TableInfoPageUI"}},{"type":"PlayerInfoPage","props":{"visible":true,"var":"playerInfoPage","runtime":"ui.mainGame.PlayerInfoPageUI"}},{"type":"NewCalculatePage","props":{"var":"calculatePart","runtime":"ui.mainGame.NewCalculatePageUI"}},{"type":"ReplayControlView","props":{"var":"replayControlView","runtime":"ui.gameCommon.ReplayControlViewUI"}},{"type":"PopChatItem","props":{"y":182,"x":91,"var":"leftPopChat","runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":411,"x":91,"var":"bottomPopChat","runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":43,"x":283,"width":417,"var":"topPopChat","height":70,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":159,"x":522,"width":417,"var":"rightPopChat","height":70,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"Box","props":{"y":0,"x":0,"var":"chatContainer"}}]}]};
		override protected function createChildren():void {
			View.regComponent("ui.mainGame.DeskBgPageUI",DeskBgPageUI);
			View.regComponent("ui.mainGame.TableInfoPageUI",TableInfoPageUI);
			View.regComponent("ui.mainGame.PlayerInfoPageUI",PlayerInfoPageUI);
			View.regComponent("ui.mainGame.NewCalculatePageUI",NewCalculatePageUI);
			View.regComponent("ui.gameCommon.ReplayControlViewUI",ReplayControlViewUI);
			View.regComponent("ui.gameCommon.shortCutChat.PopChatItemUI",PopChatItemUI);
			super.createChildren();
			createView(uiView);

		}

	}
}