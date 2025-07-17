package danmaq.mmga.data.reader
{
	import danmaq.mmga.data.CStaticPreference;
	import danmaq.nineball.core.events.CDisposableEventDispatcher;
	
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.http.HTTPService;

	public final class CWebClient extends CDisposableEventDispatcher implements IClient
	{
		
		//* constants ──────────────────────────────-*
		
		/** HTTPクライアント。 */
		private const service:HTTPService = new HTTPService();
		
		//* constructor & destructor ───────────────────────*
		
		/**
		 * コンストラクタ。
		 */
		public function CWebClient()
		{
			super(service);
			service.rootURL = CStaticPreference.instance.url;
			service.headers["Accept"] =
				"application/json, text/plain;q=0.9, */*;q=0.1";
			service.resultFormat = "text";
			service.addEventListener(ResultEvent.RESULT, onResult);
		}
		
		private function onResult(event:ResultEvent):void
		{
			dispatchEvent(event);
		}
		
		public function call(url:String, params:Object):void
		{
			service.url = url;
			service.send(params);
		}
	}
}