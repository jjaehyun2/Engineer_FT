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
	
	public class ConcatEnumerator implements IEnumerator
	{
		private var first:IEnumerator;
		private var second:IEnumerator;
		private var current:*;
		
		public function ConcatEnumerator(first:IEnumerable, second:IEnumerable)
		{
			this.first = first.getEnumerator();
			this.second = second.getEnumerator();
		}
		
		public function MoveNext():Boolean
		{
			while(first.MoveNext())
			{
				current = first.Current();
				return true;
			}
			
			while(second.MoveNext())
			{
				current = second.Current();
				return true;
			}
			
			current = null;
			return false;
		}
		
		public function Current():*
		{
			return current;
		}
		
		public function Reset():void
		{
			first.Reset();
			second.Reset();
		}
	}
}