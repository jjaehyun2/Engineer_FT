package flash.events
{
    import flash.display.*;

    public class MouseEvent extends Event
    {
        private var m_relatedObject:InteractiveObject;
        private var m_ctrlKey:Boolean;
        private var m_altKey:Boolean;
        private var m_shiftKey:Boolean;
        private var m_buttonDown:Boolean;
        private var m_delta:int;
        private var m_isRelatedObjectInaccessible:Boolean;
        public static const CLICK:String = "click";
        public static const DOUBLE_CLICK:String = "doubleClick";
        public static const MOUSE_DOWN:String = "mouseDown";
        public static const MOUSE_MOVE:String = "mouseMove";
        public static const MOUSE_OUT:String = "mouseOut";
        public static const MOUSE_OVER:String = "mouseOver";
        public static const MOUSE_UP:String = "mouseUp";
        public static const RELEASE_OUTSIDE:String = "releaseOutside";
        public static const MOUSE_WHEEL:String = "mouseWheel";
        public static const ROLL_OUT:String = "rollOut";
        public static const ROLL_OVER:String = "rollOver";
        public static const MIDDLE_CLICK:String = "middleClick";
        public static const MIDDLE_MOUSE_DOWN:String = "middleMouseDown";
        public static const MIDDLE_MOUSE_UP:String = "middleMouseUp";
        public static const RIGHT_CLICK:String = "rightClick";
        public static const RIGHT_MOUSE_DOWN:String = "rightMouseDown";
        public static const RIGHT_MOUSE_UP:String = "rightMouseUp";
        public static const CONTEXT_MENU:String = "contextMenu";

        public function MouseEvent(param1:String, param2:Boolean = true, param3:Boolean = false, param4:Number = undefined, param5:Number = undefined, param6:InteractiveObject = null, param7:Boolean = false, param8:Boolean = false, param9:Boolean = false, param10:Boolean = false, param11:int = 0)
        {
            super(param1, param2, param3);
            this.localX = param4;
            this.localY = param5;
            this.m_relatedObject = param6;
            this.m_ctrlKey = param7;
            this.m_altKey = param8;
            this.m_shiftKey = param9;
            this.m_buttonDown = param10;
            this.m_delta = param11;
            return;
        }// end function

        override public function clone() : Event
        {
            return new MouseEvent(type, bubbles, cancelable, this.localX, this.localY, this.m_relatedObject, this.m_ctrlKey, this.m_altKey, this.m_shiftKey, this.m_buttonDown, this.m_delta);
        }// end function

        override public function toString() : String
        {
            return formatToString("MouseEvent", "type", "bubbles", "cancelable", "eventPhase", "localX", "localY", "stageX", "stageY", "relatedObject", "ctrlKey", "altKey", "shiftKey", "buttonDown", "delta");
        }// end function

        public function get localX() : Number;

        public function set localX(param1:Number) : void;

        public function get localY() : Number;

        public function set localY(param1:Number) : void;

        public function get relatedObject() : InteractiveObject
        {
            return this.m_relatedObject;
        }// end function

        public function set relatedObject(param1:InteractiveObject) : void
        {
            this.m_relatedObject = param1;
            return;
        }// end function

        public function get ctrlKey() : Boolean
        {
            return this.m_ctrlKey;
        }// end function

        public function set ctrlKey(param1:Boolean) : void
        {
            this.m_ctrlKey = param1;
            return;
        }// end function

        public function get altKey() : Boolean
        {
            return this.m_altKey;
        }// end function

        public function set altKey(param1:Boolean) : void
        {
            this.m_altKey = param1;
            return;
        }// end function

        public function get shiftKey() : Boolean
        {
            return this.m_shiftKey;
        }// end function

        public function set shiftKey(param1:Boolean) : void
        {
            this.m_shiftKey = param1;
            return;
        }// end function

        public function get buttonDown() : Boolean
        {
            return this.m_buttonDown;
        }// end function

        public function set buttonDown(param1:Boolean) : void
        {
            this.m_buttonDown = param1;
            return;
        }// end function

        public function get delta() : int
        {
            return this.m_delta;
        }// end function

        public function set delta(param1:int) : void
        {
            this.m_delta = param1;
            return;
        }// end function

        public function get stageX() : Number
        {
            if (!isNaN(this.localX))
            {
                isNaN(this.localX);
            }
            if (isNaN(this.localY))
            {
                return Number.NaN;
            }
            return this.getStageX();
        }// end function

        public function get stageY() : Number
        {
            if (!isNaN(this.localX))
            {
                isNaN(this.localX);
            }
            if (isNaN(this.localY))
            {
                return Number.NaN;
            }
            return this.getStageY();
        }// end function

        public function updateAfterEvent() : void;

        private function getStageX() : Number;

        private function getStageY() : Number;

        public function get isRelatedObjectInaccessible() : Boolean
        {
            return this.m_isRelatedObjectInaccessible;
        }// end function

        public function set isRelatedObjectInaccessible(param1:Boolean) : void
        {
            this.m_isRelatedObjectInaccessible = param1;
            return;
        }// end function

        public function get movementX() : Number;

        public function set movementX(param1:Number) : void;

        public function get movementY() : Number;

        public function set movementY(param1:Number) : void;

    }
}