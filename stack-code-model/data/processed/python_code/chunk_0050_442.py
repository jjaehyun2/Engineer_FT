package flash.net.drm
{
    import flash.events.*;
    import flash.utils.*;

    class DRMManagerSession extends EventDispatcher
    {
        private var m_metadata:DRMContentData;
        private var m_checkStatusTimer:Timer;
        public var m_isInSession:Boolean;
        static const STATUS_READY:uint = 0;
        static const STATUS_NOTREADY:uint = 1;
        static const STATUS_FAILED:uint = 2;
        static const STATUS_UNKNOWN:uint = 3;

        function DRMManagerSession()
        {
            this.m_isInSession = false;
            return;
        }// end function

        public function onSessionError() : void
        {
            return;
        }// end function

        public function onSessionComplete() : void
        {
            return;
        }// end function

        public function setTimerUp() : void
        {
            if (this.m_checkStatusTimer == null)
            {
                this.m_checkStatusTimer = new Timer(100, 0);
            }
            this.m_checkStatusTimer.addEventListener(TimerEvent.TIMER, this.onCheckStatus);
            this.m_checkStatusTimer.start();
            return;
        }// end function

        public function get metadata() : DRMContentData
        {
            return this.m_metadata;
        }// end function

        public function set metadata(param1:DRMContentData) : void
        {
            this.m_metadata = param1;
            return;
        }// end function

        public function checkStatus() : uint
        {
            return this.checkStatusInner();
        }// end function

        private function isAutoResetError(param1:uint) : Boolean;

        private function doAutoReset() : void
        {
            var _loc_1:* = this.getLastError();
            if (this.isAutoResetError(_loc_1))
            {
                DRMManager.getDRMManagerInternal().resetDRMVouchersInternal(true);
            }
            return;
        }// end function

        private function onCheckStatus(event:TimerEvent)
        {
            var _loc_2:* = this.checkStatus();
            if (_loc_2 != STATUS_NOTREADY)
            {
                this.m_isInSession = false;
                this.m_checkStatusTimer.stop();
                if (_loc_2 == STATUS_READY)
                {
                    this.onSessionComplete();
                }
                else
                {
                    this.doAutoReset();
                    this.onSessionError();
                }
                this.m_checkStatusTimer.removeEventListener(TimerEvent.TIMER, this.onCheckStatus);
                this.m_checkStatusTimer = null;
            }
            return;
        }// end function

        public function getLastError() : uint;

        public function getLastSubErrorID() : uint;

        public function getLastServerErrorString() : String;

        public function issueDRMStatusEvent(param1:DRMContentData, param2:DRMVoucher)
        {
            this.issueDRMStatusEventInner(DRMStatusEvent.DRM_STATUS, param1, param2, false);
            return;
        }// end function

        private function issueDRMStatusEventInner(param1:String, param2:DRMContentData, param3:DRMVoucher, param4:Boolean) : void;

        public function issueDRMErrorEvent(param1:DRMContentData, param2:int, param3:int, param4:String) : void;

        public function errorCodeToThrow(param1:uint) : void;

        private function checkStatusInner() : uint;

    }
}