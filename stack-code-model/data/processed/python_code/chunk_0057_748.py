package flexUnitTests
{
	import System.Collection.Generic.IEnumerable;
	import System.Collection.Generic.IEnumerator;
	import System.Linq.Enumerable;
	
	import org.flexunit.assertThat;
	import org.hamcrest.collection.array;
	import org.hamcrest.object.equalTo;

	public class ZipTests extends EnumerableTestsBase
	{		
		[Test]
		public function zip_will_combine_two_enumerables():void {
			var first:IEnumerable = [1,2,3].asEnumerable();
			var second:IEnumerable = ['a','b','c'].asEnumerable();
			
			var enumerator:IEnumerator = first.zip(second, function(f,s) { return f + s }).getEnumerator();
			
			assertThat(enumerator.MoveNext(), equalTo(true))
			assertThat(enumerator.Current(), equalTo("1a"))
			assertThat(enumerator.MoveNext(), equalTo(true))
			assertThat(enumerator.Current(), equalTo("2b"))
			assertThat(enumerator.MoveNext(), equalTo(true))
			assertThat(enumerator.Current(), equalTo("3c"))
			assertThat(enumerator.MoveNext(), equalTo(false))
		}
		
		[Test]
		public function left_has_more_than_right_bound_to_right_count():void {
			var result:Array = [1,2,3,4,5]
				.zip(['a', 'b'].asEnumerable(), function(f,s) { return f + s})
				.toArray();
			
			assertThat(result, array("1a", "2b"));
		}
		
		[Test]
		public function right_has_more_than_left_bound_to_left_count():void {
			var result:Array = [1,2]
				.zip(['a', 'b', 'c', 'd', 'e'].asEnumerable(), function(f,s) { return f + s})
				.toArray();
			
			assertThat(result, array("1a", "2b"));
		}
		
		[Test]
		public function reset_zip_will_start_from_scratch():void {
			var first:IEnumerable = [1,2,3].asEnumerable();
			var second:IEnumerable = ['a','b','c'].asEnumerable();
			
			var enumerator:IEnumerator = first.zip(second, function(f,s) { return f + s }).getEnumerator();
			
			enumerator.MoveNext();
			enumerator.MoveNext();
			enumerator.Reset();
			enumerator.MoveNext();
			
			assertThat(enumerator.Current(), equalTo("1a"));
		}
		
		[Test(expected="ArgumentError")]
		public function zip_throws_ArgumentError_when_second_is_null():void {
			var result = Enumerable.empty.zip(null, function(x,s){return x});
		}
		
		[Test(expected="ArgumentError")]
		public function zip_throws_ArgumentError_when_resultSelector_is_null():void {
			var result = Enumerable.empty.zip(Enumerable.empty, null);
		}
		
	}
}