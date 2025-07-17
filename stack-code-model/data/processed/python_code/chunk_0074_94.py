/**
 * @author gyb 20141121
 */
package as3lib.helper.load
{
	import as3lib.core.convert.toUrlVariables;
	
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.net.URLLoader;
	import flash.net.URLLoaderDataFormat;
	import flash.net.URLRequest;
	import flash.net.URLRequestMethod;
	


	/**
	 * 	URLLoader用来加载文本文件(xml,php,jsp)通常用来请求服务端数据.使用 URLLoader时需要等到整个文件下载完才能使用    
	 *  <br/>可以只想图片文件的地址，用二进制URLLoaderDataFormat.BINARY接收
	 */
	public class URLLoaderHelper
	{
		//================================================= 属性==============================================
		public static var Instance:URLLoaderHelper = new URLLoaderHelper();
		
		private var _urlRequest:URLRequest;
		private function get urlRequest():URLRequest
		{
			if(_urlRequest==null)
			{
				_urlRequest = new URLRequest();
			}
			return _urlRequest;
		}
		
		//================================================= 方法==============================================
		/**
		 * 功能：管理加载过程，防止缓存，并简化 URLLoader 复杂的调用方式。
		 */
		public function load(url:String, method:String = URLRequestMethod.POST, data:Object = null):URLLoader
		{
			return loading(url,method,data,URLLoaderDataFormat.TEXT);
		}
		/**
		 * 接收格式为：原始二进制数据（通常用来实例化图片）
		 */
		public function loadBinary(url:String, method:String = URLRequestMethod.POST, data:Object = null):URLLoader
		{
			return loading(url,method,data,URLLoaderDataFormat.BINARY);
		}
		/**
		 * 接收格式为： URL 编码变量形式
		 */
		public function loadVariables(url:String, method:String = URLRequestMethod.POST, data:Object = null):URLLoader
		{
			return loading(url,method,data,URLLoaderDataFormat.VARIABLES);
		}
		private function loading(url:String, method:String = URLRequestMethod.POST, data:Object = null , dataFormat:String = URLLoaderDataFormat.TEXT):URLLoader
		{
//			url += url.indexOf("?")!=-1 ? "&": "?" ;
			var urlLoader:URLLoader = new URLLoader();
			urlLoader.addEventListener(IOErrorEvent.IO_ERROR, onHttpError);
			urlRequest.method = method;
			urlRequest.url = url;
			if(data == null) data = new Object();
			data["requestDate"] = new Date().getTime();
			urlRequest.data = toUrlVariables(data);
			urlLoader.dataFormat = dataFormat;
			urlLoader.load(urlRequest);
			return urlLoader;
		}
		//================================================= 事件==============================================
		private function onHttpError(event:IOErrorEvent):void
		{
			var faultLoader:URLLoader = event.currentTarget as URLLoader;
			trace(event.text)
		}
	}
}