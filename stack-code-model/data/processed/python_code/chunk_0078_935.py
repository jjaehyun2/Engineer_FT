package  
{
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Module 
	{
		public static var attractorUpgrade:int = 0;
		public static var recyclingUpgrade:int = 0;
		public static var cooldownUpgrade:int = 0;
		public static var enginesUpgrade:int = 0;
		public static var gunnersUpgrade:int = 0;
		public static var detonatorUpgrade:int = 0;
		
		public static var attractorDesc:String = "A strong field pulls in Drops toward you.";
		public static var recyclingDesc:String = "Recycling broken parts means more Drops.";
		public static var cooldownDesc:String = "With a gun that over heats less, you can fire many more bullets.";
		public static var enginesDesc:String = "Ramping up the engines will propel you faster.";
		public static var gunnersDesc:String = "There is never enough guns. Why not get another?";
		public static var detonatorDesc:String = "Too much to handle? Activate the Detonator by pressing the Spacebar.";
		
		public static var attractorPriceDelta:Array = [200,400,800,1600,3200, "MAXED"];
		public static var recyclingPriceDelta:Array = [200,300,400,500,600, "MAXED"];
		public static var cooldownPriceDelta:Array = [50,250,500,750,1250, "MAXED"];
		public static var enginesPriceDelta:Array = [20,120,300,500,700, "MAXED"];
		public static var gunnersPriceDelta:Array = [1000,2000,3000,4000,5000, "MAXED"];
		public static var detonatorPriceDelta:Array = [200, 1000, 2000, 4000, 6000, "MAXED"];
		
		
		
		public static var dropsCollected:int = 999;
		
		public function Module() 
		{
			
		}
		
		
		public static function canPurchase(box:UpgradeBox):Boolean
		{
			var priceOfPurchase:int = Module[box.name + "PriceDelta"][Module[box.name + "Upgrade"]];
			if (Module[box.name + "Upgrade"] < 5 && priceOfPurchase < dropsCollected) return true;
			return false;
		}
		
		public static function purchase(box:UpgradeBox):void
		{
			var priceOfPurchase:int = Module[box.name + "PriceDelta"][Module[box.name + "Upgrade"]];
			dropsCollected -= priceOfPurchase;
			
			box.gotoAndStop(box.currentFrame + 1);
			Module[box.name + "Upgrade"]++;
		}
		
		
		public static function getDescription(box:UpgradeBox):String
		{
			return "\n\n" + Module[box.name + "Desc"] + "\n\n" + "Price: " + Module[box.name + "PriceDelta"][Module[box.name + "Upgrade"]];
		}
	}

}