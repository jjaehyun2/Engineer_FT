package services.events.roomSettings
{
	import services.cairngorm.BaseEvent;
	import services.vo.backend.RoomSettingObjectVO;
	
	import mx.collections.ArrayCollection;

	public class DeleteRoomSettingEvent extends BaseEvent
	{
		public var index:int;
		public var roomSetting:RoomSettingObjectVO = new RoomSettingObjectVO();
		public var targetArray:ArrayCollection = new ArrayCollection();
		
		public function DeleteRoomSettingEvent(type:String)
		{
			super(type);
		}
		
	}
}