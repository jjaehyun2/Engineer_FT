package services.vo.search
{
	import com.adobe.cairngorm.vo.IValueObject;

	[RemoteClass(alias="MapCnlReason")]
	[Bindable]
	public class CancelationReason implements IValueObject
	{
		public var iId:int;
      	public var sName:String;
	}
}