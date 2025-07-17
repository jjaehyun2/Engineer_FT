package flash.events
{

    public class DRMReturnVoucherCompleteEvent extends Event
    {
        private var m_serverURL:String;
        private var m_licenseID:String;
        private var m_policyID:String;
        private var m_numberOfVouchersReturned:int;
        public static const RETURN_VOUCHER_COMPLETE:String = "returnVoucherComplete";

        public function DRMReturnVoucherCompleteEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:String = null, param5:String = null, param6:String = null, param7:int = 0)
        {
            super(param1, param2, param3);
            this.m_serverURL = param4;
            this.m_licenseID = param5;
            this.m_policyID = param6;
            this.m_numberOfVouchersReturned = param7;
            return;
        }// end function

        override public function clone() : Event
        {
            return new DRMReturnVoucherCompleteEvent(type, bubbles, cancelable, this.serverURL, this.licenseID, this.policyID, this.numberOfVouchersReturned);
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

        public function get licenseID() : String
        {
            return this.m_licenseID;
        }// end function

        public function set licenseID(param1:String) : void
        {
            this.m_licenseID = param1;
            return;
        }// end function

        public function get policyID() : String
        {
            return this.m_policyID;
        }// end function

        public function set policyID(param1:String) : void
        {
            this.m_policyID = param1;
            return;
        }// end function

        public function get numberOfVouchersReturned() : int
        {
            return this.m_numberOfVouchersReturned;
        }// end function

        public function set numberOfVouchersReturned(param1:int) : void
        {
            this.m_numberOfVouchersReturned = param1;
            return;
        }// end function

    }
}