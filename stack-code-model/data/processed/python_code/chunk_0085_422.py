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
	import flash.events.Event;
	
	import actionScripts.factory.FileLocation;

	public class FilePluginEvent extends Event
	{
		public static const EVENT_FILE_OPEN:String = "fileOpenEvent";
		public static const EVENT_FILE_SAVE:String = "fileSaveEvent";
		public static const EVENT_FILE_OPEN_WITH:String = "fileOpenWithEvent";
		public static const EVENT_JAVA_TYPEAHEAD_PATH_SAVE:String = "EVENT_JAVA_TYPEAHEAD_PATH_SAVE";
		
		public var file:FileLocation;
		
		public function FilePluginEvent(type:String, file:FileLocation)
		{
			this.file = file;
			super(type, false, true);
		}
		
	}
}