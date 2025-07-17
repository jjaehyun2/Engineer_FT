package utils.debug 
{
	import DebugSettings;

	public class Debugger 
	{
		
		static public function log(msg:String,id:String,addLocation:Boolean = false):void
		{
			if(!hasId(id)) return;
									
			trace(msg);
		}
		
		static private function hasId(id:String):Boolean
		{
			return DebugSettings.INTERESTS.indexOf(id) > -1;
		}		

	}
}