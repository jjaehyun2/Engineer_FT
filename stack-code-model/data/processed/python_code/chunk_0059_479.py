package com.controls
{	
	import flash.events.KeyboardEvent;
	import flash.ui.Keyboard;
	
	import flashx.textLayout.factory.StringTextLineFactory;
	import flashx.textLayout.operations.DeleteTextOperation;
	import flashx.textLayout.operations.InsertTextOperation;
	import flashx.textLayout.operations.PasteOperation;
	
	import mx.utils.StringUtil;
	
	import spark.components.TextInput;
	import spark.events.TextOperationEvent;
	import spark.globalization.StringTools;
	
	[Exclude(name="restrict", kind="property")]
	public class NumberInput extends TextInput
	{
		public function NumberInput()
		{
			super();
			updateRegex();
		}
		
		//regex pattern
		private var regex:RegExp;
		
		private var _allowNegative:Boolean;
		private var _digitBeforeDot:int = 10;
		private var _digitAfterDot:int = 10;
		/**
		 * Specifies whether negative numbers are permitted.
		 * Valid values are true or false.
		 *
		 * @default true
		 */
		public function set allowNegative(value:Boolean):void
		{
			_allowNegative = value;
			updateRegex();
		}
		
		override public function set maxChars(value:int):void
		{
			super.maxChars = value;
			updateRegex();
		}
		
		/**
		 *  @private
		 */
		override public function set restrict(value:String):void
		{
			throw(new Error("You are not allowed to change the restrict property of this class.  It is read-only."));
		}
		
		override protected function childrenCreated():void
		{
			super.childrenCreated();
			
			//listen for the text change event
			addEventListener(TextOperationEvent.CHANGING, onTextChange);
		}

		
		public function onTextChange(event:TextOperationEvent):void
		{
			// What will be the text if this input is allowed to happen
			var textToBe:String = "";
			var match:Object;
			var firstDotIndex:int;
			
			
			if(event.operation is PasteOperation)
			{
				var pasteText:String = (PasteOperation(event.operation).textScrap.textFlow.getText());
							
				if(PasteOperation(event.operation).absoluteStart > 0 && PasteOperation(event.operation).absoluteStart < text.length)
				{
					var firstPart:String = text.substr(0,PasteOperation(event.operation).absoluteStart);
					var secondPart:String = text.substr(PasteOperation(event.operation).absoluteEnd);
					textToBe = firstPart + pasteText + secondPart;
				}
				else if(PasteOperation(event.operation).absoluteStart == 0)
				{
					textToBe = pasteText + text;
				}
				else if(PasteOperation(event.operation).absoluteStart == text.length)
				{
					textToBe = text + pasteText; 
				}
				
				firstDotIndex = textToBe.indexOf(".");
				if( firstDotIndex == 0)
				{
					event.preventDefault();
				}				
				
				if(isNaN(Number(textToBe)))
				{
					event.preventDefault();
				}
				
				
				match = regex.exec(textToBe);
				if (!match || match[0] != textToBe )
				{
					// The textToBe didn't match the expression... stop the event
					event.preventDefault();
				}
			}
			else if(regex && event.operation is InsertTextOperation)
			{
				// Check selection
				if (selectionActivePosition > -1)
				{
					textToBe += text.substr(0, selectionActivePosition)
				}
				//append the newly entered text with the existing text
				textToBe += InsertTextOperation(event.operation).text;
				if (selectionAnchorPosition > -1)
				{
					textToBe += text.substr(selectionAnchorPosition, text.length - selectionAnchorPosition);
				}
				
				match = regex.exec(textToBe);
				if (!match || match[0] != textToBe)
				{
					// The textToBe didn't match the expression... stop the event
					event.preventDefault();
				}
				//special condition checking to prevent multiple dots
				firstDotIndex = textToBe.indexOf(".");
				if( firstDotIndex != -1)
				{
					var lastDotIndex:int = textToBe.lastIndexOf(".");
					if(lastDotIndex != -1 && lastDotIndex != firstDotIndex)
						event.preventDefault();
				}
				/*if( firstDotIndex == 0)
				{
					event.preventDefault();
				}*/
			}
			else if(event.operation is DeleteTextOperation){
				var start:int = (event.operation as DeleteTextOperation).absoluteStart;
				var end:int = (event.operation as DeleteTextOperation).absoluteEnd;
				if (start==0 && this.text.substr(end,1)=="."){
					event.preventDefault();
				}
			}
		}
		
		private function updateRegex():void
		{
			var regexString:String;/* = "[\\d\.\\d]{1,99}";

			var charsCount:int = (maxChars != 0) ? maxChars : 99;
			if (maxChars !=0 )
			{
				regexString = "[\\d\.\\d]{1," + charsCount + "}";		
			}
			if(_allowNegative)
			{
				regexString = "(?<![--])(^[-]{1}[\\d\\.\\d]{1," + charsCount + "}|^-)|[\\d\.\\d]{1," + charsCount + "}";		
			}*/
			
			if(_allowNegative)
			{
				regexString = "(\\-?)([1-9]\\d*\\.\\d*|0?\\.[0-9]*|[1-9]\\d*)|(\\-0\\.0)|(0\\.0)|(\\-0\\.)|(0\\.)|(\\.0)|(\\-0)|(\\-\\.)|(\\-)|(\\.)|(0)";	
			}
			else
			{
				regexString = "([1-9]\\d*\\.\\d*|0?\\.[0-9]*|[1-9]\\d*)|(0\\.0)|(0\\.)|(\\.0)|(\\.)|(0)";	
			}





			regex = new RegExp(regexString);
		}
		
		override public function set errorString(value:String):void
		{
			super.errorString = value;
		}
	}
}