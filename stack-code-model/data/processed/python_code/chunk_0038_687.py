package com.playtika.samples.loadup.model
{

	import org.puremvc.as3.multicore.interfaces.IProxy;
	import org.puremvc.as3.multicore.patterns.proxy.Proxy;
	import org.puremvc.as3.multicore.utilities.loadup.model.LoadupResourceProxy;


	public class EntityProxy extends Proxy implements IProxy
	{
		public function EntityProxy(name:String)
		{
			super(name);
		}

		protected function sendLoadedNotification(noteName:String, noteBody:String, srName:String):void
		{
			var srProxy:LoadupResourceProxy = facade.retrieveProxy(srName) as LoadupResourceProxy;
			if (!srProxy.isTimedOut())
			{
				sendNotification(noteName, noteBody);
			}
		}

	}
}