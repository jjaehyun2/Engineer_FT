package devoron.sdk.sdkmediator
{
	import devoron.file.FileInfo;
	import devoron.file.FileInfoUtils;
	import devoron.utils.ErrorInfo;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.net.registerClassAlias;
	import flash.net.URLLoader;
	import flash.net.URLLoaderDataFormat;
	import flash.net.URLRequest;
	import flash.utils.ByteArray;
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.Responder;
	
	/**
	 * SDKMediatorResponder
	 * @author Devoron
	 */
	public class SDKMediatorResponder extends Responder
	{
		protected var fileLoader:URLLoader;
		protected var resultHandler:Function;
		protected var errorHandler:Function;
		protected var path:String;
		protected var needDownload:Boolean;
		protected var fileInfo:FileInfo;
		protected var requests:Vector.<URLRequest>;
		
		public function SDKMediatorResponder(command:String, resultHandler:Function, errorHandler:Function, needDownload:Boolean = false)
		{
			super(responderResultFunction, responderErrorFunction);
			this.resultHandler = resultHandler;
			this.errorHandler = errorHandler;
			this.path = command;
			this.needDownload = needDownload;
		}
		
		public function responderResultFunction(e:*):void
		{
			//gtrace("3: " + e.message);
			
			if (e.result is FileInfo)
			{
				fileInfo = FileInfo(e.result);
				
				if (needDownload && !fileInfo.isDirectory)
				{
					fileLoader = createFileLoader();
					fileLoader.load(new URLRequest(fileInfo.nativePath));
				}
				
				else if (needDownload && fileInfo.directoryListing)
				{
					if (fileInfo.directoryListing.length > 0)
					{
						requests = new Vector.<URLRequest>();
						for each (var fi:FileInfo in fileInfo.directoryListing)
						{
							requests.push(new URLRequest(fi.nativePath));
							if (fi.isDirectory)
							{
								if (errorHandler != null)
									errorHandler.call(null, path, "Unable to load the directory " + fi.nativePath);
								return;
							}
							
						}
						fileLoader = createFileLoader();
						fileLoader.load(requests.pop());
					}
					
				}
				
				else if (resultHandler != null)
					resultHandler.call(null, fileInfo);
			}
			
			else if (e.result is Array)
			{
				if (resultHandler != null)
					resultHandler.call(null, e.result);
			}
			
			else if (e.result is ErrorInfo)
			{
				if (errorHandler != null)
					errorHandler.call(null, path, (e.result as ErrorInfo).message);
			}
		
		}
		
		public function responderErrorFunction(e:FaultEvent):void
		{
			if (errorHandler != null)
				errorHandler.call(null, path, e.message);
		}
		
		private function onFileLoadingError(e:IOErrorEvent):void
		{
			if (errorHandler != null)
				errorHandler.call(null, path, e.text);
			disposeFileLoader();
		}
		
		private function onFileLoadingComplete(e:Event):void
		{
			
			//gtrace("загружено " + fileInfo.nativePath);
			
			/*if(!requests || requests.length == 0){
			   resultHandler.call(null, );
			   disposeFileLoader();
			   }
			 else fileLoader.load(requests.pop());*/
			
			var data:ByteArray = new ByteArray();
			//data.writeObject(fileLoader.data); 
			data.writeBytes(fileLoader.data);
			data.position = 0;
			//gtrace("результирующие " + fileLoader.data.length);
			if (fileInfo.isDirectory)
				(fileInfo.directoryListing[requests.length] as FileInfo).data = data;
			else
				fileInfo.data = data;
			
			if (!requests || requests.length == 0)
			{
				resultHandler.call(null, fileInfo);
				resultHandler = null;
				errorHandler = null;
				fileInfo = null;
				path = null;
				disposeFileLoader();
			}
			else
				fileLoader.load(requests.pop());
		}
		
		protected function createFileLoader():URLLoader
		{
			var loader:URLLoader = new URLLoader();
			loader.addEventListener(Event.COMPLETE, onFileLoadingComplete/*, false, 0, true*/);
			loader.addEventListener(IOErrorEvent.IO_ERROR, onFileLoadingError/*, false, 0, true*/);
			loader.dataFormat = URLLoaderDataFormat.BINARY;
			return loader;
		}
		
		protected function disposeFileLoader():void
		{
			fileLoader.removeEventListener(Event.COMPLETE, onFileLoadingComplete);
			fileLoader.removeEventListener(IOErrorEvent.IO_ERROR, onFileLoadingError);
			fileLoader = null;
			if (requests)
			{
				requests.length = 0;
				requests = null;
			}
		}
	
	}

}