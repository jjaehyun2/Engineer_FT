package flexUnitTests
{
	import System.Collection.Generic.IEnumerable;
	import System.Linq.Enumerable;
	
	import flexunit.framework.Assert;

	public class IntegrationTests extends EnumerableTestsBase
	{		
		[Test]
		public function Do_A_Bunch_Of_Stuff() {
			var morphed:IEnumerable = [1,2,3,4,5,6]
				.where(function(x) { return x % 2 } )
				.select(function(x) { return x * 4 } )
				.skip(1);
			
			var result:int = morphed.sum();
			Assert.assertEquals(result, 32);
			
			result = morphed.sum();
			Assert.assertEquals(result, 32);
			
		}
		
		
	}
}