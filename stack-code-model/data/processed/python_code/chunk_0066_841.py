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
package UnitTest.Validation
{
	import flash.events.Event;
	import flash.events.IEventDispatcher;
	import flash.events.MouseEvent;
	import flashx.textLayout.debug.assert;
	import flashx.textLayout.elements.FlowElement;
	import flashx.textLayout.events.FlowElementMouseEvent;
	import flashx.textLayout.elements.LinkElement;

	public class FlowElementMouseEventValidator extends EventValidator
	{
		public function FlowElementMouseEventValidator(target:IEventDispatcher, expectedEvent:Event)
		{
			super(target, expectedEvent);
		}

		override protected function validateHandler(event:Event):void
		{
			super.validateHandler(event);
	   		if (event.type == MouseEvent.CLICK)
	   			event.preventDefault();
		}

		override protected function eventsAreEqual(event:Event, expectedEvent:Event):Boolean
		{
			return FlowElementMouseEvent(event).flowElement == FlowElementMouseEvent(expectedEvent).flowElement;
		}
	}
}