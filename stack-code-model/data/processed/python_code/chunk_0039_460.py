package Bezel 
{
	/**
	 * ...
	 * @author piepie62
	 */
	
	import flash.display.Loader;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.system.ApplicationDomain;
	import flash.system.LoaderContext;
	import flash.utils.ByteArray;
	 
	internal class SWFFile 
	{
		private var loader:Loader;
		private var file:File;
		public var instance:Object;
		
		public function get filePath(): String
		{
			return file.nativePath;
		}

		private var successfulLoadCallback:Function;
		private var failedLoadCallback:Function;
		
		public function SWFFile(file:File) 
		{
			if (file == null || !file.exists)
				throw new ArgumentError("Tried to create a mod with no mod file!");
			this.file = file;
			this.loader = new Loader();
		}
		
		public function load(successCallback:Function, failureCallback:Function, currentDomain: Boolean = false): void
		{
			this.successfulLoadCallback = successCallback;
			this.failedLoadCallback = failureCallback;
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, loadedSuccessfully);
			loader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, failedLoadCallback);
			var bytes:ByteArray = new ByteArray();
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.READ);
			stream.readBytes(bytes);
			stream.close();
			var context:LoaderContext;
			// The domain matters, if you load mods into the same domain as the game, they will stay loaded until you restart the entire flash application
			// This way by default (ApplicationDomain = null) they are loaded into a domain under their Loader, which lets us reload the mods without restarting the game
			if(!currentDomain)
				context = new LoaderContext(true);
			else
				context = new LoaderContext(true, ApplicationDomain.currentDomain);
			context.checkPolicyFile = false;
			context.allowCodeImport = true;
			loader.loadBytes(bytes, context);
		}
		
		public function unload(): void
		{
			this.loader.contentLoaderInfo.removeEventListener(Event.COMPLETE, loadedSuccessfully);
			this.loader.contentLoaderInfo.removeEventListener(IOErrorEvent.IO_ERROR, failedLoadCallback);
			// Make sure the mod cleans up its event subscribers and resources
			this.instance.unload();
			// Stop all execution and unsibscribe events, let garbage collection occur
			this.loader.unloadAndStop(true);
			this.instance = null;
			this.loader = null;
		}
		
		private function loadedSuccessfully(e:Event): void
		{
			this.instance = this.loader.content;
			successfulLoadCallback(this);
		}
	}

}