package factories {
	import mx.core.FlexGlobals;

	public class DarkMatterCollectorFactory extends ResourceFactory {

		/*
		Constructor is not used... 
		*/
		public function DarkMatterCollectorFactory():* {
		}
		
		[Bindable]
		public static var name:String = 'DarkMatterCollector';
		
		private static var level_rates:Array = [
			100, 500, 2500, 
		];
		
		private static var level_costs:Array = [
			300, 1500, 7500, 
		];
		
		private static var __current_level__:int = 0;
		
		public static function get current_level():int {
			return __current_level__;
		}
		
		public static function set current_level(level:int):void {
			if (__current_level__ != level) {
				__current_level__ = level;
			}
		}
		
		public static function next_level():void {
			__current_level__++;
			var app:GalaxyWars = FlexGlobals.topLevelApplication as GalaxyWars;
			app.mySO.data.__solar_resource_level__ = __current_level__;
			app.mySO.flush();
		}
		
		public static function get current_level_production_rate():Number {
			try {
				return level_rates[current_level];
			} catch (err:Error) {}
			return -1;
		}
		
		public static function get current_level_upgrade_cost():Number {
			try {
				return level_costs[current_level];
			} catch (err:Error) {}
			return -1;
		}
		
		public static function get current_level_upgrade_time():Number {
			return ResourceFactory.current_level_upgrade_time(current_level);
		}
	}
}