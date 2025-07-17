package com.sixfootsoftware.pitstop {
    import org.flixel.FlxG;

    public class PlayerScoreCalculator implements Calculator {
	
		private const MAX_TIME:uint = 10000;
        private var score:Number = 0;
        private var lastScore:Number = 0;

        public function addScore( pitTime:Number ):void {
			var time:int = ( MAX_TIME - pitTime ) / 10;
			if ( time > 0 ) {  
				this.score += time;
                FlxG.log( "score =" + score );
                FlxG.log( "time =" + time );

			}				
        }

        public function getCalculatorResult():Number {
            lastScore = score;
			return score;
		}

        public function updated():Boolean {
            return score != lastScore;
        }
    }
}