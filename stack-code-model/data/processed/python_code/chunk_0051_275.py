package com.kidoz.sdk.api.platforms
{
	import flash.events.StatusEvent;
	import flash.external.ExtensionContext;

	/**
	 * Sdk Controller Version 0.4.0
	 * */
	public class SdkController  
	{
		// Panel Types
		public static const PANEL_TYPE_BOTTOM:int = 0; 
		public static const PANEL_TYPE_TOP:int = 1; 		
		public static const PANEL_TYPE_LEFT:int = 2; 
		public static const PANEL_TYPE_RIGHT:int = 3; 
		
		// Panel Handle Positions
		public static const HANDLE_POSITION_START:int = 0; 
		public static const HANDLE_POSITION_CENTER:int = 1; 
		public static const HANDLE_POSITION_END:int = 2; 		
		
		// Banner Anchor Position
		public static const BANNER_POSITION_TOP:int = 0; 
		public static const BANNER_POSITION_BOTTOM:int = 1; 
		public static const BANNER_POSITION_TOP_LEFT:int = 2; 	
		public static const BANNER_POSITION_TOP_RIGHT:int = 3; 		
		public static const BANNER_POSITION_BOTTOM_LEFT:int = 4; 		
		public static const BANNER_POSITION_BOTTOM_RIGHT:int = 5; 	
		
		// Flexi View Anchor Position
		public static const FLEXI_VIEW_POSITION_TOP_START:int = 0; 
		public static const FLEXI_VIEW_POSITION_TOP_CENTER:int = 1; 
		public static const FLEXI_VIEW_POSITION_TOP_END:int = 2; 	
		public static const FLEXI_VIEW_POSITION_MID_START:int = 3; 		
		public static const FLEXI_VIEW_POSITION_MID_CENTER:int = 4; 		
		public static const FLEXI_VIEW_POSITION_MID_END:int = 5; 
		public static const FLEXI_VIEW_POSITION_BOTTOM_START:int = 6; 		
		public static const FLEXI_VIEW_POSITION_BOTTOM_CENTER:int = 7; 		
		public static const FLEXI_VIEW_POSITION_BOTTOM_END:int = 8;
		
        //-------------------------------------------------		
		private static var instance:SdkController;
		private static var extContext:ExtensionContext = null;	
		private static var mPublisher_id:String;
		private static var mToken:String;		
		private var mFeedViewListener:IFeedViewIntefrace = null;
		private var mPanelViewListener:IPanelViewInterface = null;
		private var mBannerViewListener:IBannerViewInterface = null;
		private var mFlexiViewListener:IFlexiViewInterface = null;
		private var mGeneralEventListener:IGeneralEventInterface = null;
		 	
		// Used for Panel interface listener
		private static const PANEL_VIEW_EVENT:String = "PANEL_VIEW_EVENT"; 
		private static const PANEL_VIEW_EVENT_EXPANDED:String = "PANEL_VIEW_EVENT_EXPANDED";
		private static const PANEL_VIEW_EVENT_COLLAPSED:String = "PANEL_VIEW_EVENT_COLLAPSED";
		private static const PANEL_VIEW_EVENT_PANEL_READY:String = "PANEL_VIEW_EVENT_PANEL_READY";
		
		// Used for Feed interface listener
		private static const FEED_VIEW_EVENT:String = "FEED_VIEW_EVENT"; 
		private static const FEED_VIEW_EVENT_READY_TOSHOW:String = "FEED_VIEW_EVENT_READY_TOSHOW"; 
		private static const FEED_VIEW_EVENT_DISMISS:String = "FEED_VIEW_EVENT_DISMISS"; 
		private static const FEED_VIEW_EVENT_OBJECT_READY:String = "FEED_VIEW_EVENT_OBJECT_READY"; 
		
		// Used for Banner interface listener
		private static const BANNER_VIEW_EVENT:String = "BANNER_VIEW_EVENT";
		private static const BANNER_VIEW_EVENT_READY:String = "BANNER_VIEW_EVENT_READY"; 
		private static const BANNER_VIEW_EVENT_SHOW:String = "BANNER_VIEW_EVENT_SHOW"; 
		private static const BANNER_VIEW_EVENT_HIDE:String = "BANNER_VIEW_EVENT_HIDE"; 
		private static const BANNER_VIEW_EVENT_CONTENT_LOADED:String = "BANNER_VIEW_EVENT_CONTENT_LOADED"; 
		private static const BANNER_VIEW_EVENT_CONTENT_LOAD_FAILED:String = "BANNER_VIEW_EVENT_CONTENT_LOAD_FAILED"; 
		
		// Used for Flexi view interface listener
		private static const FLEXI_VIEW_EVENT:String = "FLEXI_VIEW_EVENT";
		private static const FLEXI_VIEW_EVENT_READY:String = "FLEXI_VIEW_EVENT_READY"; 
		private static const FLEXI_VIEW_EVENT_VISIBLE:String = "FLEXI_VIEW_EVENT_VISIBLE"; 
		private static const FLEXI_VIEW_EVENT_HIDDEN:String = "FLEXI_VIEW_EVENT_HIDDEN"; 
		
		// Used General events interface listener
		private static const GENERAL_VIEW_EVENT:String = "GENERAL_VIEW_EVENT"; 
		private static const PLAYER_EVENT_OPEN:String = "PLAYER_EVENT_OPEN";
		private static const PLAYER_EVENT_CLOSE:String = "PLAYER_EVENT_CLOSE";
	 
		// Sdk controler constructor
		function SdkController(enforcer:SingletonEnforcer)
		{
			extContext = ExtensionContext.createExtensionContext("com.kidoz.sdk.api.platforms","KidozAirBridgeExtension");
			if(extContext) {
				// Add events listener from android native extension
				extContext.addEventListener( StatusEvent.STATUS,onStatusEventHandler);
			}
			
			if ( !extContext ) {
				throw new Error( "Volume native extension is not supported on this platform." );
			}
		} 
		
		/**
		 * Initiate Kidoz sdk controller
		 * 
		 * @param publisher_id
		 * @param String
		 */
		public static function initSdkContoller(publisher_id:String,token:String):SdkController {
			mPublisher_id = publisher_id;
			mToken = token;
			if (instance == null) {
				instance = new SdkController( new SingletonEnforcer());		
				if(instance) {
					extContext.call( "initSdk",publisher_id,token);
				}				
			}		
			return instance;
		}
		 	
		/**
		 * Status event handler , to handle events from native android extension
		 */
		private function onStatusEventHandler(event : StatusEvent ):void {
			if(event.code == FEED_VIEW_EVENT) {				
				 if(mFeedViewListener) {
					 if(event.level == FEED_VIEW_EVENT_READY_TOSHOW) {
						 mFeedViewListener.onReadyToShow();
					 }else if(event.level == FEED_VIEW_EVENT_DISMISS){
						 mFeedViewListener.onDismissView();
					 }
				 }
			}else if(event.code == PANEL_VIEW_EVENT){			
				if(mPanelViewListener) {
					if(event.level == PANEL_VIEW_EVENT_EXPANDED) {
						mPanelViewListener.onPanelViewExpanded();
					}else if(event.level == PANEL_VIEW_EVENT_COLLAPSED){
						mPanelViewListener.onPanelViewCollapsed();
					}else if(event.level == PANEL_VIEW_EVENT_PANEL_READY){
						mPanelViewListener.onPanelViewReady();
					}	
				}
			}else if(event.code == BANNER_VIEW_EVENT){	
				if(mBannerViewListener) {
					if(event.level == BANNER_VIEW_EVENT_SHOW) {
						mBannerViewListener.onBannerShow();
					}else if(event.level == BANNER_VIEW_EVENT_HIDE){
						mBannerViewListener.onBannerHide();
					}else if(event.level == BANNER_VIEW_EVENT_READY){
						mBannerViewListener.onBannerReady();
					}else if(event.level == BANNER_VIEW_EVENT_CONTENT_LOADED){
						mBannerViewListener.onBannerContentLoaded();
					}else if(event.level == BANNER_VIEW_EVENT_CONTENT_LOAD_FAILED){
						mBannerViewListener.onBannerContentLoadFailed();
					}	
				}
			}
			else if(event.code == FLEXI_VIEW_EVENT){	
				if(mFlexiViewListener) {
					if(event.level == FLEXI_VIEW_EVENT_READY) {
						mFlexiViewListener.onFlexiViewReady();
					}else if(event.level == FLEXI_VIEW_EVENT_VISIBLE){
						mFlexiViewListener.onFlexiViewVisible();
					}else if(event.level == FLEXI_VIEW_EVENT_HIDDEN){
						mFlexiViewListener.onFlexiViewHidden();
					}
				}
			}
			else if(event.code == GENERAL_VIEW_EVENT){	
				if(mGeneralEventListener) {
					if(event.level == PLAYER_EVENT_OPEN) {
						mGeneralEventListener.onPlayerOpened();
					}else if(event.level == PLAYER_EVENT_CLOSE){
						mGeneralEventListener.onPlayerClosed();
					}
				}
			}
		} 
		
		/**
		 * Add feed button to view
		 * 
		 * @param x_coord the x coordinate of the view position
		 * @param y_coord the y coordinate of the view position
		 */
		public function addFeedButton(x_coord:Number,y_coord:Number):void {
			if(extContext != null) {
				extContext.call("addFeedButton",x_coord,y_coord);
			}			
		}
			 
		
		/**
		 * Add feed button with size
		 * 
		 * @param x_coord the x coordinate of the view position
		 * @param y_coord the y coordinate of the view position 
		 * @param button_size button new size
		 */
		public function addFeedButtonWithSize(x_coord:Number,y_coord:Number,button_size:Number):void {
			if(extContext != null) {
				extContext.call("addFeedButtonWithSize",x_coord,y_coord,button_size);
			}			
		}
		
		/**
		 * Show feed view on screen
		 */
		public function showFeedView():void {
			if(extContext != null) {
				extContext.call("showFeedView");
			}			
		}	
		
		/**
		 * Dismiss feed view
		 */
		public function dismissFeedView():void {
			if(extContext != null) {
				extContext.call("dismissFeedView");
			}			
		}
		
		 
		/**
		 * Add feed panel view to screen
		 * 
		 * @param panel_type panel type (TOP,BOTTOM,RIGHT,LEFT)
		 * @param handle_position handle position (CENTER,START,STOP)
		 */
		public function addPanleView(panel_type:Number,handle_position:Number):void {
			if(extContext != null) {
				extContext.call("addPanelView",panel_type,handle_position);
			}			
		}
		
		
		/**
		 * Set panl view color in hexa representation 
		 * 
		 * @param color_hexa color in hexa representation (Example : "#ffffff")
		 */
		public function setPanelViewColor(color_hexa:String):void {
			extContext.call("setPanelViewColor",color_hexa);
		}
			
		
		/**
		 * Change panel visibility state
		 * 
		 * @param visible
		 */
		public function changePanelVisivilityState(visible:Boolean):void {
			if(extContext != null) {
				extContext.call("changePanelVisibility",visible);
			}			
		}
 
		/**
		 * Change feed button visibility state
		 * 
		 * @param visible
		 */
		public function changeFeedButtonVisivilityState(visible:Boolean):void {
			if(extContext != null) {
				extContext.call("changeFeedButtonVisibility",visible);
			}			
		}
		
		/**
		 * Collapse panel view
		 */
		public function collapsePanelView():void {
			if(extContext != null) {
				extContext.call("collapsePanelView");
			}			
		}
		
		/**
		 * Expand panel view
		 */
		public function expandPanelView():void {
			if(extContext != null) {
				extContext.call("expandPanelView");
			}			
		}
		
		/**
		 * Get panel viee current state (Expanded/Collapsed)
		 * 
		 * @return if panel expanded or not
		 */
		public function isPanelExpanded():Boolean {
			if(extContext != null) {
				return extContext.call("isPanelExpanded");
			}else {
				return false;
			}
		}
		
		/**
		 * Add Banner view to screen
		 * 
		 * @param banner_anchor_pos banner anchor position on screen (BANNER_POSITION...)
		 */
		public function addBannerView(banner_anchor_pos:Number):void {
			if(extContext != null) {
				 extContext.call("addBannerView",banner_anchor_pos);
			} 
		}
		
		/**
		 * Change Banner view anchor position on screen
		 * 
		 * @param banner_anchor_pos banner anchor position on screen (BANNER_POSITION...)
		 */
		public function changeBannerViewPosition(banner_anchor_pos:Number):void {
			if(extContext != null) {
				extContext.call("changeBannerPosition",banner_anchor_pos);
			} 
		}	
		
		/**
		 * Show banner view		 
		 */
		public function showBannerView():void {
			if(extContext != null) {
				extContext.call("showBannerView");
			}
		}
		
		/**
		 * Hide banner view		 
		 */
		public function hideBannerView():void {
			if(extContext != null) {
				extContext.call("hideBannerView");
			}
		}
			
		/**
		 * Add Flexi point view to screen
		 * 
		 * @param isAutoShow notify if to show the flexi view right away when its ready 
		 * @param initial_pos the initial position of the flexi view on screen (FLEXI_VIEW_POSITION_TOP_START... )
		 */
		public function addFlexiView(isAutoShow:Boolean,initial_pos:Number):void {
			if(extContext != null) {
				extContext.call("addFlexiView",isAutoShow,initial_pos);
			} 
		}
		
		
		/**
		 * Show and make visible flexi view on screen
		 */
		public function showFlexiView():void {
			if(extContext != null) {
				extContext.call("showFlexiView");
			} 
		}
		
		
		/**
		 * Hide and make invisible flexi point view 
		 */
		public function hideFlexiView():void {
			if(extContext != null) {
				extContext.call("hideFlexiView");
			} 
		}
		
		/**
		 * Get is felxi ciew currently visible
		 */
		public function getIsFlexiViewVisible():Boolean {
			if(extContext != null) {
				return extContext.call("getIsFlexiViewVisible");
			}else {
				return false;
			}
		}	
			
	 	
		/**
		 * Set on panel view event listener
		 * 
		 * @param listener class that implemets "IPanelViewInterface" interface
		 */
		public function setOnPanelViewEventListener(listener:IPanelViewInterface):void {
			mPanelViewListener = listener;
		}
		
		/**
		 * Set on feed view event listener
		 * 
		 * @param listener class that implemets "IFeedViewIntefrace" interface 
		 */
		public function setOnFeedViewEventListener(listener:IFeedViewIntefrace):void {
			mFeedViewListener = listener;
		}
		
		/**
		 * Set on Banner view event listener
		 * 
		 * @param listener class that implemets "IBannerViewInterface" interface 
		 */
		public function setOnBannerViewEventListener(listener:IBannerViewInterface):void {
			mBannerViewListener = listener;
		}
		
		
		/**
		 * Set on Flexi view event listener
		 * 
		 * @param listener class that implemets "IFlexiViewInterface" interface 
		 */
		public function setOnFlexiViewEventListener(listener:IFlexiViewInterface):void {
			mFlexiViewListener = listener;
		}
		
		/**
		 * Set on General event listener
		 * Used to catch sdk general event (Player opened,Player closed)
		 * 
		 * @param listener class that implemets "IGeneralEventInterface" interface 
		 */
		public function setOnGeneralEventListener(listener:IGeneralEventInterface):void {
			mGeneralEventListener = listener;
		}		
		
		/**
		 * Cleans up the instance of the native extension. 
		 */		
		public function dispose():void { 
			extContext.dispose(); 
		}
			
		/**
		 * Print function for debuging purposes
		 * 
		 * @text some thext to print
		 */		
		public function printToastDebugLog(text:String):void {
			extContext.call("printToastLog",text);
		}
	}	
}

internal class SingletonEnforcer { }