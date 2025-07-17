/*
* Copyright (c) 2011 Vyper Logix Corp., All Rights Reserved.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
* OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
* NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
* HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
* WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
* OTHER DEALINGS IN THE SOFTWARE.
*/
package com.vyperlogix {
    import com.DebuggerUtils;
    import com.ObjectUtils;
    import com.adobe.serialization.json.JSON;
    import com.adobe.serialization.json.JSONDecoder;
    
    import flash.events.ErrorEvent;
    import flash.events.Event;
    import flash.events.EventDispatcher;
    import flash.events.IOErrorEvent;
    import flash.events.SecurityErrorEvent;
    import flash.events.TimerEvent;
    import flash.net.URLLoader;
    import flash.net.URLRequest;
    import flash.net.URLRequestHeader;
    import flash.net.URLRequestMethod;
    import flash.net.URLVariables;
    import flash.utils.Timer;
    
    import mx.utils.Base64Encoder;
    
    [Event(name="complete",type="flash.events.Event")]
    [Event(name="error",type="flash.events.ErrorEvent")]
    
    /**
     * Operation class which performs URL request for API calls.
     */
    public class GoogleCloudOperation extends EventDispatcher {
        private var _data:Object;
        private var _loader:URLLoader;
        private var _tim:Timer;
		
		public static var _timeout:Number = -1;
		
		private static const gae_domain_name:String = '.appspot.com';
        
        /**
         * The URL of the request.
         */
        public var url:String;
		
		/**
		 * The air_id for the request.
		 */
		public var air_id:String;

		/**
		 * The sub_domain for the request.
		 */
		public var sub_domain:String;
        
        /**
         * The params to pass along in the URL request.
         */
        public var params:Object;
        
        /**
         * HTTP method for sending the request. Permitted values are
         * GET and POST.
         * 
         * @default <code>URLRequestMethod.GET</code>
         */
        public var method:String = URLRequestMethod.GET;
        
        /**
         * Request timeout in seconds. Value of -1 indicates no timeout.
         * 
         * @default -1
         */
        public var timeout:Number = _timeout;
        
		/**
		 * The request format. <code>GoogleCloudRequestFormat.XML</code> or <code>GoogleCloudRequestFormat.JSON</code>.
		 * 
		 * @default <code>GoogleCloudRequestFormat.JSON</code>
		 */
		public var format:String = GoogleCloudRequestFormat.JSON;
		
		/**
		 * Is the operation returning JSON ?.
		 */
		public function get is_format_json():Boolean {
			return (this.format == GoogleCloudRequestFormat.JSON);
		}
		
        /**
         * The data loaded from the URL request.
         */
        public function get data():* {
            return _data;
        }
        
        /**
         * Constructor
         */
        public function GoogleCloudOperation(url:String, params:Object = null, air_id:String=null, sub_domain:String=null) {
			this.params = params;
			this.sub_domain = sub_domain;
			this.air_id = air_id;
			var toks:Array = url.split('/');
			if (this.sub_domain is String) {
				if (toks[toks.length-1].length == 0) {
					toks.splice(toks.length-1,0,this.sub_domain);
				} else {
					toks.push(this.sub_domain);
				}
			}
			if (this.air_id is String) {
				if (toks[toks.length-1].length == 0) {
					toks.splice(toks.length-1,0,this.air_id);
				} else {
					toks.push(this.air_id);
				}
			}
			this.url = toks.join('/');
        }
        
        /**
         * Initiates the operation.
         */
        public function execute(username:String=null, password:String=null):void {
            var request:URLRequest = new URLRequest(this.url);
            request.method = this.method;
            
            var isVarsEmpty:Boolean = true;
            var vars:URLVariables;
            if (this.params) {
				var keys:Array;
				var datum:*;
                vars = new URLVariables();
                for (var prop:String in this.params) {
                    if (this.params[prop] != "" && this.params[prop] != null) {
                    	isVarsEmpty = false;
						datum = this.params[prop];
						keys = ObjectUtils.keys(datum);
						if (keys.length == 0) {
							vars[prop] = datum;
						} else {
							vars[prop] = JSON.encode(datum);
						}
                    }
                }
                request.data = vars;
            }
            
            if (request.method == URLRequestMethod.POST && isVarsEmpty) {
                vars = new URLVariables();
                vars.dummy = "";
                request.data = vars;
            }

			//trace(DebuggerUtils.getFunctionName(new Error())+'.1 --> url='+this.url);
			//trace(DebuggerUtils.getFunctionName(new Error())+'.2 --> request.data='+DebuggerUtils.explainThis(request.data));
			
			if ( (username is String) && (password is String) ) {
				var encoder:Base64Encoder = new Base64Encoder();
				encoder.encode(username+":"+password);
				var credsHeader:URLRequestHeader = new URLRequestHeader("Authorization", "Basic " + encoder.toString());
				request.requestHeaders.push(credsHeader);
			}
			
            _loader = new URLLoader();
            _loader.addEventListener(Event.COMPLETE, handleLoaderComplete);
            _loader.addEventListener(IOErrorEvent.IO_ERROR, handleLoaderError);
            _loader.addEventListener(SecurityErrorEvent.SECURITY_ERROR, handleLoaderError);
            _loader.load(request);
            
            if (timeout && timeout != -1) {
                _tim = new Timer(timeout * 1000, 1);
                _tim.addEventListener(TimerEvent.TIMER_COMPLETE, handleTimeout);
                _tim.start();
            }
        }
        
        /**
         * Handles a timeout.
         */
        private function handleTimeout(event:TimerEvent):void {
            _loader.close();
            handleError(new ErrorEvent(ErrorEvent.ERROR, false, false, "Request timed out. URL requested: " + url));
        }
        
        /**
         * @private
         */
        private function handleLoaderError(event:ErrorEvent):void {
            stopTimer();
            removeLoaderEventListeners();
			var data:String = event.currentTarget.data;
			var json:Object = null;
			var keys:Array;
			try {
				json = JSON.decode(data);
				keys = ObjectUtils.keys(json);
			} catch (err:Error) {}
            handleError(new ErrorEvent(ErrorEvent.ERROR, false, false, (json && (keys is Array) && (keys.length > 0)) ? json[keys[0]] : event.text));
        }
        
        /**
         * Handles the result of the loader.
         */
        private function handleLoaderComplete(event:Event):void {
            stopTimer();
			try {_data = (this.is_format_json) ? JSON.decode(_loader.data) : _loader.data;} 
			catch (err:Error) {_data = _loader.data;}
            removeLoaderEventListeners();
            handleComplete(event);
        }
        
        /**
         * @private
         */
        private function removeLoaderEventListeners():void {
            _loader.removeEventListener(Event.COMPLETE, handleLoaderComplete);
            _loader.removeEventListener(IOErrorEvent.IO_ERROR, handleLoaderError);
            _loader.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, handleLoaderError);
        }
        
        /**
         * @private
         */
        private function stopTimer():void {
            if (_tim) {
                _tim.stop();
            }
        }
        
        /**
         * @private
         */
        protected function handleError(event:Event):void {
            if (event is ErrorEvent) {
                dispatchEvent(event);
            } else {
                dispatchEvent(new ErrorEvent(ErrorEvent.ERROR));
            }
        }
        
        /**
         * @private
         */
        protected function handleComplete(event:Event):void {
            dispatchEvent(new Event(Event.COMPLETE));
        }
    }
}