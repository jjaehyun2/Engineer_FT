package framework.view.pages.inHouse.renders
{
	import services.vo.inHouse.PersonMessageVO;
	
	import mx.collections.ArrayCollection;
	import mx.controls.DataGrid;
	import mx.controls.dataGridClasses.DataGridItemRenderer;

	public class EmailItemRenderer extends DataGridItemRenderer
	{
		public function EmailItemRenderer()
		{
			super();
		}
		
		override public function validateNow():void
		{
			if (listData)
			{
				var provider:ArrayCollection = DataGrid(listData.owner).dataProvider as ArrayCollection;
				var item:PersonMessageVO = provider.getItemAt(listData.rowIndex) as PersonMessageVO;
				setStyle('fontWeight', (item.bIsRead) ? "normal" : "bold");
			}
			
			super.validateNow();
		}
	}
}