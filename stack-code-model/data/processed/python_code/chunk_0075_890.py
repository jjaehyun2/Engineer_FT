package flash.events
{

    public class AccelerometerEvent extends Event
    {
        private var m_accelerationX:Number;
        private var m_accelerationY:Number;
        private var m_accelerationZ:Number;
        private var m_timestamp:Number;
        public static const UPDATE:String = "update";

        public function AccelerometerEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:Number = 0, param5:Number = 0, param6:Number = 0, param7:Number = 0)
        {
            super(param1, param2, param3);
            this.m_accelerationX = param5;
            this.m_accelerationY = param6;
            this.m_accelerationZ = param7;
            this.m_timestamp = param4;
            return;
        }// end function

        override public function clone() : Event
        {
            return new AccelerometerEvent(type, bubbles, cancelable, this.m_timestamp, this.m_accelerationX, this.m_accelerationY, this.m_accelerationZ);
        }// end function

        override public function toString() : String
        {
            return formatToString("AccelerometerEvent", "type", "bubbles", "cancelable", "timestamp", "accelerationX", "accelerationY", "accelerationZ");
        }// end function

        public function get accelerationX() : Number
        {
            return this.m_accelerationX;
        }// end function

        public function set accelerationX(param1:Number) : void
        {
            this.m_accelerationX = param1;
            return;
        }// end function

        public function get accelerationY() : Number
        {
            return this.m_accelerationY;
        }// end function

        public function set accelerationY(param1:Number) : void
        {
            this.m_accelerationY = param1;
            return;
        }// end function

        public function get accelerationZ() : Number
        {
            return this.m_accelerationZ;
        }// end function

        public function set accelerationZ(param1:Number) : void
        {
            this.m_accelerationZ = param1;
            return;
        }// end function

        public function get timestamp() : Number
        {
            return this.m_timestamp;
        }// end function

        public function set timestamp(param1:Number) : void
        {
            this.m_timestamp = param1;
            return;
        }// end function

    }
}