package flash.media
{

    public class AVTagData extends Object
    {
        private var m_data:String;
        private var m_localTime:Number;

        public function AVTagData(param1:String, param2:Number)
        {
            this.m_data = param1;
            this.m_localTime = param2;
            return;
        }// end function

        public function get data() : String
        {
            return this.m_data;
        }// end function

        public function get localTime() : Number
        {
            return this.m_localTime;
        }// end function

    }
}