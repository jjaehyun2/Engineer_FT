package flash.system
{
    import __AS3__.vec.*;
    import flash.utils.*;

    final public class ApplicationDomain extends Object
    {

        public function ApplicationDomain(param1:ApplicationDomain = null)
        {
            this.ctor(param1);
            return;
        }// end function

        private function ctor(param1:ApplicationDomain) : void;

        public function get parentDomain() : ApplicationDomain;

        public function getDefinition(param1:String) : Object;

        public function hasDefinition(param1:String) : Boolean;

        public function getQualifiedDefinitionNames() : Vector.<String>;

        public function get domainMemory() : ByteArray;

        public function set domainMemory(param1:ByteArray);

        public static function get currentDomain() : ApplicationDomain;

        public static function get MIN_DOMAIN_MEMORY_LENGTH() : uint;

    }
}