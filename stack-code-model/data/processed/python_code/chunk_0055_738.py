package com.pushwoosh.nativeExtensions
{
	import flash.display.BitmapData;
	import flash.events.EventDispatcher;
	import flash.events.StatusEvent;
	import flash.external.ExtensionContext;
	import flash.system.Capabilities;
    import flash.desktop.NativeApplication;
    import flash.events.Event;
    import flash.events.InvokeEvent;
	
    public class PushNotification extends EventDispatcher 
	{  
		private static var extCtx:ExtensionContext = null;
        
        private static var _instance:PushNotification;
		
        public function PushNotification()
		{
			if (!_instance)
			{
				if (this.isPushNotificationSupported)
				{
					
					extCtx = ExtensionContext.createExtensionContext("com.pushwoosh.PushNotification", null);
				
					if (extCtx != null)
					{
						extCtx.addEventListener(StatusEvent.STATUS, onStatus);
						
						var app:NativeApplication = NativeApplication.nativeApplication;
						app.addEventListener(Event.ACTIVATE, onActivate);
						app.addEventListener(Event.DEACTIVATE, onDeactivate);
					}
					else
					{
						trace('extCtx is null.');
					}
				}
				_instance = this;
			}
			else
			{
				throw Error( 'This is a singleton, use getInstance, do not call the constructor directly');
			}
		}
		
        private function onActivate(event:Event):void {
                extCtx.call("resume");
        }

        private function onDeactivate(event:Event):void {
                extCtx.call("pause");
        }
		
		public function scheduleLocalNotification(seconds:int, alertJson:String):void
		{
			extCtx.call("scheduleLocalNotification", seconds, alertJson);
		}

		public function clearLocalNotifications():void
		{
			extCtx.call("clearLocalNotifications");
		}

		public function get isPushNotificationSupported():Boolean
		{
			//TODO: we actually support Amazon pushes!
			var result:Boolean = (Capabilities.manufacturer.search('iOS') > -1 || Capabilities.manufacturer.search('Android') > -1);
			return result;
		}
		
		public static function getInstance() : PushNotification
		{
			return _instance ? _instance : new PushNotification();
		}
	
		public function registerForPushNotification() : void
		{
			if (this.isPushNotificationSupported)
			{
				extCtx.call("registerPush");
			}
		}
		
		public function setBadgeNumberValue(value:int):void
		{
			if (this.isPushNotificationSupported)
			{
				extCtx.call("setBadgeNumber", value);
			}
		}

		// Starts location tracking.
 		public function startGeoPushes():void
		{
			if (this.isPushNotificationSupported)
			{
				extCtx.call("startGeoPushes");
			}
		}

		public function stopGeoPushes():void
		{
			if (this.isPushNotificationSupported)
			{
				extCtx.call("stopGeoPushes");
			}
		}

		public function setIntTag(name:String, value:int):void
		{
			if (this.isPushNotificationSupported)
			{
				extCtx.call("setIntTag", name, value);
			}
		}

		public function setStringTag(name:String, value:String):void
		{
			if (this.isPushNotificationSupported)
			{
				extCtx.call("setStringTag", name, value);
			}
		}

		public function unregisterFromPushNotification():void
		{
			if (this.isPushNotificationSupported)
			{
				extCtx.call("unregisterPush");
			}
		}
		
        // onStatus()
        // Event handler for the event that the native implementation dispatches.
        //
        private function onStatus(e:StatusEvent):void 
		{
			if (this.isPushNotificationSupported)
			{
				var event : PushNotificationEvent;
				var data:String = e.level;
				switch (e.code)
				{
					case "TOKEN_SUCCESS":
						event = new PushNotificationEvent( PushNotificationEvent.PERMISSION_GIVEN_WITH_TOKEN_EVENT );
						event.token = e.level;
						break;
					case "TOKEN_FAIL":
						event = new PushNotificationEvent( PushNotificationEvent.PERMISSION_REFUSED_EVENT );
						event.errorCode = "NativeCodeError";
						event.errorMessage = e.level;
						break;
					case "PUSH_RECEIVED":
						event = new PushNotificationEvent( PushNotificationEvent.PUSH_NOTIFICATION_RECEIVED_EVENT );
						if (data != null)
						{
							try
							{
								event.parameters = JSON.parse(data);
							} catch (error:Error)
							{
								trace("[PushNotification Error]", "cannot parse the params string", data);
							}
						}
						break;
					case "LOGGING":
						trace(e, e.level);
						break;
				}
				
				if (event != null)
				{
					this.dispatchEvent( event );
				}				
			}
		}
		
	}
}