package flash.events
{
    import flash.net.*;

    public class DRMAuthenticateEvent extends Event
    {
        private var m_header:String;
        private var m_userPrompt:String;
        private var m_passPrompt:String;
        private var m_urlPrompt:String;
        private var m_authenticationType:String;
        private var m_netstream:NetStream;
        public static const DRM_AUTHENTICATE:String = "drmAuthenticate";
        public static const AUTHENTICATION_TYPE_DRM:String = "drm";
        public static const AUTHENTICATION_TYPE_PROXY:String = "proxy";

        public function DRMAuthenticateEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:String = "", param5:String = "", param6:String = "", param7:String = "", param8:String = "", param9:NetStream = null)
        {
            super(param1, param2, param3);
            this.m_header = param4;
            this.m_userPrompt = param5;
            this.m_passPrompt = param6;
            this.m_urlPrompt = param7;
            this.m_authenticationType = param8;
            this.m_netstream = param9;
            return;
        }// end function

        override public function clone() : Event
        {
            return new DRMAuthenticateEvent(type, bubbles, cancelable, this.m_header, this.m_userPrompt, this.m_passPrompt, this.m_urlPrompt, this.m_authenticationType, this.m_netstream);
        }// end function

        override public function toString() : String
        {
            return formatToString("DRMAuthenticateEvent", "type", "bubbles", "cancelable", "eventPhase", "header", "usernamePrompt", "passwordPrompt", "urlPrompt", "authenticationType");
        }// end function

        public function get header() : String
        {
            return this.m_header;
        }// end function

        public function get usernamePrompt() : String
        {
            return this.m_userPrompt;
        }// end function

        public function get passwordPrompt() : String
        {
            return this.m_passPrompt;
        }// end function

        public function get urlPrompt() : String
        {
            return this.m_urlPrompt;
        }// end function

        public function get authenticationType() : String
        {
            return this.m_authenticationType;
        }// end function

        public function get netstream() : NetStream
        {
            return this.m_netstream;
        }// end function

    }
}