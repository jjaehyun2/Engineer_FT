/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
package EmptyFunctionBody {

    // due to bug 106878, the base class definition must be first
    class TestObjInner{
        function noReturnNoParamsInner() { return "noReturnNoParams"; }
        function noReturnParamsInner(s:String, b:Boolean) { return s; }
        function noReturnCustomParamInner(c:Custom) { return new Custom(); }
        function returnNoParamsInner():String { return "returnNoParams"; }
        function returnParamsInner(s:String, b:Boolean):String { return s; }
        function returnCustomNoParamsInner():Custom { return new Custom(); }
    }
    
    public class TestObj extends TestObjInner {
        public function noReturnNoParams() { return noReturnNoParamsInner(); }
        public function noReturnParams(s:String, b:Boolean) { return noReturnParamsInner(s,b); }
        public function noReturnCustomParam(c:Custom) { return noReturnCustomParamInner(c); }
        public function returnNoParams():String { return returnNoParamsInner(); }
        public function returnParams(s:String, b:Boolean):String { return returnParamsInner(s,b); }
        public function returnCustomNoParams():Custom { return returnCustomNoParamsInner(); }
    }

}