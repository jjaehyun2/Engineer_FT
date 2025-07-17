package flash.net.drm
{

    final public class DRMDeviceGroup extends Object
    {
        private var m_authMethod:String;
        private var m_url:String;
        private var m_domain:String;

        public function DRMDeviceGroup()
        {
            return;
        }// end function

        public function get serverURL() : String
        {
            return this.m_url;
        }// end function

        public function get authenticationMethod() : String
        {
            return this.m_authMethod;
        }// end function

        public function get domain() : String
        {
            return this.m_domain;
        }// end function

        public function get name() : String;

        public function set name(param1:String) : void;

        private function setFields(param1:String, param2:String, param3:String)
        {
            this.m_url = param1;
            this.m_authMethod = param2;
            this.m_domain = param3;
            return;
        }// end function

    }
}