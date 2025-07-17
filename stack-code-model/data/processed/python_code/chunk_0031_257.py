package 
{
	/**
	 * ...
	 * @author Stephen Birsa
	 */
	final internal class Chunk 
	{
		internal var blocks:Array;
		internal var name:String;
		
		final public function Chunk(name:int) 
		{
			blocks = [];
			this.name = "chunk" + name;
		}
		
	}

}