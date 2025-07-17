package flash.net
{

    final public class URLRequest extends Object
    {
        private static const kInvalidParamError:uint = 2004;

        public function URLRequest(param1:String = null)
        {
            if (param1 != null)
            {
                this.url = param1;
            }
            this.requestHeaders = [];
            return;
        }// end function

        public function get url() : String;

        public function set url(param1:String) : void;

        public function get data() : Object;

        public function set data(param1:Object) : void;

        public function get method() : String;

        public function set method(param1:String) : void
        {
            var _loc_2:* = /^(\x21|[\x23-\x26]|\x2A|\x2B|\x2D|\x2E|[\x30-\x39]|[\x41-\x5A]|[\x5E-\x7A])+$/;
            if (!_loc_2.test(param1))
            {
                Error.throwError(ArgumentError, kInvalidParamError);
            }
            this.setMethod(param1);
            return;
        }// end function

        private function setMethod(param1:String) : void;

        public function get contentType() : String;

        public function set contentType(param1:String) : void;

        public function get requestHeaders() : Array;

        public function set requestHeaders(param1:Array) : void
        {
            if (param1 != null)
            {
                this.setRequestHeaders(param1.filter(this.filterRequestHeaders));
            }
            else
            {
                this.setRequestHeaders(param1);
            }
            return;
        }// end function

        private function setRequestHeaders(param1:Array) : void;

        private function filterRequestHeaders(param1, param2:int, param3:Array) : Boolean
        {
            return true;
        }// end function

        public function get digest() : String;

        public function set digest(param1:String) : void;

        public function useRedirectedURL(param1:URLRequest, param2:Boolean = false, param3 = null, param4:String = null) : void;

        private function shouldFilterHTTPHeader(param1:String) : Boolean
        {
            return false;
        }// end function

    }
}