package com.ats.helpers {
    import com.ats.device.running.RunningDevice;
    import com.ats.tools.Python;

    import flash.desktop.NativeApplication;

    import flash.events.Event;
    import flash.events.TimerEvent;
    import flash.filesystem.File;
    import flash.filesystem.FileMode;
    import flash.filesystem.FileStream;
    import flash.net.URLLoader;
    import flash.net.URLRequest;
    import flash.net.URLStream;
    import flash.utils.ByteArray;
    import flash.utils.Timer;

    import mx.collections.ArrayCollection;

    import mx.core.FlexGlobals;

    import mx.utils.UIDUtil;

    public class Updater {

        private static const ATS_DOWNLOAD_URL:String = "http://www.actiontestscript.com"
        private static const DEFAULT_DELAY:Number =  3600000 // once a hour

        public static var shared:Updater = new Updater()

        private var updateTimer:Timer
        private var installTimer:Timer

        [Bindable]
        public var updateAvailable:Boolean = false

        public function start():void {
            checkVersion()

            updateTimer = new Timer(DEFAULT_DELAY, 0)
            updateTimer.addEventListener(TimerEvent.TIMER, timerHandler, false, 0, true)
            updateTimer.start()
        }

        public function stop():void {
            if (updateTimer) {
                updateTimer.stop()
                updateTimer.removeEventListener(TimerEvent.TIMER, timerHandler)
                updateTimer = null
            }

            if (installTimer) {
                installTimer.stop()
                installTimer.removeEventListener(TimerEvent.TIMER, installTimerHandler)
                installTimer = null
            }
        }

        private function timerHandler(event:TimerEvent):void {
            checkVersion()
        }

        private function checkVersion():void {
            const loader:URLLoader = new URLLoader();
            loader.addEventListener(Event.COMPLETE, onLoaderComponentsComplete);
            loader.load(new URLRequest(ATS_DOWNLOAD_URL + "/mobile.php?os=" + Settings.osName + "&" + UIDUtil.createUID()));
        }

        private var tempFile:File

        private function onLoaderComponentsComplete(event:Event):void {
            var loader:URLLoader = URLLoader(event.target)
            loader.removeEventListener(Event.COMPLETE, onLoaderComponentsComplete)
            const data:String = loader.data

            try {
                var jsonData:Object = JSON.parse(data) as Object
            } catch (err:Error) {
                trace("ERROR : " + err.message)
            }

            if (!jsonData.hasOwnProperty("release")) {
                trace("ERROR : BAD JSON")
                return
            }

            const version:String = jsonData.release.version
            if (version == FlexGlobals.topLevelApplication.appVersion) {
                return
            }

            tempFile = File.cacheDirectory.resolvePath("AtsMobileStation_" + version + ".zip")
            if (!tempFile.exists) {
                downloadZipFile(ATS_DOWNLOAD_URL + "/" + jsonData.release.path)
            } else {
                if (Settings.getInstance().automaticUpdateEnabled) {
                    install()
                } else {
                    updateAvailable = true
                }
            }
        }

        private function downloadZipFile(url:String):void {
            var urlStream:URLStream = new URLStream()
            urlStream.addEventListener(Event.COMPLETE, urlStreamCompleteHandler, false, 0, true)

            var urlRequest:URLRequest = new URLRequest(url)
            urlStream.load(urlRequest)
        }

        private function urlStreamCompleteHandler(event:Event):void {
            var urlStream:URLStream = URLStream(event.target)
            urlStream.removeEventListener(Event.COMPLETE, urlStreamCompleteHandler)

            var data:ByteArray = new ByteArray()
            urlStream.readBytes(data)
            urlStream.close()

            var fileStream:FileStream = new FileStream()
            fileStream.addEventListener(Event.CLOSE, fileStreamCloseHandler, false, 0, true)

            try {
                fileStream.openAsync(tempFile, FileMode.WRITE)
                fileStream.writeBytes(data)
            } catch (e:Error) {
            } finally {
                fileStream.close()
            }
        }

        private function fileStreamCloseHandler(event:Event):void {
            var fileStream:FileStream = FileStream(event.target)
            fileStream.removeEventListener(Event.CLOSE, fileStreamCloseHandler)

            updateAvailable = true
            install()
        }

        public function install():void {
            if (!canInstall()) {
                trace("ERROR : test in progress...")
                if (Settings.getInstance().automaticUpdateEnabled) {
                    startInstallTimer()
                }
            } else {
                FlexGlobals.topLevelApplication.closeAll()
                NativeApplication.nativeApplication.exit();

                var python:Python = new Python()
                python.updateApp(tempFile, FlexGlobals.topLevelApplication.appName)
            }
        }

        private static function canInstall():Boolean {
            var devices:ArrayCollection = FlexGlobals.topLevelApplication.devices.collection
            for each (var device:RunningDevice in devices) {
                if (device.locked) {
                    return false
                }
            }

            return true
        }

        private function startInstallTimer():void {
            // retry in 5 minutes
            installTimer = new Timer(1000 * 60 * 5, 1)
            installTimer.addEventListener(TimerEvent.TIMER, installTimerHandler, false, 0, true)
            installTimer.start()
        }

        private function installTimerHandler(event:TimerEvent):void {
            var timer:Timer = Timer(event.target)
            timer.removeEventListener(TimerEvent.TIMER, installTimerHandler)

            install()
        }
    }
}