package flash.errors
{

    public class DRMManagerError extends Error
    {
        private var _subErrorID:int;

        public function DRMManagerError(param1:String, param2:int, param3:int)
        {
            super(param1, param2);
            this._subErrorID = param3;
            return;
        }// end function

        public function get subErrorID() : int
        {
            return this._subErrorID;
        }// end function

        public function toString() : String
        {
            var _loc_1:* = "DRMManagerError: \'" + message + "\', error ID:\'" + errorID.toString() + "\', subErrorID:\'" + this._subErrorID.toString() + "\'";
            return _loc_1;
        }// end function

    }
}