/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */




package DefaultClass {

    import DefaultClass.*;

    dynamic class DynExtDefaultClassFinInner extends DefaultClass {
    
        // ************************************
        // access final method of parent
        // from default method of sub class
        // ************************************

        function subGetArray() : Array { return this.getFinArray(); }
        function subSetArray(a:Array) { this.setFinArray(a); }
            // this is needed so that the test cases can access this from
            // outside the class.  This way the test case itself preserved
           public function testSubGetSetArray(a:Array) : Array {
            this.subSetArray(a);
            return this.subGetArray();
           }

        // ************************************
        // access final method of parent
        // from public method of sub class
        // ************************************

        public function pubSubGetArray() : Array { return this.getFinArray(); }
        public function pubSubSetArray(a:Array) { this.setFinArray(a); }


        // ************************************
        // access final method of parent
        // from private method of sub class
        // ************************************
   

        private function privSubGetArray() : Array { return this.getFinArray(); }
        private function privSubSetArray(a:Array) { this.setFinArray(a); }

        // function to test above from test scripts
        public function testPrivSubArray(a:Array) : Array {
        this.privSubSetArray(a);
        return this.privSubGetArray();
        }

        // ************************************
        // access final method of parent
        // from final method of sub class
        // ************************************

        final function finSubGetArray() : Array { return this.getFinArray(); }
        final function finSubSetArray(a:Array) { this.setFinArray(a); }
        // function to test above from test scripts
        public function testFinSubArray(a:Array) : Array {
        this.finSubSetArray(a);
        return this.finSubGetArray();
        }

        // ***************************************
        // access final property from
        // default method of sub class
        // ***************************************

        function subGetDPArray() : Array { return finArray; }
        function subSetDPArray(a:Array) { finArray = a; }


    
    // ************************************
    // access final method of parent
    // from virtual method of sub class
    // ************************************
            
    virtual function virtSubGetArray() : Array { return this.getFinArray(); }
    virtual function virtSubSetArray(a:Array) { this.setFinArray(a); }
            
    public function testVirtSubArray(a:Array) : Array {
        this.virtSubSetArray(a);
        return this.virtSubGetArray();
    }


        public function pubSubGetDPArray() : Array { return this.finArray; }
        public function pubSubSetDPArray(a:Array) { this.finArray = a; }


        // ***************************************
        // access final property from
        // private method of sub class
        // ***************************************

    // this is needed so that the test cases can access this from
    // outside the class.  This way the test case itself preserved
    public function testSubGetSetDPArray(a:Array) : Array {
        this.subSetDPArray(a);
        return this.subGetDPArray();
    }
   
    // ***************************************
    // access final property from
    // public method of sub class
    // ***************************************

    private function privSubGetDPArray() : Array { return this.finArray; }
    private function privSubSetDPArray(a:Array) { this.finArray = a; }

    
    // this is needed so that the test cases can access this from
    // outside the class.  This way the test case itself preserved
    public function testSubPrivDPArray(a:Array) : Array {
        this.privSubSetDPArray(a);
        return this.privSubGetDPArray();
    }

    final function finSubGetDPArray() : Array { return finArray; }
    final function finSubSetDPArray(a:Array) { finArray = a; }
    
    
    // this is needed so that the test cases can access this from
    // outside the class.  This way the test case itself preserved
    public function testSubFinDPArray(a:Array) : Array {
        this.finSubSetDPArray(a);
        return this.finSubGetDPArray();
    }
    
    // ***************************************
    // access default property from
    // virtual method of sub class
    // ***************************************
            
    virtual function virtSubGetDPArray() : Array { return finArray; }
    virtual function virtSubSetDPArray(a:Array) { finArray = a; }
            
    public function testVirtSubDPArray(a:Array) : Array {
          this.virtSubSetDPArray(a);
          return this.virtSubGetDPArray();
    }

    
        // ******************************************
        // override default method of parent class
        // ******************************************
    /*
        override function overLoad() { return "This is the sub class"; }
        override function pubOverLoad() { return "This is the sub class"; }
        override function privOverLoad() { return "This is the sub class"; }
        override function statOverLoad() { return "This is the sub class"; }
        override function pubStatOverLoad() { return "This is the sub class"; }
        override function privStatOverLoad() { return "This is the sub class"; }
        
    */
    

   }
     
    // PUBLIC wrapper function for the dynamic class to be accessed;
    // otherwise it will give the error:
    // ReferenceError: DynExtDefaultClass is not defined
    //  at global$init()
    public class DynExtDefaultClassFin extends DynExtDefaultClassFinInner  {}


}