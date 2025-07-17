package flexmvcs.patterns.command {

	import flash.errors.IllegalOperationError;
	import flash.events.Event;
	import flash.utils.clearTimeout;
	import flash.utils.setTimeout;
	
	import flexmvcs.events.PayloadEvent;
	import flexmvcs.patterns.utils.Queue;
	
	import org.puremvc.interfaces.INotification;

	[Event(name="complete", type="import flexmvcs.events.PayloadEvent")]
	[Event(name="success", type="import flexmvcs.events.PayloadEvent")]
	[Event(name="failure", type="import flexmvcs.events.PayloadEvent")]
	public class CompositeCommand extends FlexCommand {

		// This value defaults to true
		public var stopOnFailure:Boolean;
		public var timeoutId:int;
		protected var startTime:Number;
		protected var queue:Queue;
		protected var command:FlexCommand;
		protected var notification:INotification;
		private var currentIndex:int;

		public function CompositeCommand() {
			queue = new Queue();
			stopOnFailure = true;
			initialize();
		}
		
		// Override this method and enqueue whatever
		// commands you want executed
		protected function initialize():void {
		}
		
		override public function execute(notification:INotification):void {
			super.execute(notification);
			this.notification = notification;
			result = new CompositeResult();
			dequeue();
		}
		
		// TODO: Add timeout if an item takes too long....
		protected function dequeue():Object {
			var item:CompositeItem;
			if(queue.peek()) {
				item = queue.dequeue() as CompositeItem;
				command = item.command;
				if(command.timeout != -1) {
					timeoutId = setTimeout(triggerTimeout, command.timeout, notification.getName(), command);
				}
				var failureHandler:Function = getCommandFailureHandler(item.failureHandler)
				command.addEventListener(PayloadEvent.FAILURE, failureHandler);
				command.addEventListener(PayloadEvent.SUCCESS, getCommandSuccessHandler(item.successHandler));
				command.addEventListener(PayloadEvent.COMPLETE, commandCompleteHandler);
				command.setFacade(getFacade());
				// If the enqueue call included a notificationClosure
				if(item.notificationClosure != null) {
					executeChildCommand(command, item.notificationClosure(notification), failureHandler);
				}
				else {
					// Otherwise use the main notification given to the composite
					executeChildCommand(command, notification, failureHandler);
				}
			}
			else {
				queueComplete();
			}
			return item;
		}
		
		// Had to pull this support for synchronous exceptions.
		// For now, it's far more helpful when they throw up the call stack....
		protected function executeChildCommand(command:FlexCommand, notification:INotification, failureHandler:Function):void {
//			try {
				command.execute(notification);
/*
			}
			catch(e:Error) {
				trace(">> CompositeCommand encountered an exception: " + e.toString());
				var event:PayloadEvent = new PayloadEvent(PayloadEvent.FAILURE);
				event.payload = e;
				failureHandler(event);
			}
*/
		}
		
		protected function triggerTimeout(name:String, command:FlexCommand=null):void {
			throw new IllegalOperationError("CompositeCommand (" + name + ") never completed, this is likely because a synchronous command never called 'dispatchSuccess' when it was complete");
		}
		
		/**
		 * Add a command to the queue
		 * @param command:FlexCommand 
		 * @param notificationClosure:Function Optional closure that will be called immediately
		 * before the command.execute is called. This closure will be sent the notification
		 * instance that the composite command was given, and should return an INotification
		 * that is configured for the particular command
		 */
		public function enqueue(command:FlexCommand, notificationClosure:Function=null, successHandler:Function=null, failureHandler:Function=null):void {
			queue.enqueue(new CompositeItem(command, notificationClosure, successHandler, failureHandler));
		}
		
		protected function queueComplete():void {
			if(result.failures.length > 0) {
				dispatchFailure(result);
			}
			else {
				dispatchSuccess(result);
			}
		}
		
		protected function commandCompleteHandler(event:Event):void {
			clearTimeout(timeoutId);
			dequeue();
		}

		private function getCommandFailureHandler(handler:Function=null):Function {
			return function(event:PayloadEvent):void {
				result.addFailure(event);
				if(stopOnFailure) {
					queue = new Queue();
					// This command will dispatch a complete event
					// immediately after this failureHandler is called
					// the queue has been reset, so the composite will complete
					// with a failure
				}
				if(handler != null) {
					handler(event);
				}
			}
		}
		
		private function getCommandSuccessHandler(handler:Function=null):Function {
			return function(event:PayloadEvent):void {
				result.addSuccess(event);
				if(handler != null) {
					handler(event);
				}
			}
		}
	}
}

import flexmvcs.patterns.command.FlexCommand;

class CompositeItem {
	public var command:FlexCommand;
	public var notificationClosure:Function;
	public var successHandler:Function;
	public var failureHandler:Function;
	
	public function CompositeItem(command:FlexCommand, notificationClosure:Function=null, successHandler:Function=null, failureHandler:Function=null):void {
		this.command = command;
		this.notificationClosure = notificationClosure;
		this.successHandler = successHandler;
		this.failureHandler = failureHandler;
	}
}