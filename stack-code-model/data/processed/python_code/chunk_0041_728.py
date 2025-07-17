package flash.net
{

    final public class NetStreamMulticastInfo extends Object
    {
        private var m_sendDataBytesPerSecond:Number;
        private var m_sendControlBytesPerSecond:Number;
        private var m_receiveDataBytesPerSecond:Number;
        private var m_receiveControlBytesPerSecond:Number;
        private var m_bytesPushedToPeers:Number;
        private var m_fragmentsPushedToPeers:Number;
        private var m_bytesRequestedByPeers:Number;
        private var m_fragmentsRequestedByPeers:Number;
        private var m_bytesPushedFromPeers:Number;
        private var m_fragmentsPushedFromPeers:Number;
        private var m_bytesRequestedFromPeers:Number;
        private var m_fragmentsRequestedFromPeers:Number;
        private var m_sendControlBytesPerSecondToServer:Number;
        private var m_receiveDataBytesPerSecondFromServer:Number;
        private var m_bytesReceivedFromServer:Number;
        private var m_fragmentsReceivedFromServer:Number;
        private var m_receiveDataBytesPerSecondFromIPMulticast:Number;
        private var m_bytesReceivedFromIPMulticast:Number;
        private var m_fragmentsReceivedFromIPMulticast:Number;

        public function NetStreamMulticastInfo(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number, param8:Number, param9:Number, param10:Number, param11:Number, param12:Number, param13:Number, param14:Number, param15:Number, param16:Number, param17:Number, param18:Number, param19:Number)
        {
            this.m_sendDataBytesPerSecond = param1;
            this.m_sendControlBytesPerSecond = param2;
            this.m_receiveDataBytesPerSecond = param3;
            this.m_receiveControlBytesPerSecond = param4;
            this.m_bytesPushedToPeers = param5;
            this.m_fragmentsPushedToPeers = param6;
            this.m_bytesRequestedByPeers = param7;
            this.m_fragmentsRequestedByPeers = param8;
            this.m_bytesPushedFromPeers = param9;
            this.m_fragmentsPushedFromPeers = param10;
            this.m_bytesRequestedFromPeers = param11;
            this.m_fragmentsRequestedFromPeers = param12;
            this.m_sendControlBytesPerSecondToServer = param13;
            this.m_receiveDataBytesPerSecondFromServer = param14;
            this.m_bytesReceivedFromServer = param15;
            this.m_fragmentsReceivedFromServer = param16;
            this.m_receiveDataBytesPerSecondFromIPMulticast = param17;
            this.m_bytesReceivedFromIPMulticast = param18;
            this.m_fragmentsReceivedFromIPMulticast = param19;
            return;
        }// end function

        public function get sendDataBytesPerSecond() : Number
        {
            return this.m_sendDataBytesPerSecond;
        }// end function

        public function get sendControlBytesPerSecond() : Number
        {
            return this.m_sendControlBytesPerSecond;
        }// end function

        public function get receiveDataBytesPerSecond() : Number
        {
            return this.m_receiveDataBytesPerSecond;
        }// end function

        public function get receiveControlBytesPerSecond() : Number
        {
            return this.m_receiveControlBytesPerSecond;
        }// end function

        public function get bytesPushedToPeers() : Number
        {
            return this.m_bytesPushedToPeers;
        }// end function

        public function get fragmentsPushedToPeers() : Number
        {
            return this.m_fragmentsPushedToPeers;
        }// end function

        public function get bytesRequestedByPeers() : Number
        {
            return this.m_bytesRequestedByPeers;
        }// end function

        public function get fragmentsRequestedByPeers() : Number
        {
            return this.m_fragmentsRequestedByPeers;
        }// end function

        public function get bytesPushedFromPeers() : Number
        {
            return this.m_bytesPushedFromPeers;
        }// end function

        public function get fragmentsPushedFromPeers() : Number
        {
            return this.m_fragmentsPushedFromPeers;
        }// end function

        public function get bytesRequestedFromPeers() : Number
        {
            return this.m_bytesRequestedFromPeers;
        }// end function

        public function get fragmentsRequestedFromPeers() : Number
        {
            return this.m_fragmentsRequestedFromPeers;
        }// end function

        public function get sendControlBytesPerSecondToServer() : Number
        {
            return this.m_sendControlBytesPerSecondToServer;
        }// end function

        public function get receiveDataBytesPerSecondFromServer() : Number
        {
            return this.m_receiveDataBytesPerSecondFromServer;
        }// end function

        public function get bytesReceivedFromServer() : Number
        {
            return this.m_bytesReceivedFromServer;
        }// end function

        public function get fragmentsReceivedFromServer() : Number
        {
            return this.m_fragmentsReceivedFromServer;
        }// end function

        public function get receiveDataBytesPerSecondFromIPMulticast() : Number
        {
            return this.m_receiveDataBytesPerSecondFromIPMulticast;
        }// end function

        public function get bytesReceivedFromIPMulticast() : Number
        {
            return this.m_bytesReceivedFromIPMulticast;
        }// end function

        public function get fragmentsReceivedFromIPMulticast() : Number
        {
            return this.m_fragmentsReceivedFromIPMulticast;
        }// end function

        public function toString() : String
        {
            return "sendDataBytesPerSecond=" + this.m_sendDataBytesPerSecond + " sendControlBytesPerSecond=" + this.m_sendControlBytesPerSecond + " receiveDataBytesPerSecond=" + this.m_receiveDataBytesPerSecond + " receiveControlBytesPerSecond=" + this.m_receiveControlBytesPerSecond + " bytesPushedToPeers=" + this.m_bytesPushedToPeers + " fragmentsPushedToPeers=" + this.m_fragmentsPushedToPeers + " bytesRequestedByPeers=" + this.m_bytesRequestedByPeers + " fragmentsRequestedByPeers=" + this.m_fragmentsRequestedByPeers + " bytesPushedFromPeers=" + this.m_bytesPushedFromPeers + " fragmentsPushedFromPeers=" + this.m_fragmentsPushedFromPeers + " bytesRequestedFromPeers=" + this.m_bytesRequestedFromPeers + " fragmentsRequestedFromPeers=" + this.m_fragmentsRequestedFromPeers + " sendControlBytesPerSecondToServer=" + this.m_sendControlBytesPerSecondToServer + " receiveDataBytesPerSecondFromServer=" + this.m_receiveDataBytesPerSecondFromServer + " bytesReceivedFromServer=" + this.m_bytesReceivedFromServer + " fragmentsReceivedFromServer=" + this.m_fragmentsReceivedFromServer + " receiveDataBytesPerSecondFromIPMulticast=" + this.m_receiveDataBytesPerSecondFromIPMulticast + " bytesReceivedFromIPMulticast=" + this.m_bytesReceivedFromIPMulticast + " fragmentsReceivedFromIPMulticast=" + this.m_fragmentsReceivedFromIPMulticast;
        }// end function

    }
}