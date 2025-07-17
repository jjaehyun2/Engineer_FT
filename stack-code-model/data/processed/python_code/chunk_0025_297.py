/**Created by the LayaAirIDE,do not modify.*/
package ui.sddzGame {
	import laya.ui.*;
	import laya.display.*; 
	import ui.sddzGame.TableInfoPageUI;
	import ui.sddzGame.PlayerInfoPageUI;
	import ui.gameCommon.shortCutChat.PopChatItemUI;
	import ui.sddzGame.CalculatePageUI;
	import ui.gameCommon.VReplayControllerUI;

	public class GameTableUI extends View {
		public var pokerContainer:Box;
		public var tableInfoPage:TableInfoPageUI;
		public var playerInfoPage:PlayerInfoPageUI;
		public var chatContainer:Box;
		public var popChat2:PopChatItemUI;
		public var popChat0:PopChatItemUI;
		public var popChat1:PopChatItemUI;
		public var calculatePart:CalculatePageUI;
		public var replayControlView:VReplayControllerUI;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":640,"height":1038},"child":[{"type":"Box","props":{"y":0,"x":0,"width":640,"height":1038},"child":[{"type":"Rect","props":{"y":0,"x":0,"width":640,"lineWidth":1,"height":1038,"fillColor":"#007058"}}]},{"type":"Box","props":{"y":0,"x":0,"var":"pokerContainer"},"child":[{"type":"Image","props":{"width":640,"height":1038}}]},{"type":"TableInfoPage","props":{"y":-3,"x":1,"var":"tableInfoPage","runtime":"ui.sddzGame.TableInfoPageUI"}},{"type":"PlayerInfoPage","props":{"y":0,"x":0,"var":"playerInfoPage","mouseThrough":false,"runtime":"ui.sddzGame.PlayerInfoPageUI"}},{"type":"Box","props":{"var":"chatContainer"}},{"type":"PopChatItem","props":{"y":332,"x":4,"var":"popChat2","runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":828,"x":4,"var":"popChat0","runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"PopChatItem","props":{"y":332,"x":218,"width":417,"var":"popChat1","height":70,"runtime":"ui.gameCommon.shortCutChat.PopChatItemUI"}},{"type":"CalculatePage","props":{"var":"calculatePart","runtime":"ui.sddzGame.CalculatePageUI"}},{"type":"VReplayController","props":{"y":0,"x":0,"var":"replayControlView","runtime":"ui.gameCommon.VReplayControllerUI"}}]};
		override protected function createChildren():void {
			View.regComponent("ui.sddzGame.TableInfoPageUI",TableInfoPageUI);
			View.regComponent("ui.sddzGame.PlayerInfoPageUI",PlayerInfoPageUI);
			View.regComponent("ui.gameCommon.shortCutChat.PopChatItemUI",PopChatItemUI);
			View.regComponent("ui.sddzGame.CalculatePageUI",CalculatePageUI);
			View.regComponent("ui.gameCommon.VReplayControllerUI",VReplayControllerUI);
			super.createChildren();
			createView(uiView);

		}

	}
}