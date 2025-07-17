/**
 * @author gyb
 * @date 20140701
 */
package as3lib.helper.load
{
	import as3lib.core.convert.toUrlVariables;
	
	import flash.display.Loader;
	import flash.display.LoaderInfo;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.net.URLRequest;
	import flash.net.URLRequestMethod;

	/**
	 *	Loader是用来代替原来MovieClip的loadMovie功能，用于加载外部的图片文件，SWF文件。<br/>
	 *	如果加载图片文件（jpg，gif，png等）时，Loader.content得到数据类型是Bitmap对象<br/>
	 *  如果加载SWF文件（flash 9 版本）时，Loader.content得到数据类型是MovieClip对象<br/>
	 *	如果加载SWF文件（flash 9 以前版本）时，Loader.content得到数据类型是AVM1Movie对象<br/>
	 *  在使用Loader来加载数据时，添加侦听事件时，注意一定要给Loader的 contentLoaderInfo属性增加事件，而不是给Loader对象增加事件。
	 */
	public  class LoaderHelper
	{
		//================================================= 属性==============================================
		public static var Instance:LoaderHelper = new LoaderHelper();
		
		private var _loaderMap:Object;
		private function get loaderMap():Object
		{
			if(_loaderMap==null)
			{
				_loaderMap = new Object();
			}
			return _loaderMap;
		}
		
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
		 * 功能：管理加载过程，进行同一时间加载同一个文件（图片或swf）时性能优化,并简化 Loader 复杂的调用方式。
		 * 注：flex是逐帧执行的程序。事件触发究其根本也不是异步的。
		 **/
		public function load(url:String,method:String= URLRequestMethod.GET,data:Object=null):Loader
		{
			return loading(url,method,data);
		}
		public function loadImage(url:String,method:String = URLRequestMethod.GET,data:Object=null):Loader
		{
			return loading(url,method,data);
		}
		private function loading(url:String,method:String = URLRequestMethod.GET,data:Object=null):Loader
		{
			var loader:Loader=new Loader();
			if(!loaderMap[url])
			{
				loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onLoadComplete);
				loader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR,onLoadError);
				
				urlRequest.method = method;
				urlRequest.url = url;
				if(data)urlRequest.data = toUrlVariables(data);
				
				loader.load(urlRequest);
				loaderMap[url] = new Object();
				loaderMap[url]["loader"] = loader;
				loaderMap[url]["queue"] = new Array();
				
			}else if(loaderMap[url]["loader"].content)
			{
				var loaderInfo:LoaderInfo = (loaderMap[url]["loader"] as Loader).loaderInfo;
				loader.loadBytes(loaderInfo.bytes);
			}else
			{
				loaderMap[url]["queue"].push(loader);
			}
			return loader;
		}
		//================================================= 事件==============================================
		/**
		 * 加载完成
		 */
		private function onLoadComplete(event:Event):void
		{
			var loaderInfo:LoaderInfo = event.currentTarget as LoaderInfo;
			for (var url:String in loaderMap)
			{
				if(loaderMap[url]["loader"] == loaderInfo.loader)
				{
					while(loaderMap[url]["queue"].length > 0)
					{
						var item:Loader = loaderMap[url]["queue"].shift() as Loader;
						item.loadBytes(loaderInfo.bytes);
						trace(item.content);
					}
					loaderMap[url] = null;
					delete loaderMap[url];
				}
			}
			removeEvent(loaderInfo);
			trace(loaderInfo.content);
		}
		/**
		 * 加载错误
		 */
		private function onLoadError(event:IOErrorEvent):void
		{
			var loaderInfo:LoaderInfo = event.currentTarget as LoaderInfo;
			for (var url:String in loaderMap)
			{
				if(loaderMap[url]["loader"] == loaderInfo.loader)
				{
					loaderMap[url] = null;
					delete loaderMap[url];
				}
			}
			removeEvent(loaderInfo);
			trace(loaderInfo);
		}
		/**
		 * 删除事件
		 */
		private function removeEvent(loaderInfo:LoaderInfo):void
		{
			loaderInfo.removeEventListener(Event.COMPLETE,onLoadComplete);
			loaderInfo.removeEventListener(IOErrorEvent.IO_ERROR,onLoadError);
		}
	}
}