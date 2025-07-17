package com.likya.pinara.utils
{
	import spark.components.CheckBox;
	import spark.core.IDisplayText;
	
	public class ToggleSwitch extends CheckBox
	{
		//RO: [SkinPart( "false")]
		private var _selectedLabelField:IDisplayText;
		public function get selectedLabelField():IDisplayText
		{
			return _selectedLabelField;
		}
		public function set selectedLabelField(selectedLabelField:IDisplayText):void
		{
			_selectedLabelField = selectedLabelField;
		}
		
		//RO: [SkinPart( "false")]
		private var _deselectedLabelField:IDisplayText;
		public function get deselectedLabelField():IDisplayText
		{
			return _deselectedLabelField;
		}
		public function set deselectedLabelField(deselectedLabelField:IDisplayText):void
		{
			_deselectedLabelField = deselectedLabelField;
		}
		
		private var _selectedLabel:String = 'Yes';
		private var _deselectedLabel:String = 'No';
		
		public function ToggleSwitch()
		{
			super();
		}
		
		public function get deselectedLabel():String
		{
			return _deselectedLabel;
		}
		
		public function set deselectedLabel(value:String):void
		{
			_deselectedLabel = value;
			if(deselectedLabelField)
			{
				deselectedLabelField.text = deselectedLabel;
			}
		}
		
		public function get selectedLabel():String
		{
			return _selectedLabel;
		}
		
		public function set selectedLabel(value:String):void
		{
			_selectedLabel = value;
			if(selectedLabelField)
			{
				selectedLabelField.text = selectedLabel;
			}
		}
		
		/*override*/ protected function partAdded(partName:String, instance:Object):void
		{
			//RO: super.partAdded(partName, instance);
			if(instance == selectedLabelField)
			{
				selectedLabelField.text = selectedLabel;
			}
			if(instance == deselectedLabelField)
			{
				deselectedLabelField.text = deselectedLabel;
			}
		}
	}
}