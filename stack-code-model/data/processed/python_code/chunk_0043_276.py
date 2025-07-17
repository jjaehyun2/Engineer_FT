package  {
	
	import flash.events.TimerEvent;
	import flash.geom.Point;
	import flash.net.navigateToURL;
	import flash.net.URLRequest;
	import flash.system.Capabilities;
	import flash.utils.setTimeout;
	import flash.utils.Timer;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.display.Stage;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.text.TextField;
	import starling.textures.TextureSmoothing;
	import starling.utils.HAlign;
	import starling.utils.VAlign;
	
	
	public class Contact {
		
		static var point:Point;
		static var contactTouchList:Vector.<Touch>;
		static var contactText:TextField;
		static var contactIcon:Image;
		static var contactIconOn:Boolean = false;
		static var contactText1:TextField;
		static var contactText2:TextField;		
		static var backButton:Sprite;
		static var backButtonFiller:Image;
		static var backButtonText:TextField;
		static var backTextColor:uint = Hud.gameTextColor;
		static var buttonColorOn:uint;
		static var backButtonOn:Boolean = false;
		
		
		static function display(stage:Stage) {
			var shift:int = int(Main.screenHeight*0.1177);
			buttonColorOn = Hud.highlightColorList[Hud.colorTheme];
			
			contactText = new TextField(int(Environment.rectSprite.width*0.625), int(Environment.rectSprite.height*0.08824), String("contact"), "Font", int(Environment.rectSprite.height*0.067), Hud.gameTextColor, false);
			contactText.hAlign = HAlign.CENTER;
			contactText.vAlign = VAlign.TOP;
			contactText.x = int((Environment.rectSprite.width/2 - contactText.width/2) + Environment.rectSprite.x);
			contactText.y = int((Environment.rectSprite.height*0.075) + Environment.rectSprite.y);
			contactText.touchable = false;
			stage.addChild(contactText);
			Screens.contactScreenObjects.push(contactText);	
			
			contactText1 = new TextField(int(Environment.rectSprite.width*0.9375), int(Environment.rectSprite.height*0.25), String("HAVE A COMMENT OR SUGGESTION? WE'D LOVE TO HEAR FROM YOU"), "Font", int(Environment.rectSprite.height*0.0422), Hud.gameTextColor, false);
			contactText1.hAlign = HAlign.CENTER;
			contactText1.vAlign = VAlign.TOP;
			contactText1.x = int((Environment.rectSprite.width/2 - contactText1.width/2) + Environment.rectSprite.x);
			contactText1.y = int((Environment.rectSprite.height*0.207) + Environment.rectSprite.y);
			contactText1.touchable = false;
			stage.addChild(contactText1);
			Screens.contactScreenObjects.push(contactText1);
			
			contactText2 = new TextField(int(Environment.rectSprite.width*0.9375), int(Environment.rectSprite.height*0.25), String("SPECIAL THANKS TO AMANDA, PIX & CAZ"), "Font", int(Environment.rectSprite.height*0.0422), Hud.gameTextColor, false);
			contactText2.hAlign = HAlign.CENTER;
			contactText2.vAlign = VAlign.TOP;
			contactText2.x = int((Environment.rectSprite.width/2 - contactText2.width/2) + Environment.rectSprite.x);
			contactText2.y = int((Environment.rectSprite.height*0.6176) + Environment.rectSprite.y);
			contactText2.touchable = false;
			stage.addChild(contactText2);
			Screens.contactScreenObjects.push(contactText2);
			
			
			
			contactIcon = Atlas.generate("contact icon");
			contactIcon.height = int(Environment.rectSprite.width*0.21875);
			contactIcon.scaleX = contactIcon.scaleY;
			contactIcon.smoothing = TextureSmoothing.BILINEAR;
			//contactIcon.color = Hud.gameTextColor;
			contactIcon.color = buttonColorOn;
			contactIcon.x = int(Main.screenWidth/2 - contactIcon.width/2);
			contactIcon.y = int((Environment.rectSprite.height*0.422) + Environment.rectSprite.y);
			stage.addChild(contactIcon);
			Screens.introScreenObjects.push(contactIcon);
			
			
			
			backButton = new Sprite();
			stage.addChild(backButton);
			
			backButtonFiller = Atlas.generate("filler");
			backButtonFiller.width = Main.screenWidth + 50;
			backButtonFiller.height = int(Environment.rectSprite.height*0.0941);
			backButtonFiller.color = stage.color;
			backButton.addChild(backButtonFiller);
			
			backButtonText = new TextField(int(Environment.rectSprite.width*0.625), int(Environment.rectSprite.height*0.0941), String("BACK"), "Font", int(Environment.rectSprite.height*0.06275), backTextColor/*stage.color*/, false);
			backButtonText.hAlign = HAlign.CENTER;
			backButtonText.vAlign = VAlign.CENTER;
			backButtonText.x = int(Main.screenWidth/2 - backButtonText.width/2);
			backButtonText.touchable = false;
			backButton.x = 0;
			backButton.y = int((Environment.rectSprite.height*0.8203) + Environment.rectSprite.y);
			
			backButton.addChild(backButtonText);
			Screens.contactScreenObjects.push(backButton);			

			stage.addEventListener(TouchEvent.TOUCH, stageContactTouchHandler);
			
			var touchDelay:Number = setTimeout(touchDelayHandler, 250);
			function touchDelayHandler() {
				stage.addEventListener(TouchEvent.TOUCH, stageContactTouchHandler);
			}
		}
		
		
		static function stageContactTouchHandler(evt:TouchEvent):void {
			contactTouchList = evt.getTouches(Environment.stageRef);
			if (contactTouchList.length > 0) {
				
				point = contactTouchList[0].getLocation(Environment.stageRef);
				
				if (contactIcon.bounds.containsPoint(point)) {
					
					if (contactTouchList[0].phase == TouchPhase.BEGAN || contactTouchList[0].phase == TouchPhase.MOVED) {
							if (!contactIconOn) {
								//contactIcon.color = Hud.iconsOnColor;
								//contactIcon.color = buttonColorOn;
								contactIconOn = true;
								
								Audio.playButton();
							}
					}						
					if (contactTouchList[0].phase == TouchPhase.ENDED) {
						contactIconOn = false;
						
						var contactTimerMail:Timer;			
						contactTimerMail = new Timer(Screens.transVal);
						contactTimerMail.start();
						
						contactTimerMail.addEventListener(TimerEvent.TIMER, contactTimerMailHandler);
						function contactTimerMailHandler(evt:TimerEvent):void {
							contactTimerMail.stop();
							contactTimerMail.removeEventListener(TimerEvent.TIMER, contactTimerMailHandler);
							contactTimerMail = null;
							
							//contactIcon.color = Hud.gameTextColor;
							
							var email:URLRequest = new URLRequest("mailto:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@gmail.com?subject=Dropsy Contact");
							navigateToURL(email, "_blank");
						}
					}
				} else 
				
				if (backButton.bounds.containsPoint(point)) {
					
					if (contactTouchList[0].phase == TouchPhase.BEGAN || contactTouchList[0].phase == TouchPhase.MOVED) {
						if (!backButtonOn) {
								
							backButtonFiller.color = buttonColorOn;
							backButtonText.color = Intro.textColorOn;
							backButtonOn = true;
							
							Audio.playButton();
						}
					}
					
					if (contactTouchList[0].phase == TouchPhase.ENDED) {
						
						backButtonFiller.color = Intro.buttonColorOff;
						backButtonText.color = Intro.textColorOff;
						backButtonOn = false;
						
						Environment.stageRef.removeEventListener(TouchEvent.TOUCH, stageContactTouchHandler);
						Data.flushSave();
						

						if (Stats.gameMode == 0) {
							Screens.gameMode = "none";
							
							backButtonFiller.color = buttonColorOn;
							backButtonText.color = Intro.textColorOn;
														
							Screens.clearContactListeners();
							
							var contactTimerIntro:Timer;			
							contactTimerIntro = new Timer(Screens.transVal);
							contactTimerIntro.start();
							
							contactTimerIntro.addEventListener(TimerEvent.TIMER, contactTimerIntroHandler);
							function contactTimerIntroHandler(evt:TimerEvent):void {
								contactTimerIntro.stop();
								contactTimerIntro.removeEventListener(TimerEvent.TIMER, contactTimerIntroHandler);
								contactTimerIntro = null;
								
								Screens.clearContactScreen();
								Screens.setIntro();
							}
						}
					}
				} else 
				
				if (backButtonOn || contactIconOn) {
					backButtonFiller.color = Intro.buttonColorOff;
					backButtonText.color = Intro.textColorOff;
					backButtonOn = false;
					contactIconOn = false;
				}
			}
		}			
	}
}