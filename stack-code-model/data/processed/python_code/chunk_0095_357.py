package flexUnitTests
{
	import System.Linq.Option.Option;
	
	import org.flexunit.assertThat;
	import org.hamcrest.object.equalTo;

	public class SingleTests extends EnumerableTestsBase
	{
		[Test]
		public function single_returns_only_item():void {
			var single:int = [3].single();
			
			assertThat(single, equalTo(3));
		}
		
		[Test(expected="RangeError")]
		public function single_throws_RangeError_when_empty():void {
			var single:int = [].single();
		}
		
		[Test(expected="RangeError")]
		public function single_throws_RangeError_when_more_than_one():void {
			var single:int = [1,2].single();
		}
		
		[Test]
		public function single_with_predicate_returns_only_item():void {
			var single:int = [3,4,5].single(function(x){return x == 4});
			
			assertThat(single, equalTo(4));
		}
		
		[Test(expected="RangeError")]
		public function single_with_predicate_throws_RangeError_when_empty():void {
			var single:int = [1,2,3].single(function(x){return x == 4});
		}
		
		[Test(expected="RangeError")]
		public function single_with_predicate_throws_RangeError_when_more_than_one():void {
			var single:int = [2,3,4,4].single(function(x){return x == 4});
		}
		
		
		
		[Test]
		public function singleOrNone_returns_only_item():void {
			var single:Option = [3].singleOrNone();
			
			assertThat(single.value, equalTo(3));
		}
		
		[Test]
		public function singleOrNone_returns_none_when_empty():void {
			var single:Option = [].singleOrNone();
			
			assertThat(single.isNone);
		}
		
		[Test(expected="RangeError")]
		public function singleOrNone_throws_RangeError_when_more_than_one():void {
			var single:Option = [1,2].singleOrNone();
		}
		
		[Test]
		public function singleOrNone_with_predicate_returns_only_item():void {
			var single:Option = [3,4,5].singleOrNone(function(x){return x == 4});
			
			assertThat(single.value, equalTo(4));
		}
		
		[Test]
		public function singleOrNone_with_predicate_returns_none_when_empty():void {
			var single:Option = [1,2,3].singleOrNone(function(x){return x == 4});
			
			assertThat(single.isNone);
		}
		
		[Test(expected="RangeError")]
		public function singleOrNone_with_predicate_throws_RangeError_none_when_more_than_one():void {
			var single:Option = [2,3,4,4].singleOrNone(function(x){return x == 4});
		}
	}
}