package services.vo.cashShift
{
	import com.adobe.cairngorm.vo.IValueObject;

	[RemoteClass(alias="MapCashier")]
	[Bindable]
	public class CashierVO implements IValueObject
	{
		  public var iCashierId:int;     			// Shift ID
		  public var iCashierNum:int;    			// The number nof the shift in a day (1,2,3)
		  public var sCashierStart:String;  		// Start time
		  public var sCashierEnd:String;    		// End time
		  public var iCashierStatusId:String;       // Shift state ID
		  public var sCashierStatusCode:String;     // Shift state code (output only)
		  public var sDate:String;
	}
}