package flexUnitTests
{
	import System.Collection.Generic.IComparer;
	import System.Collection.Generic.IEqualityComparer;
	
	public class ModelComparator implements IEqualityComparer, IComparer
	{
		public function Equals(x:*, y:*):Boolean
		{
			return x.soc == y.soc;
		}
		
		public function compare(x:*, y:*):int {
			if(x.age < y.age) return -1;
			if(x.age > y.age) return 1;
			return 0;
		}
	}
}