package Biblioteca {
	
	public class CalculadoraSimples {
		
		//Dependências
		import flash.text.TextField;
		import flash.events.MouseEvent;
		import flash.events.FocusEvent;
		import flash.display.SimpleButton;
		
		//Propriedades
		private var numX: Number;
		private var numY: Number;
		
		private var textResult: TextField;
		private var textInputX: TextField;
		private var textInputY: TextField;
		private var btnAdicao: SimpleButton;
		private var btnSubtracao: SimpleButton;
		private var btnMultiplicao: SimpleButton;
		private var btnDivisao: SimpleButton;


		//Construtor
		public function CalculadoraSimples(textResult: TextField, 
										textInputX: TextField, 
										textInputY: TextField, 
										btnAdicao: SimpleButton, 
										btnSubtracao: SimpleButton, 
										btnMultiplicao: SimpleButton,
										btnDivisao: SimpleButton) {
										
			this.textResult = textResult;
			this.textInputX = textInputX;
			this.textInputY = textInputY;
			this.btnAdicao = btnAdicao;
			this.btnSubtracao = btnSubtracao;
			this.btnMultiplicao = btnMultiplicao;
			this.btnDivisao = btnDivisao;
										
			textInputX.restrict = "0-9\\-";
			textInputY.restrict = "0-9\\-";
										
			btnAdicao.addEventListener(MouseEvent.MOUSE_DOWN, Adicao);
			btnMultiplicao.addEventListener(MouseEvent.MOUSE_DOWN, Multiplicacao);
			btnDivisao.addEventListener(MouseEvent.MOUSE_DOWN, Divisao);
			btnSubtracao.addEventListener(MouseEvent.MOUSE_DOWN, Subtracao);

			textInputX.addEventListener(FocusEvent.FOCUS_OUT, FocusOut);
			textInputY.addEventListener(FocusEvent.FOCUS_OUT, FocusOut);
		}


		private function Adicao(event: MouseEvent = null): void {
			if(HaveValues()) {
				textResult.text = "Result: " + (numX + numY);
			}
		}

		private function Multiplicacao(event: MouseEvent = null): void {
			if(HaveValues()) {
				textResult.text = "Result: " + (numX * numY);
			}
		}

		private function Subtracao(event: MouseEvent = null): void {
			if(HaveValues()) {
				textResult.text = "Result: " + (numX - numY);
			}
		}

		private function Divisao(event: MouseEvent = null): void {
			if(HaveValues()) {
				if (numY != 0 && numX == 0) {
					textResult.text = "Result: 0";
				} else if (numY == 0) {
					textResult.text = "0 is Indivisible";
				} else {
					textResult.text = "Result: " + (numX / numY);
				}
			}
		}


		private function FocusOut(event: FocusEvent) {
			var textField: TextField = TextField(event.target);
			switch (textField.name) {
				case "NumberX_input":
					numX = Number(textField.text);
					break;
				default:
					numY = Number(textField.text);
					break;
			}
		}
		
		private function HaveValues(): Boolean {
			if (textInputX.text != "" && textInputY.text != "") {
				return true;
			}
			textResult.text = "Fields emptys";
			return false;
		}
	} //Fim de CalculadoraSimples
	
}