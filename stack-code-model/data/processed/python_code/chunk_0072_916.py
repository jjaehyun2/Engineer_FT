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
	import System.Collection.Generic.IEqualityComparer;
	
	public class DistinctEnumerator implements IEnumerator
	{
		private var enumerator:IEnumerator;
		private var comparer:IEqualityComparer;
		private var visited:Array = [];
		private var current:*;
		
		public function DistinctEnumerator(enumerable:IEnumerable, comparer:IEqualityComparer)
		{
			this.enumerator = enumerable.getEnumerator(); 
			this.comparer = comparer;
		}
		
		public function MoveNext():Boolean
		{
			while(enumerator.MoveNext()) {
				var possibleCurrent:* = enumerator.Current();
				
				if(!haveVisited(possibleCurrent)) {
					current = possibleCurrent;
					visited.push(current);
					return true;
				}
			}
			
			visited = [];
			return false;
		}
		
		private function haveVisited(item:*):Boolean {
			if(comparer == null)
				return visited.indexOf(item) >= 0;
			
			for each(var visitedItem:* in visited)
			    if(comparer.Equals(visitedItem, item))
					return true;
				
			return false;
		}
		
		public function Current():*
		{
			return current;
		}
		
		public function Reset():void
		{
			enumerator.Reset();
			visited = [];
			current = null;
		}
	}
}