package com.ats.device.running.android
{
	import flash.events.Event;
	
	public class AdbProcessEvent extends Event
	{
		public static const ADB_PROGRESS:String = "adbProgress";
		public static const ADB_ERROR:String = "adbError";
		public static const ADB_EXIT:String = "adbExit";
		
		public var error:String;
		public var output:String;
		public var stackedOutput:Array;
		
		public function AdbProcessEvent(type:String, error:String, output:String=null, outputFinal:String=null)
		{
			if(error != null && error.length > 0){
				this.error = error;
			}
			this.output = output;
			if(outputFinal != null){
				stackedOutput = outputFinal.split("\n");
			}
			super(type, false, false);
		}
	}
}