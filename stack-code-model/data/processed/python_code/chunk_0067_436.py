package services.events.hotels
{
	import services.cairngorm.BaseEvent;
	import services.vo.backend.RoomSettingObjectVO;

	public class AddRoomSettingsToHotelEvent extends BaseEvent
	{
		public static var MOVE_SETTING:String = "moveSetting";
		
		public var item:RoomSettingObjectVO;
		
		public function AddRoomSettingsToHotelEvent(type:String)
		{
			super(type);
		}
		
	}
}