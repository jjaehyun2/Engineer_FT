package com.db.rds.content.ExceptionManagement.view.controls.multiSelectComboBox
{
	import com.db.rds.content.ExceptionManagement.view.controls.ThreeStateCheckBox;
	
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	import mx.core.UIComponent;
	import mx.events.DynamicEvent;

	public class MultiSelectComboBoxItemRenderer extends ThreeStateCheckBox
	{
		public function MultiSelectComboBoxItemRenderer()
		{
			addEventListener(MouseEvent.CLICK, onClick);
			setStyle("paddingLeft", 5);
			setStyle('textAlign', "left");
		}
		
		override public function set data(value:Object):void
		{
			super.data =  value;
			if(value != null)
			{
				var combo:MultiSelectComboBox = this['owner']['owner'] as MultiSelectComboBox;
				if(combo && value[combo.labelField] == combo.allItemLabel)
				{
					var allSelected:Boolean = true;
					var allNotSelected:Boolean = true;
					for each(var item:Object in combo.dataProvider)
					{
						if(item.hasOwnProperty(combo.selectionField))
						{
							if(item[combo.selectionField])
							{
								allNotSelected = false;
							}
							else
							{
								allSelected = false;
							}
						}
					}
					
					if(allSelected)
					{
						middle = false;
						selected = true;
					}
					else if(allNotSelected)
					{
						middle = false;
						selected = false;
					}
					else
					{
						middle = true;
						selected = true;
					}
				}
				else if(data.hasOwnProperty(combo.selectionField))
				{   
					selected = value.selected;
				}
			}   
		}
		
		private function onClick(event:Event):void
		{
			var combo:MultiSelectComboBox = this['owner']['owner'] as MultiSelectComboBox;
			if(combo && data[combo.labelField] == combo.allItemLabel)
			{
				middle = false;
				//selected = !selected;
				for each(var item:Object in combo.dataProvider)
				{
					if(item.hasOwnProperty(combo.selectionField))
					{
						item[combo.selectionField] = selected ? 0 : 1;
					}
				}				
			}	
			
			data.selected = selected ? 1 : 0;
			var e:DynamicEvent = new DynamicEvent(MultiSelectComboBox.UPDATE_SELECTION_STATES_EVENT, true);
			e.data = data;
			UIComponent(owner).owner.dispatchEvent(e);
		}
	}
}