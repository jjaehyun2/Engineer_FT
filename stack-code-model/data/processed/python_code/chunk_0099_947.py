/**
 * RedBox internal logger.
 * 
 * @author	The gotoAndPlay() Team
 * 			{@link http://www.smartfoxserver.com}
 * 			{@link http://www.gotoandplay.it}
 * 
 * @exclude
 */
class com.smartfoxserver.redbox.utils.Logger
{
	public static var enableLog:Boolean = false
	
	public static function log():Void
	{
		if (enableLog)
			trace("[RedBox]" + arguments.join(" "))
	}
}