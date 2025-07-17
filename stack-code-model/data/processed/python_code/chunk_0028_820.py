package  {
	
	import flash.events.TimerEvent;
	import flash.geom.Point;
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
	
	
	public class Example3 {
		
		static var tutorialText1:TextField;
		static var tutorialText2:TextField;
		static var dotID:String;
		static var dotWidthID;
		
		static var dotList:Array = [];
		static var turnRateList:Array = [0,0,0,0,0,0,0,0];
		static var dropRate:Number = 0;
		static var acceleration:Number = 1.3;
		static var initFallSpeed:Number = (Board.dotWidth) * (3/111);
		static var maxFallSpeed:Number = (Board.dotWidth) * (50/111);
		static var alphaRate:Number = 0.18;
		static var activeDot:int = 0;
		
		static var touchList:Vector.<Touch>;
		static var diffX:int;
		static var origin:Point;
		static var point:Point;
		static var target:Image;
		static var initX:int;
		static var moveOK:Boolean = false;
		
		static var reduxIcon:Image;
		static var reduxRing:Image;
		static var ringMax:int;
		static var reduxTouchList:Vector.<Touch>;
		static var iconsPoint:Point;
		static var reduxIconOn:Boolean = false;
		static var reduxOn:Boolean = false;
		static var reduxArray:Array = [];
		
		
		static function setup(stage:Stage, dotWidth:int) {
			
			dotWidthID = dotWidth;
			
			// TEXT			
			tutorialText1 = new TextField(int(Environment.rectSprite.width*0.70), int(Environment.rectSprite.height*0.4412), String("LAST ONE"), "Font", int(Environment.rectSprite.height*0.067), Hud.gameTextColor, false);
			tutorialText1.hAlign = HAlign.CENTER;
			tutorialText1.vAlign = VAlign.TOP;
			tutorialText1.x = int((Environment.rectSprite.width/2 - tutorialText1.width/2) + Environment.rectSprite.x);
			tutorialText1.y = int((Environment.rectSprite.height*0.0667) + Environment.rectSprite.y);
			tutorialText1.touchable = false;
			tutorialText1.alpha = 0;
			stage.addChild(tutorialText1);
			Screens.example1ScreenObjects.push(tutorialText1);
			
			tutorialText2 = new TextField(int(Environment.rectSprite.width*0.98), int(Environment.rectSprite.height*0.135), String("TOUCH THE ELIM\nICON THEN A BLOCK"), "Font", int(Environment.rectSprite.height*0.0471), Hud.gameTextColor, false);
			tutorialText2.hAlign = HAlign.CENTER;
			tutorialText2.vAlign = VAlign.TOP;
			tutorialText2.x = int((Environment.rectSprite.width/2 - tutorialText2.width/2) + Environment.rectSprite.x);
			tutorialText2.y = int((Environment.rectSprite.height*0.8059) + Environment.rectSprite.y);
			tutorialText2.touchable = false;
			tutorialText2.alpha = 0;
			stage.addChild(tutorialText2);
			Screens.example1ScreenObjects.push(tutorialText2);
			
			
			// DOTS
			var dot1:Image = Atlas.generate("game dot");
			dot1.color = Board.dotColors0[1];
			dot1.x = dotWidth*1;
			dot1.y = 0;
			dot1.width = Board.dotWidth;
			dot1.height = Board.dotWidth;
			dot1.smoothing = TextureSmoothing.BILINEAR;
			dot1.alpha = 0;
			dotList.push(dot1);
			Tutorial.tutSprite.addChild(dot1);
			
			var dot2:Image = Atlas.generate("game dot");
			dot2.color = Board.dotColors0[2];
			dot2.x = dotWidth*3;
			dot2.y = 0;
			dot2.width = Board.dotWidth;
			dot2.height = Board.dotWidth;
			dot2.smoothing = TextureSmoothing.BILINEAR;
			dot2.alpha = 0;
			dotList.push(dot2);
			Tutorial.tutSprite.addChild(dot2);
			
			var dot3:Image = Atlas.generate("game dot");
			dot3.color = Board.dotColors0[2];
			dot3.x = dotWidth*1;
			dot3.y = 0;
			dot3.width = Board.dotWidth;
			dot3.height = Board.dotWidth;
			dot3.smoothing = TextureSmoothing.BILINEAR;
			dot3.alpha = 0;
			dotList.push(dot3);
			Tutorial.tutSprite.addChild(dot3);
			
			var dot4:Image = Atlas.generate("game dot");
			dot4.color = Board.dotColors0[0];
			dot4.x = dotWidth*2;
			dot4.y = 0;
			dot4.width = Board.dotWidth;
			dot4.height = Board.dotWidth;
			dot4.smoothing = TextureSmoothing.BILINEAR;
			dot4.alpha = 0;
			dotList.push(dot4);
			Tutorial.tutSprite.addChild(dot4);
			
			var dot5:Image = Atlas.generate("game dot");
			dot5.color = Board.dotColors0[2];
			dot5.x = dotWidth*0;
			dot5.y = 0;
			dot5.width = Board.dotWidth;
			dot5.height = Board.dotWidth;
			dot5.smoothing = TextureSmoothing.BILINEAR;
			dot5.alpha = 0;
			dotList.push(dot5);
			Tutorial.tutSprite.addChild(dot5);
			
			var dot6:Image = Atlas.generate("game dot");
			dot6.color = Board.dotColors0[1];
			dot6.x = dotWidth*2;
			dot6.y = 0;
			dot6.width = Board.dotWidth;
			dot6.height = Board.dotWidth;
			dot6.smoothing = TextureSmoothing.BILINEAR;
			dot6.alpha = 0;
			dotList.push(dot6);
			Tutorial.tutSprite.addChild(dot6);
			
			var dot7:Image = Atlas.generate("game dot");
			dot7.color = Board.dotColors0[1];
			dot7.x = dotWidth*4;
			dot7.y = 0;
			dot7.width = Board.dotWidth;
			dot7.height = Board.dotWidth;
			dot7.smoothing = TextureSmoothing.BILINEAR;
			dot7.alpha = 0;
			dotList.push(dot7);
			Tutorial.tutSprite.addChild(dot7);
			
			var dot8:Image = Atlas.generate("game dot");
			dot8.color = Board.dotColors0[0];
			dot8.x = dotWidth*3;
			dot8.y = 0;
			dot8.width = Board.dotWidth;
			dot8.height = Board.dotWidth;
			dot8.smoothing = TextureSmoothing.BILINEAR;
			dot8.alpha = 0;
			dotList.push(dot8);
			Tutorial.tutSprite.addChild(dot8);
			
			
			// ELIM			
			iconsPoint = new Point;
			
			reduxRing = Atlas.generate("remove ring");
			reduxRing.height = int(Environment.rectSprite.width*0.21875);
			reduxRing.scaleX = reduxRing.scaleY;
			reduxRing.smoothing = TextureSmoothing.BILINEAR;
			reduxRing.color = Hud.iconsOffColor;
			reduxRing.x = int((Environment.rectSprite.width/2 - reduxRing.width/2) + Environment.rectSprite.x);
			reduxRing.y = int((Environment.rectSprite.height*0.645) + Environment.rectSprite.y);
			reduxRing.pivotX = reduxRing.width/2 * 298/reduxRing.width;
			reduxRing.pivotY = reduxRing.height/2 * 298/reduxRing.height;
			reduxRing.x += (reduxRing.width/2);
			reduxRing.y += (reduxRing.height/2);
			reduxRing.visible = false;
			reduxRing.touchable = false;
			
			ringMax = reduxRing.width * 2.22;
			
			stage.addChild(reduxRing);
			Screens.example3ScreenObjects.push(reduxRing);
			
			reduxIcon = Atlas.generate("remove icon");
			reduxIcon.height = int(Environment.rectSprite.width*0.21875);
			reduxIcon.scaleX = reduxIcon.scaleY;
			reduxIcon.smoothing = TextureSmoothing.BILINEAR;
			reduxIcon.x = int((Environment.rectSprite.width/2 - reduxIcon.width/2) + Environment.rectSprite.x);
			reduxIcon.y = int((Environment.rectSprite.height*0.645) + Environment.rectSprite.y);
			reduxIcon.color = Hud.iconsOffColor;
			reduxIcon.alpha = 0.0;
			stage.addChild(reduxIcon);
			Screens.example3ScreenObjects.push(reduxIcon);
			
			var timer5:Timer = new Timer(250);
			timer5.start();
			timer5.addEventListener(TimerEvent.TIMER, timer5Handler);
			function timer5Handler(evt:TimerEvent):void {
				timer5.addEventListener(TimerEvent.TIMER, timer5Handler);
				timer5.stop();
				timer5 = null
				
				stage.addEventListener(Event.ENTER_FRAME, fadeInTitle);
				function fadeInTitle(evt:Event):void {
					if (tutorialText1.alpha < 1.0) {
						tutorialText1.alpha += 0.08;
					} else {
						
						stage.removeEventListener(Event.ENTER_FRAME, fadeInTitle);
						
						var timer4:Timer = new Timer(250);
						timer4.start();
						
						timer4.addEventListener(TimerEvent.TIMER, timerHandler4);
						function timerHandler4(evt:TimerEvent):void {
							timer4.stop();
							timer4.removeEventListener(TimerEvent.TIMER, timerHandler4);
							timer4 = null;
							
							dot1.addEventListener(Event.ENTER_FRAME, drop);
							
							stage.addEventListener(Event.ENTER_FRAME, fadeInSubTitle);
							function fadeInSubTitle(evt:Event):void {
								if (tutorialText2.alpha < 1.0) {
									tutorialText2.alpha += 0.08;
									reduxIcon.alpha += 0.08;
								} else {
									stage.removeEventListener(Event.ENTER_FRAME, fadeInSubTitle);
								}
							}
						}
					}
				}
			}
				
			function drop(evt:Event):void {
				
				var h = evt.target;				
				
				if (turnRateList[activeDot] == 0) {
					turnRateList[activeDot] = initFallSpeed;
				}
				
				if (dotList[activeDot].alpha < 1.0) {
					dotList[activeDot].alpha += alphaRate;
				}						
				
				turnRateList[activeDot] *= acceleration;
				turnRateList[activeDot] = Math.ceil(turnRateList[activeDot]);
				
				turnRateList[activeDot] = Math.min(turnRateList[activeDot], maxFallSpeed);
				dotList[activeDot].y += turnRateList[activeDot];
				
				if (activeDot == 4 || activeDot == 0 || activeDot == 3 || activeDot == 1 || activeDot == 6) {
					if (dotList[activeDot].y > dotWidth*3) {
						dotList[activeDot].y = dotWidth*3;
						doRest();
					}
				}
				
				if (activeDot == 2 || activeDot == 5 || activeDot == 7) {
					if (dotList[activeDot].y > dotWidth*2) {
						dotList[activeDot].y = dotWidth*2;
						doRest();
					}
				}
				
				function doRest() {
					dotList[activeDot].removeEventListener(Event.ENTER_FRAME, drop);
					activeDot++;
					Audio.playClick();
					
					if (activeDot <= 7) {
						dotList[activeDot].addEventListener(Event.ENTER_FRAME, drop);
					} else {
						
						for each (var id in dotList) {
							id.addEventListener(TouchEvent.TOUCH, dotsTouch);
						}
						
						reduxIcon.addEventListener(TouchEvent.TOUCH, reduxTouchHandler);
					}
				}
			}

			
			function dotsTouch(evt:TouchEvent) {
				
				touchList = evt.getTouches(Environment.stageRef);
				
				if (touchList.length > 0) {
					if (touchList[0].phase == TouchPhase.BEGAN) {
						target = evt.target as Image;
						
						if (reduxOn) {
							check(target);
						}
					}
				}
			}
		}
		
		
		static function reduxTouchHandler(evt:TouchEvent):void {
				
			reduxTouchList = evt.getTouches(Environment.stageRef);
			if (reduxTouchList.length > 0) {
				
				iconsPoint = reduxTouchList[0].getLocation(Environment.stageRef);
			
				if (reduxIcon.bounds.containsPoint(iconsPoint)) {

					if (reduxTouchList[0].phase == TouchPhase.BEGAN || reduxTouchList[0].phase == TouchPhase.MOVED) {
						if (!reduxIconOn) {
							reduxIcon.color = Hud.iconsOnColor;
							reduxIconOn = true;
							
							Audio.playButton();
						}
					}
					
					if (reduxTouchList[0].phase == TouchPhase.ENDED) {								
							
						set();
						
						if (!reduxOn) {
							resetRedux();
						}
						reduxIconOn = false;
						
					}
				} else {
					if (!reduxOn) {
						if (reduxIconOn) {
							
							reduxIcon.color = Hud.iconsOffColor;
							reduxIconOn = false;
						}
					}
				}
			}
		}
		
		
		static function set() {
			if (!reduxOn) {
				reduxOn = true;
				setRing();
			} else {			
				if (!reduxOn) {
					reduxOn = false;
					reduxIcon.color = Hud.iconsOffColor;
				} else {
					
					reduxOn = false;
					reduxIcon.color = Hud.iconsOffColor;
				}
			}
		}
		
		
		static function check(dot) {
			var dotColor = dot.color;
			if (dotColor == Board.dotColors0[2]) {
				dotID = "red";
			}
			if (dotColor == Board.dotColors0[0]) {
				dotID = "blue";
			}
			if (dotColor == Board.dotColors0[1]) {
				dotID = "yellow";
			}
			
			for each (var idC in dotList) {
				if (dotColor == idC.color) {					
					reduxArray.push(idC);
				}
			}
			
			if (reduxArray.length > 0) { 
				reduxIcon.color = Hud.iconsOffColor;
				reduxRing.color = Hud.iconsOffColor;
				
				Environment.stageRef.removeEventListener(Event.ENTER_FRAME, moveRing);
				reduxRing.visible = false;
				reduxRing.alpha = 1.0;
				reduxRing.height = int(Environment.rectSprite.width*0.21875);
				reduxRing.scaleX = reduxRing.scaleY;
				
				elim();
				reduxIcon.removeEventListener(TouchEvent.TOUCH, reduxTouchHandler);
			}
		}
		
		
		static function elim() {
			for each (var id0 in reduxArray) {
				id0.pivotX = id0.width/2 * 256/Board.dotWidth;
				id0.pivotY = id0.height/2 * 256/Board.dotWidth;
				id0.x += (id0.width/2);
				id0.y += (id0.height/2);
			}
			
			Audio.playClear();
			
			Vibrate.buzz(250);
			
			reduxIcon.color = Hud.iconsOffColor;
			reduxRing.color = Hud.iconsOffColor;
			
			Environment.stageRef.addEventListener(Event.ENTER_FRAME, fadeOut);
		}
		
		
		static function fadeOut(evt:Event) {
			
			for each (var id in reduxArray) {
				id.alpha -= 0.06;
				id.scaleX *= 0.83;
				id.scaleY *= 0.83;
			}
			
			if (reduxArray[0].alpha <= 0) {
				Environment.stageRef.removeEventListener(Event.ENTER_FRAME, fadeOut);
				for each (var id2 in reduxArray) {
					Tutorial.tutSprite.removeChild(id2);
					id2.dispose();
					
					for (var i:int = 0; i < dotList.length; i++) {
						if (dotList[i] == id2) {
							dotList.splice(i, 1);
						}
					}
					
					turnRateList = [0,0,0,0,0,0,0,0];
				}
				
				resetRedux();
				
				Environment.stageRef.addEventListener(Event.ENTER_FRAME, nextDrop);
				function nextDrop(evt:Event) {
					
					for (var d:int = 0; d < dotList.length; d++) {
						
						
						if (dotID == "blue" && d == 4) {
							var g = evt.target;
							
							if (turnRateList[d] == 0) {
								turnRateList[d] = initFallSpeed;
							}
							
							turnRateList[d] *= acceleration;
							turnRateList[d] = Math.ceil(turnRateList[d]);
							
							turnRateList[d] = Math.min(turnRateList[d], maxFallSpeed);
							dotList[d].y += turnRateList[d];
							
							//trace(dotList[d].y, dotWidthID*3);
							
							
							if (dotList[d].y >= dotWidthID*3) {
								dotList[d].y = dotWidthID*3;
								Audio.playClick();
								Environment.stageRef.removeEventListener(Event.ENTER_FRAME, nextDrop);
								
								lastTransition();
							}
						} else
						
						if (dotID == "yellow" && d == 1) {							
							var h = evt.target;
							
							if (turnRateList[d] == 0) {
								turnRateList[d] = initFallSpeed;
							}
							
							turnRateList[d] *= acceleration;
							turnRateList[d] = Math.ceil(turnRateList[d]);
							
							turnRateList[d] = Math.min(turnRateList[d], maxFallSpeed);
							dotList[d].y += turnRateList[d];
							
							if (dotList[d].y >= dotWidthID*3) {
								dotList[d].y = dotWidthID*3;
								Audio.playClick();
								Environment.stageRef.removeEventListener(Event.ENTER_FRAME, nextDrop);
								
								lastTransition();
							}
						} else 
						
						if (dotID == "red" && d == 4) {
							var j = evt.target;
							
							if (turnRateList[d] == 0) {
								turnRateList[d] = initFallSpeed;
							}
							
							turnRateList[d] *= acceleration;
							turnRateList[d] = Math.ceil(turnRateList[d]);
							
							turnRateList[d] = Math.min(turnRateList[d], maxFallSpeed);
							dotList[d].y += turnRateList[d];
							
							
							if (dotList[d].y >= dotWidthID*3) {
								dotList[d].y = dotWidthID*3;
								Audio.playClick();
								Environment.stageRef.removeEventListener(Event.ENTER_FRAME, nextDrop);
								lastTransition();
							}
						}
					}
				}
			}
		}
		
		
		static function setRing() {
			reduxRing.visible = true;
			Environment.stageRef.addEventListener(Event.ENTER_FRAME, moveRing);
		}
		
		
		static function moveRing(evt:Event) {
			reduxRing.alpha -= 0.012;
			reduxRing.scaleX *= 1.008;
			reduxRing.scaleY *=  1.008;
			if (reduxRing.width >= ringMax) {
				reduxRing.alpha = 1.0;
				reduxRing.height = int(Environment.rectSprite.width*0.21875);
				reduxRing.scaleX = reduxRing.scaleY;
			}
		}	
		
		
		static function resetRedux() {
			reduxArray.length = 0;
			reduxOn = false;
			
			reduxIcon.color = Hud.iconsOffColor;
			reduxRing.color = Hud.iconsOffColor;
			
			Environment.stageRef.removeEventListener(Event.ENTER_FRAME, moveRing);
			reduxRing.visible = false;
			reduxRing.alpha = 1.0;
			reduxRing.height = int(Environment.rectSprite.width*0.21875);
			reduxRing.scaleX = reduxRing.scaleY;
		}
		
		
		static function lastTransition() {
			var timerDot:Timer = new Timer(1000);
			timerDot.start();
			timerDot.addEventListener(TimerEvent.TIMER, timerDotHandler);
			function timerDotHandler(evt:TimerEvent):void {
				timerDot.removeEventListener(TimerEvent.TIMER, timerDotHandler);
				timerDot.stop();
				timerDot = null;
				
				Environment.stageRef.addEventListener(Event.ENTER_FRAME, dotLoop2);
				function dotLoop2(evt:Event):void {
					
					if (tutorialText1.alpha > 0) {
						
						for each (var id in dotList) {
							id.alpha -= 0.08;
						}
						
						tutorialText1.alpha -= 0.08;
						tutorialText2.alpha -= 0.08;
						
						reduxIcon.alpha -= 0.08;
					} else {
						Environment.stageRef.removeEventListener(Event.ENTER_FRAME, dotLoop2);
						for each (var id1 in dotList) {
							Tutorial.tutSprite.removeChild(id1);
						}
						
						
						var timer:Timer = new Timer(250);
						timer.start();
						
						timer.addEventListener(TimerEvent.TIMER, timerHandler);
						function timerHandler(evt:TimerEvent):void {
							
							for each (var id2 in dotList) {
								Tutorial.tutSprite.removeChild(id2);
							}
							
							timer.stop();
							timer.removeEventListener(TimerEvent.TIMER, timerHandler);
							timer = null;
							
							tutorialText1.alpha = 1.0;
							tutorialText1.y = dotWidthID*3 + Tutorial.tutSprite.y + dotWidthID - tutorialText1.height/2;
							tutorialText1.text = String("ALL SET");
							
							Audio.playExtra();
							
							var timer2:Timer = new Timer(2000);
							timer2.start();
							timer2.addEventListener(TimerEvent.TIMER, timerHandler2);
							function timerHandler2(evt:TimerEvent):void {
								timer2.stop();
								timer2.removeEventListener(TimerEvent.TIMER, timerHandler2);
								timer2 = null;
								
								Environment.stageRef.addEventListener(Event.ENTER_FRAME, fadeInEnd2);
								function fadeInEnd2(evt:Event):void {
									if (tutorialText1.alpha > 0) {
										tutorialText1.alpha -= 0.08;
									} else {
										Environment.stageRef.removeEventListener(Event.ENTER_FRAME, fadeInEnd2);
										
										Screens.clearExample3Screen();
										Example4.setup(Environment.stageRef);
									}
								}
							}
						}
					}
				}
			}
		}
	}
}