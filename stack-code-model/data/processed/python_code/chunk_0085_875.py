/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
package StaticPublicFunctionName {

    class TestNameObjInner {

        // constructor
        function TestNameObjInner() { res = "EmptyName"; }
    
        // not the constructor but looks like it
        function testNameObjInner() { return "not the constructor" }

        static public function a1 () { return "a1"; }
        static public function a_1 () { return "a_1"; }
        static public function _a1 () { return "_a1"; }
        static public function __a1 () { return "__a1"; }
        static public function _a1_ () { return "_a1_"; }
        static public function __a1__ () { return "__a1__"; }
        static public function $a1 () { return "$a1"; }
        static public function a$1 () { return "a$1"; }
        static public function a1$ () { return "a1$"; }
        static public function A1 () { return "A1"; }
        static public function cases () { return "cases"; }
        static public function Cases () { return "Cases"; }
        static public function abcdefghijklmnopqrstuvwxyz0123456789$_ () { return "all"; }
    }

    public class TestNameObj extends TestNameObjInner {
    public function pubTestConst() { return testNameObjInner(); }
        public function puba1 () { return a1(); }
        public function puba_1 () { return a_1(); }
        public function pub_a1 () { return _a1(); }
        public function pub__a1 () { return __a1(); }
        public function pub_a1_ () { return _a1_(); }
        public function pub__a1__ () { return __a1__(); }
        public function pub$a1 () { return $a1(); }
        public function puba$1 () { return a$1(); }
        public function puba1$ () { return a1$(); }
        public function pubA1 () { return A1(); }
        public function pubcases () { return cases(); }
        public function pubCases () { return Cases(); }
        public function puball () { return abcdefghijklmnopqrstuvwxyz0123456789$_(); }
    }

}