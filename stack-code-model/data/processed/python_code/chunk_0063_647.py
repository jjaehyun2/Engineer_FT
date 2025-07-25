package org.osflash.stream
{
	import asunit.asserts.assertEquals;

	import org.osflash.stream.types.vector.StreamVectorOutput;
	/**
	 * @author Simon Richardson - me@simonrichardson.info
	 */
	public class StreamVectorOutputTest
	{
		
		protected var stream : IStreamOutput;
		
		[Before]
		public function setUp() : void
		{
			stream = new StreamVectorOutput();
		}
		
		[After]
		public function tearDown() : void
		{
			stream = null;
		}
				
		[Test]
		public function test_toString() : void
		{
			stream.writeUTF('hello');
			stream.writeUTF('world');
			stream.writeUnsignedInt(1);
			
			trace(stream.toString());
			
			assertEquals('toString method should equal', 'helloworld1', stream.toString());
		}
	}
}