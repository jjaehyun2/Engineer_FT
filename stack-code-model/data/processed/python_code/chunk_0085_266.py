package services.vo.hotels
{
	[RemoteClass(alias="MapHotelRoom")]
	public class HotelRoomObjectVO
	{
		public var iRoomId:Number;
  		public var iRoomStageId:Number;
  		public var iRoomHotelId:Number;
  		public var iRoomRTypeId:Number;
  		public var iRoomCapacity:Number;
  		public var iRoomImgULX:Number = 0;
  		public var iRoomImgULY:Number = 0;
  		public var iRoomImgWidth:Number = 0;
  		public var iRoomImgHeight:Number = 0;
  		public var aRoomSetting:Array;
  		public var sRoomName:String;
  		public var sRoomImgName:String = '_temp_img';

	}
}