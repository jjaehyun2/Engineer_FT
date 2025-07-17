package com.controls
{	
	import flash.display.Sprite;
	import flash.events.Event;
	
	import mx.controls.Alert;
	import mx.core.FlexGlobals;

	public class Alerter
	{
		public static function showException(soapEvent:Event, parent:Sprite = null, closeHandler:Function = null, defaultButtonFlag:uint = Alert.OK, iconClass:Class = null ):void
		{
			//AppModel.instance.isShowLoading = false;
			if(soapEvent.hasOwnProperty("data") && soapEvent["data"].hasOwnProperty("message") && soapEvent["data"].hasOwnProperty("title"))
			{
				Alert.show(soapEvent["data"].message, 
							soapEvent["data"].title, 
							defaultButtonFlag, 
							parent ? parent : FlexGlobals.topLevelApplication as Sprite, 
							closeHandler);
			}
		}
	}
}