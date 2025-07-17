package flexUnitTests
{
	import org.flexunit.assertThat;
	import org.hamcrest.object.equalTo;

	public class ContainsTests extends EnumerableTestsBase
	{		
		[Test]
		public function contains_returns_true_when_item_is_in_collection() {
			var dataContainsTwo:Boolean = [2,3,4].contains(2);
			
			assertThat(dataContainsTwo);
		}
		
		[Test]
		public function contains_returns_false_when_item_is_not_in_collection() {
			var dataContainsTwo:Boolean = [3,4].contains(2);
			
			assertThat(dataContainsTwo, equalTo(false));
		}
		
		[Test]
		public function contains_with_comparer_is_true_when_item_in_collection() {
			var data:Array = [
				new TestModel("brian", 33, 1234),
				new TestModel("cara", 34, 2345),
				new TestModel("eli", 0, 3456) ];
			
			var dataContainsCara:Boolean = data.contains(new TestModel("cara", 34, 2345), new ModelComparator());
			
			assertThat(dataContainsCara);
		}
		
		[Test]
		public function contains_with_comparer_is_false_when_item_is_not_in_collection() {
			var data:Array = [
				new TestModel("brian", 33, 1234),
				new TestModel("cara", 34, 2345),
				new TestModel("eli", 0, 3456) ];
			
			var dataContainsMaia:Boolean = data.contains(new TestModel("maia", 3, 4567), new ModelComparator());
			
			assertThat(dataContainsMaia, equalTo(false));
		}
		
		
	}
}