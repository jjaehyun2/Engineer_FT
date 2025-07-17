package services.events.frontend
{
	import com.adobe.cairngorm.control.CairngormEvent;

	public class GetProfileAddressesEvent extends CairngormEvent
	{
		public var profileId:int;
		
		public function GetProfileAddressesEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}