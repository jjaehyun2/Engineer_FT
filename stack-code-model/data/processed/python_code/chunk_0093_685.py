/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
package FinalInternalDynamicClassPackage {
    final internal dynamic class FinalInternalDynamicClass {

        var array:Array;                            // Default property
        static var statFunction:Function;           // Default Static property
        var finNumber:Number;                   // Default property
        static var finStatNumber:Number;        // Default Final Static property
        
        internal var internalArray:Array;                           // Internal property
        internal static var internalStatFunction:Function;          // Internal Static property
        internal var internalFinNumber:Number;              // Internal Final property
        internal static var internalFinStatNumber:Number;       // Internal Final Static property

        private var privDate:Date;                              // Private property
        private static var privStatString:String;               // Private Static property
        private var privFinalString:String;             // Private Final property
        private static var privFinalStaticString:String // Private Final Static property

        public var pubBoolean:Boolean;                      // Public property
        public static var pubStatObject:Object;             // Public Static property
        public var pubFinArray:Array;                   // Public Final property
        public static var pubFinalStaticNumber:Number   // Public Final Static property


        // *****************
        // Default methods
        // *****************
        function getArray() : Array { return array; }
        function setArray( a:Array ) { array = a; }
        
        
        // ************************
        // Default virtual methods
        // ************************
        virtual function getVirtualArray() : Array { return array; }
        virtual function setVirtualArray( a:Array ) { array = a; }
        
        
        // ***********************
        // Default Static methods
        // ***********************
        static function setStatFunction(f:Function) { statFunction = f; }
        static function getStatFunction() : Function { return statFunction; }

        
        // **********************
        // Default Final methods
        // **********************
        final function setFinNumber(n:Number) { finNumber = n; }
        final function getFinNumber() : Number { return finNumber; }

        
        // *****************
        // Internal methods
        // *****************
        internal function getInternalArray() : Array { return internalArray; }
        internal function setInternalArray( a:Array ) { internalArray = a; }
        
        
        // *************************
        // Internal virtual methods
        // *************************
        internal virtual function getInternalVirtualArray() : Array { return internalArray; }
        internal virtual function setInternalVirtualArray( a:Array ) { internalArray = a; }
        
        
        // ***********************
        // Internal Static methods
        // ***********************
        internal static function setInternalStatFunction(f:Function) { FinalInternalDynamicClass.internalStatFunction = f; }
        internal static function getInternalStatFunction() : Function { return FinalInternalDynamicClass.internalStatFunction; }
        
        
        // **********************
        // Internal Final methods
        // **********************
        internal final function setInternalFinNumber(n:Number) { internalFinNumber = n; }
        internal final function getInternalFinNumber() : Number { return internalFinNumber; }

        
        
        // *******************
        // Private methods
        // *******************
        private function getPrivDate() : Date { return privDate; }
        private function setPrivDate( d:Date ) { privDate = d; }
        // wrapper function
        public function testGetSetPrivDate(d:Date) : Date {
            setPrivDate(d);
            return getPrivDate();
        }
        
        
        // *******************
        // Private virutal methods
        // *******************
        private virtual function getPrivVirtualDate() : Date { return privDate; }
        private virtual function setPrivVirtualDate( d:Date ) { privDate = d; }
        // wrapper function
        public function testGetSetPrivVirtualDate(d:Date) : Date {
            setPrivVirtualDate(d);
            return getPrivVirtualDate();
        }


        // **************************
        // Private Static methods
        // **************************
        private static function setPrivStatString(s:String) { privStatString = s; }
        private static function getPrivStatString() : String { return privStatString; }
        // wrapper function
        public function testGetSetPrivStatString(s:String) : String {
            setPrivStatString(s);
            return getPrivStatString();
        }
        
        
        // **************************
        // Private Final methods
        // **************************
        private final function setPrivFinalString(s:String) { privFinalString = s; }
        private final function getPrivFinalString() : String { return privFinalString; }
        // wrapper function
        public function testGetSetPrivFinalString(s:String) : String {
            setPrivFinalString(s);
            return getPrivFinalString();
        }

        
        
        // *******************
        // Public methods
        // *******************
        public function setPubBoolean( b:Boolean ) { pubBoolean = b; }
        public function getPubBoolean() : Boolean { return pubBoolean; }
        
        
        // *******************
        // Public virtual methods
        // *******************
        public virtual function setPubVirtualBoolean( b:Boolean ) { pubBoolean = b; }
        public virtual function getPubVirtualBoolean() : Boolean { return pubBoolean; }


        // **************************
        // Public Static methods
        // **************************
        public static function setPubStatObject(o:Object) { FinalInternalDynamicClass.pubStatObject = o; }
        public static function getPubStatObject() : Object { return FinalInternalDynamicClass.pubStatObject; }


        // *******************
        // Public Final methods
        // *******************
        public final function setPubFinArray(a:Array) { pubFinArray = a; }
        public final function getPubFinArray() : Array { return pubFinArray; }


    }
    
    public class FinalInternalDynamicClassAccessor {
        private var Obj:FinalInternalDynamicClass = new FinalInternalDynamicClass();
        
        // Default method
        public function testGetSetArray(a:Array) : Array {
            Obj.setArray(a);
            return Obj.getArray();
        }
        // Default virtual method
        public function testGetSetVirtualArray(a:Array) : Array {
            Obj.setVirtualArray(a);
            return Obj.getVirtualArray();
        }
        // Default static method
        public function testGetSetStatFunction(f:Function) : Function {
            FinalInternalDynamicClass.setStatFunction(f);
            return FinalInternalDynamicClass.getStatFunction();
        }
        // Default final method
        public function testGetSetFinNumber(n:Number) : Number {
            Obj.setFinNumber(n);
            return Obj.getFinNumber();
        }
        
        // internal method
        public function testGetSetInternalArray(a:Array) : Array {
            Obj.setInternalArray(a);
            return Obj.getInternalArray();
        }
        // internal virtual method
        public function testGetSetInternalVirtualArray(a:Array) : Array {
            Obj.setInternalVirtualArray(a);
            return Obj.getInternalVirtualArray();
        }
        // internal static method
        public function testGetSetInternalStatFunction(f:Function) : Function {
            FinalInternalDynamicClass.setInternalStatFunction(f);
            return FinalInternalDynamicClass.getInternalStatFunction();
        }
        // internal final method
        public function testGetSetInternalFinNumber(n:Number) : Number {
            Obj.setInternalFinNumber(n);
            return Obj.getInternalFinNumber();
        }
        
        // private method
        public function testGetSetPrivDate(d:Date) : Date {
            return Obj.testGetSetPrivDate(d);
        }
        // private virtualmethod
        public function testGetSetPrivVirtualDate(d:Date) : Date {
            return Obj.testGetSetPrivVirtualDate(d);
        }
        // Private Static methods
        public function testGetSetPrivStatString(s:String) : String {
            return Obj.testGetSetPrivStatString(s);
        }
        // Private Final methods
        public function testGetSetPrivFinalString(s:String) : String {
            return Obj.testGetSetPrivFinalString(s);
        }
        
        // Public methods
        public function setPubBoolean( b:Boolean ) { Obj.setPubBoolean(b); }
        public function getPubBoolean() : Boolean { return Obj.getPubBoolean(); }
        // Public virtual methods
        public function setPubVirtualBoolean( b:Boolean ) { Obj.setPubVirtualBoolean(b); }
        public function getPubVirtualBoolean() : Boolean { return Obj.getPubVirtualBoolean(); }
        // Public Static methods
        public function setPubStatObject(o:Object) { FinalInternalDynamicClass.setPubStatObject(o); }
        public function getPubStatObject() : Object { return FinalInternalDynamicClass.getPubStatObject(); }
        // Public Final methods
        public function setPubFinArray(a:Array) { Obj.setPubFinArray(a); }
        public function getPubFinArray() : Array { return Obj.getPubFinArray(); }

    }
    
}