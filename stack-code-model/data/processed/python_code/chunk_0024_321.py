package flexUnit.model.data
{
	import services.vo.hotels.HotelInfoTotalVO;
	
	public class TestHotelData
	{
		public var hotelInfoTotal:HotelInfoTotalVO = new HotelInfoTotalVO();
		
		public var hotelInfoNewTotal:HotelInfoTotalVO = new HotelInfoTotalVO();

		public function TestHotelData()
		{
			//	hotelInfoTotal
			hotelInfoTotal.iHotelRoomCount = 50 + int(Math.random()*100);
			hotelInfoTotal.sHotelGMName = 'Jaga tester' + String(int(Math.random()*100));
			hotelInfoTotal.sHotelCode = '1419' + String(int(Math.random()*1000));
			hotelInfoTotal.iHotelCityId = 1415;//select
			hotelInfoTotal.sHotelName = 'FlexUnitTest'  + String(int(Math.random()*10000)) ;
			hotelInfoTotal.iChildAge1 = 1;
			hotelInfoTotal.iChildAge2 = 1;
			hotelInfoTotal.sHotelWeb = 'ramada.com' + String(int(Math.random()*100));
			hotelInfoTotal.iChildAge3 = 1;
			hotelInfoTotal.sHotelPhone = '0692578249' + String(int(Math.random()*100));
			hotelInfoTotal.iHotelHChainId = 1; // id group of hotel
			hotelInfoTotal.sHotelEMail = 'jamal@mail.ru' + String(int(Math.random()*100));
			hotelInfoTotal.sHotelDescription = 'Test add and edit Hotel' + String(int(Math.random()*100));
			hotelInfoTotal.sHotelCountry = 'Germany'; // select
			hotelInfoTotal.sHotelHChainName = 'RAMADA Hotels'; // select
			hotelInfoTotal.sHotelRegion = 'Thueringen'; //select
			hotelInfoTotal.iHotelRegionId = 310; 
			hotelInfoTotal.sHotelZip = '89989' + String(int(Math.random()*100));
			hotelInfoTotal.sHotelFax = '574970' + String(int(Math.random()*100));
			hotelInfoTotal.sHotelStreet = 'Hrustaleva' + String(int(Math.random()*100)); // input from keyboard	
			
			//	hotelInfoTotal for edit
			hotelInfoNewTotal.iHotelRoomCount = 50 + int(Math.random()*100);
			hotelInfoNewTotal.sHotelGMName = 'Jaga tester' + String(int(Math.random()*100));
			hotelInfoNewTotal.sHotelCode = '1419' + String(int(Math.random()*100));
			hotelInfoNewTotal.iHotelCityId = 1415;//select
			hotelInfoNewTotal.sHotelName = 'FlexUnitTest'/*  + String(int(Math.random()*100)) */;
			hotelInfoNewTotal.iChildAge1 = 1;
			hotelInfoNewTotal.iChildAge2 = 1;
			hotelInfoNewTotal.sHotelWeb = 'ramada.com' + String(int(Math.random()*100));
			hotelInfoNewTotal.iChildAge3 = 1;
			hotelInfoTotal.iHotelRegionId = 310; 
			hotelInfoNewTotal.sHotelPhone = '0692578249' + String(int(Math.random()*100));
			hotelInfoNewTotal.iHotelHChainId = 1; // id group of hotel
			hotelInfoNewTotal.sHotelEMail = 'jamal@mail.ru' + String(int(Math.random()*100));
			hotelInfoNewTotal.sHotelDescription = 'Test add and edit Hotel' + String(int(Math.random()*100));
			hotelInfoNewTotal.sHotelCountry = 'Germany'; // select
			hotelInfoNewTotal.sHotelHChainName = 'RAMADA Hotels'; // select
			hotelInfoNewTotal.sHotelRegion = 'Thueringen'; //select
			hotelInfoNewTotal.sHotelZip = '89989' + String(int(Math.random()*100));
			hotelInfoNewTotal.sHotelFax = '574970' + String(int(Math.random()*100));
			hotelInfoNewTotal.sHotelStreet = 'Hrustaleva' + String(int(Math.random()*100)); // input from keyboard		
		}	
	}
}