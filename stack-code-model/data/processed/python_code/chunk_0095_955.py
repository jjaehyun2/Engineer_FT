package
{
	import starling.errors.AbstractClassError;

	public class Constants
	{
		public static var  INDEX_SCREEN:String = "IndexScreen";
		
		public static const SKILLS:String = "Skills";
		public static const CELEBRATIONS:String = "Celebrations";
		public static const ACHIEVEMENTS:String = "Achievements";
		public static const VIDEOS:String = "Videos";
		public static const ABOUT:String = "About";
		
		public static const XBOX:String = "Xbox";
		public static const PLAYSTATION:String = "Playstation";
		
		public static var DB_NAME:String = "FIFA14.db";
		
		public function Constants() 
		{ 
			throw new AbstractClassError(); 
		}
	}
}