package General 
{
	import Descriptor.BRIEFDescriptor;
	import flash.geom.Point;
	/**
	 * ...
	 * @author Olivier Leclerc
	 */
	public class Feature 
	{
		public var score:int;
		public var pos:Point;
		public var descriptor:BRIEFDescriptor;
		public var match:Feature;
		public var consecutiveMatches:int = 1;
		
		public function Feature() 
		{
			
		}
		
	}

}