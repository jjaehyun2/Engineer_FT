package services.command.inHouse
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.inHouse.InHouseDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.inHouse.GetConferenceRoomStatusEvent;
	import services.vo.inHouse.ConferenceRoomStateVO;

	public class GetConferenceRoomStatusCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetConferenceRoomStatusEvent(event);
			var delegate:InHouseDelegate = new InHouseDelegate(this);
			delegate.getConferenceRoomStatus(_event as GetConferenceRoomStatusEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var state:ConferenceRoomStateVO = data as ConferenceRoomStateVO;
			model.inHouseModule.conferenceRoomState = state;
			model.checkOutModule.updateCheckOutState(state.oMapItemsRouting);
			
			super.result(data);
		}
	}
}