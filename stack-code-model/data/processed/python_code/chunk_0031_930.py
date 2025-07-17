package flash.events
{
    import flash.net.drm.*;

    public class DRMStatusEvent extends Event
    {
        private var m_detail:String;
        private var m_voucher:DRMVoucher;
        private var m_metadata:DRMContentData;
        private var m_isLocal:Boolean;
        public static const DRM_STATUS:String = "drmStatus";

        public function DRMStatusEvent(param1:String = "drmStatus", param2:Boolean = false, param3:Boolean = false, param4:DRMContentData = null, param5:DRMVoucher = null, param6:Boolean = false)
        {
            super(param1, param2, param3);
            this.m_detail = new String("DRM.voucherObtained");
            this.m_voucher = param5;
            this.m_metadata = param4;
            this.m_isLocal = param6;
            return;
        }// end function

        override public function clone() : Event
        {
            return new DRMStatusEvent(type, bubbles, cancelable, this.m_metadata, this.m_voucher, this.m_isLocal);
        }// end function

        override public function toString() : String
        {
            return formatToString("DRMStatusEvent", "type", "bubbles", "cancelable");
        }// end function

        public function get contentData() : DRMContentData
        {
            return this.m_metadata;
        }// end function

        public function set contentData(param1:DRMContentData) : void
        {
            this.m_metadata = param1;
            return;
        }// end function

        public function get voucher() : DRMVoucher
        {
            return this.m_voucher;
        }// end function

        public function set voucher(param1:DRMVoucher) : void
        {
            this.m_voucher = param1;
            return;
        }// end function

        public function get isLocal() : Boolean
        {
            return this.m_isLocal;
        }// end function

        public function set isLocal(param1:Boolean) : void
        {
            this.m_isLocal = param1;
            return;
        }// end function

    }
}