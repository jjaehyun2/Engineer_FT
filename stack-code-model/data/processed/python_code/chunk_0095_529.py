package  {
	
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	import starling.display.Stage;
	import starling.text.TextField;

	
	public class Score {
		
		static var currentScore:int;
		static var highScore:int;
		static var todaysHigh:int;
		static var resetPoint:Date;
		static var timedScore0:int;
		static var timedScore1:int;
		static var timedScore2:int;
		static var movesScore0:int;
		static var movesScore1:int;
		static var movesScore2:int;
		static var timedOptions:Array = [30, 60, 90];
		static var movesOptions:Array = [25, 50, 75];
		static var currentGameMode:int;
		static var movesLeftInit:int = 3;
		static var movesLeft:int = movesLeftInit;
		static var timeLeftInit:int = 90;
		static var timeLeft:int = timeLeftInit;
		static var reduxNum:int;
		static var reduxInc:int = 1;
		static var timedNum:int;
		static var timedInc:int = 1;
		static var movesNum:int;
		static var movesInc:int = 1;		
		static var prevID:int;
		static var mode:int;		
		static var newDate:Date;
		static var endDate:Date;
		static var resetTimer:Timer;
		
		
		static function setup(id:int):void {
			mode = id;
			
			reduxNum = Environment.elimUpgrade;
			reduxInc = 1;
			timedNum = Environment.timedUpgrade;
			timedInc = 1;
			movesNum = Environment.movesUpgrade;
			movesInc = 1;
			
			if (id != 1) {
				prevID = id;
			} else {
				id = prevID;
			}
			
			currentScore = 0;
			highScore = Data.saveObj.highScore;
			todaysHigh = Data.saveObj.todaysHigh;
			
			timedScore0 = Data.saveObj.timedScore0;
			timedScore1 = Data.saveObj.timedScore1;
			timedScore2 = Data.saveObj.timedScore2;
			
			movesScore0 = Data.saveObj.movesScore0;
			movesScore1 = Data.saveObj.movesScore1;
			movesScore2 = Data.saveObj.movesScore2;
			
			if (Screens.gameMode == "moves") {
				if (id == Score.movesOptions[0] || id == Score.movesOptions[1] || id == Score.movesOptions[2]) {
					movesLeftInit = id;
					movesLeft = id;
				}
			}
			if (Screens.gameMode == "timed") {
				if (id == Score.timedOptions[0] || id == Score.timedOptions[1] || id == Score.timedOptions[2]) {
					timeLeftInit = id;
					timeLeft = id;
				}
			}
		}
		
		
		static function updateScore(amt:int):void {
			Hud.hudSprite.unflatten();
			
			currentScore += amt;
			
			if (currentScore >= reduxNum*reduxInc) {
				reduxInc++;
				Audio.playUpgrade();
				Environment.currentRedux++;
				Hud.reduxText.text = String("ELIMS\n" + Environment.currentRedux);
			}
			
			if (Screens.gameMode == "perpetua") {				
				if (currentScore >= highScore) {
					highScore = currentScore;
					Data.saveObj.highScore = currentScore;
				}
				
				if (currentScore >= todaysHigh) {
					todaysHigh = currentScore;
					Data.saveObj.todaysHigh = todaysHigh;
				}
			}			
			
			if (Screens.gameMode == "timed") {
				
				
				if (currentGameMode == timedOptions[0]) {
					if (currentScore >= timedScore0) {
						timedScore0 = currentScore;
						Data.saveObj.timedScore0 = timedScore0;
					}
				}
				if (currentGameMode == timedOptions[1]) {
					if (currentScore >= timedScore1) {
						timedScore1 = currentScore;
						Data.saveObj.timedScore1 = timedScore1;
					}
				}
				if (currentGameMode == timedOptions[2]) {
					if (currentScore >= timedScore2) {
						timedScore2 = currentScore;
						Data.saveObj.timedScore2 = timedScore2;
					}
				}
								
				if (currentScore >= timedNum*timedInc) {
					timedInc++;
					Audio.playExtra();
					timeLeft += 10;
					Hud.timed.text = String(addZeros(timeLeft));
				}
			}
						
			if (Screens.gameMode == "moves") {
				if (currentGameMode == movesOptions[0]) {
					if (currentScore >= movesScore0) {
						movesScore0 = currentScore;
						Data.saveObj.movesScore0 = movesScore0;
					}
				}
				if (currentGameMode == movesOptions[1]) {
					if (currentScore >= movesScore1) {
						movesScore1 = currentScore;
						Data.saveObj.movesScore1 = movesScore1;
					}
				}
				if (currentGameMode == movesOptions[2]) {
					if (currentScore >= movesScore2) {
						movesScore2 = currentScore;
						Data.saveObj.movesScore2 = movesScore2;
					}
				}
				
				if (currentScore >= movesNum*movesInc) {
					movesInc++;
					Audio.playExtra();
					movesLeft += 10;
					Hud.moves.text = String(addZeros(movesLeft));
				}
			}
			
			Hud.score.text = String(addCommas(currentScore));
			
			if (Screens.gameMode == "perpetua") {
				Hud.highScore.text = String(addCommas(highScore));
			}
			
			Hud.hudSprite.flatten();
		}
		
		
		static function updateMoves() {
			Hud.hudSprite.unflatten();
			
			if (Screens.gameMode == "moves") {
				Score.movesLeft--;
				Hud.moves.text = String(addZeros(movesLeft));
			}
			
			Hud.hudSprite.flatten();
		}
		
		
		static function checkHigh() {
			newDate = new Date();
			
			if (newDate >= Data.saveObj.resetPoint || Data.saveObj.resetPoint.time - newDate.time > 86400000) {
				endDate = new Date();
				endDate.setDate(endDate.getDate() + 1);
				endDate.setHours(0,0,0,0);
				Data.saveObj.resetPoint = endDate;
				resetPoint = endDate;
				Data.saveObj.todaysHigh = 0;
				todaysHigh = 0;
				Data.flushSave();
				
				if (Stats.score2) {
					Stats.score2.text = String("--");
				}
			}
			
			if (resetTimer) {
				resetTimer.start();
			}
		}
		
		
		static function resetHandler(e:TimerEvent):void {
			Score.checkHigh();
		}
		
		
		static function addZeros(id:int):String {
			var scoreString:String = String(id);
			if (scoreString.length < 2) {
				scoreString = "0" + scoreString;
			}
			return scoreString;
		}
		
		
		static function addCommas(id:int):String {
			var scoreString:String = "" + id;
			for (var i:int = scoreString.length - 3; i > 0; i -= 3) {
				scoreString = scoreString.substr(0, i) + "," + scoreString.substr(i);
			}
			return scoreString;
		}
	}
}