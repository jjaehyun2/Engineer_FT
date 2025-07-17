/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Objects
{
	import flash.net.SharedObject;

	/**
	 * The HighScore class stores a single record that will be saved in a flash 
	 * cookie and restored for every new game instance. It is also constantly
	 * updated. 
	 */
	public class Highscore
	{
		private var highscoreFile:SharedObject;
		private var _rankingObject:Object = new Object();
		private var _lastScore:uint = 0;
		
		public function Highscore()
		{
			highscoreFile = SharedObject.getLocal("highscore");
			if(highscoreFile.data.ranking == null) {
				initRankingObject();
			} else {
				_rankingObject = highscoreFile.data.ranking;
			}
		}
		
		private function initRankingObject():void
		{
			_rankingObject = {score:0};
			storeRankingObject();
		}
		
		private function storeRankingObject():void
		{
			highscoreFile.data.ranking = _rankingObject;
			highscoreFile.flush();
		}
		
		public function setScore(value:uint):void
		{
			if(value > _rankingObject.score)
			{
				_rankingObject.score = value;
				storeRankingObject();
			}
			_lastScore = value;
		}
		
		public function getScore():uint
		{
			return _rankingObject.score;
		}

		public function get rankingObject():Object
		{
			return _rankingObject;
		}

		public function get lastScore():uint
		{
			return _lastScore;
		}
		
		public function set lastScore(value:uint):void
		{
			_lastScore = value;
		}
	}
}