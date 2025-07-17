package com.controls.treeDatagrid
{
	import com.controls.datagrid.CheckDataGrid;
	import com.controls.treeDatagrid.event.TreeAdvancedDataGridEvent;
	
	import flash.display.Sprite;
	import flash.events.ContextMenuEvent;
	import flash.utils.Dictionary;
	
	import mx.collections.HierarchicalCollectionView;
	import mx.collections.HierarchicalData;
	import mx.collections.IHierarchicalCollectionView;
	import mx.collections.IViewCursor;
	import mx.controls.listClasses.BaseListData;
	import mx.events.AdvancedDataGridEvent;
	
	[Event(name="expandTreeItem", type="com.db.rds.index.content.view.management.changeLog.TreeAdvancedDataGridEvent")]
	
	public class TreeDataGrid extends CheckDataGrid
	{
		public var rowColorFunction:Function;
		
		private var _parentColumnIndex:int;
		
		public function TreeDataGrid()
		{
			super();
			
			setStyle("disclosureClosedIcon", null); 
			setStyle("disclosureOpenIcon", null);
			
			addEventListener(TreeAdvancedDataGridEvent.EXPAND_TREE_ITEM, onExpandTreeItem);
		}
		
		private function onExpandTreeItem(event:TreeAdvancedDataGridEvent):void
		{
			var collection:HierarchicalCollectionView = dataProvider as HierarchicalCollectionView;
			
			if (collection && event.data.children)
			{
				var parentObject:Object = collection.getParentItem(event.data);
				if (parentObject || !event.isOpen)
				{
					expandChildrenOf(event.data, event.isOpen);
				}
				else
				{
					expandItem(event.data, event.isOpen);
				}
			}
			
			if (event.isOpen && event.data.children)
			{
				updateScrollPosition(event.data);
			}
		}
		
		public function updateScrollPosition(item:Object):void
		{
			var collection:HierarchicalCollectionView = dataProvider as HierarchicalCollectionView;
			
			var rowIndex:int = selectedIndex - (verticalScrollPosition - 1);
			var difference:int = (rowIndex + collection.calculateLength(item)) - (rowCount - 1);
			if ( difference > 0)
			{
				verticalScrollPosition += difference;
			}
		}
		
		override protected function drawRowBackground(s:Sprite, rowIndex:int, 
													  y:Number, height:Number, 
													  color:uint, dataIndex:int):void
		{
			if(rowColorFunction != null && dataProvider) 
			{
				var item:Object;
				if(dataIndex < dataProvider.length)
				{
					if (dataProvider is HierarchicalCollectionView)
					{
						var cursor:IViewCursor = IHierarchicalCollectionView(dataProvider).createCursor(); 
						for (var i:int = 0; i < rowIndex && !cursor.afterLast; i++) 
						{ 
							cursor.moveNext(); 
						} 
						item = cursor.afterLast ? null : cursor.current; 
					}
					else
					{
						item = dataProvider[dataIndex];
					}
				}
				
				if(item)
				{
					color = rowColorFunction(item, rowIndex, dataIndex, color);
				}
			}
			
			super.drawRowBackground(s, rowIndex, y, height, color, dataIndex);
		}
		
		public function get parentColumnIndex():int
		{
			return _parentColumnIndex;
		}

		public function set parentColumnIndex(value:int):void
		{
			_parentColumnIndex = value;
		}
		
	}
}