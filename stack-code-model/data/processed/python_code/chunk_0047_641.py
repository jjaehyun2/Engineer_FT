package services.vo.search
{
	import com.adobe.cairngorm.vo.IValueObject;

	[RemoteClass(alias="MapReservationView")]
	[Bindable]
	public class ReservationViewVO implements IValueObject
	{
		public var iRsvId:int;
      	public var iOrdId:int;
		public var sConfirmationCode:String;
		public var sStartDate:String;
		public var sEndDate:String;
		public var sCallerName:String;
		public var sGuestName:String;
		public var sCompanyName:String;
		public var sTravelAgencyName:String;
		public var sCity:String;
		public var sZip:String;
		public var sStreet:String;
		public var sPhoneNumber:String
		public var iCancelationId:int;
        public var sCancelationName:String;
      	public var sOrderStatus:String;
      	public var bCanCanceled:Boolean;
      	public var bIsGuarantee:Boolean;
	}
}