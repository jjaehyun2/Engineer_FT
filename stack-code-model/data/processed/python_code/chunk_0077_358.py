﻿////////////////////////////////////////////////////////////////////////////////
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
// http://www.apache.org/licenses/LICENSE-2.0 
// 
// Unless required by applicable law or agreed to in writing, software 
// distributed under the License is distributed on an "AS IS" BASIS, 
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and 
// limitations under the License
// 
// No warranty of merchantability or fitness of any kind. 
// Use this software at your own risk.
// 
////////////////////////////////////////////////////////////////////////////////
package no.doomsday.console.core.commands{
	import flash.utils.Dictionary;
	/**
	 * ...
	 * @author Andreas Rønning
	 */
	public class FunctionCallCommand extends ConsoleCommand
	{
		private var callbackDict:Dictionary;
		/**
		 * Creates a callback command, which calls a function when triggered
		 * @param	trigger
		 * The trigger phrase
		 * @param	callback
		 * The function to call
		 */
		public function FunctionCallCommand(trigger:String, callback:Function, grouping:String = "Application", helpText:String = "")
		{
			callbackDict = new Dictionary(true);
			callbackDict["callback"] = callback;
			super(trigger);
			this.grouping = grouping;
			this.helpText = helpText;
		}
		public function get callback():Function {
			return callbackDict["callback"] as Function;
		}
		
	}
	
}