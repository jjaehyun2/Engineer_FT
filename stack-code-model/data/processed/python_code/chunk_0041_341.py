package  {
	
	import flash.utils.*;
	import starling.core.Starling;
	import starling.display.Image;
	import starling.events.Event;
	import starling.events.TouchEvent;
	import starling.textures.TextureSmoothing;
	
	
	public class Drop {
		
		static var setX:Array = [Board.dotWidth*0, Board.dotWidth*1, Board.dotWidth*2, Board.dotWidth*3, Board.dotWidth*4];
		static var setXDups:Array = [];
		static var initArray:Array = [];
		static var turnRateList:Array = [0,0,0,0,0,0];
		static var allRateList:Array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
		
		static var initCount:int = Board.colorArray.length;
		static var dropCount:int = 0;
		static var dropEnd:int = 0;
		static var dropInt:int;
		
		static var firstDrop:Boolean = true;
		static var dropOver:Boolean = false;
		static var singleAllowed:Boolean = false;
		static var zeroDots:Boolean = false;
		
		static var rand:int;
		static var colRand:int;
		
		static var dropRate:Number = 0;
		static var acceleration:Number = 1.3;		
		
		static var initFallSpeed:Number = (Board.dotWidth) * (3/111);
		static var maxFallSpeed:Number = (Board.dotWidth) * (70/111);	
		static var alphaRate:Number = 0.18;
		
		static var dropY:Array = [];
		
		
		public static function setup():void {
			Board.isDropping = true;
			Board.canMove = false;
			Board.moveOn = true;
			Board.gameOver = false;
			setXDups.length = 0;
			
			for (var i:int = 0; i < initCount; i++) {
				
				var dot:Image = Atlas.generate("game dot");
				dot.color = Board.dotColorArray[Hud.colorTheme][i];
				
				if (i < 4) {
					dot.x = setX[Math.floor(Math.random()*5)];
					setXDups.push(dot.x);
				} else {
					generate();
					function generate() {
						dot.x = setX[Math.floor(Math.random()*5)];						
						if (dot.x == setXDups[0] && dot.x == setXDups[1] && dot.x == setXDups[2] && dot.x == setXDups[3]) {
							generate();
						}
					}
				}
				
				
				dot.y = -Board.dotWidth;
				dot.width = Board.dotWidth;
				dot.height = Board.dotWidth;
				dot.smoothing = TextureSmoothing.BILINEAR;
				Board.boardSprite.addChild(dot);
				Board.dotList.push(dot);
				dot.alpha = 0;
				dot.name = Board.colorArray[i];
			}
			initDrop();
		}
		
		
		static function initDrop() {
			Board.boardIsActive = true;
			
			if (dropCount < initCount) {					
				Board.dotList[dropCount].addEventListener(Event.ENTER_FRAME, moveInitDown);
				dropCount++;
			}
		}
		
		
		static function dropAll():void {
			Board.canMove = false;
			Board.isDropping = true;
			
			for (var i:int = 0; i < Board.dotList.length; i++) {
				Board.dotList[i].addEventListener(Event.ENTER_FRAME, moveAllDown);
			}
		}
		
		
		static function moveAllDown(evt:Event) {
			
			if (!Stats.isPaused) {
			
				Board.tgt1 = evt.target;
				
				for (var i:int = 0; i < Board.dotList.length; i++) {
					if (Board.tgt1 == Board.dotList[i]) {
						
						if (Drop.allRateList[i] == 0) {
							Drop.allRateList[i] = initFallSpeed;
						}
						
						Drop.allRateList[i] *= acceleration;
						Drop.allRateList[i] = Math.ceil(Drop.allRateList[i]);
						
						Drop.allRateList[i] = Math.min(Drop.allRateList[i], maxFallSpeed);
						Board.tgt1.y += Drop.allRateList[i];
						break;
					}
				}
				
				for each (var id in Board.dotList) {
					if (Board.tgt1 != id) {
						if (id.getBounds(id.parent).intersects(Board.tgt1.getBounds(Board.tgt1.parent))) {
							Board.tgt1.y = id.y - Board.tgt1.height;
							Board.tgt1.removeEventListener(Event.ENTER_FRAME, moveAllDown);
							Check.checkOff();
							break;
						}
					}
				}
				
				if (Board.tgt1.y > Board.dotWidth * 4) {
					Board.tgt1.y = Board.dotWidth * 4;
					Board.tgt1.removeEventListener(Event.ENTER_FRAME, moveAllDown);
					Check.checkOff();
				}
			}
		}
		
		
		static function newDrop() {
			if (Board.col0.length == 5 && Board.col1.length == 5 && Board.col2.length == 5 && Board.col3.length == 5 && Board.col4.length == 5) {
				End.lose();
				return;
			} else {
				generateRandomNumber();
			}
 
			function generateRandomNumber():void {
				colRand = Math.floor(Math.random()*5);

				if(Board.col0.length == 5 && colRand == 0){
					generateRandomNumber();
				}
				if(Board.col1.length == 5 && colRand == 1){
					generateRandomNumber();
				}
				if(Board.col2.length == 5 && colRand == 2){
					generateRandomNumber();
				}
				if(Board.col3.length == 5 && colRand == 3){
					generateRandomNumber();
				}
				if(Board.col4.length == 5 && colRand == 4){
					generateRandomNumber();
				}
			}
			
			rand = Math.floor(Math.random()*Board.dotColorArray[Hud.colorTheme].length);
			var dot:Image = Atlas.generate("game dot");
			dot.color = Board.dotColorArray[Hud.colorTheme][rand];
			
			dot.x = setX[colRand];
			dot.y = -Board.dotWidth;
			dot.width = Board.dotWidth;
			dot.height = Board.dotWidth;
			dot.smoothing = TextureSmoothing.BILINEAR;
			Board.boardSprite.addChild(dot);
			Board.dotList.push(dot);
			dot.alpha = 0;
			
			dot.name = Board.colorArray[rand];
			
			dot.addEventListener(Event.ENTER_FRAME, moveInitDown);
			dot.addEventListener(TouchEvent.TOUCH, Board.dotTouchHandler);
		}

			
		static function moveInitDown(evt:Event) {	
			
			if (!Stats.isPaused) {
			
				var h = evt.target;
				var newY:Number;
				
				if (firstDrop) {
					for (var i:int = 0; i < Board.dotList.length; i++) {
						if (h == Board.dotList[i]) {
							
							if (turnRateList[i] == 0) {
								turnRateList[i] = initFallSpeed;
							}
							
							if (h.alpha < 1.0) {
								h.alpha += alphaRate;
							}						
							
							turnRateList[i] *= acceleration;
							turnRateList[i] = Math.ceil(turnRateList[i]);
							
							turnRateList[i] = Math.min(turnRateList[i], maxFallSpeed);
							h.y += turnRateList[i];
							break;
						}
					}
				} else {
					if (dropRate == 0) {
						dropRate = initFallSpeed;
						dropOver = false;
					}
					
					if (h.alpha < 1.0) {
						h.alpha += alphaRate;
					}
					
					dropRate *= acceleration;
					dropRate = Math.ceil(dropRate);
					
					dropRate = Math.min(dropRate, maxFallSpeed);
					h.y += dropRate;
				}
				
				if (h.y > Board.dotWidth*4) {
					h.y = Board.dotWidth*4;
					h.removeEventListener(Event.ENTER_FRAME, moveInitDown);
					dropEnd++;
					if (dropEnd == initCount) {
						dropOver = true;
					}
					if (firstDrop) {
						initDrop();
					}
					
					Audio.playClick();
				}
				
				for each (var id in Board.dotList) {
					if (h != id) {
						if (h.y < id.y) {
							if (id.getBounds(id.parent).intersects(h.getBounds(h.parent))) {
								h.y = id.y - h.height;
								h.removeEventListener(Event.ENTER_FRAME, moveInitDown);
								dropEnd++;
								if (dropEnd == initCount) {
									dropOver = true;
								}
								if (firstDrop) {
									initDrop();
								}
								
								Audio.playClick();
								break;
							}
						}
					}
				}
				
				if (dropOver) {
					if (firstDrop) {
						firstDrop = false;
						for each (var id2 in Board.dotList) {
							id2.addEventListener(TouchEvent.TOUCH, Board.dotTouchHandler);
						}
						Environment.stageRef.addEventListener(TouchEvent.TOUCH, Board.stageTouchHandler);
						Board.reduxIcon.addEventListener(TouchEvent.TOUCH, Board.reduxTouchHandler);
						
						if (Board.stageTouchList) {
							Board.stageTouchList.length = 0;
						}
						
						if (Screens.gameMode == "timed" && dropCount == 6) {
							Hud.gameTimer.start();
							Hud.oldTime = getTimer();
						}
					}
					
					dropOver = false;
					Board.reorder();
					Check.patterns();
				}
			}
		}
	}
}