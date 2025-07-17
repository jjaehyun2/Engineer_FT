package com.adobe.dashboard.services
{
	import flash.utils.Proxy;
	import flash.utils.clearTimeout;
	import flash.utils.flash_proxy;
	import flash.utils.setTimeout;
	
	import mx.core.mx_internal;
	import mx.messaging.messages.HTTPRequestMessage;
	import mx.messaging.messages.IMessage;
	import mx.rpc.AsyncToken;
	import mx.rpc.Responder;
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	
	import spark.managers.IPersistenceManager;
	import spark.managers.PersistenceManager;

	/**
	 * cacheing system that uses PersistanceManager to store the result from data calls in SharedObjects
	 */
	dynamic public class CacheProxy extends Proxy
	{

		private var delegate:Object;

		private var persistenceManager:spark.managers.IPersistenceManager;

		public function CacheProxy(delegate:Object)
		{
			super();
			this.delegate = delegate
			persistenceManager = new spark.managers.PersistenceManager();
		}

		override flash_proxy function callProperty(methodName:*, ... args):*
		{
			try{
				var key:String = hashFunction(methodName.toString(), args);
				var cachedValue:CacheData = persistenceManager.getProperty(key) as CacheData;
				if (!cachedValue)
				{
					var returnValue:Object = delegate[methodName].apply(delegate, args);
					if (returnValue is AsyncToken)
					{
						var token:AsyncToken = returnValue as AsyncToken;
	
						var message:IMessage = new HTTPRequestMessage();
						var newToken:AsyncToken = new AsyncToken(message);
	
						token.addResponder(
							new Responder(
							function(event:ResultEvent):void
						{
							returnValue = event.result;
							var fakeEvent:ResultEvent = new ResultEvent(ResultEvent.RESULT, false, true, event.result, newToken, message);
							cachedValue = new CacheData(key, CacheData.CALL_TYPE_ASYNC, returnValue);
							persistenceManager.setProperty(key, cachedValue);
							fakeEvent.mx_internal::callTokenResponders();
						},
							function(event:FaultEvent):void
						{
							var fakeFaultEvent:FaultEvent = new FaultEvent(event.type, event.bubbles, event.cancelable, event.fault, newToken, event.message);
							fakeFaultEvent.mx_internal::callTokenResponders();
						}));
						return newToken;
					}
					else
					{
						cachedValue = new CacheData(key, CacheData.CALL_TYPE_SYNC, returnValue);
						persistenceManager.setProperty(key, cachedValue);
					}
				}
				if (cachedValue.callType == CacheData.CALL_TYPE_ASYNC)
				{
					return returnAsAsyncToken(cachedValue.value);
				}
				else
				{
					return cachedValue.value;
				}
			}catch(e:Error){
				//TODO: If t
			}

		}

		private function returnAsAsyncToken(result:Object):AsyncToken
		{
			var message:IMessage = new HTTPRequestMessage();
			var token:AsyncToken = new AsyncToken(message);


			var fakeEvent:ResultEvent = new ResultEvent(ResultEvent.RESULT, false, true, result, token, message);

			// Fake an async reponse
			var timeout:uint = setTimeout(function():void
			{
				clearTimeout(timeout);
				fakeEvent.mx_internal::callTokenResponders();
			}, 10);

			return token;
		}

		private function hashFunction(methodName:String, ... args):String
		{
			var key:String = methodName;
			for each (var o:* in args)
			{
				key += o.toString();
			}
			return key;
		}
	}

}


class CacheData
{

	public var callType:String

	public var key:String;

	public var value:Object;

	public static const CALL_TYPE_ASYNC:String = "ASYNC";

	public static const CALL_TYPE_SYNC:String = "SYNC";

	public function CacheData(k:String, t:String, v:Object)
	{
		this.key = k;
		this.callType = t;
		this.value = v;
	}
}