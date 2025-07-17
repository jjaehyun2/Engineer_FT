package  {
	
	import flash.display.MovieClip;
	
	
	public class Score extends MovieClip {
		
		
		public function Score() {
			// constructor code
		}
		public function AddScore(score:Number)
		{
			SCORE.text= 'Score: ' +score.toString();
		}
	}
	
}