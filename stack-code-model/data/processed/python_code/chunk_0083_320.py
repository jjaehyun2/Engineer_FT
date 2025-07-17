package devoron.values.text
{
	
	/**
	 * TextValue
	 * @author Devoron
	 */
	public class TextValue
	{
		public var type:String = "short";
		
		public var shortText:String = "";
		public var longText:String = "";
		public var htmlText:String = "";
		
		public var included:Boolean = true;
		public var pathToText:String = "";
		
		
		public function TextValue()
		{
		
		}
		
		/**
		 * Клонирование значения.
		 * @return
		 */
		public function clone():TextValue
		{
			var textValue:TextValue = new TextValue();
			
			textValue.type = this.type;
			
			shortText = this.shortText;
			longText = this.longText;
			htmlText = this.htmlText;
			
			return textValue;
		}
		
		public function toString():String
		{
			
			var result:String = "";
			switch (type)
			{
				case "short": 
					result += "{";
					result += qutes("id") + ":" + qutes("ShortText") + ",";
					result += qutes("data") + ":" + "{";
					result += qutes("value") + ":" + qutes(shortText);
					result += "}";
					result += "}";
					break;
				
				case "long": 
					result += "{";
					result += qutes("id") + ":" + qutes("LongText") + ",";
					result += qutes("data") + ":" + "{";
					result += qutes("included") + ":" + included + ",";
					result += qutes("$url_text") + ":" + pathToText + ",";
					result += qutes("value") + ":" + qutes(longText) + ",";
					result += "}";
					result += "}";
					break;
				
				case "html": 
					result += "{";
					result += qutes("id") + ":" + qutes("HTMLText") + ",";
					result += qutes("data") + ":" + "{";
					result += qutes("included") + ":" + included + ",";
					result += qutes("$url_text") + ":" + pathToText + ",";
					result += qutes("value") + ":" + qutes(htmlText) + ",";
					result += "}";
					result += "}";
					break;
			
			}
			return result;
		}
		
		private function qutes(str:String):String
		{
			return '"' + str + '"';
		}
	
	}

}