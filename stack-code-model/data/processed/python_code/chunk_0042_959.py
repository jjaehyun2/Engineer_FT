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
	import System.Collection.Generic.IEnumerable;
	import System.Collection.Generic.IEnumerator;
	
	internal class SelectEnumerator implements IEnumerator
	{
		private var enumerator:IEnumerator;
		private var selector:Function;
		private var current:*;
		private var count:int = -1;
		
		public function SelectEnumerator(enumerable:IEnumerable, selector:Function)
		{
			this.enumerator = enumerable.getEnumerator();
			this.selector = selector;
		}
		
		public function MoveNext():Boolean
		{
			if(enumerator.MoveNext())
			{
				current = selector.length == 1 ? selector(enumerator.Current()) : selector(enumerator.Current(), ++count);
				return true;
			}
			
			return false;
		}
		
		public function Current():*
		{
			return current;
		}
		
		public function Reset():void
		{
			enumerator.Reset();
			count = -1;
			current = null;
		}
	}
}