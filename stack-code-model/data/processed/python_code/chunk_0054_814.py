package flexmvcs.patterns.command {

	import asunit.framework.TestCase;
	
	import flash.events.Event;
	
	import org.puremvc.patterns.observer.Notification;
	import flexmvcs.events.PayloadEvent;

	public class CompositeCommandTest extends TestCase {
		private static const SUCCEED:Boolean = true;
		
		private var composite:CompositeCommand;
		private var activate:MockCommand;
		private var open:MockCommand;
		private var connect:MockCommand;

		public function CompositeCommandTest(methodName:String=null) {
			super(methodName)
		}

		override protected function setUp():void {
			super.setUp();
			// Arbitrary named command instances
			activate = new MockCommand(Event.ACTIVATE);
			open = new MockCommand(Event.OPEN);
			connect = new MockCommand(Event.CONNECT);

			composite = new CompositeCommand();
			composite.enqueue(activate);
			composite.enqueue(open);
			composite.enqueue(connect);
		}

		override protected function tearDown():void {
			super.tearDown();
			composite = null;
		}
		
		private function executeCommand():void {
			composite.execute(new Notification(Event.RENDER));
		}

		public function testInstantiated():void {
			assertTrue("composite is CompositeCommand", composite is CompositeCommand);
		}
		
		private function assertResult(result:Object, successCount:int, failureCount:int, resultCount:int):void {
			assertEquals("Successes", successCount, result.successes.length);
			assertEquals("Failures", failureCount, result.failures.length);
			assertEquals("Total Results", resultCount, result.results.length);
		}
		
		public function testSimple():void {
			composite.stopOnFailure = false;
			composite.addEventListener(Event.COMPLETE, addAsync());
			executeCommand();
		}
		
		public function testFirstFailure():void {
			composite.stopOnFailure = false;
			activate.shouldSucceed = false;
			var handler:Function = function(event:PayloadEvent):void {
				assertResult(event.payload, 2, 1, 3);
			}
			composite.addEventListener(PayloadEvent.FAILURE, addAsync(handler));
			executeCommand();
		}
		
		public function testStopOnFailure():void {
			open.shouldSucceed = false;
			var handler:Function = function(event:PayloadEvent):void {
				assertResult(event.payload, 1, 1, 2);
			}
			composite.addEventListener(PayloadEvent.COMPLETE, addAsync(handler));
			executeCommand();
		}
		
		public function testConfiguredCommand():void {
			var command:MockComposite = new MockComposite();
			var handler:Function = function(event:PayloadEvent):void {
				var result:CompositeResult = event.payload as CompositeResult;
				assertEquals(2, result.results.length);
			}
			
			command.addEventListener(PayloadEvent.COMPLETE, addAsync(handler));
			command.execute(new Notification(Event.CHANGE));
		}
		
		public function testDeepComposite():void {
			var root:MockDeepComposite = new MockDeepComposite();
			var handler:Function = function(event:PayloadEvent):void {
				var result:CompositeResult = event.payload as CompositeResult;
				assertEquals(3, result.results.length);
			}
			
			root.addEventListener(PayloadEvent.COMPLETE, addAsync(handler));
			root.execute(new Notification(Event.CHANGE));
		}
	}
}

class MockDeepComposite extends CompositeCommand {
	
	override protected function initialize():void {
		super.initialize();
		enqueue(new MockComposite());
		enqueue(new MockComposite());
		enqueue(new MockComposite());
	}
}

import flexmvcs.patterns.command.CompositeCommand;
import flash.events.Event;

class MockComposite extends CompositeCommand {
	
	override protected function initialize():void {
		super.initialize();
		enqueue(new MockCommand(Event.ACTIVATE), notificationClosure);
		enqueue(new MockCommand(Event.ADDED));
	}
	
	public function notificationClosure(notification:INotification):INotification {
		return notification;
	}
}
	
import flexmvcs.patterns.command.FlexCommand;
import flash.utils.setTimeout;
import org.puremvc.interfaces.INotification;

class MockCommand extends FlexCommand {
	public var shouldSucceed:Boolean;
	private var _name:String;
	
	public function MockCommand(name:String, succeed:Boolean=true) {
		_name = name;
		shouldSucceed = succeed;
	}
	
	override public function execute(notification:INotification):void {
		if(shouldSucceed) {
			setTimeout(dispatchSuccess, 1, _name);
		}
		else {
			setTimeout(dispatchFailure, 1, _name);
		}
	}
}