package application.assetLibs {
	
	import application.MainSettings;
	import flash.events.ProgressEvent;
	import flash.events.Event;

	
	public class ItemLoader extends LoaderCore {
		
		public function ItemLoader(url:String) {
			
			_callLoadAssets(url);
			
		}
		
		override public function _onComplete(event:Event):void {
			
			try {
				
				var $o:Object = event.target.applicationDomain;
				
				 //cards: */
				 
				ItemLibrary.getItem.NewCards                          = $o.getDefinition("dynamicClass.NewCards") as Class;
				
				//alerts & popups
				ItemLibrary.getItem.AlertJoin_Source                  = $o.getDefinition("dynamicClass.AlertJoin_Source") as Class;
				ItemLibrary.getItem.AlertJoinWaiting_Source           = $o.getDefinition("dynamicClass.AlertJoinWaiting_Source") as Class;
				ItemLibrary.getItem.AlertError_Source                 = $o.getDefinition("dynamicClass.AlertError_Source") as Class;
				ItemLibrary.getItem.AlertReplayGame_Source            = $o.getDefinition("dynamicClass.AlertReplayGame_Source") as Class;
				ItemLibrary.getItem.AlertGameOverWin_Source           = $o.getDefinition("dynamicClass.AlertGameOverWin_Source") as Class;
				ItemLibrary.getItem.AlertGameOverLoose_Source         = $o.getDefinition("dynamicClass.AlertGameOverLoose_Source") as Class;

				ItemLibrary.getItem.DropDownItem_Source               = $o.getDefinition("dynamicClass.DropDownItem_Source") as Class;
				
				ItemLibrary.getItem.LobbyScroller                     = $o.getDefinition("dynamicClass.LobbyScroller") as Class;
				ItemLibrary.getItem.LobbyRoomItem                     = $o.getDefinition("dynamicClass.LobbyRoomItem") as Class;
				ItemLibrary.getItem.TablePlayGame_Source              = $o.getDefinition("dynamicClass.TablePlayGame_Source") as Class;
				ItemLibrary.getItem.CardColorChoose_Source            = $o.getDefinition("dynamicClass.CardColorChoose_Source") as Class;
				ItemLibrary.getItem.CardHighColor_Source              = $o.getDefinition("dynamicClass.CardHighColor_Source") as Class;
				ItemLibrary.getItem.Chat_Source                       = $o.getDefinition("dynamicClass.Chat_Source") as Class;
				ItemLibrary.getItem.ChatItem                          = $o.getDefinition("dynamicClass.ChatItem") as Class;
				
				ItemLibrary._effectSpark                              = $o.getDefinition("dynamicClass.EffectSpark") as Class;
				ItemLibrary._lobbyStatistics_Source                   = $o.getDefinition("dynamicClass.LobbyStatistics_Source") as Class;
				ItemLibrary._lobbyStatisticsItem_Source               = $o.getDefinition("dynamicClass.LobbyStatisticsItem_Source") as Class;
				ItemLibrary._lobbyScene                               = $o.getDefinition("dynamicClass.LobbyScene") as Class;
				ItemLibrary._creatRoom                                = $o.getDefinition("dynamicClass.CreatRoom") as Class;
				ItemLibrary._gameLogo                                 = $o.getDefinition("dynamicClass.GameLogo") as Class;
				ItemLibrary._alertBugReport_Source                    = $o.getDefinition("dynamicClass.AlertBugReport_Source") as Class;
				
				ItemLibrary._historyBg_Source                         = $o.getDefinition("dynamicClass.HistoryBg_Source") as Class;
				ItemLibrary._historyListItem_Source                   = $o.getDefinition("DynamicClass.HistoryListItem_Source") as Class;
				ItemLibrary._historyController_Source                 = $o.getDefinition("dynamicClass.HistoryController_Source") as Class;
				
				_configureRemoveListeners();
				
				_loaded = true;
				dispatchEvent(new AppEvent(AppEvent.RESOURCE_LOADED, null, true));
			} catch (e:ReferenceError) {
				
				//MainSettings.instance.container.preloader.error_txt.text = e;
				throw new Error("error loading ItemLibrary: " + e);
				
			}
		}

		
		override public function _onProgressHandler(event:ProgressEvent):void {
			
			MainSettings.instance.container.preloader._updateProgress(event.bytesTotal, event.bytesLoaded, null, 'Loading Graphic Assets...');
		
		}
	}
}