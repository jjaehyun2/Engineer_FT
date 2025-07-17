package flexUnitTests
{
	import System.Collection.Generic.IGrouping;
	import System.Linq.Grouping;
	
	import org.flexunit.assertThat;
	import org.hamcrest.collection.array;
	import org.hamcrest.object.equalTo;

	public class GroupingTests
	{		
		[Test]
		public function Grouping_is_an_Array_with_a_key():void {
			var grouping:IGrouping = new Grouping("foo", [1,2,3,4,5]);
			
			assertThat(grouping.key, equalTo("foo"));
			assertThat(grouping.toArray(), array(1,2,3,4,5));
		}
		
		[Test]
		public function Grouping_without_Array_source_defaults_to_empty():void {
			var grouping:IGrouping = new Grouping("foo");
			
			assertThat(grouping.toArray().length, equalTo(0));
		}
		
		[Test(expected="ArgumentError")]
		public function Grouping_throws_ArgumentError_when_key_is_null():void {
			var grouping:IGrouping = new Grouping(null);
		}
		
		[Test]
		public function adding_to_Grouping_adds_to_end():void {
			var grouping:Grouping = new Grouping(0);
			
			grouping.add(5);
			grouping.add(6);
			
			assertThat(grouping.toArray(), array(5,6));
		}
		
	}
}