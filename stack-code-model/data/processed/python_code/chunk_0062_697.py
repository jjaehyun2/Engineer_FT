package net.guttershark.support.preloading
{
	import flash.events.SecurityErrorEvent;
	
	import net.guttershark.control.PreloadController;
	import net.guttershark.support.preloading.events.AssetCompleteEvent;
	import net.guttershark.support.preloading.events.AssetErrorEvent;
	import net.guttershark.support.preloading.events.AssetOpenEvent;
	import net.guttershark.support.preloading.events.AssetProgressEvent;
	import net.guttershark.support.preloading.events.AssetStatusEvent;
	import net.guttershark.support.preloading.workers.WorkerInstances;
	import net.guttershark.util.StringUtils;	

	/**
	 * The Asset class defines an asset to preload with a PreloadController.
	 * 
	 * @see net.guttershark.control.PreloadController PreloadController class
	 * @see net.guttershark.managers.AssetManager AssetManager class
	 */
	final public class Asset
	{

		/**
		 * The controller that receives updates from this item.
		 */
		private var controller:PreloadController;

		/**
		 * The worker that is doing the loading work.
		 */
		private var worker:*;
		
		/**
		 * The file type of this asset. This will be a file extension less the period (jpg).
		 */
		public var fileType:String;
		
		/**
		 * The URI to the file to load.
		 */
		public var source:String;
		
		/**
		 * The identifier of this item in the AssetManager
		 * 
		 * @see net.guttershark.managers.AssetManager AssetManager class.
		 */
		public var libraryName:String;
		
		/**
		 * The data for this asset after the asset has been loaded. 
		 * 
		 * <p>This will be a reference to the loader that was used
		 * in loading the data.</p>
		 */
		public var data:*;
		
		/**
		 * Constructor for Asset instances.
		 * 
		 * @param source The source URL to the asset
		 * @param libraryName The name to be used in an AssetLibrary
		 * @param forceFileType	Force the asset's file type (file extension without the ".", EX: xml);
		 */
		public function Asset(source:String, libraryName:String = null, forceFileType:String = null)
		{
			if(!forceFileType)
			{
				var fileType:String = StringUtils.gi().findFileType(source);
				if(!fileType) throw new Error("The filetype could not be found for this item: " + source);
				this.fileType = fileType;
			}
			else this.fileType = forceFileType;
			this.source = source;
			if(!libraryName)
			{
				trace("WARNING: No library name was supplied for asset with source {"+source+"} using the source as the libraryName");
				this.libraryName = source;
			}
			else this.libraryName = libraryName;
		}

		/**
		 * @private
		 * 
		 * Starts the load process for this item.
		 * 
		 * @param controller A preload controller that is controlling this asset.
		 */
		public function load(controller:PreloadController):void
		{
			this.controller = controller;
			worker = WorkerInstances.GetWorkerInstance(fileType);
			addListenersToWorker();
			worker.load(this);
		}
		
		/**
		 * removes listeners
		 */
		private function removeListenersFromWorker():void
		{
			if(!worker) return;
			worker.removeEventListener(AssetCompleteEvent.COMPLETE,onComplete);
			worker.removeEventListener(AssetProgressEvent.PROGRESS,controller.progress);
			worker.removeEventListener(AssetErrorEvent.ERROR,onError);
			worker.removeEventListener(AssetOpenEvent.OPEN,controller.open);
			worker.removeEventListener(AssetStatusEvent.STATUS,onHTTPStatus);
			worker.removeEventListener(SecurityErrorEvent.SECURITY_ERROR,onSecurityError);
		}
		
		/**
		 * adds listeners
		 */
		private function addListenersToWorker():void
		{
			if(!worker) return;
			worker.addEventListener(AssetCompleteEvent.COMPLETE,onComplete);
			worker.addEventListener(AssetProgressEvent.PROGRESS,controller.progress);
			worker.addEventListener(AssetErrorEvent.ERROR,onError);
			worker.addEventListener(AssetOpenEvent.OPEN,controller.open);
			worker.addEventListener(AssetStatusEvent.STATUS,onHTTPStatus);
			worker.addEventListener(SecurityErrorEvent.SECURITY_ERROR,onSecurityError);
		}
		
		private function onComplete(e:AssetCompleteEvent):void
		{
			controller.complete(e);
			dispose();
		}
		
		private function onError(e:AssetErrorEvent):void
		{
			if(!controller)
			{
				dispose();
				return;
			}
			controller.error(e);
			dispose();
		}
		
		private function onHTTPStatus(h:AssetStatusEvent):void
		{
			if(!controller)
			{
				dispose();
				return;
			}
			controller.httpStatus(h);
			dispose();
		}
		
		/**
		 * Handles security error, the controller doesn't specifically handle it.
		 */
		private function onSecurityError(se:SecurityError):void
		{
			dispose();
			throw se;
		}
		
		/**
		 * @private
		 * 
		 * Returns the bytes loaded for this item.
		 */
		public function get bytesLoaded():Number
		{
			return worker.bytesLoaded;
		}
		
		/**
		 * @private
		 * 
		 * Returns the bytes total for this item.
		 */
		public function get bytesTotal():Number
		{
			return worker.bytesTotal;
		}
		
		/**
		 * The dispose method only disposes of unused properties
		 * after the asset is complete / errored out, to completely
		 * dispose of the Asset, use <em><code>disposeFinal</code></em>
		 */
		public function dispose():void
		{
			removeListenersFromWorker();
			if(worker) worker.dispose();
			worker = null;
			controller = null;
			libraryName = null;
			fileType = null;
		}
	}
}