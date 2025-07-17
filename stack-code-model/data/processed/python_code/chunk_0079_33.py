////////////////////////////////////////////////////////////////////////////////
// Copyright 2016 Prominic.NET, Inc.
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
// Author: Prominic.NET, Inc.
// No warranty of merchantability or fitness of any kind. 
// Use this software at your own risk.
////////////////////////////////////////////////////////////////////////////////

package actionScripts.valueObjects
{
	/**
	 * Implementation of Diagnostic interface from Language Server Protocol
	 * 
	 * <p><strong>DO NOT</strong> add new properties or methods to this class
	 * that are specific to Moonshine IDE or to a particular language. Create a
	 * subclass for new properties or create a utility function for methods.</p>
	 * 
	 * @see https://microsoft.github.io/language-server-protocol/specification#diagnostic
	 */
	public class Diagnostic
	{
		public static const SEVERITY_ERROR:int = 1;
		public static const SEVERITY_WARNING:int = 2;
		public static const SEVERITY_INFORMATION:int = 3;
		public static const SEVERITY_HINT:int = 4;

		public function Diagnostic()
		{
		}

		public var path:String;
		public var message:String;
		public var range:Range;
		public var severity:int;
		public var code:String;

		public static function parse(original:Object):Diagnostic
		{
			var vo:Diagnostic = new Diagnostic();
			vo.message = original.message;
			vo.code = original.code;
			vo.range = Range.parse(original.range);
			vo.severity = original.severity;
			return vo;
		}

		public static function parseWithPath(path:String, original:Object):Diagnostic
		{
			var vo:Diagnostic = new Diagnostic();
			vo.path = path;
			vo.message = original.message;
			vo.code = original.code;
			vo.range = Range.parse(original.range);
			vo.severity = original.severity;
			return vo;
		}
	}
}