package services.vo.backend
{
	import com.adobe.cairngorm.vo.IValueObject;

	[Bindable]
	[RemoteClass(alias="MapPackage")]
	public class PackageVO implements IValueObject
	{
		public var iPackageId:int = 0;
		public var iHotelId:int;
		public var iRoomQualityId:int;
		public var sPackageName:String;
		public var fPriceOneAdult:Number = 0;
		public var fPriceTwoAdults:Number = 0;
		public var fPriceExtraAdult:Number = 0;
		public var fPriceChildAbove:Number = 0;
		public var fPriceChildMiddle:Number = 0;
		public var fPriceChildBelow:Number = 0;

		public var bPriceIsRelative:Boolean;
		public var bPriceIsPerStay:Boolean;
		public var sDateStart:String; //  (Y-m-d)
		public var sDateEnd:String;
		public var iMinStay:int=0;
		public var iMaxStay:int=0;
		public var sDescription:String;
		[Transient]
	  	public var bIsSelected:Boolean = false;
	}
}