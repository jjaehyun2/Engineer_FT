package flexUnitTests
{
	import System.Linq.Enumerable;
	
	import flexunit.framework.Assert;
	
	import org.flexunit.assertThat;
	import org.hamcrest.object.equalTo;

	public class AggregateTests extends EnumerableTestsBase
	{		
		[Test]
		public function aggregate_will_aggregate_all_items()
		{
			var data:Array = [1,2,3,4];
			var product:int = data.aggregate(1, 
				function(accumulate:int, item:int) { return accumulate * item });
			
			assertThat(product, equalTo(24));
		}
		
		[Test]
		public function aggregte_without_seed_applies_accumulator_to_all_items():void {
			var sentence:String = "the quick brown fox jumps over the lazy dog";
			var words:Array = sentence.split(" ");
			var reversed = words.aggregate(function(workingSentance, next) { return next + " " + workingSentance });
		
			assertThat(reversed, equalTo("dog lazy the over jumps fox brown quick the"));
		}
		
		[Test]
		public function aggregte_without_seed_applies_accumulator_to_all_items2():void {
			var numbers:Array = [1,2,3,4,5];
			var sum:int = numbers.aggregate(function(sum, next) { return sum + next });
			
			assertThat(sum, equalTo(15));
		}
		
		[Test]
		public function aggregate_with_result_selector_aggregagtes_and_selects():void {
			var fruits:Array = [ "apple", "mango", "orange", "passionfruit", "grape" ];
			var longestName:String = fruits.aggregate("banana", 
				function(longest:String, next:String) { return next.length > longest.length ? next : longest },
				function(fruit:String) { return fruit.toUpperCase() });
			
			assertThat(longestName, equalTo("PASSIONFRUIT")); 
		}
		
		[Test]
		public function sum_will_sum_the_values_of_a_collection()
		{
			var data:Array = [1,2,3,4];
			var sum:int = data.sum();
			
			assertThat(sum, equalTo(10));
		}
		
		[Test]
		public function aum_with_selector_sums_the_selected_values()
		{
			var data:Array = ["a", "ab", "abc", "abcd"];
			var sum:int = data.sum(function(item:String) { return item.length });
			
			assertThat(sum, equalTo(10));
		}
		
		[Test]
		public function sum_with_empty_collection_is_zero()
		{
			assertThat([].sum(), equalTo(0));
		}
		
		[Test]
		public function min_gets_the_minimum_value()
		{
			var min:int = [4,6,3,4,5,2,9].min();
			
			assertThat(min, equalTo(2));
		}
		
		[Test]
		public function min_with_selector_gets_the_min_of_the_selected_value()
		{
			var min:int = ["abcd", "ab", "abc", "abcde"].min(function(item:String) { return item.length });
			
			assertThat(min, equalTo(2));
		}
		
		[Test(expected="RangeError")]
		public function min_with_empty_collection_throws_exception()
		{
			var min = [].min();
		}
		
		[Test]
		public function max_gets_the_maximum_value()
		{
			var max:int = [4,6,3,4,9,2,5].max();
			
			assertThat(max, equalTo(9));
		}
		
		[Test]
		public function max_with_selector_gets_the_max_of_the_selected_value()
		{
			var max:int = ["abcd", "ab", "abc", "abcde", "a"].max(function(item:String) { return item.length });
			
			assertThat(max, equalTo(5));
		}
		
		[Test(expected="RangeError")]
		public function max_with_empty_collection_throws_exception()
		{
			var max = [].max();
		}
		
		[Test]
		public function average_gets_the_average_value()
		{
			var average:Number = [4,5,6].average();
			
			assertThat(average, equalTo(5));
		}
		
		[Test]
		public function average_with_selector_gets_avarage_of_selected_value():void {
			var average:Number = ["a", "ab", "abc", "abcd"]
				.average(function(item:String):int { return item.length; });
			
			assertThat(average, equalTo(2.5));
		}
		
	}
}