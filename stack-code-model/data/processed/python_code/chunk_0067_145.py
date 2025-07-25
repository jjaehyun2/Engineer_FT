/*******************************************************************************
* The MIT License
* 
* Copyright (c) 2011 Jens Struwe.
* 
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
* 
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
* THE SOFTWARE.
******************************************************************************/
package com.sibirjak.jakute.framework.states {
	import com.sibirjak.jakute.framework.JCSS_ComponentStyleManager;
	import com.sibirjak.jakute.framework.core.JCSS_ID;

	/**
	 * @author Jens Struwe 11.01.2011
	 */
	public class JCSS_StateListener {
		
		protected var _styleManager : JCSS_ComponentStyleManager;
		
		public var listenerID : uint;

		public function JCSS_StateListener(styleManager : JCSS_ComponentStyleManager) {
			_styleManager = styleManager;
			listenerID = JCSS_ID.uniqueID();
		}
		
		public function notifyParentStateChanged(dispatcher : JCSS_StateDispatcher) : void {
			//trace ("state changed", this, dispatcher);
			// template method
		}
		
		public function registered(dispatcher : JCSS_StateDispatcher) : void {
			//trace("listener registered LISTENER:", this, "DISPATCHER:", dispatcher);
			// template method
		}

	}
}