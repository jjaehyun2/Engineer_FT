package stimsulsoftreports
{	
	import org.apache.royale.events.Event;
	import mx.utils.ByteArray;

	public class SendEMailEvent extends Event
	{
        public static const SENDEMAILREPORT:String = "sendEMailReport";

        public var email:String;
        public var subject:String;
        public var message:String;
        public var fileName:String;
        public var fileData:ByteArray;
		
		public function SendEMailEvent()
		{
			super(SENDEMAILREPORT);
		}
	}
}