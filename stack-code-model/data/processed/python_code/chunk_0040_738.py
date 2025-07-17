package  {
	
	public class EquationResolver {

		public function EquationResolver() {
			// constructor code
		}
		
		public static function handleEquations(equations:Vector.<LinearEquation>):EquationAnswer {
			var existingParameterColomns:int = equations[0].getAllCoefficients().length;
			var hintEquations:Vector.<LinearEquation> = new <LinearEquation> [];
			var equationIndex:int = 0;
			while(existingParameterColomns > 1) {
				var futureDerivative:Vector.<LinearEquation> = new <LinearEquation> [];
				for(var i:int = 0; i < equations.length - 1; i++) {
					if(revealExistingLookaheadParameters(equations[i]) == revealExistingLookaheadParameters(equations[i + 1]))
						futureDerivative.push(EquationBinder.eliminateInitialCoefficient(equations[i], equations[i + 1]));
				}
				hintEquations.push(equations[0]);
				equations = futureDerivative;
				existingParameterColomns--;
			}
			trace(hintEquations[2]);
			var answer:EquationAnswer = new EquationAnswer(hintEquations.length);
			for (var j:int = hintEquations.length - 1; j > -1; j--) {
				var thisLine:Vector.<Number> = hintEquations[j].getAllCoefficients();
				var notAnswerPortion:Number = 0;
				for(var k:int = j - 1; k < j; k--) {
					notAnswerPortion += thisLine[k]*(answer.getParameter(k));
				}
				answer.setParameter(j, (thisLine[thisLine.length - 1] - notAnswerPortion)/thisLine[0]);
				trace(notAnswerPortion);
			}
			return answer;
		}
		
		private static function revealExistingLookaheadParameters(equation:LinearEquation):int {
			var result:int = 0;
			var coefficients:Vector.<Number> = equation.getAllCoefficients().slice(0, -1);
			for(var i:int = 0; i < coefficients.length; i++) {
				if(coefficients[i] != 0)
					result++;
				else
					break;
			}
			return result;
		}

	}
	
}