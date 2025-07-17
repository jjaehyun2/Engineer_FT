package  {
	
	public class Sum {

		public function Sum() {
			// constructor code
		}
		
		public function calculateAllInts( ints:Vector.<int> ):int {
			
			var result:int = 0;
			for each ( var number:int in ints ) {
				
				result += number;
				
			}
			return result;
			
		}
		
		public function calculateAllNumbers( numbers:Vector.<Number> ):Number {
			
			var result:Number = 0;
			for each ( var number:Number in numbers ) {
				
				result += number;
				
			}
			return result;
			
		}

	}
	
}