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
package org.apache.royale.core.layout
{
	/**
	 *  The LayoutData class is a utility class for holding margins, border and padding of
	 *  a component.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.0
	 */
	public class LayoutData
	{
	    public function LayoutData()
	    {
	    }
	    
		private var _border:EdgeData;
        private var _padding:EdgeData;
        private var _margins:MarginData;

		public function get border():EdgeData
		{
			return _border;
		}
		public function set border(value:EdgeData):void
		{
            _border = value;
		}
        
        public function get padding():EdgeData
        {
            return _padding;
        }
        public function set padding(value:EdgeData):void
        {
            _padding = value;
        }
        
        public function get margins():MarginData
        {
            return _margins;
        }
        public function set margins(value:MarginData):void
        {
            _margins = value;
        }
	}


}