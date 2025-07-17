package starling.utils
{
	import starling.display.DisplayObject;

	import com.assukar.airong.reflection.ReflectionUtils;
	/**
	 * @author Assukar
	 */
	public class TreeUtils
	{
		static public function dump(dob: DisplayObject, header: String = ""): String
		{
			if (ReflectionUtils.getClassName(dob) == "StarlingSprite") return "";
			else return header + ReflectionUtils.getClassName(dob) + ":" + dob + 
				(dob.parent?"\n" + dump(dob.parent, header+"."):"");
		}
	}
}