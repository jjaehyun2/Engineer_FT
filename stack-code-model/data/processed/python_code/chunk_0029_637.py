package com.demy.waterslide.stages 
{
	import com.demy.waterslide.stages.StageList;
	import com.demy.waterslide.GameStage;
	import feathers.controls.Button;
	import feathers.controls.Header;
	import feathers.controls.Panel;
	import feathers.core.PopUpManager;
	import feathers.data.ListCollection;
	import feathers.layout.HorizontalLayout;
	import feathers.layout.VerticalLayout;
	import feathers.skins.IStyleProvider;
	import starling.display.DisplayObject;
	import starling.events.Event;
	/**
	 * ...
	 * @author 
	 */
	public class StageListPanel extends Panel
	{		
		public static const EDIT:String = "edit stage";
		
		public static var globalStyleProvider:IStyleProvider;
		
		private static const NEW_STAGE_NAME:String = "Сцена";
		
		private var listView:StageList;
		private var addButton:Button;
		
		public function StageListPanel() 
		{
			createAndAddList();
			createAndAddButton();
			validate();			
		}
		
		override protected function initialize():void 
		{
			super.initialize();
			
			title = "Сцена:";
		}
		
		private function createAndAddList():void 
		{
			listView = new StageList();
			listView.dataProvider = new ListCollection([]);
			listView.addEventListener(Event.SELECT, selectStage);
			listView.addEventListener(EDIT, showEditStageDialog);
			addChild(listView);
		}
		
		private function selectStage(e:Event = null):void 
		{
			dispatchEventWith(Event.SELECT, false, listView.selectedItem);
		}
		
		private function showEditStageDialog(e:Event):void 
		{
			showEditDialog(listView.selectedItem as GameStage, false);
		}
		
		private function createAndAddButton():void 
		{
			addButton = new AddStageButton();
			addChild(addButton);
			addButton.addEventListener(Event.TRIGGERED, showAddStageDialog);
		}
		
		private function showAddStageDialog(e:Event):void 
		{
			showEditDialog(new GameStage(NEW_STAGE_NAME.concat(listView.dataProvider.length)), true);
		}
		
		private function showEditDialog(gameStage:GameStage, isNew:Boolean):void 
		{
			const dialog:Panel = new EditStageDialog(gameStage);
			PopUpManager.addPopUp(dialog);
			if (isNew) 
			{
				dialog.addEventListener(Event.COMPLETE, addItem);
			}
			else
			{
				dialog.addEventListener(Event.COMPLETE, updateItem);
			}
		}
		
		private function addItem(e:Event):void 
		{
			if ((e.data as GameStage).name == "") return;
			listView.dataProvider.addItem(e.data as GameStage);
			e.currentTarget.removeEventListener(Event.COMPLETE, addItem);
			PopUpManager.removePopUp(e.currentTarget as DisplayObject);
		}
		
		private function updateItem(e:Event):void 
		{
			if ((e.data as GameStage).name == "") return;
			listView.dataProvider.updateItemAt(listView.selectedIndex);
			e.currentTarget.removeEventListener(Event.COMPLETE, updateItem);
			PopUpManager.removePopUp(e.currentTarget as DisplayObject);
		}
		
		public function addAndSelectStage(stage:GameStage):void
		{
			listView.dataProvider.addItem(stage);
			listView.selectedIndex = listView.dataProvider.length - 1;
			updateList();
			selectStage();
		}
		
		private function updateList():void 
		{
			listView.invalidate(INVALIDATION_FLAG_DATA);
			dispatchEventWith(Event.CHANGE);
		}
		
		private function disposeListView():void 
		{
			if (listView)
			{
				listView.removeEventListener(Event.SELECT, selectStage);
				listView.dispose();
				listView = null;
			}
		}
		
		public function setWidth(value:Number):void
		{
			listView.width = value - addButton.width - getGap();
		}
		
		private function getGap():Number 
		{
			if (layout is HorizontalLayout) return (layout as HorizontalLayout).gap
			if (layout is VerticalLayout) return (layout as VerticalLayout).gap
			return 0;
		}
		
		override protected function get defaultStyleProvider():IStyleProvider
		{
			return StageListPanel.globalStyleProvider;
		}
		
		override public function dispose():void 
		{
			disposeListView();
			
			addButton.removeEventListener(Event.TRIGGERED, showAddStageDialog);
			addButton.dispose();
			addButton = null;
			
			super.dispose();
		}
		
	}

}