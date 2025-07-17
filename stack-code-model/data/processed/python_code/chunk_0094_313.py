package controls {
	import mx.core.UITextField;
	
	public class SpecialUITextField extends UITextField {
		public function SpecialUITextField() {
			super();
		}

		private static const TEXT_WIDTH_PADDING:int = 5;

		override public function truncateToFit(truncationIndicator:String = null):Boolean {
			validateNow();
			
			return true;
		}
	}
}