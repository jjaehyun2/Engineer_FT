package flexUnitTests
{
	import System.Collection.Generic.IEnumerable;
	
	import org.flexunit.assertThat;
	import org.hamcrest.collection.array;

	public class ReverseTests extends EnumerableTestsBase
	{		
		[Test]
		public function reverse_enumerates_collections_in_reverse():void {
			var reverse:IEnumerable = [1,2,3,4,5].reverseEnumerate();
			
			assertThat(reverse.toArray(), array(5,4,3,2,1));
		}
		
		
	}
}