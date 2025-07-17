package com.db.rds.content.ExceptionManagement.view.controls.renderers
{
	import com.db.rds.content.ExceptionManagement.domain.EMFieldsMap;
	import com.db.rds.content.ExceptionManagement.view.controls.PagingControl;
	import com.db.rds.content.ExceptionManagement.view.skin.PagingGroupItemRendererSkin;
	
	import mx.containers.VBox;
	import mx.controls.Label;
	import mx.controls.advancedDataGridClasses.AdvancedDataGridItemRenderer;
	import mx.controls.listClasses.IListItemRenderer;
	import mx.core.IDataRenderer;
	
	import spark.components.SkinnableContainer;

	public class PagingGroupItemRenderer extends SkinnableContainer implements IListItemRenderer
	{
		private var pagingControl:PagingControl;
				
		public function PagingGroupItemRenderer()
		{
			super(); 
			setStyle("skinClass", com.db.rds.content.ExceptionManagement.view.skin.PagingGroupItemRendererSkin);
		}
		
		protected override function createChildren():void
		{
			super.createChildren();
			
			if(!pagingControl)
			{
				pagingControl = new PagingControl();
				addElement(pagingControl);
			}
		}
		
		protected override function commitProperties():void
		{
			super.commitProperties();
			
			if(pagingControl && data)
			{
				if(data[EMFieldsMap.PROP_IS_PAGES_ROW] == 1)
				{
					pagingControl.pagesCount = data[EMFieldsMap.PROP_PAGES_COUNT];
				}
			}
			
		}
		
		private var _data:Object;
		
		public function get data():Object
		{
			return _data;
		}
		
		public function set data(value:Object):void
		{
			_data = value;
			invalidateProperties();
		}
	}
}