package com.controls.comboBoxes.autocompleteComboBox
{
	public class AutoCompleteMatchType
	{
		
		public static const NONE:AutoCompleteMatchType = 
			new AutoCompleteMatchType("NONE",
				function (labelStr:String, itemStr:String):Boolean {
					return true;
				}
			)

		public static const BEGINNING:AutoCompleteMatchType = 
			new AutoCompleteMatchType("BEGINNING",
				function (labelStr:String, itemStr:String):Boolean {
					return (itemStr.toLowerCase().substring(0, labelStr.length) == labelStr.toLowerCase());
				}
		)

		public static const ANYPART:AutoCompleteMatchType = 
			new AutoCompleteMatchType("ANYPART",
				function (labelStr:String, itemStr:String):Boolean {
					return itemStr.toLowerCase().indexOf(labelStr.toLowerCase()) >= 0;
				}
			)
			
		public static const FULL:AutoCompleteMatchType = 
			new AutoCompleteMatchType("FULL",
				function (labelStr:String, itemStr:String):Boolean {
					return itemStr.toLowerCase() == labelStr.toLowerCase();
				}
			)
			

		public var matchFunction:Function;
		public var id:String;
		public function AutoCompleteMatchType(id:String, matchFunction:Function)
		{
			this.id = id;
			this.matchFunction = matchFunction;
		}
		
		public function toString():String{
			return "AutoCompleteMatchType::"+id;
		}
	}
}