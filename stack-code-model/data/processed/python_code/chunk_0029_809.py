import com.GameInterface.DistributedValueBase;
import flash.geom.Point;
class com.fox.ResChanger 
{
	public static function main():Void
	{
		if (!DistributedValueBase.GetDValue("ResChanger_Loaded"))
		{
			var target:Array = DistributedValueBase.GetDefaultDValue("ResChanger_Resolution").split(",");
			var mode = Number(DistributedValueBase.GetDefaultDValue("ResChanger_DisplayMode"));
			var current:Point = DistributedValueBase.GetDValue("DisplayResolution");
			if (current.x != Number(target[0]))
			{
				DistributedValueBase.SetDValue("DisplayResolution", new Point(Number(target[0]), Number(target[1])));
			}
			if (mode != DistributedValueBase.GetDValue("DisplayMode"))
			{
				DistributedValueBase.SetDValue("DisplayMode", mode);
			}
			DistributedValueBase.AddVariable("ResChanger_Loaded", true);
		}
	}
}