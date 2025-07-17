package flash.events
{

    public class FullScreenEvent extends ActivityEvent
    {
        private var m_fullScreen:Boolean;
        private var m_interactive:Boolean;
        public static const FULL_SCREEN:String = "fullScreen";
        public static const FULL_SCREEN_INTERACTIVE_ACCEPTED:String = "fullScreenInteractiveAccepted";

        public function FullScreenEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:Boolean = false, param5:Boolean = false)
        {
            super(param1, param2, param3);
            this.m_fullScreen = param4;
            this.m_interactive = param5;
            return;
        }// end function

        override public function clone() : Event
        {
            return new FullScreenEvent(type, bubbles, cancelable, this.fullScreen, this.interactive);
        }// end function

        override public function toString() : String
        {
            return formatToString("FullScreenEvent", "type", "bubbles", "cancelable", "eventPhase", "fullScreen", "interactive");
        }// end function

        public function get fullScreen() : Boolean
        {
            return this.m_fullScreen;
        }// end function

        public function get interactive() : Boolean
        {
            return this.m_interactive;
        }// end function

    }
}