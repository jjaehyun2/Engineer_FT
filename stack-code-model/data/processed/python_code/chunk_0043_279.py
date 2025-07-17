package services.events.frontend
{
	import com.adobe.cairngorm.control.CairngormEvent;

	public class CheckLoginEvent extends CairngormEvent
	{
		public var login:String;
		
		public function CheckLoginEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}