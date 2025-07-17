package com.db.rds.content.ExceptionManagement.view.controls
{
	import com.db.rds.content.ExceptionManagement.domain.EMFieldsMap;
	import com.db.rds.content.ExceptionManagement.view.controls.renderers.CheckBoxRenderer;
	
	import mx.controls.advancedDataGridClasses.AdvancedDataGridColumn;
	import mx.controls.advancedDataGridClasses.AdvancedDataGridRendererDescription;
	import mx.controls.advancedDataGridClasses.AdvancedDataGridRendererProvider;
	import mx.core.ClassFactory;
	
	public class CheckAdvancedDataGridRendererProvider extends AdvancedDataGridRendererProvider
	{
		public function CheckAdvancedDataGridRendererProvider()
		{
			super();
		}
		
		public override function describeRendererForItem(data:Object, 
														 dataDepth:int, 
														 column:AdvancedDataGridColumn,
														 description:AdvancedDataGridRendererDescription):void
		{
			// check for matching properties
			if(checkMatch(data, dataDepth, column))
			{
				if(data.hasOwnProperty(EMFieldsMap.PROP_IS_PAGES_ROW) && data[EMFieldsMap.PROP_IS_PAGES_ROW] == 1)
				{
					description.columnSpan = this.columnSpan;
					description.renderer = this.renderer;
				}
				else
				{
					description.columnSpan = 1;
					var cf:ClassFactory = new ClassFactory(com.db.rds.content.ExceptionManagement.view.controls.renderers.CheckBoxRenderer);
					description.renderer = cf;
				}
			}
		}
	}
}