package services.vo.reservation
{
	import com.adobe.cairngorm.vo.IValueObject;

	[RemoteClass(alias="MapCreditCard")]
	[Bindable]
	public class CreditCardVO implements IValueObject
	{
		public var iId:int;
    	public var sCardNumber:String;
    	public var sExpDate:String;
    	public var bIsIndividual:Boolean;
    	public var iType:int;
    	public var sOwnerName:String;
	}
}