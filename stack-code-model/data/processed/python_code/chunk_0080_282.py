package services.events.reports
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;

	public class GetItemTreeEvent extends BaseEvent
	{		
		
		public function GetItemTreeEvent(type:String)
		{
			super(AppController.GET_ITEM_TREE_EVENT);
		}		
	}
}