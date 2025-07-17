package framework.view.pages.checkIn
{
	import mx.collections.HierarchicalData;
	import mx.controls.AdvancedDataGrid;
	import mx.core.ClassFactory;

	public class RoomListDataGrid extends AdvancedDataGrid
	{
		
		public function RoomListDataGrid()
		{
			super();			
			itemRenderer = new ClassFactory(RoomListItemRenderer);
			groupItemRenderer = new ClassFactory(RoomListGroupItemRenderer);
		}
		
	}
}