package  
{
	/**
	 * ...
	 * @author Alvaro
	 */
	public class LevelFactory
	{
		[Embed(source = 'lvl/Level_01_hit.csv', mimeType = "application/octet-stream")] private var LVL_01_HIT:Class;
		[Embed(source = 'lvl/Level_01_bg.csv', mimeType = "application/octet-stream")] private var LVL_01_BG:Class;
		[Embed(source = 'lvl/Level_01_spr.csv', mimeType = "application/octet-stream")] private var LVL_01_SPR:Class;
		
		[Embed(source = 'lvl/Level_02_hit.csv', mimeType = "application/octet-stream")] private var LVL_02_HIT:Class;
		[Embed(source = 'lvl/Level_02_bg.csv', mimeType = "application/octet-stream")] private var LVL_02_BG:Class;
		[Embed(source = 'lvl/Level_02_spr.csv', mimeType = "application/octet-stream")] private var LVL_02_SPR:Class;
		
		private var levels:Array = new Array();
		
		public function LevelFactory() 
		{
			levels.push(new Level(LVL_01_HIT, LVL_01_BG, LVL_01_SPR));
			levels.push(new Level(LVL_02_HIT, LVL_02_BG, LVL_02_SPR));
		}
		
		public function getLevel(level:int):Level
		{
			var index:int = level - 1;
			return levels[index] as Level;
		}
		
		public function getLevelCount():int
		{
			return levels.length;
		}
		
	}

}