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
package flashx.textLayout.conversion
{
	import flash.utils.Dictionary;
	
	[ExcludeClass]
	/**
	 * @private  
	 */
	internal class CustomFormatImporter implements IFormatImporter
	{
		private var _rslt:Dictionary = null;
		
		public function CustomFormatImporter()
		{ }
		public function reset():void
		{ _rslt = null; }
		public function get result():Object
		{ return _rslt; }
		public function importOneFormat(key:String,val:String):Boolean
		{
			if (_rslt == null)
				_rslt = new Dictionary();
			_rslt[key] = val;
			return true; 
		}
	}
}