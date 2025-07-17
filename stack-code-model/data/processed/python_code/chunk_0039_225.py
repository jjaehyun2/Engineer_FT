package flexUnitTests
{
	import System.Linq.Enumerable;
	import System.Linq.Option.Option;
	
	import org.flexunit.assertThat;
	import org.hamcrest.object.equalTo;

	public class ElementAtTests extends EnumerableTestsBase
	{		
		[Test]
		public function elementAt_returns_element_at_index():void {
			var element:int = [2,4,6,8].elementAt(2);
			
			assertThat(element, equalTo(6));
		}
		
		[Test(expected="RangeError")]
		public function elementAt_throws_RangeError_if_index_less_than_zero():void {
			var element:int = [2,4,6,8].elementAt(-1);
		}
		
		[Test(expected="RangeError")]
		public function elementAt_throws_RangeError_if_index_greater_than_length():void {
			var element:int = [2,4,6,8].elementAt(4);
		}
		
		
		[Test]
		public function elementAtOrNone_returns_element_at_index():void {
			var element:Option = [2,4,6,8].elementAtOrNone(2);
			
			assertThat(element.value, equalTo(6));
		}
		
		[Test]
		public function elementAt_returns_none_if_index_less_than_zero():void {
			var element:Option = [2,4,6,8].elementAtOrNone(-1);
			
			assertThat(element.isNone);
		}
		
		[Test]
		public function elementAt_returns_none_if_index_greater_than_length():void {
			var element:Option = [2,4,6,8].elementAtOrNone(4);
			
			assertThat(element.isNone);
		}
	}
}