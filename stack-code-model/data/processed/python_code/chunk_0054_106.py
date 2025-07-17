package com.grantech.controls.items
{
	import com.grantech.managers.DataManager;
	import com.grantech.models.ControlsHelper;
	import com.grantech.utils.Localizations;

	import feathers.controls.PickerList;
	import feathers.controls.popups.CalloutPopUpContentManager;
	import feathers.controls.renderers.DefaultListItemRenderer;
	import feathers.controls.renderers.IListItemRenderer;
	import feathers.data.ArrayCollection;

	import starling.events.Event;
	
	public class InspectorComboItemRenderer extends InspectorBaseItemRenderer
	{
		public function InspectorComboItemRenderer() { super(); }
		override protected function redrawControl():void
		{
			super.redrawControl();

			if (this.valueDisplay == null)
			{
				this.valueDisplay = new PickerList();
				this.valueDisplay.layoutData = VALUE_LAYOUTDATA;
				this.addChild(this.valueDisplay);

				var combo:PickerList = valueDisplay as PickerList;
				combo.popUpContentManager = new CalloutPopUpContentManager();
				combo.itemRendererFactory = function():IListItemRenderer
				{
					var itemRenderer:DefaultListItemRenderer = new DefaultListItemRenderer();
					itemRenderer.labelFunction = labelFunction;
					return itemRenderer;
				}
				combo.labelFunction = this.labelFunction;
			}
			
			var listData:Array = ControlsHelper.instance.getData(this.label) as Array;
			combo = valueDisplay as PickerList;
			combo.removeEventListeners(Event.CHANGE);
			combo.dataProvider = new ArrayCollection(listData);
			combo.selectedIndex = listData.indexOf(this.value+"");
			combo.prompt = this.labelFunction(listData[combo.selectedIndex]);
			combo.addEventListener(Event.CHANGE, comboDisplay_changeHandler);
		}
		private function labelFunction(item:Object):String
		{
			return Localizations.instance.get(this.label + "_" + item);
		}
		
		private function comboDisplay_changeHandler(e:Event):void
		{
			if (valueDisplay == null)
				return;

			if (PickerList(valueDisplay).selectedItem == this.value)
				return;
			this.value = PickerList(valueDisplay).selectedItem;
			DataManager.instance.selectedlayer.setProperty(this.label, this.value);
		}
	}
}