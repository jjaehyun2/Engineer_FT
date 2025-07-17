package flexUnitTests
{
	import System.Collection.Generic.*;
	import System.Linq.*;
	import System.Linq.Option.Option;
	
	import flexunit.framework.Assert;
	
	import org.flexunit.assertThat;
	import org.hamcrest.object.equalTo;

	public class FirstTests extends EnumerableTestsBase
	{				
		[Test]
		public function first_without_predicate_returns_first_item()
		{
			var result:int = [1,2,3,4,5].first();
			
			Assert.assertEquals(result, 1);
		}

		[Test(expected="RangeError")]
		public function first_throws_range_error_when_sequence_is_empty():void {
			var result = [].first();
		}
		
		[Test]
		public function First_with_predicate_returns_first_match()
		{
			var result:int = [1,2,3,4,5].first(function(x){return x >= 4;});
			
			Assert.assertEquals(result, 4);  
		}
		
		[Test(expected="RangeError")]
		public function first_with_predicate_throws_range_error_when_no_match():void {
			var result = [].first(function(x){return true});
		}
		
		[Test]
		public function firstOrNone_without_predicate_returns_first_item()
		{
			var result:Option = [1,2,3,4,5].firstOrNone();
			
			assertThat(result.value, equalTo(1));
		}
		
		[Test]
		public function firstOrNone_returns_none_when_sequence_is_empty():void {
			var result:Option = [].firstOrNone();
			assertThat(result.isNone)
		}
		
		[Test]
		public function firstOrNone_with_predicate_returns_none_when_no_match():void {
			var result:Option = [].firstOrNone(function(x){return true});
			assertThat(result.isNone)
		}
		
		[Test]
		public function firstOrNone_with_predicate_returns_first_match()
		{
			var result:Option = [1,2,3,4,5].firstOrNone(function(x){return x >= 4;});
			
			assertThat(result.value, equalTo(4));
		}
	}
}