package flash.net.drm
{

    final public class VoucherAccessInfo extends Object
    {
        private var m_deviceGroup:DRMDeviceGroup;
        private var m_displayName:String;
        private var m_authMethod:String;
        private var m_domain:String;
        private var m_policyID:String;

        public function VoucherAccessInfo()
        {
            return;
        }// end function

        public function get displayName() : String
        {
            return this.m_displayName;
        }// end function

        public function get authenticationMethod() : String
        {
            return this.m_authMethod;
        }// end function

        public function get domain() : String
        {
            return this.m_domain;
        }// end function

        public function get policyID() : String
        {
            return this.m_policyID;
        }// end function

        public function get deviceGroup() : DRMDeviceGroup
        {
            return this.m_deviceGroup;
        }// end function

        private function setDeviceGroup(param1:DRMDeviceGroup)
        {
            this.m_deviceGroup = param1;
            return;
        }// end function

        private function setFields(param1:String, param2:String, param3:String, param4:String)
        {
            this.m_displayName = param1;
            this.m_authMethod = param2;
            this.m_domain = param3;
            this.m_policyID = param4;
            return;
        }// end function

    }
}