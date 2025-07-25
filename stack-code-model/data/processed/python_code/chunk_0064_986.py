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
package valueObjects
{
  import org.apache.royale.collections.ArrayList;
    
    [RemoteClass(alias="org.apache.royale.amfsamples.valueobjects.Product")]
	public class Product
	{
		public function Product()
		{
		}

		private var _name:String;

        [Bindable("__NoChangeEvent__")]
        public function get name():String
        {
            return _name;
        }

        public function set name(value:String):void
        {
            _name = value;
        }

        private var _description:String;

        [Bindable("__NoChangeEvent__")]
        public function get description():String
        {
            return _description;
        }

        public function set description(value:String):void
        {
            _description = value;
        }

        private var _taxonomy:Taxonomy;

        [Bindable("__NoChangeEvent__")]
        public function get taxonomy():Taxonomy
        {
            return _taxonomy;
        }

        public function set taxonomy(value:Taxonomy):void
        {
            _taxonomy = value;
        }

        // collection of zones (Zone), we can use ArrayList
        private var _zones:ArrayList;

        [Bindable("__NoChangeEvent__")]
        public function get zones():ArrayList
        {
            return _zones;
        }

        public function set zones(value:ArrayList):void
        {
            _zones = value;
        }

        private var _flavors:ArrayList = null;

        [Bindable("__NoChangeEvent__")]
        public function get flavors():ArrayList
        {
            return _flavors;
        }

        public function set flavors(value:ArrayList):void
        {
            _flavors = value;
        }

	}
}