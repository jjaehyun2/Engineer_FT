package  {
	
	public class EquationBinder {

		public function EquationBinder() {
			// constructor code
		}
		
		public static function eliminateInitialCoefficient(a:LinearEquation, b:LinearEquation):LinearEquation {
			var coefficientsOfA:Vector.<Number> = new Vector.<Number>().concat(a.getAllCoefficients());
			var coefficientsOfB:Vector.<Number> = new Vector.<Number>().concat(b.getAllCoefficients());
			var multiplier:Number = coefficientsOfB[0]/coefficientsOfA[0];
			coefficientsOfA.shift();
			coefficientsOfB.shift();
			for (var i:int = 0; i < coefficientsOfA.length; i++) {
				coefficientsOfA[i] = coefficientsOfA[i]*multiplier - coefficientsOfB[i];
			}
			return new LinearEquation().substitute(coefficientsOfA);
		}

	}
	
}