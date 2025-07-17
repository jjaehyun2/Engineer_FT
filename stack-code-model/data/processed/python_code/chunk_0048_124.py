package flash.events
{

    public class DRMLicenseRequestEvent extends Event
    {
        private var m_serverURL:String;
        public static const LICENSE_REQUEST:String = "licenseRequest";

        public function DRMLicenseRequestEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:String = null)
        {
            super(param1, param2, param3);
            this.m_serverURL = param4;
            return;
        }// end function

        override public function clone() : Event
        {
            return new DRMLicenseRequestEvent(type, bubbles, cancelable, this.serverURL);
        }// end function

        public function get serverURL() : String
        {
            return this.m_serverURL;
        }// end function

        public function set serverURL(param1:String) : void
        {
            this.m_serverURL = param1;
            return;
        }// end function

    }
}