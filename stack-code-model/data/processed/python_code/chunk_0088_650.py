package com.ats.helpers {
	
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	
	public class DeviceSettingsHelper {
		
		private const deviceSettingsFile:File = File.userDirectory.resolvePath(".actiontestscript/mobilestation/settings/devicesSettings.txt");
		public static var shared:DeviceSettingsHelper = new DeviceSettingsHelper();
		
		public function DeviceSettingsHelper() {
			if (deviceSettingsFile.exists) {
				this.settings = fetchSettings()
			} else {
				this.settings = new Vector.<DeviceSettings>()
				saveAll()
			}
		}
		
		public var settings:Vector.<DeviceSettings>
		
		public function settingsForDevice(deviceId:String):DeviceSettings {
			var deviceSettings:DeviceSettings
			for each(deviceSettings in settings) {
				if (deviceSettings.deviceId == deviceId.toLowerCase()) {
					return deviceSettings
				}
			}
			
			return null
		}
		
		public function save(deviceSettings:DeviceSettings):void {
			var existingDeviceSettings:DeviceSettings = settingsForDevice(deviceSettings.deviceId)
			if (existingDeviceSettings != null) {
				var index:int = settings.indexOf(existingDeviceSettings)
				settings.removeAt(index)
			}
			
			settings.push(deviceSettings)
			saveAll()
		}
		
		private function saveAll():void {
			var fileStream:FileStream = new FileStream()
			fileStream.open(deviceSettingsFile, FileMode.WRITE)
			for each(var deviceSettings:DeviceSettings in settings) {
				fileStream.writeUTFBytes(deviceSettings.toString() + "\n")
			}
			fileStream.close()
		}
		
		private function fetchSettings():Vector.<DeviceSettings> {
			var fileStream:FileStream = new FileStream()
			fileStream.open(deviceSettingsFile, FileMode.READ)
			var contentString:String = fileStream.readUTFBytes(fileStream.bytesAvailable)
			fileStream.close()
			
			var settings:Vector.<DeviceSettings> = new Vector.<DeviceSettings>()
			var lines:Array = contentString.split("\n")
			for each(var text:String in lines) {
				var deviceSettings:DeviceSettings = DeviceSettings.initFromDeviceSettingsString(text)
				if (deviceSettings != null) {
					settings.push(deviceSettings)
				}
			}
			
			return settings
		}
		
		// utils
		
		public function assignedPorts():Vector.<int> {
			var ports:Vector.<int> = new Vector.<int>()
			var mapInt:Function = function (setting:DeviceSettings, index:int, vector:Vector.<DeviceSettings>):void { ports.push(setting.port) }
			settings.forEach(mapInt)
			return ports.sort(0)
		}
		
		public function assignedPortAvailable(fromIndex:int = 8080):Boolean {
			return assignedPorts().indexOf(fromIndex) == -1;
		}
		
		public function nextPortAvailable(fromIndex:int = 8080):int {
			var ports:Vector.<int> = assignedPorts();
			while (ports.indexOf(fromIndex) != -1) {
				fromIndex += 1;
			}
			return fromIndex;
		}
	}
}