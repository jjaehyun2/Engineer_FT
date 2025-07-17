package flash.security
{

    public class X500DistinguishedName extends Object
    {

        public function X500DistinguishedName()
        {
            return;
        }// end function

        public function get commonName() : String;

        public function get organizationName() : String;

        public function get organizationalUnitName() : String;

        public function get localityName() : String;

        public function get stateOrProvinceName() : String;

        public function get countryName() : String;

        public function toString() : String;

    }
}