package services.vo.frontend
{
	[RemoteClass(alias="MapReservationOrder")]
	public class ReservationOrderVO
	{
		public var iId:int = 0;
	  	public var iHotelId:int = 0;
	  	public var iReservationId:int = 0;
	  	public var iDateFrom:Number = 0;
	  	public var iDateTo:Number = 0;
	  
	  	/**
	   	* @var int room type id (info about quality, bed type and capacity)
	   	*/
	  	public var iRtypeId:int = 0;
	  	
	  	/**
	   	* @var int this price will be compared with value calculated on server side -
	   	* if mismatched, then exception will be thrown 
	   	*/
	  	public var iPrice:int = 0;
	  
	  	/**
	   	* @var int order status
	   	* 1 - tentative
	   	* 2 - definite
	   	* 3 - canceled
	   	* 4 - closed
	   	*/
	  	public var iStatus:int = 0;
	  
	  	public var iCutoffDate:int = 0;
	  
	  	public var iAdultNumber:int = 0;
	  	public var iChildrenLess12Number:int = 0;
	  	public var iChildrenMore12Number:int = 0;
	  	
	  	public var iOrderRateId:int = 0;
  		public var iOrderRateType:int = 0;
  
  		public var iOrderDateCount:int = 0;
	  	
	  	public var iRoomCount:int = 0;
	  	public var sRoomTypeFullName:String = "";
	  	
	  	public var aRooms:Array = new Array();

	}
}