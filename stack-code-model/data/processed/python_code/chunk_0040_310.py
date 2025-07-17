package com.riaspace.nativeApplicationUpdater
{
	import air.update.events.DownloadErrorEvent;
	import air.update.events.StatusUpdateErrorEvent;
	import air.update.events.StatusUpdateEvent;
	import air.update.events.UpdateEvent;
	
	import com.riaspace.nativeApplicationUpdater.events.CannotPerformUpdateEvent;
	import com.riaspace.nativeApplicationUpdater.utils.HdiutilHelper;
	
	import flash.desktop.NativeApplication;
	import flash.desktop.NativeProcess;
	import flash.desktop.NativeProcessStartupInfo;
	import flash.events.ErrorEvent;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IOErrorEvent;
	import flash.events.ProgressEvent;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.net.URLStream;
	import flash.utils.ByteArray;
	import flash.utils.setTimeout;
	
	import mx.events.CloseEvent;
	import mx.rpc.events.ResultEvent;

	[Event(name="initialized", type="air.update.events.UpdateEvent")]
	[Event(name="checkForUpdate", type="air.update.events.UpdateEvent")]
	[Event(name="updateStatus",type="air.update.events.StatusUpdateEvent")]
	[Event(name="updateError",type="air.update.events.StatusUpdateErrorEvent")]
	[Event(name="downloadStart",type="air.update.events.UpdateEvent")]
	[Event(name="downloadError",type="air.update.events.DownloadErrorEvent")]
	[Event(name="downloadComplete",type="air.update.events.UpdateEvent")]
	[Event(name="progress",type="flash.events.ProgressEvent")]
	[Event(name="error",type="flash.events.ErrorEvent")]
	[Event(name="cannotPerformUpdate",type="com.riaspace.nativeApplicationUpdater.events.CannotPerformUpdateEvent")]
	
	public class NativeApplicationUpdater extends EventDispatcher {
		
		/**
		 * The updater has not been initialized.
		 **/
		public static const UNINITIALIZED:String = "UNINITIALIZED";
		
		/**
		 * The updater is initializing.
		 **/
		public static const INITIALIZING:String = "INITIALIZING";
		
		/**
		 * The updater has been initialized.
		 **/
		public static const READY:String = "READY";
		
		/**
		 * The updater has not yet checked for the update descriptor file.
		 **/
		public static const BEFORE_CHECKING:String = "BEFORE_CHECKING";
		
		/**
		 * The updater is checking for an update descriptor file.
		 **/
		public static const CHECKING:String = "CHECKING";
		
		/**
		 * The update descriptor file is available.
		 **/
		public static const AVAILABLE:String = "AVAILABLE";

		/**
		 * The updater is downloading the AIR file.
		 **/
		public static const DOWNLOADING:String = "DOWNLOADING";
		
		/**
		 * The updater has downloaded the AIR file.
		 **/
		public static const DOWNLOADED:String = "DOWNLOADED";
		
		/**
		 * The updater is installing the AIR file.
		 **/
		public static const INSTALLING:String = "INSTALLING";
		
		[Bindable]		
		public var updateURL:String;
		
		protected var _json_decoder:Function;
		
		protected var _isOSWindows:Function;

		protected var _isOSMac:Function;

		protected var _isOSLinux:Function;
		
		protected var _isNewerVersionFunction:Function;
		
		protected var _updateDescriptor:Object;
		
		protected var _updateVersion:String;
		
		protected var _updatePackageURL:String;
		
		protected var _updateDescription:String;

		protected var _currentVersion:String;
		
		protected var _downloadedFile:File;
		
		protected var _installerType:String;
		
		protected var _currentState:String = UNINITIALIZED;
		
		protected var updateDescriptorLoader:URLLoader;
		
		protected var urlStream:URLStream;
		
		protected var fileStream:FileStream;
		
		protected var currentPosition:uint = 0;
		
		public function NativeApplicationUpdater() {
		}
		
		public function initialize():void {
			if (currentState == UNINITIALIZED) {
				currentState = INITIALIZING;
				
				var applicationDescriptor:XML = NativeApplication.nativeApplication.applicationDescriptor;
				var xmlns:Namespace = new Namespace(applicationDescriptor.namespace());
				
				if (xmlns.uri == "http://ns.adobe.com/air/application/2.0")
					currentVersion = applicationDescriptor.xmlns::version;
				else
					currentVersion = applicationDescriptor.xmlns::versionNumber;

				if (this.isOSWindows()) {
					installerType = "exe";
				} else if (this.isOSMac()) {
					installerType = "dmg";
				} else if (this.isOSLinux()) {
					if ((new File("/usr/bin/dpkg")).exists)
						installerType = "deb";
					else
						installerType = "rpm";
				} else {
					dispatchEvent(new ErrorEvent(ErrorEvent.ERROR, false, false, "Not supported os type!", UpdaterErrorCodes.ERROR_9000));
				}
				
				currentState = READY;
				dispatchEvent(new UpdateEvent(UpdateEvent.INITIALIZED));
			}
		}
		
		public function checkNow():void {
			if (currentState == READY) {
				currentState = BEFORE_CHECKING;
				
				var checkForUpdateEvent:UpdateEvent = new UpdateEvent(UpdateEvent.CHECK_FOR_UPDATE, false, true);
				dispatchEvent(checkForUpdateEvent);

				if (!checkForUpdateEvent.isDefaultPrevented()) {
					addEventListener(StatusUpdateEvent.UPDATE_STATUS,
						function(event:StatusUpdateEvent):void {
							if (event.available && !event.isDefaultPrevented())
								downloadUpdate();
						});
					addEventListener(UpdateEvent.DOWNLOAD_COMPLETE,
						function(event:UpdateEvent):void {
							if (!event.isDefaultPrevented())
								//installUpdate();
								setTimeout(installUpdate, 1500); // This is a hack for all platforms as download complete event may be fired before file is released.
						});
					
					checkForUpdate();
				}
			}
		}
		
		/**
		 * ------------------------------------ CHECK FOR UPDATE SECTION -------------------------------------
		 */

		/**
		 * Checks for update, this can be runned only in situation when UpdateEvent.CHECK_FOR_UPDATE was cancelled.
		 */ 
		public function checkForUpdate():void {
			var _this:NativeApplicationUpdater = this;
			if (currentState == BEFORE_CHECKING) {
				currentState = CHECKING;
				
				updateDescriptorLoader =  new URLLoader();
				updateDescriptorLoader.addEventListener(Event.COMPLETE,  updateDescriptorLoader_completeHandler);
				updateDescriptorLoader.addEventListener(IOErrorEvent.IO_ERROR, updateDescriptorLoader_ioErrorHandler);
				try {
					updateDescriptorLoader.load(new URLRequest(updateURL));
				} catch(error:Error) {
					dispatchEvent(new StatusUpdateErrorEvent(StatusUpdateErrorEvent.UPDATE_ERROR, false, false, 
						"Error downloading update descriptor file: " + error.message, 
						UpdaterErrorCodes.ERROR_9002, error.errorID));
				}
			}
		}

		protected function updateDescriptorLoader_completeHandler(event:Event):void {
			this.updateDescriptorLoader.removeEventListener(Event.COMPLETE, updateDescriptorLoader_completeHandler);
			
			this.updateDescriptor = {};
			if (this._json_decoder is Function) {
				try {
					this.updateDescriptor = this._json_decoder(updateDescriptorLoader.data);
					trace('NativeApplicationUpdater.updateDescriptorLoader_completeHandler().1 --> this.updateDescriptor='+this.updateDescriptor);
					this.updateVersion = this.updateDescriptor[this.installerType].v;
					trace('NativeApplicationUpdater.updateDescriptorLoader_completeHandler().1 --> this.updateVersion='+this.updateVersion);
					this.updateDescription = this.updateDescriptor[this.installerType].d;
					trace('NativeApplicationUpdater.updateDescriptorLoader_completeHandler().1 --> this.updateDescription='+this.updateDescription);
					this.updatePackageURL = this.updateDescriptor[this.installerType].u;
					trace('NativeApplicationUpdater.updateDescriptorLoader_completeHandler().1 --> this.updatePackageURL='+this.updatePackageURL);
				} catch (err:Error) {
					trace('NativeApplicationUpdater.updateDescriptorLoader_completeHandler().ERROR --> error='+err.toString());
				}
			}
			
			if (!this.updateVersion || !this.updatePackageURL) {
				dispatchEvent(new StatusUpdateErrorEvent(StatusUpdateErrorEvent.UPDATE_ERROR, false, false, 
					"Update package is not defined for current installerType: " + installerType, UpdaterErrorCodes.ERROR_9001));
				return;
			}

			this.currentState = AVAILABLE;			
			this.dispatchEvent(new StatusUpdateEvent(
				StatusUpdateEvent.UPDATE_STATUS, false, true, 
				isNewerVersionFunction.call(this, currentVersion, updateVersion), updateVersion)); // TODO: handle last event param with details (description)
		}
		
		protected function updateDescriptorLoader_ioErrorHandler(event:IOErrorEvent):void {
			updateDescriptorLoader.removeEventListener(IOErrorEvent.IO_ERROR, updateDescriptorLoader_ioErrorHandler); 
			
			dispatchEvent(new StatusUpdateErrorEvent(StatusUpdateErrorEvent.UPDATE_ERROR, false, false, 
				"IO Error downloading update descriptor file: " + event.text, UpdaterErrorCodes.ERROR_9003, event.errorID));
		}

		/**
		 * ------------------------------------ DOWNLOAD UPDATE SECTION -------------------------------------
		 */

		/**
		 * Starts downloading update.
		 */
		public function downloadUpdate():void {
			if (currentState == AVAILABLE) {
				downloadedFile = File.createTempFile();
				
				fileStream = new FileStream();
				fileStream.addEventListener(IOErrorEvent.IO_ERROR, urlStream_ioErrorHandler);
				fileStream.addEventListener(Event.CLOSE, urlStream_closeHandler);
				fileStream.openAsync(downloadedFile, FileMode.WRITE);
				
				urlStream = new URLStream();
				urlStream.addEventListener(Event.OPEN, urlStream_openHandler);
				urlStream.addEventListener(ProgressEvent.PROGRESS, urlStream_progressHandler);
				urlStream.addEventListener(Event.COMPLETE, urlStream_completeHandler);
				urlStream.addEventListener(IOErrorEvent.IO_ERROR, urlStream_ioErrorHandler);

				try {
					urlStream.load(new URLRequest(updatePackageURL));
				} catch(error:Error) {
					dispatchEvent(new DownloadErrorEvent(DownloadErrorEvent.DOWNLOAD_ERROR, false, false, 
						"Error downloading update file: " + error.message, UpdaterErrorCodes.ERROR_9004, error.message));
				}
			}
		}

		protected function urlStream_openHandler(event:Event):void {
			currentState = NativeApplicationUpdater.DOWNLOADING;
			dispatchEvent(new UpdateEvent(UpdateEvent.DOWNLOAD_START));
		}
		
		protected function urlStream_closeHandler(event:Event):void {
			currentState = NativeApplicationUpdater.DOWNLOADED;
			dispatchEvent(new UpdateEvent(UpdateEvent.DOWNLOAD_COMPLETE, false, true));
		}
		
		protected function urlStream_progressHandler(event:ProgressEvent):void {
			var bytes:ByteArray = new ByteArray();
			var offset:uint = currentPosition;
			currentPosition += urlStream.bytesAvailable;
			
			urlStream.readBytes(bytes, offset);
			fileStream.writeBytes(bytes, offset);
			
			dispatchEvent(event.clone());
		}
		
		protected function urlStream_completeHandler(event:Event):void {
			urlStream.close();
			fileStream.close();
		}

		protected function urlStream_ioErrorHandler(event:IOErrorEvent):void {
			dispatchEvent(new DownloadErrorEvent(DownloadErrorEvent.DOWNLOAD_ERROR, false, false, 
				"Error downloading update file: " + event.text, UpdaterErrorCodes.ERROR_9005, event.errorID));
		}
		
		/**
		 * ------------------------------------ INSTALL UPDATE SECTION -------------------------------------
		 */
		
		/**
		 * Installs downloaded update
		 */ 
		public function installUpdate():void {
			if (currentState == DOWNLOADED) {
				if (this.isOSWindows()) {
					installFromFile(downloadedFile);
				}	else if (this.isOSMac()) {
					var hdiutilHelper:HdiutilHelper = new HdiutilHelper(downloadedFile);
					hdiutilHelper.addEventListener(Event.COMPLETE, hdiutilHelper_completeHandler);
					hdiutilHelper.addEventListener(ErrorEvent.ERROR, hdiutilHelper_errorHandler);
					hdiutilHelper.attach();
				} else if (this.isOSLinux()) {
					installFromFile(downloadedFile);
				}
			}
		}

		private function hdiutilHelper_errorHandler(event:ErrorEvent):void {
			var hdiutilHelper:HdiutilHelper = event.target as HdiutilHelper;
			hdiutilHelper.removeEventListener(Event.COMPLETE, hdiutilHelper_completeHandler);
			hdiutilHelper.removeEventListener(ErrorEvent.ERROR, hdiutilHelper_errorHandler);
			
			dispatchEvent(new ErrorEvent(ErrorEvent.ERROR, false, false, "Error attaching dmg file!", UpdaterErrorCodes.ERROR_9008));
		}

		private function hdiutilHelper_completeHandler(event:Event):void	{
			var hdiutilHelper:HdiutilHelper = event.target as HdiutilHelper;
			hdiutilHelper.removeEventListener(Event.COMPLETE, hdiutilHelper_completeHandler);
			hdiutilHelper.removeEventListener(ErrorEvent.ERROR, hdiutilHelper_errorHandler);
			
			var attachedDmg:File = new File(hdiutilHelper.mountPoint);
			var files:Array = attachedDmg.getDirectoryListing();
			
			if (files.length == 1) {
				var installFileFolder:File = File(files[0]).resolvePath("Contents/MacOS");
				var installFiles:Array = installFileFolder.getDirectoryListing();

				if (installFiles.length == 1)
					installFromFile(installFiles[0]);
				else
					dispatchEvent(new ErrorEvent(ErrorEvent.ERROR, false, false, 
						"Contents/MacOS folder should contain only 1 install file!", UpdaterErrorCodes.ERROR_9006));
			} else {
				dispatchEvent(new ErrorEvent(ErrorEvent.ERROR, false, false, "Mounted volume should contain only 1 install file!", UpdaterErrorCodes.ERROR_9007));
			}
		}
		
		protected function installFromFile(updateFile:File):void {
			var beforeInstallEvent:UpdateEvent = new UpdateEvent(UpdateEvent.BEFORE_INSTALL, false, true);
			dispatchEvent(beforeInstallEvent);
			
			if (!beforeInstallEvent.isDefaultPrevented()) {
				currentState = INSTALLING;
				
				if (this.isOSLinux()) {
					updateFile.openWithDefaultApplication();
				} else {
					try {
						var info:NativeProcessStartupInfo = new NativeProcessStartupInfo();
						info.executable = updateFile;
						
						var installProcess:NativeProcess = new NativeProcess();
						installProcess.start(info);
					} catch (err:Error) {
						dispatchEvent(new CannotPerformUpdateEvent(CannotPerformUpdateEvent.TYPE_CANNOT_PERFORM_UPDATE,err));
					}
				}
			}
		}
		
		[Bindable]
		public function get currentVersion():String {
			return _currentVersion;
		}

		protected function set currentVersion(value:String):void {
			_currentVersion = value;
		}

		[Bindable]
		public function get updateVersion():String {
			return _updateVersion;
		}

		protected function set updateVersion(value:String):void {
			_updateVersion = value;
		}

		[Bindable]
		public function get updateDescriptor():Object {
			return _updateDescriptor;
		}

		protected function set updateDescriptor(value:Object):void {
			_updateDescriptor = value;
		}

		[Bindable]
		public function get currentState():String {
			return _currentState;
		}

		protected function set currentState(value:String):void {
			_currentState = value;
		}

		[Bindable]
		public function get downloadedFile():File {
			return _downloadedFile;
		}

		protected function set downloadedFile(value:File):void {
			_downloadedFile = value;
		}

		[Bindable]
		public function get json_decoder():Function {
			return this._json_decoder;
		}
		
		public function set json_decoder(json_decoder:Function):void {
			if (json_decoder is Function) {
				this._json_decoder = json_decoder;
			}
		}
		
		[Bindable]
		public function get isNewerVersionFunction():Function {
			if (_isNewerVersionFunction != null)
				return _isNewerVersionFunction;
			else
				return function(currentVersion:String, updateVersion:String):Boolean { return currentVersion != updateVersion};
		}

		public function set isNewerVersionFunction(value:Function):void {
			_isNewerVersionFunction = value;
		}
		
		[Bindable]
		public function get isOSWindows():Function {
			if (_isOSWindows is Function) {
				return _isOSWindows;
			} 
			return function():Boolean { return false};
		}
		
		public function set isOSWindows(value:Function):void {
			_isOSWindows = value;
		}

		[Bindable]
		public function get isOSMac():Function {
			if (_isOSMac is Function) {
				return _isOSMac;
			} 
			return function():Boolean { return false};
		}
		
		public function set isOSMac(value:Function):void {
			_isOSMac = value;
		}

		[Bindable]
		public function get isOSLinux():Function {
			if (_isOSLinux is Function) {
				return _isOSLinux;
			} 
			return function():Boolean { return false};
		}
		
		public function set isOSLinux(value:Function):void {
			_isOSLinux = value;
		}

		[Bindable]
		public function get installerType():String {
			return _installerType;
		}

		protected function set installerType(value:String):void {
			_installerType = value;
		}

		[Bindable]
		public function get updatePackageURL():String {
			return _updatePackageURL;
		}
		
		protected function set updatePackageURL(value:String):void {
			_updatePackageURL = value;
		}
		
		[Bindable]
		public function get updateDescription():String {
			return _updateDescription;
		}
		
		protected function set updateDescription(value:String):void {
			_updateDescription = value;
		}
	}
}