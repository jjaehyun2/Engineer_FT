package services.command.backend
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.backend.AddHotelSubGroupDelegate;
	import services.events.backend.AddHotelSubGroupsEvent;
	import framework.model.AppModelLocator;
	import services.vo.items.ItemsGroupVO;
	
	import mx.controls.Alert;
	import mx.rpc.IResponder;

	public class AddHotelSubGroupCommand implements ICommand, IResponder
	{
		/**
		 *  This property contains the model with all data.
		 *  
		 *  @see framework.model.RModel
		 */
		private var model:AppModelLocator = AppModelLocator.getInstance();
		/**
		 *  This property contains the event to make the request to add
		 *  new hotel main groups.
		 *  
		 *  @see services.events.backend.AddHotelMainGroupsEvent
		 */
		private var evt:AddHotelSubGroupsEvent;
		/**
		 *  Interface method. 
		 *  <p>Execute for forwarding the event to the method
		 *  <code>addHotelSubGroups()</code>.
		 * 
		 *  @see com.adobe.cairngorm.commands.ICommand
		 *  @see services.events.backend.AddHotelMainGroupsEvent
		 *  @see services.business.backend.AddHotelMainGroupDelegate
		 *  
		 *  @see services.business.backend.AddHotelSubGroupDelegate.addHotelSubGroups
		 */
		public function execute(event:CairngormEvent):void
		{
			evt = AddHotelSubGroupsEvent(event);
			var delegate:AddHotelSubGroupDelegate = new AddHotelSubGroupDelegate(this);
			
			delegate.addHotelSubGroups(evt);
		}
		/**
		 *  The handler for result of execution of request for
		 *  <code>addHotelSubGroups()</code>.
		 *  <p>This handler can get result for 2 modes:
		 *     <ul>
		 *     <li>add mode - for adding new sub groups;</li>
		 *     <li>edit mode - for editing selected sub group.</li>
		 *     </ul>
		 *  
		 *  @see services.business.backend.AddHotelSubGroupDelegate.addHotelSubGroups
		 */
		public function result(data:Object):void
		{
			var items:Array = data as Array;
			var group:ItemsGroupVO = model.itemsModule.hotelItemsGroupProvider.getItemAt(evt.groupIndex) as ItemsGroupVO;
			
			for(var i:int = 0; i < items.length; i++)
			{
				if (evt.subGroupIndex + i != group.aSubGroups.length)
				{
					// edit mode
					group.aSubGroups[evt.subGroupIndex + i] = items[i] as ItemsGroupVO;
				}
				else
				{
					// add mode
					group.aSubGroups[evt.subGroupIndex + i] = items[i] as ItemsGroupVO;
				}
			}
			
			model.itemsModule.hotelItemsGroupProvider.setItemAt(group, evt.groupIndex);
			model.itemsModule.hotelItemsGroupProvider.refresh();
			
			if (evt.callBack != null)
				evt.callBack();
			
			model.appEnabled--;
		}
		/**
		 *  The handler for faulting execution of request for
		 *  <code>addHotelSubGroups()</code>.
		 *  
		 *  @see services.business.backend.AddHotelSubGroupDelegate.addHotelSubGroups
		 */
		public function fault(info:Object):void
		{
			model.appEnabled--;
			
			Alert.show("Hotel sub group could not be added");
		}
	}
}