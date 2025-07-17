//Copyright 2010 SRT Solutions
//
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//	You may obtain a copy of the License at
//
//http://www.apache.org/licenses/LICENSE-2.0
//
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//	See the License for the specific language governing permissions and
//limitations under the License.

package System.Linq
{
	import System.Collection.Generic.IEnumerator;
	
	import flash.utils.Dictionary;
	
	public class GroupingEnumerator implements IEnumerator
	{
		private var dictionary:Dictionary;
		private var keys:Array = new Array();
		private var index:int = -1;
		
		public function GroupingEnumerator(dictionary:Dictionary)
		{
			this.dictionary = dictionary;
			for(var itemName in dictionary)
				keys.push(itemName);
		}
		
		public function MoveNext():Boolean
		{
			return ++index < keys.length;
		}
		
		public function Current():*
		{
			return dictionary[keys[index]];
		}
		
		public function Reset():void
		{
			index = -1;
		}
	}
}