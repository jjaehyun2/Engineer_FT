package flash.net.drm
{
    import __AS3__.vec.*;
    import flash.utils.*;

    public class DRMContentData extends Object
    {
        private var m_licenseID:String;
        private var m_domain:String;
        private var m_voucherAccessInfo:Vector.<VoucherAccessInfo>;
        private static var m_internalOnly:ByteArray = new ByteArray();

        public function DRMContentData(param1:ByteArray = null)
        {
            var _loc_2:* = this.setRawMetadataInner(param1);
            if (_loc_2 != 0)
            {
                this.errorCodeToThrow(_loc_2);
            }
            return;
        }// end function

        public function get serverURL() : String
        {
            return this.FMRMSURL;
        }// end function

        private function get FMRMSURL() : String;

        public function get authenticationMethod() : String;

        public function get licenseID() : String
        {
            if (this.m_licenseID == null)
            {
                this.m_licenseID = this.getLicenseIDInner();
            }
            return this.m_licenseID;
        }// end function

        public function get domain() : String
        {
            if (this.m_domain == null)
            {
                this.m_domain = this.getDomainInner();
            }
            return this.m_domain;
        }// end function

        public function getVoucherAccessInfo() : Vector.<VoucherAccessInfo>
        {
            if (this.m_voucherAccessInfo == null)
            {
                this.populateVoucherAccessInfo();
            }
            return this.m_voucherAccessInfo;
        }// end function

        private function getLicenseIDInner() : String;

        private function getDomainInner() : String;

        private function setRawMetadataInner(param1:ByteArray) : uint;

        private function errorCodeToThrow(param1:uint) : void;

        private function populateVoucherAccessInfo() : void;

        private function addVoucherAccessInfo(param1:VoucherAccessInfo) : void
        {
            if (this.m_voucherAccessInfo == null)
            {
                this.m_voucherAccessInfo = new Vector.<VoucherAccessInfo>;
            }
            this.m_voucherAccessInfo.push(param1);
            return;
        }// end function

    }
}