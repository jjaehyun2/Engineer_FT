/**
 * Copyright (C) 2008 Darshan Sawardekar.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.puremvc.as3.multicore.utilities.fabrication.addons.mock {
    import com.anywebcam.mock.Mock;

    import flash.events.Event;
    import flash.events.EventDispatcher;
    import flash.events.IEventDispatcher;

    import org.puremvc.as3.multicore.utilities.fabrication.addons.IMockable;

    /**
	 * @author Darshan Sawardekar
	 */
	public class EventDispatcherMock extends EventDispatcher implements IMockable {

		private var _mock:Mock;

		public function EventDispatcherMock(target:IEventDispatcher = null) {
			super(target);
		}

		public function get mock():Mock {
			if (_mock == null) {
				_mock = new Mock(this, true);
			}
			
			return _mock;
		}

		override public function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void {
			mock.addEventListener(type, listener, useCapture, priority, useWeakReference);
		}

		override public function removeEventListener(type:String, listener:Function, useCapture:Boolean = false):void {
			mock.removeEventListener(type, listener, useCapture);
		}

		override public function dispatchEvent(event:Event):Boolean {
			return mock.dispatchEvent(event);
		}

		override public function hasEventListener(type:String):Boolean {
			return mock.hasEventListener(type);
		}

		override public function willTrigger(type:String):Boolean {
			return mock.willTrigger(type);
		}
	}
}