package services.vo.reservation
{
	import com.adobe.cairngorm.vo.IValueObject;

	[RemoteClass(alias="MapGuaratnee")]
	[Bindable]
	public class GuaratneeVO implements IValueObject
	{
		public var iId:int;
    	public var iCompanyId:int;
    	public var iAgencyId:int;
    	public var oCreditCard:CreditCardVO;
    	public var oDeposit:DepositVO;
    	public var iGuaranteeType:int;
    	public var bPayedByUser:Boolean;
		

	    public static const GUARANTEE_COMPANY:int = 1;
	    public static const GUARANTEE_TRAVEL_AGENCY:int = 2;
	    public static const GUARANTEE_CREDIT_CARD:int = 3;
	    public static const GUARANTEE_DEPOSIT:int = 4;
	}
}