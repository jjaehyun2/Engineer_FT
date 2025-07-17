package kitaec.controls.comboboxes {
	
	import mx.collections.IList;

	public class AutoPopulatedValueComboBox extends ValueComboBox {
		
		private var oldSelectedValue:String;
		
		private var isDataProviderChanged:Boolean;
		
		
		override public function set dataProvider(value:IList):void {
			oldSelectedValue = selectedValue;
			if (value != dataProvider) {
				isDataProviderChanged = true;
			}
			super.dataProvider = value;
		}
		
		override public function set selectedValue(value:String):void {
			isDataProviderChanged = false;
			if (value == selectedValue) {
				invalidateProperties();
			} else {
				oldSelectedValue = selectedValue;
				super.selectedValue = value;
			}
		}
		
		override protected function findSelectedItem():void {
			if (selectedValue || !isDataProviderChanged) {
				super.findSelectedItem();
			} else {
				if (dataProvider && dataProvider.length > 0 && oldSelectedValue) {
					for each (var item:Object in dataProvider) {
						if (item[valueField] == oldSelectedValue) {
							selectedItem = null;
							selectedItem = item;
							isDataProviderChanged = false;
							return;
						}
					}
				}
				selectedIndex = -1;
				isDataProviderChanged = false;
			}
		}
	}
}