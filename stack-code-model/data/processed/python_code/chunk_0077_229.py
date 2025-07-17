package com {
	import com.adobe.serialization.json.JSON;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.http.mxml.HTTPService;
	import mx.utils.ArrayUtil;
	
	import controls.Alert.AlertPopUp;

	public class EzHTTPService {
		public var srvc:HTTPService = new HTTPService;
		public var requestObj:Object = new Object;

		public var isDebugMode:Boolean = false;

		public var isRunningLocal:Boolean = true;
		
		public var userID:String = "";

		private var __concurrency__:String = CONCURRENCY_MULTIPLE;
		
		public const arrayResultType:String = "array";
		public const objectResultType:String = "object";
		public const xmlResultType:String = "xml";
		public const e4xResultType:String = "e4x";
		public const flashvarsResultType:String = "flashvars";
		public const textResultType:String = "text";

		public var allowedResultTypes:Array = [];
		
		public const jsonResultType:String = "json";
		public var specialResultTypes:Array = [];

		public const DEBUG_MODE_ON:Boolean = true;
		public const DEBUG_MODE_OFF:Boolean = false;
		
		public const RUNNING_LOCAL:Boolean = true;
		public const RUNNING_REMOTE:Boolean = false;
		
		public const CONCURRENCY_MULTIPLE:String = 'multiple';
		public const CONCURRENCY_SINGLE:String = 'single';
		public const CONCURRENCY_LAST:String = 'last';
		
		public const CONTENT_TYPE_JSON:String = 'application/json';
		
		private var __alertShowFunc__:Function;

		private var __faultCallBack__:Function;

		private var __fault_count__:uint = 0;
		
		private var __showBusyCursor__:Boolean = false;
		
		private var __errorHandler__:Function;
		
		private var __contentType__:String;

		private var callback:Function;
		
		private var resultFormats:Array = [];
		
		public function get showBusyCursor():Boolean {
			return this.__showBusyCursor__;
		}
		
		public function set showBusyCursor(value:Boolean):void {
			if (this.__showBusyCursor__ != value) {
				this.__showBusyCursor__ = value;
			}
		}
		
		public function get contentType():String {
			return this.__contentType__;
		}
		
		public function set contentType(contentType:String):void {
			if (this.__contentType__ != contentType) {
				this.__contentType__ = contentType;
			}
		}
		
		public function get is_content_type_json():Boolean {
			return (this.contentType == this.CONTENT_TYPE_JSON);
		}
		
		public function get faultCallBack():Function {
			return this.__faultCallBack__;
		}
		
		public function set faultCallBack(faultCallBack:Function):void {
			if (this.__faultCallBack__ != faultCallBack) {
				this.__faultCallBack__ = faultCallBack;
			}
		}
		
		public function get alertShowFunc():Function {
			return this.__alertShowFunc__;
		}
		
		public function set alertShowFunc(alertShowFunc:Function):void {
			if (this.__alertShowFunc__ != alertShowFunc) {
				this.__alertShowFunc__ = alertShowFunc;
			}
		}
		
		public function get errorHandler():Function {
			return this.__errorHandler__;
		}
		
		public function set errorHandler(errorHandler:Function):void {
			if (this.__errorHandler__ != errorHandler) {
				this.__errorHandler__ = errorHandler;
			}
		}
		
		public function get concurrency():String {
			return this.__concurrency__;
		}
		
		public function set concurrency(concurrency:String):void {
			if (this.__concurrency__ != concurrency) {
				if ( (concurrency == CONCURRENCY_SINGLE) || (concurrency == CONCURRENCY_MULTIPLE) || (concurrency == CONCURRENCY_LAST) ) {
					this.__concurrency__ = concurrency;
				}
			}
		}

		public function get fault_count():uint {
			return this.__fault_count__;
		}
		
		public function makeIntoArrayCollection(obj:*):ArrayCollection {
			var ar:Array = new Array;
			if (obj != null) {
				if (obj is Array) {
					ar = obj;
				} else if (obj is ArrayCollection) {
					ar = obj.source;
				} else {
					ar = mx.utils.ArrayUtil.toArray(obj);
				}
			}
			return new ArrayCollection(ar);
		}
		
		public function makeEventResultIntoArrayCollection(event:ResultEvent):ArrayCollection {
			return makeIntoArrayCollection(event.result.source);
		}
		
		public function htmlForAspConversion(inStr:String = ""):String {
			var patLT:RegExp = /\</g;
			var patGT:RegExp = /\>/g;
			return inStr.replace(patLT,"&lt;").replace(patGT,"&gt;");
		}
		
		public function myCallback(event:*):void { // NOTE - event data type here is "*" to allow soft errors to be redirected into the incoming data stream...
			this.__fault_count__ = 0;
			var ac:ArrayCollection = event.result as ArrayCollection;
			try {
				for (var i:int = 0; i < ac.length; i++) {
					trace(DebuggerUtils.getFunctionName(new Error())+'.1 --> content='+ac.source[i]);
					ac.source[i] = com.adobe.serialization.json.JSON.decode(StringUtils.json(ac.source[i]));
				}
			} catch (err:Error) {} // ignore the errors from this - soft complaints all.
			this.callback(event);
		}

		public function onFaultHandler(event:FaultEvent):void {
			var reason:String = event.toString();
			AlertPopUp.errorNoOkay('Reason:\n\n'+reason,'WARNING ('+this.srvc.url+')');
		}
		
		private function myFaultCallback(event:FaultEvent):void {
			this.__fault_count__++;
			if (this.faultCallBack is Function) {
				this.faultCallBack(event);
			} else {
				this.onFaultHandler(event);
			}
		}
		
		public function EzHTTPService(_isDebugMode:Boolean = this.DEBUG_MODE_OFF, _isRunningLocal:Boolean = this.RUNNING_LOCAL):void {
			this.isDebugMode = _isDebugMode;
			this.isRunningLocal = _isRunningLocal;
			// BEGIN:  DO NOT PLACE A MIME TYPE HERE OR BAD EVIL THINGS CAN HAPPEN...
			//this.srvc.contentType = 'application/json'; // remember to set the request headers... DUH !!!
			// END!    DO NOT PLACE A MIME TYPE HERE OR BAD EVIL THINGS CAN HAPPEN...
			this.srvc.addEventListener(ResultEvent.RESULT, this.myCallback);
			this.srvc.addEventListener(FaultEvent.FAULT, this.myFaultCallback);
			this.allowedResultTypes.push(this.arrayResultType);
			this.allowedResultTypes.push(this.objectResultType);
			this.allowedResultTypes.push(this.xmlResultType);
			this.allowedResultTypes.push(this.e4xResultType);
			this.allowedResultTypes.push(this.flashvarsResultType);
			this.allowedResultTypes.push(this.textResultType);
			this.specialResultTypes.push(this.jsonResultType);
		}
		
		private function __invokeHTTPService(url:String, method:String, data:*, callback:Function, resultFormat:String):void {
			var title:String = "";
			var msg:String = "";
			this.srvc.showBusyCursor = this.showBusyCursor;
			this.srvc.url = url;
			this.srvc.useProxy = false;
			try {
				this.srvc.resultFormat = ((resultFormat is String) ? resultFormat : this.arrayResultType);
			} catch (e:Error) {
				this.srvc.resultFormat = 'array';
			}
			this.srvc.method = (method != null) ? method : "POST";
			this.callback = callback;
			this.srvc.concurrency = this.__concurrency__; // "multiple|single|last"
			if (this.is_content_type_json) {
				this.srvc.contentType = this.__contentType__;
				this.srvc.headers = { Accept: this.contentType };
			}
			this.srvc.makeObjectsBindable = true;
			if (method == 'POST') {
				this.srvc.request = this.requestObj;
				if (this.requestObj != null) {
					if (this.isDebugMode) {
						this.srvc.request.debugMode = "1";
					}
					this.srvc.request.runningLocal = (this.isRunningLocal) ? "1" : "0";
					if ( (this.userID is String) && (this.userID.length > 0) ) {
						this.srvc.request.userid = this.userID;
					}
					var i:String;
					if (data) {
						if (!this.is_content_type_json) {
							try {
								for (i in data) {
									this.srvc.request[i] = data[i];
								}
							} catch (err:Error) {}
						}
					}
				}
			}
			try {
				if (this.is_content_type_json) {
					var json:String = com.adobe.serialization.json.JSON.encode(data);
					this.srvc.request = json;
					this.srvc.send();
				} else {
					this.srvc.send();
				}
			} catch (err:Error) {
				if (this.errorHandler is Function) {
					this.errorHandler(err);
				} else {
					title = "Error :: invokeHTTPService()";
					msg = err.toString();
					if (this.alertShowFunc is Function) {
						this.alertShowFunc(msg, title);
					} else {
						mx.controls.Alert.show(msg, title);
					}
				}
			}
		}
		
		private function invokeHTTPService(url:String, data:*, callback:Function, resultFormat:String):void {
			return this.__invokeHTTPService(url, 'POST', data, callback, resultFormat);
		}

		public function post(url:String, data:*, callback:Function, resultFormat:String):void {
			var toks:Array = ((resultFormat is String) ? resultFormat : this.arrayResultType).split('|');
			toks.forEach(function (element:*, index:int, arr:Array):void{ arr[index] = StringUtils.trim(element as String); });
			if (toks.indexOf(this.arrayResultType) == -1) {
				toks.push(this.arrayResultType);
			}
			this.resultFormats = toks;
			var toks2:ArrayCollection = new ArrayCollection();
			ArrayCollectionUtils.appendAllInto(toks2,toks);
			for (var i:int = toks2.length-1; i >= 0; i--) {
				if (this.allowedResultTypes.indexOf(toks2[i]) == -1) {
					toks2.removeItemAt(i);
				}
			}
			resultFormat = toks2.source.join('');
			this.invokeHTTPService(url, data, callback, resultFormat);
		}
		
		public function send(url:String, callback:Function, resultFormat:String):void {
			return this.post(url,{},callback,((resultFormat is String) ? resultFormat : this.arrayResultType));
		}
		
		private function __send__(url:String, callback:Function, resultFormat:String):void {
			return this.__invokeHTTPService(url, 'GET', null, callback, resultFormat);
		}
		
		public function get(url:String, callback:Function, resultFormat:String):void {
			return this.__send__(url,callback,((resultFormat is String) ? resultFormat : this.arrayResultType));
		}
		
	}
}