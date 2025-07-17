package com.controls.treeDatagrid.renderer
{

	import com.controls.treeDatagrid.TreeDataGrid;
	import com.controls.treeDatagrid.TreeDataGridColumn;
	import com.controls.treeDatagrid.event.TreeAdvancedDataGridEvent;
	import com.controls.treeDatagrid.skin.TreeToggleButtonSkin;
	
	import flash.events.MouseEvent;
	import flash.utils.Dictionary;
	
	import mx.binding.utils.BindingUtils;
	import mx.collections.HierarchicalCollectionView;
	import mx.collections.IHierarchicalCollectionView;
	import mx.collections.IViewCursor;
	import mx.controls.AdvancedDataGrid;
	import mx.controls.advancedDataGridClasses.AdvancedDataGridColumn;
	import mx.controls.advancedDataGridClasses.AdvancedDataGridListData;
	import mx.controls.listClasses.BaseListData;
	import mx.controls.listClasses.IDropInListItemRenderer;
	import mx.controls.listClasses.IListItemRenderer;
	import mx.events.FlexEvent;
	
	import spark.components.HGroup;
	import spark.components.Label;
	import spark.components.ToggleButton;
	import spark.layouts.VerticalAlign;

	public class TreeColumnItemRenderer extends HGroup implements IDropInListItemRenderer,
		IListItemRenderer
	{
		private var _listData:BaseListData;

		private var _data:Object;

		private var _toggleButton:ToggleButton;

		private var _label:Label;

		private var _labelText:String;

		public function TreeColumnItemRenderer()
		{
			super();
			percentHeight = 100;
			percentWidth = 100;
			verticalAlign = VerticalAlign.MIDDLE;

		}
		
		override protected function createChildren():void
		{
			_toggleButton = new ToggleButton();
			_toggleButton.setStyle("skinClass", TreeToggleButtonSkin);
			_toggleButton.visible = true;
			_toggleButton.addEventListener(MouseEvent.CLICK, toggleButtonClickHandler);
			addElement(_toggleButton);

			_label = new Label();
			_label.percentWidth = 100;
			_label.maxDisplayedLines = 1;
			addElement(_label);
		}

		private function toggleButtonClickHandler(event:MouseEvent):void
		{
			dispatchEvent(new TreeAdvancedDataGridEvent(TreeAdvancedDataGridEvent.EXPAND_TREE_ITEM,
														true, false, data, _toggleButton.selected));
		}

		public function get data():Object
		{
			return _data;
		}

		public function set data(value:Object):void
		{
			_data = value;
		}

		public function get listData():BaseListData
		{
			return _listData;
		}

		public function set listData(value:BaseListData):void
		{
			_listData = value;
			if (_listData)
			{
				drawRenderer();
			}
		}
		
		public function get labelText():String
		{
			return _label.text;
		}

		private function drawRenderer():void
		{
			var currentData:AdvancedDataGridListData = listData as AdvancedDataGridListData;
			if (currentData)
			{
				var gridOwner:TreeDataGrid = listData.owner as TreeDataGrid;
				var item:Object = currentData.item;
				var childColumn:TreeDataGridColumn = gridOwner.columns[currentData.columnIndex] as TreeDataGridColumn;
				var childDataField:String = childColumn ? childColumn.childDataField : "";
				var dataField:String = currentData.dataField;
	
				_toggleButton.visible = item.hasOwnProperty(dataField) && ((item[dataField] &&
					(item.hasOwnProperty("children")) &&
					(childDataField ? !item[childDataField] : true)) ||
					currentData.columnIndex == gridOwner.parentColumnIndex);
				_toggleButton.selected = (listData.owner as AdvancedDataGrid).isItemOpen(item);
				_label.text = _toggleButton.visible ? currentData.label : "";
				
			}

		}
		
		private function doubleClickHandler(event:MouseEvent):void
		{
		}
		
	}
}