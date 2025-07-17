package tests 
{
	
	public class TestLength extends ArrayClearTest
	{
		public function TestLength() 
		{
			name = "Test: Setting length = 0\t\t\t";
		}
		
		override public function clearArrays():void 
		{
			var array:Array;
			for (var i:int = 0; i < m_array.length; i++)
			{
				m_array[i].length = 0;
			}
		}
		
	}
	
}