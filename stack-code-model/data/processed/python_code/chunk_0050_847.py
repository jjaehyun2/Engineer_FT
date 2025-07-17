package flexUnitTests
{
	import org.flexunit.assertThat;
	import org.hamcrest.object.equalTo;

	public class CountTests extends EnumerableTestsBase
	{		
		[Test]
		public function count_gets_the_number_of_items():void {
			var count:int = [1,2,3].count();
			assertThat(count, equalTo(3));
			
			var count:int = [2,3,4,5].count();
			assertThat(count, equalTo(4));
		}
		
		[Test]
		public function empty_array_yields_zero_count():void {
			assertThat([].count(), equalTo(0));
		}
		
		[Test]
		public function count_with_predicate_filters_before_count():void {
			var count:int = [1,2,3,4,5,6].count(function(i:int):Boolean { return i > 4 });
			
			assertThat(count, equalTo(2));
		}
		
	}
}