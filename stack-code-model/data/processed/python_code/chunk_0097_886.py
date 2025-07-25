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
package flashx.textLayout.elements
{
	import flash.display.Sprite;
	
	//import mx.core.IIMESupport;
	
	public class CellContainer extends Sprite// implements IIMESupport
	{
		private var _imeMode:String;
		private var _enableIME:Boolean;
		public var element:TableCellElement;

		public function CellContainer(imeEnabled:Boolean = true)
		{
			_enableIME = imeEnabled;
		}
		
		public function get enableIME():Boolean
		{
			return false;
		}
		
		public function set enableIME(value:Boolean):void
		{
			_enableIME = value;
		}
		
		public function get imeMode():String
		{
			return _imeMode;
		}
		
		public function set imeMode(value:String):void
		{
			_imeMode = value;
		}
	}
}