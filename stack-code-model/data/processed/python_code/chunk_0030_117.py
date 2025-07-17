package services.events.inHouse
{
	import services.cairngorm.BaseEvent;
	import services.vo.backend.PackageRequestVO;
	
	public class GetPackagesEvent extends BaseEvent
	{
		public var packageRequest:PackageRequestVO = new PackageRequestVO();
		public var departureDate:String;
		
		public function GetPackagesEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type,bubbles,cancelable);
		}

	}
}