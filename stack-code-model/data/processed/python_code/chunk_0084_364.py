package  {
	
	import flash.events.TimerEvent;
	import flash.utils.*;
	import flash.utils.getTimer;
	import flash.utils.Timer;
	import starling.core.Starling;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.text.TextField;
	import starling.utils.HAlign;
	
	
	public class End {
		
		static var endVal:int;
		static var rateFreqMatch:Boolean = false;
		
		
		static function lose() {
			Board.boardIsActive = false;
			Board.ended = true;
			
			rateFreqMatch = false;
			Data.saveObj.timesPlayed++;
			removeAllListeners();
			Audio.playGameOver();
			
			var reduxInt:int = setInterval(reduxBalance, 250);
			function reduxBalance() {
				clearInterval(reduxInt);
				Redux.balanceRedux();
			}
			
			var endInt:int = setInterval(endAnimation, 1500);
			function endAnimation() {
				clearInterval(endInt);
				Score.checkHigh();
				Screens.currentScreen = "stats";
				
				for each (var id in Data.saveObj.rateFreq) {
					if (Data.saveObj.timesPlayed == id) {
						rateFreqMatch = true;
						break;
					}
				}
				
				if (!Data.saveObj.hasRated && !Data.saveObj.declinedRating && rateFreqMatch) {
					var endTimerRating:Timer;
					endTimerRating = new Timer(Screens.transVal);
					endTimerRating.start();
					
					endTimerRating.addEventListener(TimerEvent.TIMER, endTimerRatingHandler);
					function endTimerRatingHandler(evt:TimerEvent):void {
						endTimerRating.stop();
						endTimerRating.removeEventListener(TimerEvent.TIMER, endTimerRatingHandler);
						endTimerRating = null;
						
						Screens.setStats(2);
						
						if (CONFIG::AIR && Environment.ratingSupported) {
							Rating.showRateBox();
						}
					}
				} else {
					if (CONFIG::AIR) {
						if (CONFIG::ANDROID) {
							AdsAndroid.attemptTimer.stop();
							AdsAndroid.attemptTimer.removeEventListener(TimerEvent.TIMER, AdsAndroid.attemptTimerHandler);
							AdsAndroid.showAd();
						}
					}
					
					var endTimerStats:Timer;			
					endTimerStats = new Timer(Screens.transVal);
					endTimerStats.start();
					
					endTimerStats.addEventListener(TimerEvent.TIMER, endTimerStatsHandler);
					function endTimerStatsHandler(evt:TimerEvent):void {
						endTimerStats.stop();
						endTimerStats.removeEventListener(TimerEvent.TIMER, endTimerStatsHandler);
						endTimerStats = null;
						
						Screens.setStats(2);
					}
				}
			}
		}
		
		
		static function clear() {
			Redux.waitingForStats = false;
			
			Board.target = null;
			
			Redux.reduxOn = false;
			Score.reduxInc = 1;
			
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
			
			Score.currentScore = 0;
			
			Check.redHorzElim.length = 0;
			Check.redVertElim.length = 0;
			Check.yellowHorzElim.length = 0;
			Check.yellowVertElim.length = 0;
			Check.purpleHorzElim.length = 0;
			Check.purpleVertElim.length = 0;
			Check.greenHorzElim.length = 0;
			Check.greenVertElim.length = 0;
			Check.blueHorzElim.length = 0;
			Check.blueVertElim.length = 0;
			Check.orangeHorzElim.length = 0;
			Check.orangeVertElim.length = 0;
			Check.removeArray.length = 0;
			
			Check.row0 = [null, null, null, null, null];
			Check.row1 = [null, null, null, null, null];
			Check.row2 = [null, null, null, null, null];
			Check.row3 = [null, null, null, null, null];
			Check.row4 = [null, null, null, null, null];
			
			Screens.clearIntroScreen();
			
			for each (var id in Board.dotList) {
				id.removeEventListener(Event.ENTER_FRAME, Drop.moveInitDown);
				id.removeEventListener(Event.ENTER_FRAME, Drop.moveAllDown);
				id.removeEventListener(TouchEvent.TOUCH, Board.dotTouchHandler);
				Board.boardSprite.removeChild(id);
			}
			
			Environment.stageRef.removeEventListener(TouchEvent.TOUCH, Board.stageTouchHandler);
			Environment.stageRef.removeEventListener(TouchEvent.TOUCH, Board.reduxTouchHandler);
			Environment.stageRef.removeChild(Intro.statsIcon);
			Environment.stageRef.removeChild(Intro.optionsIcon);
			
			if (Stats.gameMode == 2) {
				for (var j:int = 0; j < Board.rows; j++) {
					Board["moveList" + j].length = 0;
					Board["xList" + j].length = 0;
					Board["row" + j].length = 0;
					Board["col" + j].length = 0;
				}
			}
			
			for (var i2:int = 0; i2 < Drop.allRateList.length; i2++) {
				Drop.allRateList[i2] = 0;
			}
			
			Drop.turnRateList = [0,0,0,0,0,0];
			Board.dotList.length = 0;
		}
		
		
		static function removeAllListeners() {
			for each (var id in Board.dotList) {
				id.removeEventListener(Event.ENTER_FRAME, Drop.moveInitDown);
				id.removeEventListener(Event.ENTER_FRAME, Drop.moveAllDown);
				id.removeEventListener(TouchEvent.TOUCH, Board.dotTouchHandler);
			}
			
			if (Stats.gameMode == 2) {
				Board.reduxIcon.removeEventListener(TouchEvent.TOUCH, Board.reduxTouchHandler);
				Board.statsIcon.removeEventListener(TouchEvent.TOUCH, Board.statsIconTouchHandler);	
			}
			
			Environment.stageRef.removeEventListener(Event.ENTER_FRAME, Redux.fadeOut);
			Environment.stageRef.removeEventListener(Event.ENTER_FRAME, Redux.moveRing);
			Environment.stageRef.removeEventListener(TouchEvent.TOUCH, Board.stageTouchHandler);
			
			if (Stats.gameMode != 0) {
				Board.statsIcon.removeEventListener(TouchEvent.TOUCH, Board.statsIconTouchHandler);
			}
			
			Environment.stageRef.removeEventListener(TouchEvent.TOUCH, Board.reduxTouchHandler);
		}
	}
}