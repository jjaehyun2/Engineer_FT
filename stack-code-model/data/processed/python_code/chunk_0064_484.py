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

package mx.automation.codec
{ 
	
	import mx.automation.tool.IToolPropertyDescriptor; 
	import mx.automation.IAutomationManager;
	import mx.automation.IAutomationObject;
	
	/**
	 * Translates between internal Flex description of a scroll event 
	 * and automation-friendly version
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public class DateScrollDetailPropertyCodec extends DefaultPropertyCodec
	{
		/**
		 *  Constructor
		 *  
		 *  @langversion 3.0
		 *  @playerversion Flash 9
		 *  @playerversion AIR 1.1
		 *  @productversion Flex 3
		 */ 
		public function DateScrollDetailPropertyCodec()
		{
			super();
		}
		
		/**
		 *  @private
		 */ 
		override public function encode(automationManager:IAutomationManager,
										obj:Object, 
										pd:IToolPropertyDescriptor,
										relativeParent:IAutomationObject):Object
		{
			var val:int = 0;
			
			if (!("detail" in obj))
				return val;
			
			switch (obj["detail"])
			{
				case "nextMonth": 
					return 1;
				case "nextYear": 
					return 2;
				case "previousMonth": 
					return 3;
				case "previousYear": 
					return 4;
			}
			
			return val;
		}
		
		/**
		 *  @private
		 */ 
		override public function decode(automationManager:IAutomationManager,
										obj:Object, 
										value:Object,
										pd:IToolPropertyDescriptor,
										relativeParent:IAutomationObject):void
		{
			var details:Array = 
				[
					"nextMonth", "nextYear", "previousMonth", "previousYear"
				];
			
			if ("detail" in obj && value < details.length)
				obj["detail"] = details[Number(value)-1];
		}
	}
	
}