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
package org.apache.royale.html.beads
{
	COMPILE::SWF {
	import flash.display.InteractiveObject;
	}
	
	import org.apache.royale.core.Bead;
	import org.apache.royale.core.IStrand;
	import org.apache.royale.core.IUIBase;
	import org.apache.royale.events.Event;
	import org.apache.royale.events.ValueEvent;
	import org.apache.royale.utils.sendStrandEvent;

	COMPILE::JS{
		import org.apache.royale.core.WrappedHTMLElement;
		import org.apache.royale.core.HTMLElementWrapper;
	}
	/**
	 *  The DisableBead class is a specialty bead that can be used with
	 *  any UIBase. When disabled is true, the bead prevents interaction with the component.
	 *  The appearance of the component when disabled is controlled by a separate bead.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.0
	 */
	public class DisableBead extends Bead
	{
		/**
		 *  constructor.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.0
		 */
		public function DisableBead()
		{
		}
		
		private var _disabled:Boolean;
		
		/**
		 *  @copy org.apache.royale.core.IBead#strand
		 *  
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.0
		 *  @royaleignorecoercion org.apache.royale.core.HTMLElementWrapper
		 */
		override public function set strand(value:IStrand):void
		{	
			_strand = value;
			COMPILE::JS
			{
				_lastTabVal = (_strand as HTMLElementWrapper).element.getAttribute("tabindex");
			}
			updateHost();
		}
		
		public function get disabled():Boolean
		{
			return _disabled;
		}
		
		/**
		 *  @private
		 *  @royaleignorecoercion org.apache.royale.core.HTMLElementWrapper
		 */
		public function set disabled(value:Boolean):void
		{
			if (value != _disabled)
			{
				COMPILE::JS
				{
					if(value && _strand)
						_lastTabVal = (_strand as HTMLElementWrapper).element.getAttribute("tabindex");
				}
				_disabled = value;
				updateHost();
				throwChangeEvent();
			}
		}

		private function disabledChangeHandler(e:Event):void
		{
			updateHost();
		}
		/**
		 * 	@royaleignorecoercion org.apache.royale.core.IUIBase
		 */
		private function get host():IUIBase
		{
			return _strand as IUIBase;
		}
		
		COMPILE::JS
		private var _lastTabVal:String;
		
		/**
		 * @royaleignorecoercion org.apache.royale.core.HTMLElementWrapper
		 */
		private function updateHost():void
		{
			if(!_strand)//bail out
				return;
			COMPILE::SWF {
				var interactiveObject:InteractiveObject = _strand as InteractiveObject;
				interactiveObject.mouseEnabled = !disabled;
			}
			
			COMPILE::JS {
				var elem:HTMLElement = (_strand as HTMLElementWrapper).element;
				elem.style["pointerEvents"] = disabled ? "none" : "";
				if(disabled)
					elem.setAttribute("tabindex", "-1");
				else
					_lastTabVal ?
						elem.setAttribute("tabindex", _lastTabVal) :
						elem.removeAttribute("tabindex");
			}
				
		}
		
		private function throwChangeEvent():void
		{
			if (_strand)
			{
				sendStrandEvent(_strand,new ValueEvent("disabledChange", disabled));
			}
		}

		
	}
}