package flexUnitTests
{
	import System.Collection.Generic.*;
	import System.Linq.*;
	
	import flexunit.framework.*;
	
	import mx.collections.ArrayCollection;
	
	import org.flexunit.assertThat;
	import org.hamcrest.collection.array;
	import org.hamcrest.object.equalTo;

	public class WhereTests extends EnumerableTestsBase
	{	
		[Test]
		public function where_filters_on_predicate(): void
		{
			var data:Array = [1, 2, 3, 4, 5];
			var filtered:IEnumerable = data.where(function(x){return x >= 4});
			var enumerator:IEnumerator = filtered.getEnumerator();
			
			assertThat(enumerator.MoveNext(), equalTo(true));
			assertThat(enumerator.Current(), equalTo(4));
			assertThat(enumerator.MoveNext(), equalTo(true));
			assertThat(enumerator.Current(), equalTo(5));
			assertThat(enumerator.MoveNext(), equalTo(false));
		}
		
		[Test]
		public function where_with_static_predicate_and_no_index_does_not_fail(): void
		{
			var filtered:Array = [1, 2, 3, 4, 5].where(greaterOrEqual4).toArray();
			
			assertThat(filtered, array(4,5));
		}
		
		private function greaterOrEqual4(x) { return x >= 4 }
		
		[Test]
		public function where_with_index_passes_index_if_defined():void {
			var data:Array = 
				[1, 2, 3, 4, 5]
				.where(function(x,i) { return i  < 3 })
				.toArray();
			
			assertThat(data, array(1,2,3));
		}
		
		[Test]
		public function resetting_where_starts_over()
		{
			var data:Array = [1, 2, 3, 4, 5];
			var filtered:IEnumerable = data.where(function(x){return x >= 4});
			var enumerator:IEnumerator = filtered.getEnumerator();
			
			enumerator.MoveNext();
			enumerator.MoveNext();
			enumerator.Reset();
			enumerator.MoveNext();
			
			assertThat(enumerator.Current(), equalTo(4));
		}
		
		[Test(expected="ArgumentError")]
		public function where_throws_ArgumentError_when_predicate_is_null():void {
			var filtered = [].where(null);
		}
		
	}
}