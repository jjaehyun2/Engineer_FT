package  {
	
	public class LinearEquation {
		
		private var coefficients:Vector.<Number> = new <Number> [];

		public function LinearEquation(...coefficients) {
			// constructor code
			for each(var coefficient:Number in coefficients) {
				this.coefficients.push(coefficient);
			}			
		}
		
		public function substitute(newCoefficients:Vector.<Number>):LinearEquation {
			coefficients = coefficients.concat(newCoefficients);
			return this;
		}
		
		public function getAllCoefficients():Vector.<Number> {
			return coefficients;
		}
		
		public function toString():String {
			return coefficients.toString();
		}

	}
	
}