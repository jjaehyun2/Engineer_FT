package  
{
	import net.flashpunk.utils.Data;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class ScoreTracker 
	{
		private static var level1Score:int = 60 * 60 - 2;
		private static var level2Score:int = 60 * 60 - 2;
		private static var level3Score:int = 60 * 60 - 2;
		
		public function ScoreTracker() 
		{
			
		}
		
		//returns true for better score, false for worse
		public static function beatLevel(level:int, score:int):Boolean
		{
			if (level == 1 && level1Score > score)
			{
				level1Score = score;
				Data.writeInt("Level1Score", score);
				Data.save("miniPassage");
				return true;
			}
			if (level == 2 && level2Score > score)
			{
				level2Score = score;
				Data.writeInt("Level2Score", score);
				Data.save("miniPassage");
				return true;
			}
			if (level == 3 && level3Score > score)
			{
				level3Score = score;
				Data.writeInt("Level3Score", score);
				Data.save("miniPassage");
				return true;
			}
			return false;
		}
		
		public static function loadHighScores():void
		{
			Data.load("miniPassage");
			level1Score = Data.readInt("Level1Score", 60 * 60);
			level2Score = Data.readInt("Level2Score", 60 * 60);
			level3Score = Data.readInt("Level3Score", 60 * 60);
		}
		
		public static function getHighScore(level:int):int
		{
			if (level == 1)
			{
				return level1Score;
			}
			if (level == 2)
			{
				return level2Score;
			}
			if (level == 3)
			{
				return level3Score;
			}
			trace("[ScoreTracker][getHighScore()]Level not found " + level);
			return -1;
		}
		
		public static function getCombinedScore():int
		{
			if (level1Score < 100 || level2Score < 100 || level3Score < 100) return 9999999; //anti cheat measure. 
			
			return level1Score + level2Score + level3Score;
		}
	}

}