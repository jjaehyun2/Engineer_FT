package services.events.frontend
{
	import services.cairngorm.BaseEvent;
	
	
	public class LoginEvent extends BaseEvent
	{
		public var userLogin:String;
		public var userPassword:String;

		
		public function LoginEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	    /*public function UserLogin():String
		{
            return userLogin;
        }

       	public function UserPassword():String
        {
            return userPassword;
        }*/
		
	}
}