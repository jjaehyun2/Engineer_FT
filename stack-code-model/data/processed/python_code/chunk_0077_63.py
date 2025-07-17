package flash.net.drm
{
    import flash.events.*;
    import flash.utils.*;

    class DRMModuleCycleProvider extends Object
    {
        private var m_heartBeatTimer:Timer;

        function DRMModuleCycleProvider()
        {
            return;
        }// end function

        private function startTimer() : void
        {
            if (this.m_heartBeatTimer == null)
            {
                this.m_heartBeatTimer = new Timer(30, 0);
                this.m_heartBeatTimer.addEventListener(TimerEvent.TIMER, this.onHeartBeat);
            }
            this.m_heartBeatTimer.start();
            return;
        }// end function

        private function onHeartBeat(event:TimerEvent)
        {
            var _loc_2:* = this.iHeartBeat();
            if (!_loc_2)
            {
                this.m_heartBeatTimer.stop();
                this.m_heartBeatTimer.removeEventListener(TimerEvent.TIMER, this.onHeartBeat);
            }
            return;
        }// end function

        private function iHeartBeat() : Boolean;

    }
}