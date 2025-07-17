package 
{
    import Object.*;

    dynamic public class Object
    {
        public static const length:int = 1;

        public function Object()
        {
            return;
        }// end function

        function isPrototypeOf(param1 = undefined) : Boolean
        {
            return _isPrototypeOf(this, param1);
        }// end function

        function hasOwnProperty(param1 = undefined) : Boolean
        {
            return _hasOwnProperty(this, param1);
        }// end function

        function propertyIsEnumerable(param1 = undefined) : Boolean
        {
            return _propertyIsEnumerable(this, param1);
        }// end function

        private static function _hasOwnProperty(param1, param2:String) : Boolean;

        private static function _propertyIsEnumerable(param1, param2:String) : Boolean;

        static function _setPropertyIsEnumerable(param1, param2:String, param3:Boolean) : void;

        private static function _isPrototypeOf(param1, param2) : Boolean;

        private static function _toString(param1) : String;

        static function _dontEnumPrototype(param1:Object) : void
        {
            var _loc_2:* = null;
            for (_loc_2 in param1)
            {
                
                _setPropertyIsEnumerable(param1, _loc_2, false);
            }
            return;
        }// end function

        static function init()
        {
            return;
        }// end function

        public static function _init()
        {
            prototype.hasOwnProperty = function (param1 = undefined) : Boolean
            {
                return this.hasOwnProperty(param1);
            }// end function
            ;
            prototype.propertyIsEnumerable = function (param1 = undefined)
            {
                return this.propertyIsEnumerable(param1);
            }// end function
            ;
            prototype.setPropertyIsEnumerable = function (param1:String, param2:Boolean) : void
            {
                _setPropertyIsEnumerable(this, param1, param2);
                return;
            }// end function
            ;
            prototype.isPrototypeOf = function (param1 = undefined) : Boolean
            {
                return this.isPrototypeOf(param1);
            }// end function
            ;
            var _loc_2:* = function () : String
            {
                return _toString(this);
            }// end function
            ;
            prototype.toLocaleString = function () : String
            {
                return _toString(this);
            }// end function
            ;
            prototype.toString = _loc_2;
            prototype.valueOf = function ()
            {
                return this;
            }// end function
            ;
            _dontEnumPrototype(prototype);
            return;
        }// end function

    }
}