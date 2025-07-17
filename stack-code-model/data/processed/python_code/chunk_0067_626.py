package validators {
	import vyperlogix.utils.StringUtils;
	
	import mx.validators.ValidationResult;
	import mx.validators.Validator;
	
	public class RssFeedValidator extends Validator {
		private var results:Array;
		
		public function RssFeedValidator() {
			super();
		}
		
		override protected function doValidation(value:Object):Array {
			var inputValue:String = String(value);
			
			results = [];
			
			results = super.doValidation(value);        
			if (results.length > 0)
				return results;

			var bool:Boolean = StringUtils.isUrl(inputValue);
			trace('(RssFeedValidator.doValidation).1 --> value='+value+', inputValue.length='+inputValue.length+', bool='+bool);
			if ( (!value) || (inputValue.length < 4) || (!bool) ) {
				results.push(new ValidationResult(true, null, "Not a URL !", "You must enter a valie URL."));
				return results;
			}       
			
			return results;
		}
	}
}