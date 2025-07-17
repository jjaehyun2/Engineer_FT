package flash.events
{

    class DRMCustomProperties extends Object
    {

        function DRMCustomProperties()
        {
            return;
        }// end function

        private static function createObj() : Object
        {
            return new Object();
        }// end function

        private static function setCustomProp(param1:Object, param2:String, param3:String) : void
        {
            param1[param2] = param3;
            return;
        }// end function

        private static function setCustomProp15(param1:Object, param2:String, param3:String) : void
        {
            param1[unescape(param2.replace(/\+/g, " "))] = unescape(param3.replace(/\+/g, " "));
            return;
        }// end function

    }
}