package  {
	
	import flash.geom.Point;
	import flash.events.TimerEvent;
	import flash.text.TextFormat;
	import flash.utils.*;
	import flash.utils.setTimeout;
	import flash.utils.Timer;
	import starling.animation.Transitions;
	import starling.animation.Tween;
	import starling.core.Starling;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.display.Stage;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.text.TextField;
	import starling.textures.Texture;
	import starling.textures.TextureSmoothing;
	import starling.utils.HAlign;
	import starling.utils.VAlign;

	
	public class Store {
		
		static var point:Point;
		static var storeTouchList:Vector.<Touch>;
		static var purchaseWindowUp:Boolean = false;
		static var storeBG:Image;
		static var storeHeaderLarge:TextField;
		static var storeHeaderSmall:TextField;
		static var storeButton1:Sprite;
		static var storeButton1Filler:Image;
		static var storeButton1Sub:Sprite;
		static var storeButton1Text1:TextField;
		static var storeButton1Text2:TextField;
		static var storeButton1Text3:TextField;
		static var storeButton2:Sprite;
		static var storeButton2Filler:Image;
		static var storeButton2Sub:Sprite;
		static var storeButton2Text1:TextField;
		static var storeButton2Text2:TextField;
		static var storeButton2Text3:TextField;
		static var storeButton3:Sprite;
		static var storeButton3Filler:Image;
		static var storeButton3Sub:Sprite;
		static var storeButton3Text1:TextField;
		static var storeButton3Text2:TextField;
		static var storeButton3Text3:TextField;
		static var cancelButton:Sprite;
		static var cancelButtonFiller:Image;
		static var cancelButtonText:TextField;
		static var statusText:TextField;
		static var elimText:TextField;
		static var storeButton1On:Boolean = false;
		static var storeButton2On:Boolean = false;
		static var storeButton3On:Boolean = false;
		static var cancelButtonOn:Boolean = false;
		static var didPurchase:Boolean = false;


		static function display(stage:Stage) {
			storeBG = Atlas.generate("filler");
			storeBG.width = int(Main.screenWidth*0.84375);
			storeBG.x = int((Main.screenWidth - storeBG.width)/2);
			storeBG.y = storeBG.x;
			storeBG.height = Main.screenHeight - (Main.screenWidth - storeBG.width);
			storeBG.color = Hud.statsBoxColor;
			storeBG.touchable = false;
			stage.addChild(storeBG);
			Screens.storeScreenObjects.push(storeBG);
			
			storeHeaderLarge = new TextField(int(Environment.rectSprite.width*0.76), int(Environment.rectSprite.height*0.0638), String("PURCHASE ELIMS"), "Font", int(Environment.rectSprite.height*0.052), Intro.textColorOff, false);
			storeHeaderLarge.hAlign = HAlign.CENTER;
			storeHeaderLarge.vAlign = VAlign.CENTER;
			storeHeaderLarge.x = Main.screenWidth/2 - storeHeaderLarge.width/2;
			storeHeaderLarge.y = int((Environment.rectSprite.height*0.0942) + Environment.rectSprite.y);
			storeHeaderLarge.touchable = false;
			storeHeaderLarge.visible = false;
			stage.addChild(storeHeaderLarge);
			Screens.storeScreenObjects.push(storeHeaderLarge);
			
			storeHeaderSmall = new TextField(int(Environment.rectSprite.width*0.58), int(Environment.rectSprite.height*0.075), String("HOW MANY WOULD\nYOU LIKE?"), "Font", int(Environment.rectSprite.height*0.0295), Intro.textColorOff, false);
			storeHeaderSmall.hAlign = HAlign.CENTER;
			storeHeaderSmall.vAlign = VAlign.CENTER;
			storeHeaderSmall.x = Main.screenWidth/2 - storeHeaderSmall.width/2;
			storeHeaderSmall.y = int((Environment.rectSprite.height*0.1745) + Environment.rectSprite.y);
			storeHeaderSmall.touchable = false;
			storeHeaderSmall.visible = false;
			stage.addChild(storeHeaderSmall);
			Screens.storeScreenObjects.push(storeHeaderSmall);
			
			storeButton1 = new Sprite();
			stage.addChild(storeButton1);
			storeButton1.visible = false;
			storeButton1Filler = Atlas.generate("filler");
			storeButton1Filler.width = storeBG.width;
			storeButton1Filler.height = int(Environment.rectSprite.height*0.1196);
			storeButton1Filler.color = Hud.storeBoxColor;
			storeButton1.addChild(storeButton1Filler);
			storeButton1Sub = new Sprite();
			storeButton1.addChild(storeButton1Sub);
			storeButton1Text1 = new TextField(int(Environment.rectSprite.width*0.159375), int(Environment.rectSprite.height*0.0588), String("50"), "Font", int(Environment.rectSprite.height*0.0412), Hud.highlightColorList[Hud.colorTheme], false);
			storeButton1Text1.hAlign = HAlign.LEFT;
			storeButton1Text1.vAlign = VAlign.CENTER;
			storeButton1Text1.touchable = false;
			storeButton1Text2 = new TextField(int(Environment.rectSprite.width*0.192), int(Environment.rectSprite.height*0.055), String("ELIMS"), "Font", int(Environment.rectSprite.height*0.033), Intro.textColorOff, false);
			storeButton1Text2.hAlign = HAlign.RIGHT;
			storeButton1Text2.vAlign = VAlign.CENTER;
			storeButton1Text2.x = int((Environment.rectSprite.width*0.28) - storeButton1Text2.width);
			storeButton1Text2.y = int(Environment.rectSprite.width*0.006);
			storeButton1Text2.touchable = false;
			storeButton1Sub.addChild(storeButton1Text1);
			storeButton1Sub.addChild(storeButton1Text2);
			storeButton1Sub.x = storeButton1Filler.width/2 - storeButton1Sub.width/2;
			storeButton1Sub.y = int(Environment.rectSprite.height*0.00873);
			storeButton1Text3 = new TextField(int(Environment.rectSprite.width*0.234375), int(Environment.rectSprite.height*0.0589), String("$0.99"), "Font", int(Environment.rectSprite.height*0.0412), Intro.textColorOff, false);
			storeButton1Text3.hAlign = HAlign.CENTER;
			storeButton1Text3.vAlign = VAlign.CENTER;
			storeButton1Text3.x = storeButton1Filler.width/2 - storeButton1Text3.width/2;
			storeButton1Text3.y = int(Environment.rectSprite.height*0.0523);
			storeButton1Text3.touchable = false;
			if (Environment.totalRedux + Environment.currentRedux >= 999500) {
				storeButton1Text1.color = 0x7B7B7B;
				storeButton1Text2.color = 0x7B7B7B;
				storeButton1Text3.color = 0x7B7B7B;
			}
			storeButton1.x = storeBG.x;
			storeButton1.y = int((Environment.rectSprite.height*0.3245) + Environment.rectSprite.y);
			storeButton1.addChild(storeButton1Text3);
			Screens.storeScreenObjects.push(storeButton1);
			
			storeButton2 = new Sprite();
			stage.addChild(storeButton2);
			storeButton2.visible = false;
			storeButton2Filler = Atlas.generate("filler");
			storeButton2Filler.width = storeBG.width;
			storeButton2Filler.height = int(Environment.rectSprite.height*0.1196);
			storeButton2Filler.color = Hud.storeBoxColor;
			storeButton2.addChild(storeButton2Filler);
			storeButton2Sub = new Sprite();
			storeButton2.addChild(storeButton2Sub);
			storeButton2Text1 = new TextField(int(Environment.rectSprite.width*0.234375), int(Environment.rectSprite.height*0.0588), String("300"), "Font", int(Environment.rectSprite.height*0.0412), Hud.highlightColorList[Hud.colorTheme], false);
			storeButton2Text1.hAlign = HAlign.LEFT;
			storeButton2Text1.vAlign = VAlign.CENTER;
			storeButton2Text1.touchable = false;
			storeButton2Text2 = new TextField(int(Environment.rectSprite.width*0.1875), int(Environment.rectSprite.height*0.055), String("ELIMS"), "Font", int(Environment.rectSprite.height*0.033), Intro.textColorOff, false);
			storeButton2Text2.hAlign = HAlign.RIGHT;
			storeButton2Text2.vAlign = VAlign.CENTER;
			storeButton2Text2.x = int((Environment.rectSprite.width*0.325) - storeButton2Text2.width);
			storeButton2Text2.y = int(Environment.rectSprite.width*0.006);
			storeButton2Text2.touchable = false;
			storeButton2Sub.addChild(storeButton2Text1);
			storeButton2Sub.addChild(storeButton2Text2);
			storeButton2Sub.x = storeButton2Filler.width/2 - storeButton2Sub.width/2;
			storeButton2Sub.y = int(Environment.rectSprite.height*0.00873);
			storeButton2Text3 = new TextField(int(Environment.rectSprite.width*0.234375), int(Environment.rectSprite.height*0.0589), String("$1.99"), "Font", int(Environment.rectSprite.height*0.0412), Intro.textColorOff, false);
			storeButton2Text3.hAlign = HAlign.CENTER;
			storeButton2Text3.vAlign = VAlign.CENTER;
			storeButton2Text3.x = storeButton2Filler.width/2 - storeButton2Text3.width/2;
			storeButton2Text3.y = int(Environment.rectSprite.height*0.0523);
			storeButton2Text3.touchable = false;
			if (Environment.totalRedux + Environment.currentRedux >= 998500) {
				storeButton2Text1.color = 0x7B7B7B;
				storeButton2Text2.color = 0x7B7B7B;
				storeButton2Text3.color = 0x7B7B7B;
			}
			storeButton2.x = storeBG.x;
			storeButton2.y = int((Environment.rectSprite.height*0.4902) + Environment.rectSprite.y);
			storeButton2.addChild(storeButton2Text3);
			Screens.storeScreenObjects.push(storeButton2);
			
			storeButton3 = new Sprite();
			stage.addChild(storeButton3);
			storeButton3.visible = false;
			storeButton3Filler = Atlas.generate("filler");
			storeButton3Filler.width = storeBG.width;
			storeButton3Filler.height = int(Environment.rectSprite.height*0.1196);
			storeButton3Filler.color = Hud.storeBoxColor;
			storeButton3.addChild(storeButton3Filler);
			storeButton3Sub = new Sprite();
			storeButton3.addChild(storeButton3Sub);
			storeButton3Text1 = new TextField(int(Environment.rectSprite.width*0.234375), int(Environment.rectSprite.height*0.0588), String("1,000"), "Font", int(Environment.rectSprite.height*0.0412), Hud.highlightColorList[Hud.colorTheme], false);			
			storeButton3Text1.hAlign = HAlign.LEFT;
			storeButton3Text1.vAlign = VAlign.CENTER;
			storeButton3Text1.touchable = false;
			storeButton3Text2 = new TextField(int(Environment.rectSprite.width*0.1875), int(Environment.rectSprite.height*0.055), String("ELIMS"), "Font", int(Environment.rectSprite.height*0.033), Intro.textColorOff, false);
			storeButton3Text2.hAlign = HAlign.RIGHT;
			storeButton3Text2.vAlign = VAlign.CENTER;
			storeButton3Text2.x = int((Environment.rectSprite.width*0.392) - storeButton3Text2.width);
			storeButton3Text2.y = int(Environment.rectSprite.width*0.006);
			storeButton3Text2.touchable = false;
			storeButton3Sub.addChild(storeButton3Text1);
			storeButton3Sub.addChild(storeButton3Text2);
			storeButton3Sub.x = storeButton3Filler.width/2 - storeButton3Sub.width/2;
			storeButton3Sub.y = int(Environment.rectSprite.height*0.00873);
			storeButton3Text3 = new TextField(int(Environment.rectSprite.width*0.234375), int(Environment.rectSprite.height*0.05882), String("$2.99"), "Font", int(Environment.rectSprite.height*0.0412), Intro.textColorOff, false);
			storeButton3Text3.hAlign = HAlign.CENTER;
			storeButton3Text3.vAlign = VAlign.CENTER;
			storeButton3Text3.x = storeButton3Filler.width/2 - storeButton3Text3.width/2;
			storeButton3Text3.y = int(Environment.rectSprite.height*0.0523);
			storeButton3Text3.touchable = false;
			if (Environment.totalRedux + Environment.currentRedux >= 995000) {
				storeButton3Text1.color = 0x7B7B7B;
				storeButton3Text2.color = 0x7B7B7B;
				storeButton3Text3.color = 0x7B7B7B;
			}			
			storeButton3.x = storeBG.x;
			storeButton3.y = int((Environment.rectSprite.height*0.6559) + Environment.rectSprite.y);
			storeButton3.addChild(storeButton3Text3);
			Screens.storeScreenObjects.push(storeButton3);
			
			cancelButton = new Sprite();			
			stage.addChild(cancelButton);
			cancelButton.visible = false;
			cancelButtonFiller = Atlas.generate("filler");
			cancelButtonFiller.width = storeBG.width;
			cancelButtonFiller.height = int(Environment.rectSprite.height*0.06);
			cancelButtonFiller.color = storeBG.color;
			cancelButton.addChild(cancelButtonFiller);
			cancelButtonText = new TextField(cancelButtonFiller.width, cancelButtonFiller.height, String("BACK"), "Font", int(Environment.rectSprite.height*0.0412), Intro.textColorOff, false);
			cancelButtonText.hAlign = HAlign.CENTER;
			cancelButtonText.vAlign = VAlign.CENTER;
			cancelButtonText.touchable = false;
			cancelButton.x = storeBG.x;
			cancelButton.y = int((Environment.rectSprite.height*0.8460) + Environment.rectSprite.y);
			cancelButton.addChild(cancelButtonText);
			Screens.storeScreenObjects.push(cancelButton);
			
			statusText = new TextField(int(Environment.rectSprite.width*0.625), int(Environment.rectSprite.height*0.30), String("LOADING"), "Font", int(Environment.rectSprite.height*0.052), Intro.textColorOff, false);
			statusText.hAlign = HAlign.CENTER;
			statusText.vAlign = VAlign.CENTER;
			statusText.touchable = false;
			statusText.visible = false;
			statusText.x = int(storeBG.x + (storeBG.width/2) - (statusText.width/2));
			statusText.y = int(Environment.rectSprite.height*0.174);
			stage.addChild(statusText);
			Screens.storeScreenObjects.push(statusText);
			
			elimText = new TextField(int(Environment.rectSprite.width*0.625), int(Environment.rectSprite.height*0.0686), String("0"), "Font", int(Environment.rectSprite.height*0.052), Hud.highlightColorList[Hud.colorTheme], false);
			elimText.hAlign = HAlign.CENTER;
			elimText.vAlign = VAlign.CENTER;
			elimText.touchable = false;
			elimText.visible = false;
			elimText.x = int(storeBG.x + (storeBG.width/2) - (elimText.width/2));
			elimText.y = int(Environment.rectSprite.height*0.4676);
			stage.addChild(elimText);
			Screens.storeScreenObjects.push(elimText);
			
			storeButton1Filler.color = Hud.storeBoxColor;
			storeButton1On = false;
			storeButton2Filler.color = Hud.storeBoxColor;
			storeButton2On = false;
			storeButton3Filler.color = Hud.storeBoxColor;
			storeButton3On = false;
			cancelButtonFiller.color = storeBG.color;
			cancelButtonText.color = Intro.textColorOff;
			cancelButtonOn = false;
			
			showStore();
		}
		
		
		static function stageStoreTouchHandler(evt:TouchEvent):void {
			storeTouchList = evt.getTouches(Environment.stageRef);
			if (storeTouchList.length > 0) {
				
				point = storeTouchList[0].getLocation(Environment.stageRef);
				
				if (storeButton1 && storeButton1.visible && storeButton1.bounds.containsPoint(point) && Environment.totalRedux + Environment.currentRedux < 999950) {
					if (storeTouchList[0].phase == TouchPhase.BEGAN || storeTouchList[0].phase == TouchPhase.MOVED) {
						if (!storeButton1On) {
							storeButton1Filler.color = Hud.storeBoxColorOn;
							storeButton1On = true;
							
							storeButton2Filler.color = Hud.storeBoxColor;
							storeButton2On = false;
							
							storeButton3Filler.color = Hud.storeBoxColor;
							storeButton3On = false;
							
							Audio.playButton();
						}
					}
					if (storeTouchList[0].phase == TouchPhase.ENDED) {
						Environment.stageRef.removeEventListener(TouchEvent.TOUCH, stageStoreTouchHandler);
						
						var storeTimerPurchase1:Timer;			
						storeTimerPurchase1 = new Timer(Screens.transVal);
						storeTimerPurchase1.start();
						
						storeTimerPurchase1.addEventListener(TimerEvent.TIMER, storeTimerPurchase1Handler);
						function storeTimerPurchase1Handler(evt:TimerEvent):void {
							storeTimerPurchase1.stop();
							storeTimerPurchase1.removeEventListener(TimerEvent.TIMER, storeTimerPurchase1Handler);
							storeTimerPurchase1 = null;
							
							if (CONFIG::AIR) {
								if (CONFIG::ANDROID) {
									StoreAndroid.purchaseElims("elims50");
								}
								if (CONFIG::IOS) {
									StoreApple.purchaseElims("elims50");
								}
							}
						}
					}
				} else 
				
				if (storeButton2 && storeButton2.visible && storeButton2.bounds.containsPoint(point) && Environment.totalRedux + Environment.currentRedux < 999700) {
					if (storeTouchList[0].phase == TouchPhase.BEGAN || storeTouchList[0].phase == TouchPhase.MOVED) {
						if (!storeButton2On) {
							storeButton1Filler.color = Hud.storeBoxColor;
							storeButton1On = false;
							
							storeButton2Filler.color = Hud.storeBoxColorOn;
							storeButton2On = true;
							
							storeButton3Filler.color = Hud.storeBoxColor;
							storeButton3On = false;
							
							Audio.playButton();
						}
					}
					if (storeTouchList[0].phase == TouchPhase.ENDED) {
						Environment.stageRef.removeEventListener(TouchEvent.TOUCH, stageStoreTouchHandler);
						
						var storeTimerPurchase2:Timer;			
						storeTimerPurchase2 = new Timer(Screens.transVal);
						storeTimerPurchase2.start();
						
						storeTimerPurchase2.addEventListener(TimerEvent.TIMER, storeTimerPurchase2Handler);
						function storeTimerPurchase2Handler(evt:TimerEvent):void {
							storeTimerPurchase2.stop();
							storeTimerPurchase2.removeEventListener(TimerEvent.TIMER, storeTimerPurchase2Handler);
							storeTimerPurchase2 = null;
							
							if (CONFIG::AIR) {
								if (CONFIG::ANDROID) {
									StoreAndroid.purchaseElims("elims301");
								}
								if (CONFIG::IOS) {
									StoreApple.purchaseElims("elims301");
								}
							}
						}
					}
				} else
				
				if (storeButton3 && storeButton3.visible && storeButton3.bounds.containsPoint(point) && Environment.totalRedux + Environment.currentRedux < 999000) {
					if (storeTouchList[0].phase == TouchPhase.BEGAN || storeTouchList[0].phase == TouchPhase.MOVED) {
						if (!storeButton3On) {							
							storeButton1Filler.color = Hud.storeBoxColor;
							storeButton1On = false;
							
							storeButton2Filler.color = Hud.storeBoxColor;
							storeButton2On = false;
							
							storeButton3Filler.color = Hud.storeBoxColorOn;
							storeButton3On = true;
							
							Audio.playButton();
						}
					}
					if (storeTouchList[0].phase == TouchPhase.ENDED) {		
						Environment.stageRef.removeEventListener(TouchEvent.TOUCH, stageStoreTouchHandler);
						
						var introTimerIntroSelect3:Timer;			
						introTimerIntroSelect3 = new Timer(Screens.transVal);
						introTimerIntroSelect3.start();
						
						introTimerIntroSelect3.addEventListener(TimerEvent.TIMER, introTimerIntroSelect3Handler);
						function introTimerIntroSelect3Handler(evt:TimerEvent):void {
							introTimerIntroSelect3.stop();
							introTimerIntroSelect3.removeEventListener(TimerEvent.TIMER, introTimerIntroSelect3Handler);
							introTimerIntroSelect3 = null;
							
							if (CONFIG::AIR) {
								if (CONFIG::ANDROID) {
									StoreAndroid.purchaseElims("elims1000");
								}
								if (CONFIG::IOS) {
									StoreApple.purchaseElims("elims1000");
								}
							}	
						}		
					}
				} else
				
				if (cancelButton && cancelButton.visible && cancelButton.bounds.containsPoint(point)) {
					if (storeTouchList[0].phase == TouchPhase.BEGAN || storeTouchList[0].phase == TouchPhase.MOVED) {
						if (!cancelButtonOn) {
							cancelButtonFiller.color = Intro.buttonColorOn;
							cancelButtonText.color = Intro.textColorOn;
							cancelButtonOn = true;
							
							Audio.playButton();
						}
					}
					if (storeTouchList[0].phase == TouchPhase.ENDED) {
						cancelButtonOn = false;
						
						Screens.clearStoreListeners();
						
						var storeTimerStats:Timer;			
						storeTimerStats = new Timer(Screens.transVal);
						storeTimerStats.start();
						
						storeTimerStats.addEventListener(TimerEvent.TIMER, storeTimerStatsHandler);
						function storeTimerStatsHandler(evt:TimerEvent):void {
							storeTimerStats.stop();
							storeTimerStats.removeEventListener(TimerEvent.TIMER, storeTimerStatsHandler);
							storeTimerStats = null;
							
							Screens.clearStoreScreen();
							Screens.setStats(Stats.gameMode);
						}
						return;
					}
				} else 
				
				if (storeButton1On || storeButton2On || storeButton3On || cancelButtonOn) {
					storeButton1Filler.color = Hud.storeBoxColor;
					storeButton1On = false;
					
					storeButton2Filler.color = Hud.storeBoxColor;
					storeButton2On = false;
					
					storeButton3Filler.color = Hud.storeBoxColor;
					storeButton3On = false;
					
					cancelButtonFiller.color = storeBG.color;
					cancelButtonText.color = Intro.textColorOff;
					cancelButtonOn = false;
				}
			}
		}
		
		
		static function showLoading() {
			storeHeaderLarge.visible = false;
			storeHeaderSmall.visible = false;
			storeButton1.visible = false;
			storeButton2.visible = false;
			storeButton3.visible = false;
			cancelButton.visible = false;
			statusText.text = String("LOADING");
			statusText.visible = true;
			elimText.visible = false;
		}
		
		
		static function showStore() {
			if (CONFIG::AIR) {
				if (CONFIG::ANDROID) {
					showItems();
				}
				if (CONFIG::IOS) {
					showLoading();
					StoreApple.check();
				}
			} else {
				showDenied();
			}
		}
		
		
		static function showItems() {
			storeHeaderLarge.visible = true;
			storeHeaderSmall.visible = true;
			storeButton1.visible = true;
			storeButton2.visible = true;
			storeButton3.visible = true;
			statusText.visible = false;
			elimText.visible = false;
			cancelButton.visible = true;
			
			var touchDelay:Number = setTimeout(touchDelayHandler, 250);
			function touchDelayHandler() {
				Environment.stageRef.addEventListener(TouchEvent.TOUCH, stageStoreTouchHandler);
			}
		}
		
		
		static function showDenied() {
			storeHeaderLarge.visible = false;
			storeHeaderSmall.visible = false;
			storeButton1.visible = false;
			storeButton2.visible = false;
			storeButton3.visible = false;
			statusText.text = String("NO CONNECTION\n\n: (");
			statusText.visible = true;
			elimText.visible = false;
			cancelButton.visible = true;
			
			var touchDelay:Number = setTimeout(touchDelayHandler, 250);
			function touchDelayHandler() {
				Environment.stageRef.addEventListener(TouchEvent.TOUCH, stageStoreTouchHandler);
			}
		}
		
		
		static function resetItems() {
			storeButton1Filler.color = Hud.storeBoxColor;
			storeButton1On = false;
			
			storeButton2Filler.color = Hud.storeBoxColor;
			storeButton2On = false;
			
			storeButton3Filler.color = Hud.storeBoxColor;
			storeButton3On = false;
			
			cancelButtonFiller.color = storeBG.color;
			cancelButtonText.color = Intro.textColorOff;
			cancelButtonOn = false;
			
			Environment.stageRef.removeEventListener(TouchEvent.TOUCH, stageStoreTouchHandler);
			showItems();
		}
		
		
		static function showUpdating() {
			storeHeaderLarge.visible = false;
			storeHeaderSmall.visible = false;
			storeButton1.visible = false;
			storeButton2.visible = false;
			storeButton3.visible = false;
			cancelButton.visible = false;
			statusText.text = String("UPDATING");
			statusText.visible = true;
			elimText.visible = false;
			cancelButton.visible = false;
		}
		
		
		static function showStatus(id:String) {
			storeHeaderLarge.visible = false;
			storeHeaderSmall.visible = false;
			storeButton1.visible = false;
			storeButton2.visible = false;
			storeButton3.visible = false;
			cancelButton.visible = false;
			
			if (didPurchase) {
				didPurchase = false;
				
				var upInt:int = setInterval(playUp, 250);
				function playUp() {
					clearInterval(upInt);
					Audio.playUpgrade();
				}
			}
			
			statusText.text = String("ELIMS ADDED\nTO YOUR\nTOTAL");
			statusText.visible = true;
			elimText.text = String(id);
			elimText.visible = true;
			cancelButton.visible = true;
			
			var touchDelay:Number = setTimeout(touchDelayHandler, 250);
			function touchDelayHandler() {
				Environment.stageRef.addEventListener(TouchEvent.TOUCH, stageStoreTouchHandler);
			}
		}
		
		
		static function showFail() {
			storeHeaderLarge.visible = false;
			storeHeaderSmall.visible = false;
			storeButton1.visible = false;
			storeButton2.visible = false;
			storeButton3.visible = false;
			cancelButton.visible = false;
			statusText.text = String("FAIL");
			statusText.visible = true;
			elimText.visible = false;
			cancelButton.visible = true;
			var touchDelay:Number = setTimeout(touchDelayHandler, 250);
			function touchDelayHandler() {
				Environment.stageRef.addEventListener(TouchEvent.TOUCH, stageStoreTouchHandler);
			}
		}
	}
}