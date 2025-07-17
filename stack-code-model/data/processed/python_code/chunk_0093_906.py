package  {
	import flash.text.TextField;
	
	public class ScoreKeeper {
		private var scoreField:TextField;
		private var timeField:TextField;
		private var score:Number;
		private var permy:Permy;
		private var hiScoreField:TextField;
	
		public function ScoreKeeper(scoreField:TextField,timeField:TextField,hiScoreField:TextField,permy:Permy) {
			this.scoreField = scoreField;
			this.timeField = timeField;
			this.hiScoreField = hiScoreField;
			this.permy = permy;
			this.score = 0;
			this.scoreField.text = "0";
		}
		
		public function setScoreField(score:Number) {
			this.scoreField.text = score.toString();
		}
		
		public function setTimeField(time:Number) {
			this.timeField.text = time.toFixed(1);
		}
		
		public function setHiScoreField(hiScore:Number) {
			this.hiScoreField.text = this.permy.getHiScore().toString();
		}

		public function getScore():Number {
			return this.score;
		}
		
		public function getTimeField():TextField {
			return this.timeField;
		}
		
		public function getHiScoreField():TextField {
			return this.hiScoreField;
		}
		
		public function getScoreField():TextField {
			return this.scoreField;
		}
		
		public function setScore(score:Number) {
			this.score = score;
			this.scoreField.text = score.toString();
		}

	}
	
}