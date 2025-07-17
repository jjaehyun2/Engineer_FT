package application.utils{

	import flash.display.Loader;
	import flash.display.Stage;
	import flash.events.Event;

	import flash.events.IOErrorEvent;
	import flash.display.MovieClip;
	
	import flash.net.URLLoader;
	import flash.net.URLVariables;
	import flash.net.URLRequestMethod;
	import flash.net.URLRequest;
	import flash.system.LoaderContext;
	
	import flash.system.Security;
	import flash.system.LoaderContext;
	import flash.events.HTTPStatusEvent;
	import flash.events.ProgressEvent;
	import flash.events.IEventDispatcher;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.SecurityErrorEvent;



	public class SendAndLoadData extends MovieClip {
		
		private var $loader:URLLoader;

		public function SendAndLoadData(dis:Boolean = true) {

			
		}

		
		public function initUser(url:String, object:Object, method = 'get'):void {
			
			if (!object || !url) return;
			
			var $value:URLVariables = new URLVariables;
			
			for (var prop:String in object) { 
				$value[prop] = object[prop];
				//trace(prop + ' = ' + object[prop])
				//$root.debugTxt.text += String(prop + ' = ' + object[prop]);
	
			}

			
			if ($loader) {
				
				try {
					 $loader.close();
				} catch (error:Error) {
					//throw new Error("Error load Valid XML: "+error);
				}
				
				configureRemoveListeners($loader);
				$loader = null;
			}
			
			
			$loader = new URLLoader();
			configureListeners($loader);
			
			var request:URLRequest = new URLRequest(url);//firstUserInfo
			request.data = $value;
			request.method = method == 'get'? URLRequestMethod.GET : URLRequestMethod.POST;
			
		//	trace(url);
			
			
			try {
				$loader.load(request);
				
			} catch (error:Error) {
				
				throw new Error("Error load Valid XML: " + error);
				//dispatchEvent(new AppEvent(AppEvent.XML_LOADED_ERROR, null ,true));
			}
			

		}
		
		
		private function configureRemoveListeners(dispatcher:IEventDispatcher):void {
			dispatcher.removeEventListener(Event.COMPLETE, onXmlComplete);
            dispatcher.removeEventListener(Event.OPEN, onXMLOpenHandler);
            dispatcher.removeEventListener(ProgressEvent.PROGRESS, onXMLOprogressHandler);
            dispatcher.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, onXMLSecurityErrorHandler);
            dispatcher.removeEventListener(HTTPStatusEvent.HTTP_STATUS, onXMLHttpStatusHandler);
            dispatcher.removeEventListener(IOErrorEvent.IO_ERROR, onXMLIoErrorHandler);
		}
		
		private function configureListeners(dispatcher:IEventDispatcher):void {
            dispatcher.addEventListener(Event.COMPLETE, onXmlComplete);
            dispatcher.addEventListener(Event.OPEN, onXMLOpenHandler);
            dispatcher.addEventListener(ProgressEvent.PROGRESS, onXMLOprogressHandler);
            dispatcher.addEventListener(SecurityErrorEvent.SECURITY_ERROR, onXMLSecurityErrorHandler);
            dispatcher.addEventListener(HTTPStatusEvent.HTTP_STATUS, onXMLHttpStatusHandler);
            dispatcher.addEventListener(IOErrorEvent.IO_ERROR, onXMLIoErrorHandler);
        }
		
		private function onXMLOpenHandler(event:Event):void {
           // trace("openHandler: " + event);

        }

        private function onXMLOprogressHandler(event:ProgressEvent):void {
           //race("progressHandler loaded:" + event.bytesLoaded + " total: " + event.bytesTotal);
			
        }

        private function onXMLSecurityErrorHandler(event:SecurityErrorEvent):void {
          // MainSettings.instance.container.debTxt.text += 'ERROR SecurityErrorEvent MUI: '+event+' \n';
		  
			
        }

        private function onXMLHttpStatusHandler(event:HTTPStatusEvent):void {
          
			//MainSettings.instance.container.debTxt.text += 'ERROR HTTPStatusEvent MUI: '+event+' \n';
        }

		
		private function onXMLIoErrorHandler(e:IOErrorEvent):void {
			//throw new Error("Has problem loading the XML File: " + e);
			//dispatchEvent(new AppEvent(AppEvent.XML_LOADED_ERROR, null ,true));
			//MainSettings.instance.container.loaderDebugTxt.appendText('\n "Has problem loading the XML File: ' + e);
           //trace("Has problem loading the XML File."+e);
        }
		
		
		private function onXmlComplete(e:Event):void {
			
			//trace('FROM SERVER: '+e.target.data);
			
			try {
				
				//$loadedXMLContent = XML(e.target.data);
				
				
				var $data:Object = new Object;
				$data.data = String(e.target.data);

				dispatchEvent(new AppEvent(AppEvent.XML_LOADED, $data , false));
				
				
				if ($loader) {
				
					try {
						 $loader.close();
					} catch (error:Error) {
						//throw new Error("Error load Valid XML: "+error);
					}
					
					configureRemoveListeners($loader);
					$loader = null;
				}


			} catch (error:TypeError) {
				
				trace('XMP PARCE ERROR: '+error);

			}
		}

	}

}