package services.vo.profiles
{
	import com.adobe.cairngorm.vo.IValueObject;
	
	import services.vo.common.MarketCodesVO;
	import services.vo.common.SourceCodesVO;
	
	[RemoteClass(alias="MapCallerProfile")]
	[Bindable]
	public class ProfileCallerVO implements IValueObject
	{
		public var iId:int;
  		public var iReservationId:int;
  		public var iProfileId:int;
  		public var iSourceCodeId:int;
  		public var iMarketCodeId:int;
  		public var oProfile:ProfilePersonalVO = new ProfilePersonalVO();
  		public var oSourceCode:SourceCodesVO;
  		public var oMarketCode:MarketCodesVO;
  		public var iCompanyId:int;
  		public var sCompanyName:String;
  		public var iTravelAgencyId:int;
  		public var sTravelAgencyName:String;
  		[Transient]
  		public var bIsTravelAgency:Boolean; 
	}
}