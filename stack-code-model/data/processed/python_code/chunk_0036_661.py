package services.vo.reservation
{
	import com.adobe.cairngorm.vo.IValueObject;
	
	[RemoteClass(alias="MapReservationRoomBlocked")]
	[Bindable]
	public class ReservationRoomBlockedVO implements IValueObject
	{
		public var iReservationId:int;
		public var iRoomType:int;
		public var iRoomQuantity:int;
		
		public var sDate:String;
		
		public var iPriceBarId:int;
		public var iBarId:int;
		public var iCompanyPriceId:int;
		public var iPackagePriceId:int;
		
		public var iMarketCodeId:int;  
		
		//------------------------
		[Transient]
		public var sRoomTypeName:String;		
		[Transient]
		public var iRoomQuantityAvail:int;
		[Transient]
		public var iRoomQuantityPicked:int;
	}
}