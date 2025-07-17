package services.events.roomTypes
{
	import services.cairngorm.BaseEvent;
	import services.vo.backend.BedTypeObjectVO;

	public class AddBedTypeEvent extends BaseEvent
	{
		public var bedType:BedTypeObjectVO = new BedTypeObjectVO();
		public var capacitList:Array = new Array();
		
		public function AddBedTypeEvent(type:String)
		{
			super(type);
		}
		
	}
}