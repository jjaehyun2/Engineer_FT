package com.db.rds.content.ExceptionManagement.view.controls.multiSelectComboBox
{
	import com.db.rds.content.ExceptionManagement.view.controls.renderers.CheckBoxRenderer;
	
	import flash.events.Event;
	
	import mx.collections.ArrayCollection;
	import mx.collections.IList;
	import mx.controls.ComboBox;
	import mx.core.ClassFactory;
	import mx.core.IFactory;
	import mx.events.DynamicEvent;
	
	import spark.components.DropDownList;

	[Event(name="selectionChanged", type="flash.events.Event")]

	public class MultiSelectComboBox extends ComboBox
	{
		public static const UPDATE_SELECTION_STATES_EVENT:String = "updateSelectionStates";
		
		public static const STATE_SELECTED:int = 1;
		public static const STATE_UNSELECTED:int = 0;
		public static const STATE_SEMISELECTED:int = -1;
		
		public var allItemNeeded:Boolean = true;
		public var allItemID:Number = -100;
		public var allItemLabel:String = "All";
		
		[Inspectable(enumeration="{MultiSelectComboBox.STATE_SELECTED},{MultiSelectComboBox.STATE_UNSELECTED},{MultiSelectComboBox.STATE_SEMISELECTED}")]
		public var startAllItemsSelectionState:int = STATE_SELECTED;
		
		public var nothingSelectedLabel:String = "";
		public var anySelectedLabel:String = "...";
		
		private var _dropdownFactory:ClassFactory;
		private var _itemRendererFactory:ClassFactory;
		
		public var maxDropDownHeight:Number = 200;
		
		public var idField:String = "id";
		public var selectionField:String = "selected";
		
		[Bindable]
		private var allLevelItems:Object;
		
		public function MultiSelectComboBox()
		{
			super();
			
			_dropdownFactory = new ClassFactory(MultiSelectComboBoxDropDown);
			dropdownFactory = _dropdownFactory;

			_itemRendererFactory = new ClassFactory(MultiSelectComboBoxItemRenderer);

			this.addEventListener(UPDATE_SELECTION_STATES_EVENT, updateSelectionStates);
		}

		protected override function commitProperties():void
		{
			super.commitProperties();
			
			itemRenderer = itemRendererFactory;
		}
		
		private function get itemRendererFactory():IFactory
		{
			_itemRendererFactory = new ClassFactory(MultiSelectComboBoxItemRenderer);
			return _itemRendererFactory;
		}

		private function updateSelectionStates(event:DynamicEvent):void
		{
			if(event.data[labelField] == allItemLabel)
			{
				for each(var item:Object in dataProvider)
				{
					item[selectionField] = event.data[selectionField];
				}
			}
			else
				updateAllItemSelectionState();

			this.text = selectedLabel;
			
			dropdown.invalidateList();
			dropdown.invalidateDisplayList();
			
			dispatchEvent(new Event("selectionChanged"));
		}

		public function get selectedItems():Array
		{
			var arr:Array = [];
			
			for each(var item:Object in dataProvider)
			{
				if(item != null && item[selectionField] == STATE_SELECTED && item[labelField] != allItemLabel)
					arr.push(item);
			}
			
			return arr;
		}

		public function get selectedItemsIDs():Array
		{
			var arr:Array = [];
			
			for each(var item:Object in selectedItems)
			{
				if(item.hasOwnProperty(idField))
					arr.push(item[idField]);
			}
			
			return arr;
		}

		public function get selectedItemsLabels():Array
		{
			var arr:Array = [];
			
			for each(var item:Object in selectedItems)
			{
				if(item.hasOwnProperty(labelField))
					arr.push(item[labelField]);
			}
			
			return arr;
		}
		
		public override function get selectedLabel():String
		{
			if(selectedItemsLabels.length == 0)
				return nothingSelectedLabel;
			else if(isAllItemsSelected)
				return allLevelItems[labelField] as String;
			return anySelectedLabel
		}
		
		public override function set dataProvider(value:Object):void
		{
			super.dataProvider = value;
			
			removeNullableItems();
			
			if(this.dataProvider != null && this.dataProvider.hasOwnProperty("length") && this.dataProvider.length > 0)
			{
				if(allItemNeeded && !hasAllItem)
					initAllItem(startAllItemsSelectionState);
				
				ArrayCollection(dataProvider).addItemAt(allLevelItems, 0);
				
				updateAllItemSelectionState();
			}
		}

		public function set allItemState(state:int):void
		{
			if(!allItemNeeded)
				return;
				
			if(!dataProvider || dataProvider['length'] == 0 || !hasAllItem)
			{
				if(!allLevelItems)
					initAllItem(state);
				else
					allLevelItems[selectionField] = state;

				if(!dataProvider)
					dataProvider = new ArrayCollection();

				dataProvider.addItemAt(allLevelItems, 0);
			}
			else
				allLevelItems[selectionField] = state;
				
			var e:DynamicEvent = new DynamicEvent(UPDATE_SELECTION_STATES_EVENT, false);
			e.data = allLevelItems;
			dispatchEvent(e);
		}
		
		private function initAllItem(state:int):void
		{
			allLevelItems = new Object();
			allLevelItems[idField] = allItemID;
			allLevelItems[labelField] = allItemLabel;
			allLevelItems[selectionField] = state;
		}
		
		private function get hasAllItem():Boolean
		{
			for each(var item:Object in dataProvider)
			{
				if(item != null && item[labelField] == allItemLabel)
					return true;
			}
			return false;
		}
		
		private function updateAllItemSelectionState():void
		{
			if(!allItemNeeded || !dataProvider || dataProvider.length == 0)
				return;
			
			if(isAllItemsSelected)
				allLevelItems[selectionField] = STATE_SELECTED;
			else if(selectedItemsLabels.length > 0)
				allLevelItems[selectionField] = STATE_SEMISELECTED;
			else
				allLevelItems[selectionField] = STATE_UNSELECTED;
		} 
		
		private function get isAllItemsSelected():Boolean
		{
			if(!allItemNeeded)
				return false;
				
			return selectedItemsLabels.length == dataProvider.length - 1;
		}
		
		private function removeNullableItems():void
		{
			for (var i:int = 0; i < this.dataProvider.length; i++)
			{
				if(this.dataProvider[i] == null)
					IList(this.dataProvider).removeItemAt(i);
			}
		}
	}
}