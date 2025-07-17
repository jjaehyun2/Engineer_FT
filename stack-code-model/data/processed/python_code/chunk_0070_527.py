package flash.net.drm
{

    public class DRMPlaybackTimeWindow extends Object
    {
        private var m_length:uint;
        private var m_startDate:Date;
        private var m_endDate:Date;

        public function DRMPlaybackTimeWindow()
        {
            return;
        }// end function

        private function init(param1:Number, param2:Number, param3:Number) : void
        {
            this.m_length = param1;
            if (param2 > 0)
            {
                this.m_startDate = new Date(param2 * 1000);
            }
            if (param3 > 0)
            {
                this.m_endDate = new Date(param3 * 1000);
            }
            return;
        }// end function

        public function get period() : uint
        {
            return this.m_length;
        }// end function

        public function get startDate() : Date
        {
            return this.m_startDate;
        }// end function

        public function get endDate() : Date
        {
            return this.m_endDate;
        }// end function

    }
}