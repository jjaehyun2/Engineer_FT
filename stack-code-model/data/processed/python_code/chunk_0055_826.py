package asunit.printers {
	import asunit.framework.IResult;
	import asunit.framework.IRunListener;
	import asunit.framework.ITestFailure;
	import asunit.framework.ITestSuccess;
	import asunit.framework.ITestWarning;
	import asunit.framework.Method;

	import flash.events.DataEvent;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IOErrorEvent;
	import flash.events.SecurityErrorEvent;
	import flash.events.TimerEvent;
	import flash.net.XMLSocket;
	import flash.system.fscommand;
	import flash.utils.Timer;
	import flash.utils.getQualifiedClassName;
	import flash.utils.getTimer;
	
	public class FlexUnitCIPrinter extends EventDispatcher implements IRunListener
	{
		protected static const DEFAULT_SERVER:String = "127.0.0.1";
		protected static const DEFAULT_PORT:uint = 1024;

		public var port:uint;
		public var server:String; //this is local host. same machine

		private static const SUCCESS:String = "success";
		private static const ERROR:String = "error";
		private static const FAILURE:String = "failure";
		private static const IGNORE:String = "ignore";
		
		private static const START_OF_TEST_RUN_ACK : String = "<startOfTestRunAck/>";
		private static const END_OF_TEST_ACK : String ="<endOfTestRunAck/>";
		private static const END_OF_TEST_RUN : String = "<endOfTestRun/>";
		
		private var socket:XMLSocket;		
		private var connectTimeout:Timer;
		
		protected var messageQueue:Array;
		
		private var startTime : int;
		
		public function FlexUnitCIPrinter() 
		{
			this.port = port;
			this.server = server;
			messageQueue = [];
			
			socket = new XMLSocket();
			socket.addEventListener(Event.CONNECT, onConnect);
			socket.addEventListener(DataEvent.DATA, onData);
			socket.addEventListener(IOErrorEvent.IO_ERROR, onErrorEvent);
			socket.addEventListener(SecurityErrorEvent.SECURITY_ERROR, onErrorEvent);
   	   		socket.addEventListener(Event.CLOSE, onErrorEvent);
			
			connectTimeout = new Timer(5000, 1);
			connectTimeout.addEventListener(TimerEvent.TIMER_COMPLETE, onConnectTimeout);
			connectTimeout.start();

			connect();
		}
	
		protected function connect(ip:String = DEFAULT_SERVER, port:uint = DEFAULT_PORT):void {
   	   		try {
   	   			socket.connect(ip, port);
   	   		}
			catch (e:Error) {
   	   			trace('## Error connecting to socket: ' + e.message);
   	   		}
		}	
		
		private function onConnectTimeout(event:TimerEvent):void {
			throw new Error('Timed out waiting to connect to socket.');
		}
		
		public function onTestIgnored(method:Method):void {
			var xmlMessageIgnore:String = "<testcase classname='" + getQualifiedClassName(method.scope)
				+ "' name='" + method.name + "' status='"+IGNORE+"'>"
				+ "<skipped />"
				+ "</testcase>";
			sendMessage(xmlMessageIgnore);
		}
		
		protected static function xmlEscapeMessage(message:String):String {
			if (!message) return '';
			
			var escape:XML = <escape/>;
			escape.setChildren( message );
			return escape.children()[0].toXMLString();
		}			
		
		public function onTestFailure(failure:ITestFailure):void {
			sendMessage(getFailureMessage(failure));
		}

		protected function getFailureMessage(failure:ITestFailure):String {
			var status:String = failure.isFailure ? FAILURE : ERROR;
//			var stackTrace:String = xmlEscapeMessage(failure.thrownException.getStackTrace());
			var stackTrace:String = failure.thrownException.getStackTrace();
			var xml:String =
				"<testcase classname='" + getQualifiedClassName(failure.failedTest)
				+ "' name='" + failure.failedMethod
				+ "' time='0.000' status='" + status + "'>"
				
					+ "<error message='" + xmlEscapeMessage(failure.exceptionMessage) 
					+ "' type='"+ getQualifiedClassName(failure.thrownException) +"' >"
						+ "<![CDATA[" + stackTrace + "]]>"
					+ "</error>"				
						
				+ "</testcase>";

			return xml;
		}		
				
		protected function sendMessage(message:String):void {
			if (!socket.connected) {
				messageQueue.push(message);
				return;
			}
			socket.send(message);
		}
	
		protected function onConnect(event:Event):void {
			connectTimeout.stop();
			sendQueuedMessages();
		}
		
		protected function sendQueuedMessages():void {
			while (messageQueue.length) {
				sendMessage(messageQueue.shift());
			}
		}		

		private function onData( event : DataEvent ) : void
		{
			if (event.data == END_OF_TEST_ACK) {
				exit();
			}
		}

		protected function onErrorEvent(event:Event):void {
			trace('FlexUnitCIPrinter::onErrorEvent() - event: ' + event);
			//throw new Error('FlashBuilderPrinter::onErrorEvent() - event: ' + event);
		}
		
		public function onRunStarted():void {
		}
		
        public function onTestStarted(test:Object):void {
            startTime = getTimer();
        }
        
        public function onTestCompleted(test:Object):void {
//            testTimes.push({test:test, duration:duration});
        }
        
		public function onTestSuccess(success:ITestSuccess):void 
		{
			//TODO: move test time into ITestSuccess
            var duration:Number = (getTimer() - startTime) / 1000;
			var xmlMessageSuccess:String = "<testcase classname='" + getQualifiedClassName(success.test) 
				+ "' name='" + success.method + "' time='0.000' status='"+SUCCESS+"'/>";
			sendMessage(xmlMessageSuccess);			
		}
				
		public function onRunCompleted(result:IResult):void {
			sendMessage(END_OF_TEST_RUN);
		}		
		
		protected function exit():void
		{
			socket.close();
			fscommand("quit");
		}

		public function onWarning(warning:ITestWarning) : void {
		}
	}
}