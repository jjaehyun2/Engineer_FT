package com.yjacket.taskerTasker.util
{
	import mx.controls.Alert;
	import mx.events.CloseEvent;
	
	public class Confirm
	{	 
		public static function show(closeHandler:Function=null, message:String=null, title:String=null):void
		{
			Alert.show(
				message != null ? message : "Continue?"
				, title != null ? title : "CONFIRM"
				, 3
				, null
				, function(event:CloseEvent):void{
					if (event.detail == Alert.YES)
						if (closeHandler != null) closeHandler();	
				});
		}
	}
}