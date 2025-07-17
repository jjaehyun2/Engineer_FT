package 
{

    final public class QName extends Object
    {
        public static const length:Object = 2;

        public function QName(param1 = undefined, param2 = undefined)
        {
            return;
        }// end function

        public function get localName() : String;

        public function get uri();

        function valueOf() : QName
        {
            return this;
        }// end function

        function toString() : String
        {
            if (this.uri === "")
            {
                return this.localName;
            }
            if (this.uri === null)
            {
                return "*::" + this.localName;
            }
            var _loc_1:* = this.uri.charCodeAt((this.uri.length - 1));
            var _loc_2:* = this.uri;
            if (_loc_1 >= 57344)
            {
            }
            if (_loc_1 <= 63743)
            {
                _loc_2 = _loc_2.substr(0, (_loc_2.length - 1));
            }
            if (_loc_2 === "")
            {
                return this.localName;
            }
            return _loc_2 + "::" + this.localName;
        }// end function

        prototype.toString = function () : String
        {
            if (prototype === this)
            {
                return "";
            }
            if (!(this is QName))
            {
                Error.throwError(TypeError, 1004, "QName.prototype.toString");
            }
            var _loc_1:* = this;
            return _loc_1.toString();
        }// end function
        ;
        _dontEnumPrototype(prototype);
    }
}