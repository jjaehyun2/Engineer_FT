package src.data
{
	import src.assets.Levels;

	public class LevelEndVO
	{
		protected const MAXIMUM_GAME_TIME_BONUS:uint = 100 * 60 * 2;
		
		private var _gameTime:		Number;
		
		private var _score:			int;
		
		private var _levelID:		uint;
		private var _worldID:	uint;
		private var _collectedCoin:	uint;
		private var _starCount:		uint;
		
		private var _winState:		Boolean;
		
		public function LevelEndVO( collectedCoin:uint, gameTime:Number, winState:Boolean, levelID:uint, levelPackID:uint ):void
		{
			_collectedCoin = collectedCoin;
			_gameTime = gameTime;
			_winState = winState;
			_levelID = levelID;
			_worldID = levelPackID;
			
			calculateScore( );
			calculateStarCount( );
		}
		
		protected function calculateScore( ):void
		{
			_score = 0;
			
			if ( _winState )
			{
				_score += Math.floor( MAXIMUM_GAME_TIME_BONUS - _gameTime / 10 );
				_score += _collectedCoin * 50;
			} else
			{
				
			}
		}
		
		protected function calculateStarCount( ):void
		{
			if ( _winState )
			{
				_starCount = Levels.levels[_worldID][_levelID].scoreToStarCount( _score );
			}
			else
			{
				_starCount = 0;
			}
		}
		
		public function get score( ):int
		{
			return _score;
		}
		
		public function get isWon( ):Boolean
		{
			return _winState;
		}
		
		public function get id( ):uint
		{
			return _levelID;
		}
		
		public function get worldID( ):uint
		{
			return _worldID;
		}
		
		public function get starCount( ):uint
		{
			return _starCount;
		}

		public function get collectedCoin( ):uint
		{
			return _collectedCoin;
		}

		public function get gameTime( ):Number
		{
			return _gameTime;
		}
	}
}