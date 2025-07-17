package adobe.utils
{
    import flash.events.*;

    final public class ProductManager extends EventDispatcher
    {

        public function ProductManager(param1:String = null, param2:Boolean = false)
        {
            this.ctor(param1, param2);
            return;
        }// end function

        private function ctor(param1:String, param2:Boolean) : void;

        public function get running() : Boolean;

        public function get installed() : Boolean;

        public function launch(param1:String = null) : Boolean;

        public function get installedVersion() : String;

        public function download(param1:String = null, param2:String = null, param3:Array = null) : Boolean
        {
            var _loc_5:* = 0;
            var _loc_6:* = 0;
            var _loc_4:* = null;
            if (param2 != null)
            {
                _loc_4 = new String();
                if (param3 != null)
                {
                    _loc_5 = param3.length;
                    _loc_6 = 0;
                    while (_loc_6 < _loc_5)
                    {
                        
                        _loc_4 = _loc_4 + (this.validate(param3[_loc_6]) + "/");
                        _loc_6 = _loc_6 + 1;
                    }
                }
                _loc_4 = _loc_4 + this.validate(param2);
            }
            return this.doDownload(param1, _loc_4);
        }// end function

        private function doDownload(param1:String, param2:String) : Boolean;

        private function validate(param1:String) : String
        {
            var _loc_2:* = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_";
            var _loc_3:* = param1.length;
            var _loc_4:* = 0;
            while (_loc_4 < _loc_3)
            {
                
                if (_loc_2.indexOf(param1.charAt(_loc_4)) == -1)
                {
                    throw new ArgumentError();
                }
                _loc_4 = _loc_4 + 1;
            }
            return param1;
        }// end function

        public function doSelfUpgrade(param1:String) : Boolean;

        public static function get isAllowed() : Boolean;

    }
}