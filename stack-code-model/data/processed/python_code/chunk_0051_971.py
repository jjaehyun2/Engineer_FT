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
package actionScripts.plugins.svn.event
{
	import flash.events.Event;
	import flash.filesystem.File;
	
	import actionScripts.valueObjects.ProjectVO;
	import actionScripts.valueObjects.RepositoryItemVO;

	public class SVNEvent extends Event
	{
		public static const EVENT_CHECKOUT:String = "checkoutEvent";
		public static const SVN_AUTH_REQUIRED:String = "svnAuthRequired";
		public static const SVN_ERROR:String = "svnError";
		public static const SVN_RESULT:String = "svnResult";
		public static const SVN_REMOTE_LIST:String = "svnRemoteList";
		
		public var file:File;
		public var url:String;
		public var project:ProjectVO;
		public var authObject: Object; // [username, password]
		public var extras:Array;
		public var repository:RepositoryItemVO;
		 
		public function SVNEvent(type:String, file:File, url:String=null, project:ProjectVO=null, authObject:Object=null, ...param)
		{
			this.file = file;
			this.url = url;
			this.authObject = authObject;
			this.project = project;
			this.extras = param;
			super(type, false, true);
		}
	}
}