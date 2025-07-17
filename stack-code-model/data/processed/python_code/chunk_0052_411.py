package flash.net.drm
{
    import flash.events.*;
    import flash.net.*;
    import flash.utils.*;

    class DRMURLDownloadContext extends EventDispatcher
    {
        private var httpStatus:uint;
        private var urlLoader:URLLoader;
        private var networkTimeOutTimer:Timer;
        private var isDownloading:Boolean;

        function DRMURLDownloadContext()
        {
            this.httpStatus = 0;
            this.isDownloading = false;
            return;
        }// end function

        public function httpPostAndReceiveASync(param1:String, param2:String, param3:String, param4:ByteArray, param5:uint) : void
        {
            var _loc_7:* = null;
            var _loc_8:* = null;
            if (param5 == 0)
            {
                _loc_7 = new DRMLicenseRequestEvent(DRMLicenseRequestEvent.LICENSE_REQUEST);
                _loc_7.serverURL = param1;
                DRMManager.getDRMManager().dispatchEvent(_loc_7);
                param1 = _loc_7.serverURL;
            }
            var _loc_6:* = new URLRequest(param1);
            _loc_6.method = URLRequestMethod.POST;
            _loc_6.data = param4;
            if (param2 != null)
            {
            }
            if (param3 != null)
            {
                _loc_8 = new Array(new URLRequestHeader(param2, param3));
                _loc_6.requestHeaders = _loc_8;
            }
            this.doURLDownload(_loc_6);
            return;
        }// end function

        public function httpGetASync(param1:String) : void
        {
            var _loc_2:* = new URLRequest(param1);
            this.doURLDownload(_loc_2);
            return;
        }// end function

        private function doURLDownload(param1:URLRequest) : void
        {
            this.urlLoader = new URLLoader();
            this.urlLoader.dataFormat = URLLoaderDataFormat.BINARY;
            this.urlLoader.addEventListener(Event.COMPLETE, this.onAsyncDownloadComplete);
            this.urlLoader.addEventListener(IOErrorEvent.IO_ERROR, this.onAsyncIOError);
            this.urlLoader.addEventListener(SecurityErrorEvent.SECURITY_ERROR, this.onAsyncSecurityError);
            this.urlLoader.addEventListener(HTTPStatusEvent.HTTP_STATUS, this.onHTTPStatus);
            this.urlLoader.addEventListener(ProgressEvent.PROGRESS, this.onProgress);
            this.urlLoader.load(param1);
            this.networkTimeOutTimer = new Timer(DRMManager.networkIdleTimeout);
            this.networkTimeOutTimer.addEventListener(TimerEvent.TIMER, this.onTimer);
            this.networkTimeOutTimer.start();
            this.isDownloading = true;
            return;
        }// end function

        private function onTimer(event:TimerEvent)
        {
            if (this.isDownloading)
            {
                this.iOnTimeoutError(0);
            }
            this.cleanUp();
            return;
        }// end function

        private function onProgress(event:ProgressEvent) : void
        {
            this.networkTimeOutTimer.reset();
            this.networkTimeOutTimer.start();
            return;
        }// end function

        private function onAsyncDownloadComplete(event:Event) : void
        {
            var _loc_2:* = this.urlLoader.data as ByteArray;
            this.iOnDownloadComplete(_loc_2);
            this.cleanUp();
            return;
        }// end function

        private function onAsyncIOError(event:Event) : void
        {
            var _loc_2:* = event as IOErrorEvent;
            this.iOnIOError(this.httpStatus, _loc_2.text);
            this.cleanUp();
            return;
        }// end function

        private function onAsyncSecurityError(event:Event) : void
        {
            var _loc_2:* = event as SecurityErrorEvent;
            this.iOnSecurityError(_loc_2.text);
            this.cleanUp();
            return;
        }// end function

        private function onHTTPStatus(event:Event) : void
        {
            var _loc_2:* = event as HTTPStatusEvent;
            this.httpStatus = _loc_2.status;
            return;
        }// end function

        private function cleanUp() : void
        {
            if (this.urlLoader)
            {
                this.urlLoader.removeEventListener(Event.COMPLETE, this.onAsyncDownloadComplete);
                this.urlLoader.removeEventListener(IOErrorEvent.IO_ERROR, this.onAsyncIOError);
                this.urlLoader.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, this.onAsyncSecurityError);
                this.urlLoader.removeEventListener(HTTPStatusEvent.HTTP_STATUS, this.onHTTPStatus);
            }
            if (this.networkTimeOutTimer)
            {
                this.networkTimeOutTimer.stop();
            }
            this.isDownloading = false;
            return;
        }// end function

        private function iOnDownloadComplete(param1:ByteArray) : void;

        private function iOnTimeoutError(param1:uint) : void;

        private function iOnIOError(param1:uint, param2:String) : void;

        private function iOnSecurityError(param1:String) : void;

    }
}