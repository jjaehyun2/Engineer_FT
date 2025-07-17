package com.controls.datagrid
{

	import com.controls.datagrid.renderer.CheckDataGridHeaderRenderer;
	import com.controls.datagrid.renderer.CheckDataGridItemRenderer;
	
	import mx.controls.advancedDataGridClasses.AdvancedDataGridColumn;
	import mx.core.ClassFactory;

	public class CheckDataGridColumn extends AdvancedDataGridColumn
	{

		//--------------------------------------------------------------------------
		//
		//  Constructor
		//
		//--------------------------------------------------------------------------

		public function CheckDataGridColumn(columnName:String=null)
		{
			super(columnName);

			width=23;
			sortable=false;
			draggable=false;

			itemRenderer=new ClassFactory(CheckDataGridItemRenderer);
			headerRenderer=new ClassFactory(CheckDataGridHeaderRenderer);
		}

	}

}