package services.vo.hotels
{	
	[RemoteClass(alias="MapHotelStage")]
	[Bindable]
	public class HotelStageObjectVO
	{
		public var iStageId:Number;
  		public var iStageHotelId:Number;
  		public var iStageRoomCount:Number;
  		public var iStageLevel:Number;
  		public var sStageName:String;
  		public var sStageFloorPlanName:String;
  		public var aMapHotelRooms:Array = new Array(); // list of HotelRoomObjectVO
	}
}