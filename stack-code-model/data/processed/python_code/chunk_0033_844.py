package 
{
	import com.utilities.EmbedSecure;
	import com.utilities.LinkButtons;
	import flash.display.DisplayObject;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.ContextMenuEvent;
	import flash.events.Event;
	import flash.events.ProgressEvent;
	import flash.events.TimerEvent;
	import flash.net.URLRequest;
	import flash.utils.getDefinitionByName;
	import flash.ui.ContextMenu;
	import flash.ui.ContextMenuItem;
	import flash.utils.Timer;
	import flash.net.*;
	//import com.utilities.MochiBot;
	///import com.utilities.MochiAd;
	//import com.utilities.MochiServices
	//import com.utilities.MochiScores
	//import mochi.as3.MochiAd;

	/**
	 * ...
	 * @author Ian Stokes www.unit2design.com
	 */
	public dynamic class Preloader extends MovieClip
	{
		
		[Embed (source = './embed/preloader.swf' , mimeType = "application/octet-stream")]
		private var preloadArt : Class;
		
		private var _preloader:MovieClip;
		public static var preRef:Preloader;
		public static var stageObj:Stage
		public var _started:Boolean = false
		private var _adDone:Boolean=false
		public static var loadingScores:Boolean = true
		private var _locked:Boolean=false
		//public  var mochiClip:MovieClip = new MovieClip();
		public function Preloader() 
		{
			if (stage == null) {
			addEventListener(Event.ADDED_TO_STAGE, initPreloader)	
			}else {
			initPreloader();	
			}
		}
		private function delLock(event:Event):void {
			
			//var allowed_site:String = "www.villagethegame.com";
            //var domain:String = this.root.loaderInfo.url.split("/")[2];
           //if (domain.indexOf(allowed_site) == (domain.length - allowed_site.length)) {
              //}else {
				//this.visible = false;
				//LinkButtons.getUrl("http://www.villagethegame.com");
			 //}
			
		}
		private function initPreloader(event:Event=null):void {
			var preloadArtSecure:EmbedSecure = new EmbedSecure(preloadArt);
			preloadArtSecure.addEventListener(EmbedSecure.ARTREADY_EVENT, init);
			addEventListener(Event.ENTER_FRAME, checkFrame);
			this.stage.frameRate = 61;
			this.stage.quality = "HIGH";
			this.stage.scaleMode = StageScaleMode.NO_SCALE;
			this.stage.align = StageAlign.TOP_LEFT;
			var myMenu:ContextMenu = new ContextMenu();
			var copyright:ContextMenuItem = new ContextMenuItem( "Copyright ©2010 villagethegame" );
            var more:ContextMenuItem = new ContextMenuItem( "★ Village The Game ★" );
			copyright.addEventListener( ContextMenuEvent.MENU_ITEM_SELECT, visit_flashmo );
			more.addEventListener( ContextMenuEvent.MENU_ITEM_SELECT, visit_flashmo );
            more.separatorBefore = false;
            myMenu.hideBuiltInItems();
			myMenu.customItems.push(copyright);
			myMenu.customItems.push(more);
			this.contextMenu = myMenu;
			stageObj = stage
			//MochiAd.showPreGameAd({clip:this, id:"17f8fa80ed3b0fa1", res:"750x550"});
		}
		private function visit_flashmo(event:Event):void {
			 var flashmo_link:URLRequest = new URLRequest( "http://www.villagethegame.com" );
			 navigateToURL( flashmo_link, "_blank" );
            
		}
		private function init(event:Event):void {
			
			var tempClass:Class = event.target.grabClass("loadersystem");
			_preloader = new tempClass();
			addChild(_preloader);
			/*
			this.addChild(mochiClip);
			MochiServices.connect("f43f29dc53d9dbb9", mochiClip);
			var _mochiads_game_id:String = "f43f29dc53d9dbb9";
			MochiAd.showPreGameAd( { clip:mochiClip, id:_mochiads_game_id, res:"640x480", ad_finished:completeAd } );
			MochiBot.track(this, "80240503") 
			MochiAd.showPreGameAd( { clip:mochiClip, id:_mochiads_game_id, res:"640x480" } );
			*/
			//completeAd();
			
		}
		private function checkFrame(e:Event):void 
		{
			var percent:uint = (root.loaderInfo.bytesLoaded / root.loaderInfo.bytesTotal) * 100;
			if(_preloader){
				_preloader.hold.percent.text = String((percent)).substr(0, 3) + "%";
				_preloader.hold.bar.scaleX = root.loaderInfo.bytesLoaded / root.loaderInfo.bytesTotal };
			if (currentFrame == totalFrames)
			{
			   removeEventListener(Event.ENTER_FRAME, checkFrame);
			   var fdPre:Timer = new Timer(20, 10);
			   fdPre.addEventListener(TimerEvent.TIMER, fadeOutPreloader);
			   fdPre.addEventListener(TimerEvent.TIMER_COMPLETE, removeMainPreloader);
			   fdPre.start();
			}
		}
		private function fadeOutPreloader(event:TimerEvent):void {
			_preloader.alpha-=.1
		}
		private function removeMainPreloader(event:TimerEvent):void {
		    event.target.removeEventListener(TimerEvent.TIMER, fadeOutPreloader);
			event.target.removeEventListener(TimerEvent.TIMER_COMPLETE, removeMainPreloader);
			_started = true;
			//temp..remove
			completeAd();
			//
		}
		private function completeAd():void 
		{
			stop();
			var mainClass:Class = getDefinitionByName("Main") as Class;
			addChildAt(new mainClass() as DisplayObject, 0);
			removeChild(_preloader)
		}
		public static  function setHighScore(scr:Number):void {
		    loadingScores = true;
		    stageObj.quality = "high";
		    if(scr>0){
				//MochiScores.showLeaderboard( { boardID:"828ceea45de30cb3", score:scr, onClose:leaderboardClose } ) 
			}
		}
	    private static function leaderboardClose():void {
			loadingScores = false;
			stageObj.quality = "low"; 
	    }
	}
}