package com.ats.helpers {
	import flash.errors.IOError;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.system.Capabilities;

	import mx.utils.UIDUtil;

	public class Settings {

		private static const APP_FOLDER_WINDOWS:String = "AppData/Local";
		private static const APP_FOLDER_MACOS:String = "Library";
		public static const isMacOs:Boolean = Capabilities.os.indexOf("Mac") > -1;
		public static const workAdbFolder:File = File.applicationDirectory.resolvePath("assets/tools/android");
		public static const workFolder:File = File.userDirectory.resolvePath(".atsmobilestation");
		private static const settingsFolder:File = File.userDirectory.resolvePath(".actiontestscript/mobilestation/settings");
		private static var _instance:Settings = new Settings();

		[Bindable]
		public var automaticUpdateEnabled:Boolean = true;

		[Bindable]
		public var appIdentifier:String;

		[Bindable]
		public var appleDeveloperTeamId:String

		public static function get defaultAppFolder():File {
			return isMacOs ? File.userDirectory.resolvePath(APP_FOLDER_MACOS) : File.userDirectory.resolvePath(APP_FOLDER_WINDOWS)
		}

		public static function get osName():String {
			return isMacOs ? "macos" : "windows"
		}

		public static function get logsFolder():File {
			return workFolder.resolvePath("logs");
		}

		public static function get devicesSettingsFile():File {
			return settingsFolder.resolvePath("devicesSettings.txt");
		}

		public static function get settingsFile():File {
			return settingsFolder.resolvePath("settings.txt");
		}

		public static function get adbFile():File {
			return workAdbFolder.resolvePath("adb" + (isMacOs ? "" : ".exe"))
		}

		public static function getInstance():Settings {
			return _instance;
		}

		public static function cleanLogs():void {
			try {
				logsFolder.deleteDirectory(true);
			} catch (err:IOError) {
			}
		}

		public function Settings() {
			if (_instance) {
				throw new Error("Settings is a singleton and can only be accessed through Settings.getInstance()");
			}

			loadProperties()
		}

		public function loadProperties():void {
			var appIdentifier:String

			var file:File = settingsFile;
			var fileStream:FileStream = new FileStream();
			if (file.exists) {
				fileStream.open(file, FileMode.READ);

				var settingsContent:String = fileStream.readUTFBytes(fileStream.bytesAvailable);
				var settingsContentArray:Array = settingsContent.split("\n");

				for each(var setting:String in settingsContentArray) {
					if (setting != "") {
						var key:String = setting.split("==")[0];
						var value:String = setting.split("==")[1];
						if (isMacOs && key == "development_team") {
							appleDeveloperTeamId = value
						} else if (key == "identifier") {
							appIdentifier = value
						} else if (key == "automatic_update") {
							automaticUpdateEnabled = value == "true"
						}
					}
				}
				fileStream.close();

				if (appIdentifier == null) {
					appIdentifier = UIDUtil.createUID()
					settingsContentArray.push("identifier==" + appIdentifier)

					fileStream.open(file, FileMode.WRITE)
					fileStream.writeUTFBytes(settingsContentArray.join("\n"))
					fileStream.close()
				}

			} else {
				fileStream.open(file, FileMode.WRITE)
				appIdentifier = UIDUtil.createUID()
				fileStream.writeUTFBytes("identifier==" + UIDUtil.createUID())
				fileStream.close()
			}

			this.appIdentifier = appIdentifier
		}

		public function save():void {
			var propertiesToSave:Vector.<String> = new Vector.<String>()
			propertiesToSave.push("identifier==" + appIdentifier)
			propertiesToSave.push("automatic_update==" + automaticUpdateEnabled)
			if (isMacOs) {
				propertiesToSave.push("development_team==" + appleDeveloperTeamId)
			}

			var file:File = settingsFile
			var fileStream:FileStream = new FileStream()
			fileStream.open(file, FileMode.WRITE)
			fileStream.writeUTFBytes(propertiesToSave.join("\n"))
			fileStream.close()
		}
	}
}