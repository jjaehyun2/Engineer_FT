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

package mx.collections {
    import mx.utils.ObjectUtil;

    public class ComplexSortField extends SortField implements IComplexSortField
    {
        private var _nameParts:Array;

        public function ComplexSortField(name:String = null,
                                         caseInsensitive:Boolean = false,
                                         descending:Boolean = false,
                                         numeric:Object = null)
        {
            super(name, caseInsensitive, descending, numeric);
            _nameParts = name ? name.split(".") : [];
        }

        public function get nameParts():Array
        {
            return _nameParts;
        }

        override public function objectHasSortField(object:Object):Boolean
        {
            return object && nameParts && nameParts.length && object.hasOwnProperty(nameParts[0]);
        }

        override protected function getSortFieldValue(obj:Object):*
        {
            return ObjectUtil.getValue(obj, _nameParts);
        }

        override public function get arraySortOnOptions():int
        {
            return -1;
        }
    }
}