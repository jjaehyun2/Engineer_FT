package methods 
{
	import elements.Accumulated;
	import elements.Roulette;
	import managers.RouletteManager;
	/**
	 * ...
	 * @author LeleoSan
	 */
	public class System 
	{
		
		public static function getValues():Array
		{
			/** consts */
			const D:int = -500;//POSITION WIN
			
			function raffle():String
			{
				var n:int = Math.round(Math.random() * (Roulette.TYPES.length - 1));
				return Roulette.TYPES[n].name;
			}
			function getPosition(_id:int, _name:String):int
			{
				var current:int;
				for (var i:int = 0; i < Roulette.TYPES.length; i++) {
					if (RouletteManager.values[_id][i][0] == _name) {
						current = RouletteManager.values[_id][i][1];
						return current;
					}
				}
				return 0;
			}
			
			var name0:String;
			var name1:String;
			var name2:String;
			
			if (Accumulated.active) {
				var special:int = Math.round(Math.random() * 3);
				if (special == 1) {
					var raffleSole:String = raffle();
					name0 = raffleSole;
					name1 = raffleSole;
					name2 = raffleSole;
				} else {
					name0 = raffle();
					name1 = raffle();
					name2 = raffle();
				}
			} else {
				name0 = raffle();
				name1 = raffle();
				name2 = raffle();
			}
			
			var one:int = -getPosition(0, name0);
			var two:int = -getPosition(1, name1);
			var three:int = -getPosition(2, name2);
			
			return [[name0, (one + D) / 10], [name1, (two + D) / 10], [name2, (three + D) / 10]];
		}
		
	}

}