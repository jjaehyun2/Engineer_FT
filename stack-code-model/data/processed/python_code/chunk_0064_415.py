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
	
	
	public class Example2 {
		
		static var tutorialText1:TextField;
		static var tutorialText2:TextField;
		
		static var dotList:Array = [];
		static var turnRateList:Array = [0,0,0,0];
		static var dropRate:Number = 0;
		static var acceleration:Number = 1.3;
		static var initFallSpeed:Number = (Board.dotWidth) * (3/111);
		static var maxFallSpeed:Number = (Board.dotWidth) * (50/111);
		static var alphaRate:Number = 0.18;
		static var activeDot:int = 0;
		static var dropInt:int = 4;
		static var newDropList:Array = [];
		
		static var touchList:Vector.<Touch>;
		static var diffX:int;
		static var origin:Point;
		static var point:Point;
		static var target:Image;
		static var initX:int;
		static var moveOK:Boolean = false;
		static var dot3End:Boolean = false;
		static var dot4End:Boolean = false;
		
		
		static function setup(stage:Stage, dotWidth:int) {
			
			// TEXT
			tutorialText1 = new TextField(int(Environment.rectSprite.width*0.70), int(Environment.rectSprite.height*0.4412), String("NOW TRY\nTHIS"), "Font", int(Environment.rectSprite.height*0.067), Hud.gameTextColor, false);
			tutorialText1.hAlign = HAlign.CENTER;
			tutorialText1.vAlign = VAlign.TOP;
			tutorialText1.x = int((Environment.rectSprite.width/2 - tutorialText1.width/2) + Environment.rectSprite.x);
			tutorialText1.y = int((Environment.rectSprite.height*0.0667) + Environment.rectSprite.y);
			tutorialText1.touchable = false;
			tutorialText1.alpha = 0;
			stage.addChild(tutorialText1);
			Screens.example2ScreenObjects.push(tutorialText1);
			
			tutorialText2 = new TextField(int(Environment.rectSprite.width*0.80), int(Environment.rectSprite.height*0.13), String("SLIDE THE YELLOW\nONE AWAY"), "Font", int(Environment.rectSprite.height*0.0471), Hud.gameTextColor, false);
			tutorialText2.hAlign = HAlign.CENTER;
			tutorialText2.vAlign = VAlign.TOP;
			tutorialText2.x = int((Environment.rectSprite.width/2 - tutorialText2.width/2) + Environment.rectSprite.x);
			tutorialText2.y = int((Environment.rectSprite.height*0.8059) + Environment.rectSprite.y);
			tutorialText2.touchable = false;
			tutorialText2.alpha = 0;
			stage.addChild(tutorialText2);
			Screens.example2ScreenObjects.push(tutorialText2);
			
			
			// DOTS
			var dot1:Image = Atlas.generate("game dot");
			dot1.color = Board.dotColors0[2];
			dot1.x = dotWidth*2;
			dot1.y = 0;
			dot1.width = Board.dotWidth;
			dot1.height = Board.dotWidth;
			dot1.smoothing = TextureSmoothing.BILINEAR;
			dot1.alpha = 0;
			dotList.push(dot1);
			Tutorial.tutSprite.addChild(dot1);
			
			var dot2:Image = Atlas.generate("game dot");
			dot2.color = Board.dotColors0[2];
			dot2.x = dotWidth*2;
			dot2.y = 0;
			dot2.width = Board.dotWidth;
			dot2.height = Board.dotWidth;
			dot2.smoothing = TextureSmoothing.BILINEAR;
			dot2.alpha = 0;
			dotList.push(dot2);
			Tutorial.tutSprite.addChild(dot2);
			
			var dot3:Image = Atlas.generate("game dot");
			dot3.color = Board.dotColors0[1];
			dot3.x = dotWidth*2;
			dot3.y = 0;
			dot3.width = Board.dotWidth;
			dot3.height = Board.dotWidth;
			dot3.smoothing = TextureSmoothing.BILINEAR;
			dot3.alpha = 0;
			dotList.push(dot3);
			Tutorial.tutSprite.addChild(dot3);
			
			var dot4:Image = Atlas.generate("game dot");
			dot4.color = Board.dotColors0[2];
			dot4.x = dotWidth*2;
			dot4.y = 0;
			dot4.width = Board.dotWidth;
			dot4.height = Board.dotWidth;
			dot4.smoothing = TextureSmoothing.BILINEAR;
			dot4.alpha = 0;
			dotList.push(dot4);
			Tutorial.tutSprite.addChild(dot4);
			
			
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
				
				
				if (dotList[activeDot].y > dotWidth*dropInt) {
					dotList[activeDot].y = dotWidth*dropInt;
					dropInt--;
					dotList[activeDot].removeEventListener(Event.ENTER_FRAME, drop);
					activeDot++;
					Audio.playClick();
					
					if (activeDot <= 3) {
						dotList[activeDot].addEventListener(Event.ENTER_FRAME, drop);
					} else {
						
						var timer3:Timer = new Timer(350);
						timer3.start();
						timer3.addEventListener(TimerEvent.TIMER, timerHandler3);
						function timerHandler3(evt:TimerEvent):void {
							timer3.stop();
							timer3.removeEventListener(TimerEvent.TIMER, timerHandler3);
							timer3 = null;
														
							stage.addEventListener(Event.ENTER_FRAME, fadeIn);
							function fadeIn(evt:Event):void {
								if (tutorialText2.alpha < 1.0) {
									tutorialText2.alpha += 0.08;
								} else {
									
									dot3.addEventListener(TouchEvent.TOUCH, moveDot3);
									stage.removeEventListener(Event.ENTER_FRAME, fadeIn);
								}
							}
						}
					}
				}
			}

			
			function moveDot3(evt:TouchEvent) {
				
				touchList = evt.getTouches(Environment.stageRef);
				
				if (touchList.length > 0) {
					if (!moveOK && touchList[0].phase == TouchPhase.BEGAN) {
						origin = touchList[0].getLocation(Tutorial.tutSprite);
						point = touchList[0].getLocation(Tutorial.tutSprite);
						target = evt.target as Image;
						initX = target.x;
						moveOK = true;
					}
				
					if (moveOK && touchList[0].phase == TouchPhase.MOVED) {
						point = touchList[0].getLocation(Tutorial.tutSprite);
						target.x -= origin.x - point.x;
						diffX = point.x - origin.x;
						
						// BOUNDS
						if (target.x < 0) {
							target.x = 0;
						}
						if (target.x >= dotWidth*4) {
							target.x = dotWidth*4;
						}
												
						if (!target.bounds.containsPoint(point)) {						
							origin.x = target.x + target.width/2;
							origin.y = target.y + target.height/2;
						} else {
							origin = touchList[0].getLocation(Tutorial.tutSprite);
						}
					}
			
					if (moveOK && touchList[0].phase == TouchPhase.ENDED) {
						
						moveOK = false;
						
						// SNAP
						if (target.x < dotWidth/2) {
							target.x = 0;
						} else 
						
						if (target.x >= dotWidth/2 && target.x < dotWidth*1.5) {
							target.x = dotWidth;
						} else 
						
						if (target.x >= dotWidth*1.5 && target.x < dotWidth*2.5) {
							target.x = dotWidth*2;
						} else 
						
						if (target.x >= dotWidth*2.5 && target.x < dotWidth*3.5) {
							target.x = dotWidth*3;
						} else 
						
						if (target.x >= dotWidth*3.5) {
							target.x = dotWidth*4;
						}
												
						// CHECK						
						if (dot3.x != dotWidth*2) {
							dot3.removeEventListener(TouchEvent.TOUCH, moveDot3);
							
							turnRateList = [0,0,0,0];
							newDropList = [dot3, dot4];							
							
							stage.addEventListener(Event.ENTER_FRAME, drop2);
							function drop2(evt:Event):void {
								for (var d:int = 0; d < newDropList.length; d++) {
									
									var g = evt.target;				
				
									if (turnRateList[d] == 0) {
										turnRateList[d] = initFallSpeed;
									}
									
									turnRateList[d] *= acceleration;
									turnRateList[d] = Math.ceil(turnRateList[d]);
									
									turnRateList[d] = Math.min(turnRateList[d], maxFallSpeed);
									newDropList[d].y += turnRateList[d];
									
									
									if (!dot3End && dot3.y >= dotWidth*4) {
										dot3.y = dotWidth*4;
										dot3End = true;
										newDropList.splice(0,1);
										Audio.playClick();
									}
									
									if (!dot4End && dot4.y >= dotWidth*2) {
										dot4.y = dotWidth*2;
										dot4End = true;
										newDropList.splice(1,1);
										Audio.playClick();
									}
									
									if (dot3End && dot4End) {
										stage.removeEventListener(Event.ENTER_FRAME, drop2);
										
										dot1.pivotX = dot1.width/2 * 256/dotWidth;
										dot1.pivotY = dot1.height/2 * 256/dotWidth;
										dot1.x += (dot1.width/2);
										dot1.y += (dot1.height/2);
										
										dot2.pivotX = dot2.width/2 * 256/dotWidth;
										dot2.pivotY = dot2.height/2 * 256/dotWidth;
										dot2.x += (dot2.width/2);
										dot2.y += (dot2.height/2);
										
										dot4.pivotX = dot4.width/2 * 256/dotWidth;
										dot4.pivotY = dot4.height/2 * 256/dotWidth;
										dot4.x += (dot4.width/2);
										dot4.y += (dot4.height/2);
										
										Audio.playClear();
										
										stage.addEventListener(Event.ENTER_FRAME, animate);
									}
								}
							}

							function animate(evt:Event) {
								
								dot1.alpha -= 0.06;
								dot1.scaleX *= 0.83;
								dot1.scaleY *= 0.83;
								
								dot2.alpha -= 0.06;
								dot2.scaleX *= 0.83;
								dot2.scaleY *= 0.83;
								
								dot4.alpha -= 0.06;
								dot4.scaleX *= 0.83;
								dot4.scaleY *= 0.83;
																
								if (dot1.alpha <=0) {
									stage.removeEventListener(Event.ENTER_FRAME, animate);
									
									Tutorial.tutSprite.removeChild(dot1);
									Tutorial.tutSprite.removeChild(dot2);
									Tutorial.tutSprite.removeChild(dot4);
									
									
									var timerDot:Timer = new Timer(600);
									timerDot.start();
									timerDot.addEventListener(TimerEvent.TIMER, timerDotHandler);
									function timerDotHandler(evt:TimerEvent):void {
										timerDot.removeEventListener(TimerEvent.TIMER, timerDotHandler);
										timerDot.stop();
										timerDot = null;
										
										stage.addEventListener(Event.ENTER_FRAME, dotLoop2);
										function dotLoop2(evt:Event):void {
											if (dot3.alpha > 0) {
												dot3.alpha -= 0.08;
												
												tutorialText1.alpha -= 0.08;
												tutorialText2.alpha -= 0.08;
											} else {
												stage.removeEventListener(Event.ENTER_FRAME, dotLoop2);
												Tutorial.tutSprite.removeChild(dot3);
												
												var timer:Timer = new Timer(250);
												timer.start();
												
												timer.addEventListener(TimerEvent.TIMER, timerHandler);
												function timerHandler(evt:TimerEvent):void {
													
													Tutorial.tutSprite.removeChild(dot3);
													
													timer.stop();
													timer.removeEventListener(TimerEvent.TIMER, timerHandler);
													timer = null;
													
													tutorialText1.alpha = 1.0;
													tutorialText1.y = dotWidth*3 + Tutorial.tutSprite.y + dotWidth - tutorialText1.height/2;
													tutorialText1.text = String("MASTERFUL");
													
													Audio.playExtra();
													
													var timer2:Timer = new Timer(2000);
													timer2.start();
													timer2.addEventListener(TimerEvent.TIMER, timerHandler2);
													function timerHandler2(evt:TimerEvent):void {
														timer2.stop();
														timer2.removeEventListener(TimerEvent.TIMER, timerHandler2);
														timer2 = null;
														
														stage.addEventListener(Event.ENTER_FRAME, fadeInEnd2);
														function fadeInEnd2(evt:Event):void {
															if (tutorialText1.alpha > 0) {
																tutorialText1.alpha -= 0.08;
															} else {
																stage.removeEventListener(Event.ENTER_FRAME, fadeInEnd2);
																
																Screens.clearExample2Screen();
																Example3.setup(stage, dotWidth);
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
					}
				}
			}
		}
	}
}