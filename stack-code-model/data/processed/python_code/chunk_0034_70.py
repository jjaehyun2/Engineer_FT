package flash.security
{
    import flash.utils.*;

    public class X509Certificate extends Object
    {

        public function X509Certificate()
        {
            return;
        }// end function

        public function get version() : uint;

        public function get serialNumber() : String;

        public function get signatureAlgorithmOID() : String;

        public function get signatureAlgorithmParams() : ByteArray;

        public function get issuer() : X500DistinguishedName;

        public function get validNotBefore() : Date;

        public function get validNotAfter() : Date;

        public function get subject() : X500DistinguishedName;

        public function get subjectPublicKeyAlgorithmOID() : String;

        public function get subjectPublicKey() : String;

        public function get issuerUniqueID() : String;

        public function get subjectUniqueID() : String;

        public function get encoded() : ByteArray;

    }
}