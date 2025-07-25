////////////////////////////////////////////////////////////////////////////////
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
package actionScripts.events
{
	import actionScripts.valueObjects.Location;
	import actionScripts.valueObjects.Position;

	import flash.events.Event;

	public class GotoDefinitionEvent extends Event
	{
		public static const EVENT_SHOW_DEFINITION_LINK:String = "newShowDefinitionLink";

		public var locations:Vector.<Location>;
		public var position:Position;
		public var uri:String;

		public function GotoDefinitionEvent(type:String, locations:Vector.<Location>, position:Position, uri:String)
		{
			super(type, false, true);
			this.locations = locations;
			this.position = position;
			this.uri = uri;
		}

	}
}