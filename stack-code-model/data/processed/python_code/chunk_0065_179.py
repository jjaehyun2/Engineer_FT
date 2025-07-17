package  {
	
	public class ColorPortionResolver {

		public function ColorPortionResolver() {
			// constructor code
		}
		
		public static function separateColor(red:Number, green:Number, blue:Number):Vector.<Number> {
			var result:Vector.<Number> = new <Number> [];
			var white:Number = Math.min(red, green, blue);
			
			
			result.push(white);
			
			return result;
		}

	}
	
}