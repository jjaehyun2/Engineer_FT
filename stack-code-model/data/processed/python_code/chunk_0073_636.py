package services.events.inHouse
{
	import services.cairngorm.BaseEvent;

	public class AttachConferenceRoomToAccountEvent extends BaseEvent
	{
		public var confRoomId:Number;
		public var hotelId:Number;
		public var profileId:Number;
		public var isCompany:Boolean;
		
		public function AttachConferenceRoomToAccountEvent(type:String)
		{
			super(type);
		}
	}
}