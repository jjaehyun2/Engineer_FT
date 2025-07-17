package tests
{

	public class TestBrackets extends ArrayClearTest
	{
		public function TestBrackets() 
		{
			name = "Test: Using array = []\t\t\t";
		}
		
		override public function clearArrays():void 
		{
			var array:Array;
			for (var i:int = 0; i < m_array.length; i++)
			{
				m_array[i] = [];
			}
		}		
	}
	
}