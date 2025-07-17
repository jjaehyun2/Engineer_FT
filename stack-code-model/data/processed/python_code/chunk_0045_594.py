import com.GameInterface.UtilsBase;
/**
 * ...
 * @author Chosen-Wan
 */
class com.chosen.mobradar.Utils
{
	private function Utils() {}
	
	public static function Log(msg:Object)
	{
		UtilsBase.PrintChatText("<font color=#FFFF00>Mob Radar</font>: " + msg);
	}
}