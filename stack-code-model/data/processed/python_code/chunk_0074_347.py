package flexUnit.model.data
{	
	import framework.model.AppModelLocator;
	
	import services.vo.backend.PackageRequestVO;
	
	public class TestReservationData
	{					
		[Bindable]
		private var model:AppModelLocator = AppModelLocator.getInstance();	
		
		public var packageRequest:PackageRequestVO = new PackageRequestVO();
		
		public function TestReservationData()
		{			
			packageRequest.iHotelId = model.hotelsModule.hotelTotalInfo.iHotelId;
			packageRequest.iRoomQualityId = 25;
			packageRequest.sDateStart = "01/01/2010";
			packageRequest.sDateEnd = "02/01/2010";
			
		}

	}
}