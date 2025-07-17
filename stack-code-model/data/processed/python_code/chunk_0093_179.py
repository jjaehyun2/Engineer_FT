package classes 
{
	/**
	 * ...
	 * @author Lucas Moyano
	 */
	public class Keys 
	{
		public static const S1_PENDULUM					:int = 0;
		public static const S2_TRY_METAL_DOOR		:int = 1;
		public static const S2_METAL_DOOR				:int = 2;
		public static const S3_TILE_A						:int = 3;
		public static const S3_TILE_B						:int = 4;
		public static const S3_CIRCLE_DOOR			:int = 5;
		public static const S4_SECRET_DOOR			:int = 6;
		public static const S1_KEY							:int = 7;
		public static const S5_HAND_BLUE				:int = 8;
		public static const S5_HAND_RED					:int = 9;
		public static const S5_TEMP_HAND_BLUE		:int = 8;
		
		public static var COUNT_KICK:int = 0;
		
		public static var FIRST_METAL_DOOR:Character = null;
		public static var SECOND_METAL_DOOR:Character = null;
		
		private static var keys:Array;
		
		public static function id(value:int):Boolean
		{
			return keys[value];
		}
		
		public static function setId(id:int, value:Boolean):void
		{
			keys[id] = value;
		}
		
		public static function resetFlags():void
		{
			SECOND_METAL_DOOR = null;
			FIRST_METAL_DOOR = null;
			COUNT_KICK = 0;
			if (!keys)
			{
				keys = [];
			}
			
			for (var i:int = 0; i < 500; i++) 
			{
				keys[i] = false;
			}
		}
		
	}

}