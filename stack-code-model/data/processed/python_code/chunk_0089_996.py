package
{
	/**
	 * ...
	 * @author Ghelle
	 */
	
	import Assets;
	import com.bonsters.B;
	import com.greensock.TweenLite;
	import com.greensock.TweenMax;
	import com.mesmotronic.ane.AndroidFullScreen;
	import com.xtdstudios.common.assetsLoader.AssetsLoaderFromByteArray;
	import com.xtdstudios.DMT.DMTBasic;
	import com.xtdstudios.common.assetsLoader.AssetsLoaderFromExternalURL;
	import flash.display.SimpleButton;
	import flash.display.StageDisplayState;
	import flash.events.MouseEvent;
	import flash.system.Security;
	OO::MOB { import flash.desktop.NativeApplication; }
	OO::MOB { import flash.desktop.SystemIdleMode; }
	import flash.display.Bitmap;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageQuality;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.external.ExternalInterface;
	import flash.geom.Rectangle;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.system.ApplicationDomain;
	import flash.system.Capabilities;
	import flash.system.System;
	import flash.text.TextField;
	import flash.text.TextFieldType;
	import flash.ui.Keyboard;
	import flash.utils.ByteArray;
	import game.Audio;
	import game.Cloud;
	import game.DataBox;
	import game.InApp;
	import game.events.OOe;
	import game.StarlingRoot;
	import game.Ads;
	import starling.core.Starling;
	import starling.events.Event;
	
	
	
	
	
	
	public class GAME extends Sprite
	{
		
		/*
		OO::AND {
			[Embed(source="assets/graphics/splashScreenRelease.jpg", mimeType="image/jpg")]
			public static const splashScreen:Class;
		}
		OO::IOS {
			[Embed(source="assets/graphics/splashScreen.jpg", mimeType="image/jpg")]
			public static const splashScreen:Class;
		}
		OO::FB {
			[Embed(source="assets/graphics/splashScreen.jpg", mimeType="image/jpg")]
			public static const splashScreen:Class;
		}
		OO::WEB {
			[Embed(source="assets/graphics/splashScreen.jpg", mimeType="image/jpg")]
			public static const splashScreen:Class;
		}
		*/
		
		
		/*
		[Embed(source="assets/vector/popups.swf", mimeType="application/octet-stream")] 
		private var popups:Class;
		*/
		
		//public var splashScreen:flash.display.Sprite;
		
		public static var main:GAME;
		
		private var starling:Starling;
		private var starlingRoot:StarlingRoot;
		
		
		public var andMarketLink:String = "market://details?id=air.com.bonsters.ooppo";
		
		
		OO::AND {
			public var platform:String = "and";
			public var segmentPublisher:String = "Android"; 
		}
		OO::IOS {
			public var platform:String = "ios";
			public var segmentPublisher:String = "iOS";
		}
		OO::FB {
			public var platform:String = "fb";
			public var segmentPublisher:String = "Facebook";
		}
		OO::WEB {
			public var platform:String = "web";
			public var segmentPublisher:String = "WEB";
		}
		
		
		
		
		
		
		
		
		public function GAME()
		{
			GAME.main = this;
			
			this.addEventListener(flash.events.Event.ADDED_TO_STAGE, handleAdedToStage);
			
		}
		
		
		
		// ------------------------------------- GAME START PLACE ------------------------------------------
		
		public function handleAdedToStage(event:flash.events.Event):void
		{
			this.removeEventListener(flash.events.Event.ADDED_TO_STAGE, handleAdedToStage);
			
			B.Log("==========", "handleAdedToStage", "==========");
			
			
			
			
			
			// --------- STAGE SCALE ---------
			
			
			//stage.scaleMode = StageScaleMode.SHOW_ALL;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			
			stage.quality = StageQuality.BEST;
			
			stage.color = 0xB0E0FF;
			
			stage.addEventListener(flash.events.Event.RESIZE, resizeStage);
			
			
			
			
			
			
			
			
			
			// --------- STAFF ---------
			
			
			OO::sitelock
			{
				if (siteLockCheck() == "lock") return;
			}
			
			
			
			
			OO::MOB { NativeApplication.nativeApplication.systemIdleMode = SystemIdleMode.KEEP_AWAKE; }
			
			
			
			stage.addEventListener(MouseEvent.RIGHT_CLICK, function (e):void {} );
			
			
			
			
			
			
			
			
			TweenLite.delayedCall(0.02, initStarling);
			
		}
		
		
		
		private function initStarling():void
		{
			B.Log("==========", "initStarling", "==========");
			
			// ---------------------- STARLING START ----------------------
			
			Starling.multitouchEnabled = false;
			Starling.handleLostContext = true;
			
			starling = new Starling(game.StarlingRoot, stage, null, null, "auto", "auto");
			
			Starling.current.stage.addEventListener("starlingAddedToStage", starlingAddedToStageHandler);
			
			
			addEventListener("CHANGE_GAME_STATUS", ChangeGameStatus);
			Starling.current.stage.addEventListener("CHANGE_GAME_STATUS", ChangeGameStatus);
			
			addEventListener("UI", showUI);
			Starling.current.stage.addEventListener("UI", showUI);
			
			starling.simulateMultitouch = false;
			starling.antiAliasing = 1;
			starling.start();
			
			
			
			OO::stats {
				Starling.current.showStats = true;
			}
			
			
			// ---------------------- -------------- ----------------------
			
			
			
			setFocusListener();
			
			
			
			
			
			
		}
		
		
		public function starlingAddedToStageHandler(e:*):void
		{
			B.Log("==========", "starlingAddedToStageHandler", "==========");
			
			//starlingRoot = starling.stage.getChildAt(0) as Game; // good too
			starlingRoot = Starling.current.root as game.StarlingRoot;
			
			
			
			
		}
		
		
		
		
		
		
		
		
		//------------------------------------- RESIZE SCREENS --------------------------------------
		
		
		private function resizeStage(e:flash.events.Event):void {
			
			if (starlingRoot)
			{
				
				if (!starling.isStarted) {
					
					starling.start();
					stage.frameRate = 60;
					
					TweenLite.delayedCall( 
						0.1, 
						function ():void
						{
							TweenMax.pauseAll();
							
							starling.stop(true);
							stage.frameRate = 0.1;
						}
					);
				}
				
				
				var ar:Number = stage.stageWidth / stage.stageHeight;
				var sc:Number = stage.stageHeight / 800;
				
				
				var viewPortRectangle:Rectangle = new Rectangle();
				viewPortRectangle.height = stage.stageHeight;
				viewPortRectangle.width = stage.stageWidth;
				Starling.current.viewPort = viewPortRectangle;
				
				
				starling.stage.stageHeight = 800;
				starling.stage.stageWidth = 800 * ar;
				
				
				
				
				starlingRoot.setMask(
					(Starling.current.stage.stageWidth - 600) / 2 ,
					0,
					600,
					800
				)
				
				alignUIs();
				
				
			}
			
			
			alignUIsFL();
		}
		
		
		
		public function alignUIs():void
		{
			
			starlingRoot.PLAY.x = (Starling.current.stage.stageWidth - 450) / 2;
			starlingRoot.screenMAIN.x = (Starling.current.stage.stageWidth - 450) / 2;
			starlingRoot.screenSELECT.x = (Starling.current.stage.stageWidth - 450) / 2;
			starlingRoot.screenPLAY.x = (Starling.current.stage.stageWidth - 450) / 2;
			starlingRoot.screenPAUSE.x = (Starling.current.stage.stageWidth - 450) / 2;
			starlingRoot.screenEND.x = (Starling.current.stage.stageWidth - 450) / 2;
			
			
			for each (var item:String in dmtUIs) 
			{
				if (starlingRoot[item]) starlingRoot[item].x = (Starling.current.stage.stageWidth - 450) / 2 + 450 / 2;
			}
			
			if (starlingRoot.popupSETTINGS) starlingRoot.popupSETTINGS.resize();
			if (starlingRoot.popupREG) starlingRoot.popupREG.resize();
			
		}
		
		
		
		private function alignUIsFL():void
		{
			
			var sc:Number = stage.stageHeight / 800;
			
			if (splashScreen) {
				splashScreen.scaleX = splashScreen.scaleY = sc;
				splashScreen.x = stage.stageWidth / 2;
			}
			
			
		}
		
		
		
		
		
		
		
		
		
		
		
		
		
		//------------------------- FOCUS ----------------------------
		
		
		
		private function setFocusListener():void 
		{
			
			//stage.addEventListener(flash.events.Event.ACTIVATE, activated);
			stage.addEventListener(flash.events.Event.DEACTIVATE, deactivated);
			
		}
		
		
		
		private function deactivated(event:flash.events.Event):void 
		{
			stage.removeEventListener(flash.events.Event.DEACTIVATE, deactivated);
			stage.addEventListener(flash.events.Event.ACTIVATE, activated);
			
			
			
			
			OO::IOS 
			{
				TweenMax.pauseAll();
				
				starling.stop(true);
				stage.frameRate = 0.1;
				return;
				
			}
			
			
			TweenLite.delayedCall( 
				0.05,
				function ():void
				{
					TweenMax.pauseAll();
					
					starling.stop(true);
					stage.frameRate = 0.1;
				}
			);
		}
		
		
		
		
		private function activated(event:flash.events.Event):void 
		{
			stage.addEventListener(flash.events.Event.DEACTIVATE, deactivated);
			stage.removeEventListener(flash.events.Event.ACTIVATE, activated);
			
			
			
			if (!starling.isStarted) starling.start(); 
			stage.frameRate = 60;
			
			
			TweenMax.ticker.dispatchEvent(new flash.events.Event("enterFrame"));
			TweenMax.resumeAll();
			
			
			
		}
		
		
		
		
		
		
		
		
		
		
		// ------------------- SITELOCK -----------------------
		
		
		private function siteLockCheck():String
		{
			
			var url:String;
			if (ExternalInterface.available){
				url = ExternalInterface.call("window.location.href.toString"); }
			else{
				url = loaderInfo.loaderURL; }
			
			
			var allowedDomains:String = "bonsters.co|chesswoodknights.com|ooppogame.com|gator4119.hostgator.com|flashgamelicense.com|fgl.com|www.fgl.com";
			 
			var allowedPattern:String = "^http(|s)://("+allowedDomains+")/";
			var domainCheck:RegExp = new RegExp(allowedPattern, "i");
			
			
			if (!domainCheck.test(url)){
				// domain check failed, abort application
				
				
				B.Log(url);
				return "lock";
			}else{
				// domain okay, proceed
				
				return "ok";
			}
		}
		
		
		
		
	}

}