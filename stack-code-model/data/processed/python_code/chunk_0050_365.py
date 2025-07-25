////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////
package flexUnitTests.reflection.support
{
    
    
    /**
     * @royalesuppresspublicvarwarning
     */
    public class TestClass3 extends TestClass1 implements ITestInterface2, ITestInterface3
    {
        
        public var something:String;
        
        
        public function someMethod2(compulsoryArg:int, optArg:String = null):TestClass1
        {
            return null;
        }
        
        public function get someValue2():Boolean
        {
            return false;
        }
    }
}