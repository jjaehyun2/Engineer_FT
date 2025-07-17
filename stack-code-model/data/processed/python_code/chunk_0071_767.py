package services.events.frontend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.vo.frontend.UserProfileVO;

	public class ConfirmFirstLoginEvent extends CairngormEvent
	{
		public function ConfirmFirstLoginEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}