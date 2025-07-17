/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Enum
{
	import de.p3337.zzznake.Util.CStringUtils;
	
	/**
	 * This class provides a list of all available sound files that can be passed to the Jukebox:
	 * THEME, GAME_OVER, or CRUNCH_FOOD.
	 */
	public class SoundFile {
		
		public var Text:String;
		{CStringUtils.InitEnumConstants(SoundFile);} // static ctor
		
		public static const THEME:SoundFile = new SoundFile();
		public static const GAME_OVER:SoundFile = new SoundFile();
		public static const CRUNCH_FOOD:SoundFile = new SoundFile();
	}
}