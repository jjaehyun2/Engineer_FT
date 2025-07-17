package flash.events
{
    import flash.utils.*;

    public class SampleDataEvent extends Event
    {
        private var m_position:Number;
        private var m_data:ByteArray;
        public static const SAMPLE_DATA:String = "sampleData";

        public function SampleDataEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:Number = 0, param5:ByteArray = null)
        {
            super(param1, param2, param3);
            this.m_position = param4;
            this.m_data = param5;
            return;
        }// end function

        override public function clone() : Event
        {
            return new SampleDataEvent(type, bubbles, cancelable, this.position, this.data);
        }// end function

        override public function toString() : String
        {
            return formatToString("SampleDataEvent", "type", "bubbles", "cancelable", "eventPhase", "position", "data");
        }// end function

        public function get position() : Number
        {
            return this.m_position;
        }// end function

        public function set position(param1:Number)
        {
            this.m_position = param1;
            return;
        }// end function

        public function get data() : ByteArray
        {
            return this.m_data;
        }// end function

        public function set data(param1:ByteArray)
        {
            this.m_data = param1;
            return;
        }// end function

    }
}