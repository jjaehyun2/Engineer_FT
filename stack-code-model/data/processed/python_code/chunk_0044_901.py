package src.assets
{
	import src.constant.CStarRequired;
	import src.constant.CWorldNames;
	import src.data.CarData;

	public class CarDatas
	{
		public static var MAX_SPEED:Number = 14;
		public static var MIN_SPEED:Number = 9;
		public static var MAX_ROTATION:Number = 9;
		public static var MIN_ROTATION:Number = 5;
		public static var MAX_DAMPING:Number = .9;
		public static var MIN_DAMPING:Number = .4;

		public static var CAR_DATAS:Vector.<CarData> = new <CarData>[
			// LEVEL PACK CARS =========================================
			new CarData(
					/*ID*/              0,
					/*GRAPHIC ID*/      0,
					/*NAME*/            "RED MONSTER",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           10,
					/*ROTATION*/        6,
					/*DAMPING*/         .8,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   -1
			),
			new CarData(
					/*ID*/              3,
					/*GRAPHIC ID*/      6,
					/*NAME*/            "SANTA ROCK",
					/*STAR_REQUIRED*/	CStarRequired.UNLOCK_CAR_TYPE_3,
					/*SPEED*/           10,
					/*ROTATION*/        6,
					/*DAMPING*/         .8,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   0
			),
			new CarData(
					/*ID*/              1,
					/*GRAPHIC ID*/      1,
					/*NAME*/            "SNOWY",
					/*STAR_REQUIRED*/	CStarRequired.UNLOCK_CAR_TYPE_1,
					/*SPEED*/           11,
					/*ROTATION*/        6,
					/*DAMPING*/         .8,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   -1
			),
			new CarData(
					/*ID*/              2,
					/*GRAPHIC ID*/      5,
					/*NAME*/            "GHOST",
					/*STAR_REQUIRED*/	CStarRequired.UNLOCK_CAR_TYPE_2,
					/*SPEED*/           11,
					/*ROTATION*/        6,
					/*DAMPING*/         .65,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   0
			),
			new CarData(
					/*ID*/              4,
					/*GRAPHIC ID*/      8,
					/*NAME*/            "TURTLE",
					/*STAR_REQUIRED*/	CStarRequired.UNLOCK_CAR_TYPE_4,
					/*SPEED*/           12,
					/*ROTATION*/        7,
					/*DAMPING*/         .65,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   0
			),
			new CarData(
					/*ID*/              5,
					/*GRAPHIC ID*/      13,
					/*NAME*/            "CANDY CAR",
					/*STAR_REQUIRED*/	CStarRequired.UNLOCK_CAR_TYPE_5,
					/*SPEED*/           13,
					/*ROTATION*/        8,
					/*DAMPING*/         .6,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   0
			),

			// CUSTOM CARS =============================================
			new CarData(
					/*ID*/              1000,
					/*GRAPHIC ID*/      2,
					/*NAME*/            "BLUE HOOK",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           11,
					/*ROTATION*/        7,
					/*DAMPING*/         .75,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   -2
			),
			new CarData(
					/*ID*/              1001,
					/*GRAPHIC ID*/      3,
					/*NAME*/            "MOUNTAIN HUNTER",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           11,
					/*ROTATION*/        7,
					/*DAMPING*/         .75,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   -1
			),
			new CarData(
					/*ID*/              1002,
					/*GRAPHIC ID*/      4,
					/*NAME*/            "LIGHTNING",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           12,
					/*ROTATION*/        7.5,
					/*DAMPING*/         .65,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   0
			),
			new CarData(
					/*ID*/              1003,
					/*GRAPHIC ID*/      7,
					/*NAME*/            "JUDGE",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           13,
					/*ROTATION*/        7,
					/*DAMPING*/         .6,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   0
			),
			new CarData(
					/*ID*/              1004,
					/*GRAPHIC ID*/      9,
					/*NAME*/            "HAWK",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           14,
					/*ROTATION*/        8,
					/*DAMPING*/         .5,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   0
			),

			// TASKS CARS =============================================
			new CarData(
					/*ID*/              2000,
					/*GRAPHIC ID*/      10,
					/*NAME*/            "DAWN",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           11,
					/*ROTATION*/        7,
					/*DAMPING*/         .75,
					/*BODY_X_OFFSET*/   0,
					/*BODY_Y_OFFSET*/   -2,
					/*BODY_G_X_OFFSET*/ 0,
					/*BODY_G_Y_OFFSET*/ 0,
					/*UNLOCK_INFORMATION*/	CWorldNames.SHARP_MOUNTAIN.toUpperCase() + ' TASKS'
			),
			new CarData(
					/*ID*/              2001,
					/*GRAPHIC ID*/      11,
					/*NAME*/            "Drift",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           12,
					/*ROTATION*/        7.5,
					/*DAMPING*/         .65,
					/*BODY_X_OFFSET*/   -2,
					/*BODY_Y_OFFSET*/   -4,
					/*BODY_G_X_OFFSET*/ 0,
					/*BODY_G_Y_OFFSET*/ 0,
					/*UNLOCK_INFORMATION*/	CWorldNames.ICE_WORLD.toUpperCase() + ' TASKS'
			),
			new CarData(
					/*ID*/              2002,
					/*GRAPHIC ID*/      12,
					/*NAME*/            "Desert Rock",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           13,
					/*ROTATION*/        7,
					/*DAMPING*/         .6,
					/*BODY_X_OFFSET*/   -2,
					/*BODY_Y_OFFSET*/   -4,
					/*BODY_G_X_OFFSET*/ -2.5,
					/*BODY_G_Y_OFFSET*/ 0,
					/*UNLOCK_INFORMATION*/	CWorldNames.DESERT_VALLEY.toUpperCase() + ' TASKS'
			),
			new CarData(
					/*ID*/              2003,
					/*GRAPHIC ID*/      13,
					/*NAME*/            "MISSING CAR!!!!!",
					/*STAR_REQUIRED*/	0,
					/*SPEED*/           14,
					/*ROTATION*/        .5,
					/*DAMPING*/         .5,
					/*BODY_X_OFFSET*/   -2,
					/*BODY_Y_OFFSET*/   -4,
					/*BODY_G_X_OFFSET*/ -2.5,
					/*BODY_G_Y_OFFSET*/ 0,
					/*UNLOCK_INFORMATION*/	CWorldNames.CANDY_WORLD.toUpperCase() + ' TASKS'
			)
		];

		public static function getData( carType:uint ):CarData
		{
			for( var i:uint = 0; i < CAR_DATAS.length; i++ )
			{
				if( CAR_DATAS[ i ].id == carType )
				{
					return CAR_DATAS[ i ];
				}
			}
			return null;
		}
	}
}