package flash.automation
{

    public class AutomationAction extends Object
    {
        private var _type:String = "";

        public function AutomationAction()
        {
            return;
        }// end function

        public function get type() : String
        {
            return this._type;
        }// end function

        public function set type(param1:String) : void
        {
            this._type = param1;
            return;
        }// end function

    }
}