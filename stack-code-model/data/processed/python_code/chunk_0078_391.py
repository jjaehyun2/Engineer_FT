package services.vo.inHouse
{
	import services.vo.MapValueObject;
	
	[RemoteClass(alias="MapRateChange")]
	[Bindable]
	public class RateChangeVO extends MapValueObject
	{
		public static const RATE_TYPE_BAR:int = 1;
		public static const RATE_TYPE_COMPANY:int = 2;
		public static const RATE_TYPE_PACKAGE:int = 3;
		
		public var lRsvId:Number = 0;
		public var iRateType:int = RATE_TYPE_BAR;
		public var lRateId:Number = 0;
		public var lQuality:Number = 0;
	}
}