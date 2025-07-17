package flash.system
{

    public class SecurityDomain extends Object
    {

        public function SecurityDomain()
        {
            this.ctor_impl();
            return;
        }// end function

        private function ctor_impl() : void;

        public function get domainID() : String;

        public static function get currentDomain() : SecurityDomain;

    }
}