package services.events.backend
{
	import services.cairngorm.BaseEvent;
	import services.vo.backend.ReportVO;

	public class GetReportEvent extends BaseEvent
	{
		public var report:ReportVO;				
		
		public function GetReportEvent(type:String)
		{
			super(type);
		}
		
	}
}