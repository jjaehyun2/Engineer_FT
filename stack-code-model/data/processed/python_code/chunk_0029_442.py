package com.wm.net.py 
{
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	
	/**
	 * ...
	 * @author wmTiger
	 */
	public class ByteArrayLittle extends ByteArray 
	{
		
		public function ByteArrayLittle() 
		{
			super();
			endian = Endian.LITTLE_ENDIAN;
		}
		
	}

}