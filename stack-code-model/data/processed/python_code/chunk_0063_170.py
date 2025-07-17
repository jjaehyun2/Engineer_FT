package  {
	
	import flash.events.TimerEvent;
	import flash.geom.Point;
	import flash.utils.getDefinitionByName;
	import flash.utils.Timer;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.display.Stage;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.text.TextField;
	import starling.textures.Texture;
	import starling.textures.TextureSmoothing;
	import starling.utils.HAlign;
	import starling.utils.VAlign;
	
	
	public class Board {
		
		static var boardSprite:Sprite;
		static var boardFiller:Image;
		static var dotClass:Class;
		static var dotList:Array = [];
		static var colorArray:Array = ["red", "yellow", "purple", "green", "blue", "orange"];
		static var dotColors0:Array = [0x00A39F, 0xFFE51B, 0xF5334F, 0xA8A8A8, 0xFE9827, 0x91DB38];
		static var dotColors1:Array = [0x003C4F, 0x008397, 0x9CA3A3, 0x06B157, 0x4A636D, 0x008363];
		static var dotColors2:Array = [0x660047, 0xE71248, 0x005B78, 0x629C1B, 0xFFCD00, 0xFF8700];
		static var dotColors3:Array = [0x88E962, 0x46C4AD, 0xFF69B1, 0xCBCBCB, 0x12BCFF, 0xA066CF];
		static var dotColorArray:Array = [dotColors0, dotColors1, dotColors2, dotColors3];
		static var colorString:String;
		static var moveList0:Array, moveList1:Array, moveList2:Array, moveList3:Array, moveList4:Array;
		static var xList0:Array, xList1:Array, xList2:Array, xList3:Array , xList4:Array;
		static var row0:Array, row1:Array, row2:Array, row3:Array, row4:Array;
		static var col0:Array, col1:Array, col2:Array, col3:Array, col4:Array;
		static var rows:int = 5;
		static var dotWidth:int = int(Environment.rectSprite.width*0.1734375);
		static var stageTouchList:Vector.<Touch>;
		static var touchList:Vector.<Touch>;
		static var diffX:int;
		static var origin:Point;
		static var point:Point;
		static var target:Image;
		static var initX:int;
		static var canMove:Boolean = true;
		static var isDropping:Boolean = false;
		static var moveOn:Boolean = false;
		static var gameOver:Boolean = false;
		static var stageHit:Boolean = false;
		static var tgt1;
		static var orderInt = 0;
		static var statsIcon:Image;
		static var statsIconTouchList:Vector.<Touch>;
		static var reduxIcon:Image;
		static var reduxRing:Image;
		static var ringMax:int;
		static var reduxTouchList:Vector.<Touch>;
		static var iconsPoint:Point;
		static var boardIsActive:Boolean = false;
		static var statsIconOn:Boolean = false;
		static var reduxIconOn:Boolean = false;
		static var ended:Boolean = false;
		
		
		static function setup(stage:Stage):void {
			if (CONFIG::AIR) {
				if (CONFIG::ANDROID) {
					AdsAndroid.loadAd();
				}
				if(CONFIG::IOS) {
					
				}
			}
			
			iconsPoint = new Point;
			
			for (var i:int = 0; i < 5; i++) {
				Board["moveList" + i] = [];
				Board["xList" + i] = [];
				Board["row" + i] = [];
				Board["col" + i] = [];
			}
			
			boardSprite = new Sprite();
			stage.addChild(boardSprite);
			Screens.currentScreenObjects.push(boardSprite);
			
			boardFiller = Atlas.generate("filler");
			boardFiller.width = dotWidth*5;
			boardFiller.height = dotWidth*5;
			boardSprite.addChild(boardFiller);
			boardFiller.touchable = false;
			boardFiller.visible = false;
			
			boardSprite.x = int(Environment.rectSprite.x + Environment.rectSprite.width/2 - boardSprite.width/2);
			boardSprite.y = int(Environment.rectSprite.y + Environment.rectSprite.height/2 - boardSprite.height/2);
			
			statsIcon = Atlas.generate("stats icon");
			statsIcon.height = int(Environment.rectSprite.width*0.21875); // 0.24375
			statsIcon.scaleX = statsIcon.scaleY;
			statsIcon.smoothing = TextureSmoothing.BILINEAR;
			statsIcon.color = Hud.iconsOffColor;
			statsIcon.x = int(Board.boardSprite.x + dotWidth - statsIcon.width/2);			
			statsIcon.y = int(Environment.rectSprite.height*0.8176 + Environment.rectSprite.y);
			stage.addChild(statsIcon);
			Screens.currentScreenObjects.push(statsIcon);
			statsIcon.addEventListener(TouchEvent.TOUCH, statsIconTouchHandler);
			
			reduxRing = Atlas.generate("remove ring");
			reduxRing.height = int(Environment.rectSprite.width*0.21875); // 203125
			reduxRing.scaleX = reduxRing.scaleY;
			reduxRing.smoothing = TextureSmoothing.BILINEAR;
			reduxRing.color = Hud.iconsOffColor;
			reduxRing.x = int(Main.screenWidth - reduxRing.width - statsIcon.x);
			reduxRing.y = int(Environment.rectSprite.height*0.8176 + Environment.rectSprite.y);
			
			reduxRing.pivotX = reduxRing.width/2 * 298/reduxRing.width;
			reduxRing.pivotY = reduxRing.height/2 * 298/reduxRing.height;
			reduxRing.x += (reduxRing.width/2);
			reduxRing.y += (reduxRing.height/2);
			
			reduxRing.visible = false;
			reduxRing.touchable = false;
			ringMax = reduxRing.width * 2.22;
			stage.addChild(reduxRing);
			Screens.currentScreenObjects.push(reduxRing);
			
			reduxIcon = Atlas.generate("remove icon");
			reduxIcon.height = int(Environment.rectSprite.width*0.21875); // 203125
			reduxIcon.scaleX = reduxIcon.scaleY;
			reduxIcon.smoothing = TextureSmoothing.BILINEAR;
			reduxIcon.x = int(Main.screenWidth - reduxIcon.width - statsIcon.x);
			reduxIcon.y = int(Environment.rectSprite.height*0.8176 + Environment.rectSprite.y);
			reduxIcon.color = Hud.iconsOffColor;
			stage.addChild(reduxIcon);
			Screens.currentScreenObjects.push(reduxIcon);
			
			Drop.setup();
		}
		
		
		static function statsIconTouchHandler(evt:TouchEvent):void {
			
			if (!Stats.isPaused) {
			
				statsIconTouchList = evt.getTouches(Environment.stageRef);
				if (statsIconTouchList.length > 0) {
					
					iconsPoint = statsIconTouchList[0].getLocation(Environment.stageRef);
				
					if (statsIcon.bounds.containsPoint(iconsPoint)) {
					
						if (statsIconTouchList[0].phase == TouchPhase.BEGAN || statsIconTouchList[0].phase == TouchPhase.MOVED) {
							if (!statsIconOn) {
								statsIcon.color = Hud.iconsOnColor;
								statsIconOn = true;
								
								Audio.clearChannel.stop();
								Audio.playButton();
							}
							
						}
						
						if (statsIconTouchList[0].phase == TouchPhase.ENDED) {
							
							statsIcon.color = Hud.iconsOffColor;
							statsIconOn = false;
							
							if (Board.boardIsActive) {
								Environment.stageRef.removeEventListener(TouchEvent.TOUCH, stageTouchHandler);
								statsIcon.color = Hud.iconsOnColor;
								Stats.isPaused = true;
								
								if (Screens.gameMode == "timed") {
									Audio.playPause();
									Stats.isPaused = true;
									Hud.pauseHandler();									
									Board.boardSprite.flatten();
								}
								
								var boardTimerStats:Timer;			
								boardTimerStats = new Timer(Screens.transVal);
								boardTimerStats.start();
								
								boardTimerStats.addEventListener(TimerEvent.TIMER, boardTimerStatsHandler);
								function boardTimerStatsHandler(evt:TimerEvent):void {
									boardTimerStats.stop();
									boardTimerStats.removeEventListener(TimerEvent.TIMER, boardTimerStatsHandler);
									boardTimerStats = null;
									
									Screens.setStats(1);
								}
							}
						}
					} else {
						if (statsIconOn) {
							statsIcon.color = Hud.iconsOffColor;
							statsIconOn = false;
						}
					}
				}
			}
		}
		
		
		static function reduxTouchHandler(evt:TouchEvent):void {
			
			if (!Stats.isPaused) {
				
				reduxTouchList = evt.getTouches(Environment.stageRef);
				if (reduxTouchList.length > 0) {
					
					iconsPoint = reduxTouchList[0].getLocation(Environment.stageRef);
				
					if (reduxIcon.bounds.containsPoint(iconsPoint)) {
						
						if (reduxTouchList[0].phase == TouchPhase.BEGAN || reduxTouchList[0].phase == TouchPhase.MOVED) {
							if (!reduxIconOn && !moveOn && canMove) {
								reduxIcon.color = Hud.iconsOnColor;
								reduxIconOn = true;
								
								Hud.hudSprite.unflatten();
								Hud.reduxText.color = Hud.iconsOnColor;
								Hud.hudSprite.flatten();
								
								if (Environment.currentRedux > 0) {
									Audio.playButton();
								} else {
									Audio.playOut();
								}
							}
						}
						
						if (reduxTouchList[0].phase == TouchPhase.ENDED) {								
							if (!moveOn && canMove) {
								Redux.set();
								
								if (!Redux.reduxOn) {
									Redux.resetRedux();
								}
								reduxIconOn = false;
							}
						}
					} else {
						if (!Redux.reduxOn) {
							if (reduxIconOn) {
								reduxIcon.color = Hud.iconsOffColor;
								reduxIconOn = false;
								
								Hud.hudSprite.unflatten();
								Hud.reduxText.color = Hud.iconsOffColor;
								Hud.hudSprite.flatten();
							}
						}
					}
				}	
			}
		}
		
		
		static function stageTouchHandler(evt:TouchEvent):void {
			
			if (!Stats.isPaused) {
				
				stageTouchList = evt.getTouches(Environment.stageRef);
				
				if (stageTouchList.length > 0) {
					
					if (evt.target == Environment.stageRef && !moveOn && canMove && stageTouchList[0].phase == TouchPhase.BEGAN) {
						
						if (evt.target == Environment.stageRef) {
							Redux.resetRedux();
						}
						
						for (var b:int = 0; b < rows; b++) {
							snap(b);
						}				
						if (canMove) {
							disable();
							Drop.dropAll();
							
							Score.updateMoves();
						}
					}
				}
			}
		}
		
		
		static function dotTouchHandler(evt:TouchEvent):void {
			
			if (!Stats.isPaused) {
			
				touchList = evt.getTouches(Environment.stageRef);
				
				if (touchList.length > 0) {
					if (!moveOn && canMove && touchList[0].phase == TouchPhase.BEGAN) {
						
						if (Redux.reduxOn) {
							
							Redux.check(evt.target);
							
						} else {
						
							moveOn = true;
							origin = touchList[0].getLocation(boardSprite);
							point = touchList[0].getLocation(boardSprite);
							target = evt.target as Image;
							initX = target.x;
							
							
							for (var r:int = 0; r < rows; r++) {
								if (Board["moveList" + r].length == 0) {
									Board["moveList" + r].push(target);
									Board["xList" + r].push(target.x);
								}
							}
							
						}
					}
				
					if (moveOn && target && canMove && touchList[0].phase == TouchPhase.MOVED) {
						point = touchList[0].getLocation(boardSprite);
						target.x -= origin.x - point.x;
						diffX = point.x - origin.x;
						
						for (var q:int = 0; q < rows; q++) {
							for (var s:int = 1; s < 6; s++) {
								dotClass = getDefinitionByName("RowCount" + s) as Class;
								if (Board["row" + q].length == s) {
									dotClass["check"](diffX, Board["row" + q], Board["xList" + q], target, Board["moveList" + q]);
								}
							}
						}
						
						if (!target.bounds.containsPoint(point)) {						
							origin.x = target.x + target.width/2;
							origin.y = target.y + target.height/2;
							
						} else {
							origin = touchList[0].getLocation(boardSprite);
						}
					}
			
					if (moveOn && touchList[0].phase == TouchPhase.ENDED) {
						
						for (var b:int = 0; b < rows; b++) {
							snap(b);
						}
						
						if (target.x == initX) {
							disable();
							reorder();
							reset();
							
						} else {
							if (canMove) {
								disable();
								Drop.dropAll();
								Score.updateMoves();
								
							}
						}
					}
				}
			}
		}
		
		
		static function snap(t):void {
			if (Board["moveList" + t].length > 0) {
				for (var i:int = 1; i < 6; i++) {
					dotClass = getDefinitionByName("RowCount" + i) as Class;
					if (Board["row" + t].length == i) {
						dotClass["snap"](Board["row" + t]);
					}
				}
			}
		}
		
		
		static function reorder() {			
			for (var i:int = 0; i < rows; i++) {
				Board["row" + i].length = 0;
			}
			
			for (var k:int = 0; k < rows; k++) {
				for (var j:int = 0; j < dotList.length; j++) {
					if (dotList[j].y == (dotWidth * 4) - (k * dotWidth)) {
						Board["row" + k].push(dotList[j]);
					}
				}
			}
			
			for (var m:int = 0; m < rows; m++) {
				Board["row" + m].sortOn("x", Array.NUMERIC);
			}
			
			for (var c:int = 0; c < rows; c++) {
				Board["col" + c].length = 0;
			}
			
			for each (var id in dotList) {
				if (id.x == dotWidth * 0) {
					col0.push(id);
				}
				if (id.x == dotWidth * 1) {
					col1.push(id);
				}
				if (id.x == dotWidth * 2) {
					col2.push(id);
				}
				if (id.x == dotWidth * 3) {
					col3.push(id);
				}
				if (id.x == dotWidth * 4) {
					col4.push(id);
				}
			}
			
			
			Drop.dropY.length = 0;
			for (var r:int = 0; r < 5; r++) {
				for each (var rY in Board["row" + r]) {
					Drop.dropY.push(rY.y);
				}
			}
		}
		
		
		static function disable() {
			Environment.stageRef.removeEventListener(TouchEvent.TOUCH, stageTouchHandler);
			for each (var id in dotList) {
				id.removeEventListener(TouchEvent.TOUCH, dotTouchHandler);
			}
		}
		
		
		static function reset():void {
			target = null;			
			isDropping = false;
			canMove = true;
			moveOn = false;
			Drop.singleAllowed = true;			
			Check.soundCheck = false;
						
			for (var i:int = 0; i < rows; i++) {
				Board["moveList" + i].length = 0;
				Board["xList" + i].length = 0;
				Board["row" + i].length = 0;
				Board["col" + i].length = 0;
			}
			
			for (var i2:int = 0; i2 < Drop.allRateList.length; i2++) {
				Drop.allRateList[i2] = 0;
			}
			
			Drop.turnRateList = [0,0,0,0,0,0];
			
			Drop.initArray.length = 0;
			Drop.dropEnd = 0;
			Drop.initCount = 1;
			Drop.dropRate = 0;
			
			if (!gameOver) {
				reorder();
				dotList.length = 0;
				for (var d:int = 0; d < rows; d++) {
					for each (var id2 in Board["row" + d]) {
						dotList.push(id2);
						id2.addEventListener(TouchEvent.TOUCH, dotTouchHandler);
					}
				}
				
				Environment.stageRef.addEventListener(TouchEvent.TOUCH, stageTouchHandler);
				if (col0.length == 5 && col1.length == 5 && col2.length == 5 && col3.length == 5 && col4.length == 5) {
					
					Board.boardIsActive = false;
					
					if (Screens.gameMode == "timed") {
						Score.timeLeft = Score.timeLeftInit;
						Environment.stageRef.removeEventListener(TouchEvent.TOUCH, stageTouchHandler);
						
						
						Hud.gameTimer.stop();
						Hud.timeElapsed = 0;
						Hud.gameTimer.removeEventListener(TimerEvent.TIMER, Hud.handleTimer);
					}
					
					if (Board.reduxRing) {
						Redux.resetRedux();
					}
					Board.reduxIcon.removeEventListener(TouchEvent.TOUCH, Board.reduxTouchHandler);
					Board.statsIcon.removeEventListener(TouchEvent.TOUCH, Board.statsIconTouchHandler);
					
					
					End.lose();
				}
			}
			
			if (Board.dotList.length == 0) {
				if (!Board.gameOver) {
					
					Board.target = null;
					
					Board.canMove = true;
					Board.isDropping = false;
					Board.moveOn = false;
					Board.orderInt = 0;
					Board.gameOver = true;
					Board.stageHit = false;
					
					Drop.firstDrop = true;
					Drop.dropOver = false;
					Drop.singleAllowed = false;
					
					Drop.initCount = Board.colorArray.length;
					Drop.dropCount = 0;
					Drop.dropEnd = 0;
					Drop.initArray.length = 0;
					Drop.dropRate = 0;
					Drop.dropInt = 0;
					
					Drop.initCount = 1;
					Board.gameOver = false;
					Drop.setup();
				} else {
					End.clear();
				}
			}
		}
	}
}