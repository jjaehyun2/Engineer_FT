package flexmvcs.patterns.command {

	import asunit.framework.TestCase;
	import org.puremvc.patterns.observer.Notification;
	import flexmvcs.patterns.command.MockConstants;
	import flash.events.Event;
	import flexmvcs.events.PayloadEvent;

	public class FlexCommandTest extends TestCase {
		private var command:MockCommand;

		public function FlexCommandTest(methodName:String=null) {
			super(methodName)
		}

		override protected function setUp():void {
			super.setUp();
			command = new MockCommand();
		}

		override protected function tearDown():void {
			super.tearDown();
			command = null;
		}

		public function testInstantiated():void {
			assertTrue("command is FlexCommand", command is FlexCommand);
		}
		
		public function testFailure():void {
			command.addEventListener(PayloadEvent.FAILURE, addAsync());
			command.execute(new Notification(MockConstants.CONFIGURE));
		}
		
		public function testAsyncFailureWithMessage():void {
			runFailure(command);
		}

		public function testFailureWithMessage():void {
			command.isAsync = true;
			runFailure(command);
		}
		
		private function runFailure(command:MockCommand):void {
			var msg:String = "Something Failed";
			command.failureMessage = msg;
			
			var handler:Function = function(event:PayloadEvent):void {
				assertEquals("Message should be what was sent in", msg, event.payload);
			}

			command.addEventListener(PayloadEvent.FAILURE, addAsync(handler));
			command.execute(new Notification(MockConstants.CONFIGURE));
		}
		
		public function testComplete():void {
			command.shouldSucceed = true;
			command.addEventListener(Event.COMPLETE, addAsync());
			command.execute(new Notification(MockConstants.CONFIGURE));
		}

		public function testAsyncComplete():void {
			command.isAsync = true;
			command.shouldSucceed = true;
			command.addEventListener(Event.COMPLETE, addAsync());
			command.execute(new Notification(MockConstants.CONFIGURE));
		}
	}
}

import flexmvcs.patterns.command.FlexCommand;
import org.puremvc.interfaces.INotification;
import flash.utils.setTimeout;

class MockCommand extends FlexCommand {
	public var isAsync:Boolean;
	public var shouldSucceed:Boolean;
	public var failureMessage:String;
	
	override public function execute(notification:INotification):void {
		super.execute(notification);
		if(shouldSucceed) {
			if(isAsync) {
				setTimeout(dispatchSuccess, 1);	
			}
			else {
				dispatchSuccess();
			}
		}
		else {
			if(isAsync) {
				setTimeout(dispatchFailure, 1, failureMessage);
			}
			else {
				dispatchFailure(failureMessage);
			}
		}
	}
}