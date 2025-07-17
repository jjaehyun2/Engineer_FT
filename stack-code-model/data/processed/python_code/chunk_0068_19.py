package flash.automation
{

    public class MouseAutomationAction extends AutomationAction
    {
        private var _stageX:Number = 0;
        private var _stageY:Number = 0;
        private var _delta:int = 0;
        public static const MOUSE_DOWN:String = "mouseDown";
        public static const MOUSE_MOVE:String = "mouseMove";
        public static const MOUSE_UP:String = "mouseUp";
        public static const MOUSE_WHEEL:String = "mouseWheel";
        public static const MIDDLE_MOUSE_DOWN:String = "middleMouseDown";
        public static const MIDDLE_MOUSE_UP:String = "middleMouseUp";
        public static const RIGHT_MOUSE_DOWN:String = "rightMouseDown";
        public static const RIGHT_MOUSE_UP:String = "rightMouseUp";

        public function MouseAutomationAction(param1:String, param2:Number = 0, param3:Number = 0, param4:int = 0)
        {
            super.type = param1;
            this._stageX = param2;
            this._stageY = param3;
            this._delta = param4;
            return;
        }// end function

        public function get stageX() : Number
        {
            return this._stageX;
        }// end function

        public function set stageX(param1:Number) : void
        {
            this._stageX = param1;
            return;
        }// end function

        public function get stageY() : Number
        {
            return this._stageY;
        }// end function

        public function set stageY(param1:Number) : void
        {
            this._stageY = param1;
            return;
        }// end function

        public function get delta() : int
        {
            return this._delta;
        }// end function

        public function set delta(param1:int) : void
        {
            this._delta = param1;
            return;
        }// end function

    }
}