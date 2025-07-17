package flexUnitTests
{
	import System.Collection.Generic.IEnumerable;
	import System.Linq.Enumerable;
	import System.Linq.FunctionBuilder.element;
	
	import org.flexunit.assertThat;
	import org.hamcrest.number.IsGreaterThanMatcher;
	import org.hamcrest.object.equalTo;

	public class AnyTests extends EnumerableTestsBase
	{		
		[Test]
		public function populated_enumerable_has_any():void {
			assertThat([1].any(), equalTo(true));
		}
		
		[Test]
		public function unpopulated_enumerable_does_not_have_any():void {
			assertThat([].any(), equalTo(false));
		}
		
		[Test]
		public function any_with_predicate_returns_true_when_matched():void {
			assertThat([1,2,3].any(element.isGreaterThan(2)));
		}
		
		[Test]
		public function any_with_predicate_returns_false_when_not_matched():void {
			assertThat([1,2].any(element.isGreaterThan(2)), equalTo(false));
		}
	}
}