package services.vo.frontend
{
    [RemoteClass(alias="MapReservationCalendarCell")]
    public class ReservationCalendarCellVO
    {
        public var iEmptyCount:int;
        public var iRoomCapacity:int;
        public var iSysRoomTypeId:int;
        public var iHotelRoomTypeId:Number;

        public var fPriceOne:Number;
        public var fPriceTwo:Number;
        public var fPriceThree:Number;
        public var fPriceExtra:Number;
        public var fPriceChildAbove:Number;
        public var fPriceChildMiddle:Number;
        public var fPriceChildBefore:Number;
 		public var iCompanyRateId:int;
		public var iPackageRateId:int;
		public var iRateId:int;
		public var iBarId:int;
		public var sEvent:String;

        public var iMinStay:int;
        public var iCanselationPolicy:int;
        public var sCanselationDescription:String;

        public var bIsGuarantee:Boolean;
        public var bIsClosedToArrival:Boolean;
        public var bPriceIsPerStay:Boolean;

        [Transient]
        public var date:Date;
    }
}