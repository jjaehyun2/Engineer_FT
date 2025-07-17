package controls.login.events {
	import flash.events.Event;

	public class LoginRequestedEvent extends Event {
		public function LoginRequestedEvent(type:String, username:String, password:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);

            this.username = username;
            this.password = password;
		}
		
        public static const TYPE_LOGIN_REQUESTED:String = "loginRequested";

        public var username:String;
        public var password:String;

        override public function clone():Event {
            return new LoginRequestedEvent(type, username, password);
        }
	}
}