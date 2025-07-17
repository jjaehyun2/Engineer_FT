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
	
	internal class WhereEnumerator implements IEnumerator
	{
		private var enumerator:IEnumerator;
		private var predicate:Function;
		private var count:int = -1;
		
		public function WhereEnumerator(enumerable:IEnumerable, predicate:Function)
		{
			this.enumerator = enumerable.getEnumerator();
			this.predicate = predicate;
		}
		
		public function MoveNext():Boolean
		{
			while(enumerator.MoveNext())
			{
				var matched:Boolean = predicate.length == 1 ? 
					predicate(enumerator.Current()) : 
					predicate(enumerator.Current(), ++count);
				
				if(matched)
					return true;
			}
			
			return false;
		}
		
		public function Current():*
		{
			return enumerator.Current();
		}

		public function Reset():void
		{
			enumerator.Reset();
			count = -1;
		}
	}
}