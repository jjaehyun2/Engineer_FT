package services.vo.reports
{
	import com.adobe.cairngorm.vo.IValueObject;
	
	[RemoteClass(alias="MapPaymentOfDay")]
	public class PaymentOfTheDayVO implements IValueObject
	{
	  public var aCashier:Array = [];
	  public var aTransactionCode:Array = [];
	}
}