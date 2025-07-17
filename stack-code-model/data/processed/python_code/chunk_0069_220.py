package h2olib.control
{
	import flash.events.TextEvent;
	
	import mx.controls.TextInput;

	public class NumericTextInput extends TextInput
	{
		public function NumericTextInput()
		{
			super();
			restrict = "[0-9.]";
			maxChars = 10;
			addEventListener(TextEvent.TEXT_INPUT, onTextInput);
		}



		private function onTextInput(event:TextEvent):void
		{
			if(text.indexOf(".")>-1 && event.text == ".")
			{
				event.preventDefault();
				return;
			}
			
			var newText:String;
			if(selectionBeginIndex == text.length)
			{
	            newText = text + event.text;
			}
			else
			{
				newText = text.substring(0,selectionBeginIndex) + event.text + text.substring(selectionEndIndex,text.length);
			}

			var pattern1:String = "\\.([0-9]){1," + _digitAfterDot + "}$";
            //var mask:RegExp = /^([0-9]){1,7}.([0-9]){1,2}$/ig;//new RegExp(pattern,"ig");
			var mask1:RegExp = new RegExp(pattern1,"ig");

			var pattern2:String = "^([0-9]){1," + _digitBeforeDot + "}\\.([0-9]){1," + _digitAfterDot + "}$";
            //var mask:RegExp = /^([0-9]){1,7}.([0-9]){1,2}$/ig;//new RegExp(pattern,"ig");
			var mask2:RegExp = new RegExp(pattern2,"ig");
			
			

            //if(((newText.replace('.','')).length > _digitBeforeDot)	|| (newText.length > _digitAfterDot && newText.indexOf(".") > -1 && newText.indexOf(".") < newText.length - 1))
            if(newText.indexOf(".") == -1 && newText.length > _digitBeforeDot)
            {
  				event.preventDefault();
				return;          	
            }
            
            if(newText.indexOf(".") > -1)
            {
            	if(newText.substr(0,newText.indexOf(".")).length -1 > _digitBeforeDot)
            	{
  					event.preventDefault();
					return;
            	}
             	if(newText.substr(newText.indexOf(".")).length - 1 > _digitAfterDot)
            	{
  					event.preventDefault();
					return;
            	}           	
            } 
            
            if(newText.length > 1)
            {
	            if(newText.indexOf(".") == 0)
	            {            
		            if (!mask1 || !mask1.test(newText))
		        	{
		            	event.preventDefault();
		        	}
	            }
	            else
	            {
	            	if(newText.replace('.','').length > _digitBeforeDot)
	            	{
		            	if (!mask2 || !mask2.test(newText))
		        		{
		            		event.preventDefault();
		        		}
	            	}
	            }
            }
		}

		public function set value(value:Number):void
		{
			text = isNaN(value) ? "0.00" : value.toString();
		}
		public function get value():Number
		{
			return Number(text);
		}
		private var _digitBeforeDot:int = 7;
		public function set digitBeforeDot(value:int):void
		{
			_digitBeforeDot =  value;
			maxChars = _digitBeforeDot + _digitAfterDot + 1;
		}
		private var _digitAfterDot:int = 2;
		public function set digitAfterDot(value:int):void
		{
			_digitAfterDot = value;
			maxChars = _digitBeforeDot + _digitAfterDot + 1;
		}
	}
}