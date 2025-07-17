package services.events.miscellaneous.countries
{
	import services.cairngorm.BaseEvent;
	import services.vo.common.RegionVO;

	public class DeleteRegionEvent extends BaseEvent
	{
		public var region:RegionVO = new RegionVO();
		
		public function DeleteRegionEvent(type:String)
		{
			super(type);
		}
	}
}