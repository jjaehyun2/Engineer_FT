package  
{
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class DataManager
	{
		public static var allyBullets:Vector.<Entity> = new Vector.<Entity>();
		public static var effects:Vector.<Entity> = new Vector.<Entity>();
		public static var children:Vector.<Child> = new Vector.<Child>();
		public static var mother:Mother
		
		public static var childTransferRate:int = 2;
		public static var childMaxAmmo:int = 30;
		public static var childForce:int = 2;
		public static var childLife:int = 100;
		public static var childShotSpeed:int = 10;
		
		
		public function DataManager() 
		{
			
		}
		
	}

}