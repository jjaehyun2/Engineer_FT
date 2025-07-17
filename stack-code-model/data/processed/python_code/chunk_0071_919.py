package flash.ui
{

    final public class Mouse extends Object
    {

        public function Mouse()
        {
            return;
        }// end function

        public static function hide() : void;

        public static function show() : void;

        public static function get supportsCursor() : Boolean;

        public static function get cursor() : String;

        public static function set cursor(param1:String) : void;

        public static function registerCursor(param1:String, param2:MouseCursorData) : void;

        public static function unregisterCursor(param1:String) : void;

        public static function get supportsNativeCursor() : Boolean;

    }
}