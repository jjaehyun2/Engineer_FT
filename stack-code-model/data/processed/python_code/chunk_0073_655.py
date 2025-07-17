package com.db.rds.content.ExceptionManagement.view.controls.renderers
{
	import com.db.rds.content.ExceptionManagement.view.controls.ThreeStateCheckBox;
	
	import flash.display.DisplayObjectContainer;
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	import mx.collections.ArrayCollection;
	import mx.collections.HierarchicalData;
	import mx.controls.AdvancedDataGrid;
	import mx.controls.CheckBox;
	import mx.controls.DataGrid;
	import mx.controls.advancedDataGridClasses.AdvancedDataGridColumn;
	import mx.controls.listClasses.AdvancedListBase;
	import mx.controls.listClasses.ListBase;
	import mx.core.UIComponent;
	import mx.events.CollectionEvent;
	
	public class CheckBoxHeaderRenderer extends ThreeStateCheckBox
	{	
		public function CheckBoxHeaderRenderer()
		{
			super();
			addEventListener(MouseEvent.CLICK, onClick);
			setStyle("paddingLeft", 5);
		}
		
		override public function set owner(value:DisplayObjectContainer):void
		{
			super.owner = value;
			
			if(owner)
			{
				owner.addEventListener("calculateMainCheckBoxState", onCalculateMainCheckBoxState);	
			}
			
		}
		
		private function onCalculateMainCheckBoxState(event:Event):void
		{
			calculateState();
		}
		
		override public function set data(value:Object):void
		{
			super.data =  value;
			calculateState();
		}
		
		private function calculateState():void
		{
			var item:Object;
			var allSelected:Boolean = true;
			var allNotSelected:Boolean = true;
			
			if(data is AdvancedDataGridColumn)
			{
				var grid:Object = this.owner as Object;
				var itemSource:ArrayCollection = grid.dataProvider.source is HierarchicalData ? grid.dataProvider.source.source : grid.dataProvider.source;
				
				for each(item in itemSource)
				{
					if(item.hasOwnProperty("selected"))
					{
						if(item.selected == -1)
						{
							allSelected = false;
							allNotSelected = false;
						}
						else if(item.selected == 1)
						{
							allNotSelected = false;
						}
						else if(item.selected == 0)
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
		}

		private function onClick(event:Event):void
		{			
			if(owner.hasOwnProperty("dataProvider"))
			{
				var item:Object;
				var grid:Object = this.owner as Object;
				var itemSource:ArrayCollection = grid.dataProvider.source is HierarchicalData ? grid.dataProvider.source.source : grid.dataProvider.source;
				
				for each(item in itemSource)
				{
					middle = false;
					selected = !selected;
					
					if(item.hasOwnProperty("selected"))
					{
						setState(itemSource.source, !selected);
					}
				}				
			}

			dispatchCustomEvent(new Event("checkBoxClick"));		
		} 
		
		private function setState(array:Array, flag:Boolean):void
		{
			for each(var item:Object in array)
			{
				if(item.hasOwnProperty("children"))
				{
					setState(item["children"], flag);
				}
				else
				{
					if(item.hasOwnProperty("selected"))
					{
						item["selected"] = flag;
					}
				}					
			}
		}
		
		private function dispatchCustomEvent(event:Event):void
		{
			if(this.owner is AdvancedDataGrid || this.owner is DataGrid)
			{
				this.owner.dispatchEvent(event);
			}
			else if(Object(this.owner).hasOwnProperty("owner"))
			{				
				Object(this.owner).owner.dispatchEvent(event);
			}
			else
			{
				throw new Error("Invalid CheckBoxItemRenderer owner!");
			}
		}
	}
}