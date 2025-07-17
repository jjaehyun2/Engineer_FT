package flash.accessibility
{
    import flash.display.*;

    final public class Accessibility extends Object
    {

        public function Accessibility()
        {
            return;
        }// end function

        public static function get active() : Boolean;

        public static function sendEvent(param1:DisplayObject, param2:uint, param3:uint, param4:Boolean = false) : void;

        public static function updateProperties() : void;

    }
}