package flash.utils
{

    dynamic public class Dictionary extends Object
    {

        public function Dictionary(param1:Boolean = false)
        {
            this.init(param1);
            return;
        }// end function

        private function init(param1:Boolean) : void;

        prototype.toJSON = function (param1:String)
        {
            return "Dictionary";
        }// end function
        ;
        _dontEnumPrototype(prototype);
    }
}