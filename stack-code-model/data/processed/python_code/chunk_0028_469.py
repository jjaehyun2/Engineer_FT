package services.cairngorm
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.adobe.cairngorm.control.CairngormEventDispatcher;
	
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	
	import flexUnit.CompleteEvent;
	
	import framework.model.AppModelLocator;
	import framework.module.CommonModule;
	
	import mx.managers.CursorManager;
	import mx.rpc.IResponder;
	
	import services.events.IBaseEvent;

	public class BaseCommand implements ICommand, IResponder
	{
		// ================================================================= //
		//                           VARIABLES                               //
		// ================================================================= //
		/**
		 *  This property contains the model with all data.
		 *
		 *  @see framework.model.AppModelLocator
		 */
		protected var model:AppModelLocator = AppModelLocator.getInstance();
		/**
		 *  This property is common module. This module is storage for all
		 *  common variables in the system.
		 *
		 *  @default model.commonModule
		 *
		 *  @see framework.module.CommonModule
		 */
		protected var _storage:CommonModule = model.commonModule;
		/**
		 *  This property contain event for remote function call.
		 *
		 *  @see services.events.IBaseEvent
		 */
		protected var _event:IBaseEvent;
		
		private var tmrUnlock:Timer = new Timer(500, 1);
		
		// ================================================================= //
		//                       INTERFACE METHODS                           //
		// ================================================================= //
		/**
		 *  Called by the Front Controller to execute the command.
		 *
		 *  The single entry point into an ICommand, the execute() method is
		 *  called by the Front Controller when a user-gesture indicates that
		 *  the user wishes to perform a task for which a particularconcrete
		 *  command class has been provided.
		 *
		 *  @param event:CairngormEvent — When the Front Controller receives
		 *         notification of a user gesture, the Event that it receives
		 *         contains both the type of the event (indicating which command
		 *         should handle the work) but also any data associated with the
		 *         event.
		 */
		public function execute(event:CairngormEvent):void
		{
			// TODO : override this method for your delegate
		}

		/**
		 *  This method is called by a service when the return value has been
		 *  received.
		 *
		 *  This method is called by a service when the return value has been
		 *  received. While data is typed as Object, it is often (but not always)
		 *  an mx.rpc.events.ResultEvent.
		 *
		 *  @param data:Object
		 */
		public function result(data:Object):void
		{
			if ((_event) && (_event.callBack is Function))
			{
				_event.callBack();
			}
			
			//tmrUnlock.addEventListener(TimerEvent.TIMER_COMPLETE, unlock);
			//tmrUnlock.start();
			model.owner.callLater(unlock);
			//model.owner.callLater(unlock);
			//	For tests
			var completeEvent:CompleteEvent = new CompleteEvent((_event as BaseEvent).type + "Complete");
			completeEvent.status = CompleteEvent.OK;
			completeEvent.dispatch();
			trace("--> Event: " + completeEvent.type + " - dispatched" );
			// TODO : override this method to get result
		}

		/**
		 *  This method is called by a service when an error has been received.
		 *
		 *  This method is called by a service when an error has been received.
		 *  While info is typed as Object it is often (but not always) an
		 *  mx.rpc.events.FaultEvent.
		 *
		 *  @param info:Object
		 */
		public function fault(info:Object):void
		{
			// TODO : override this method to get fault data
			// unlock system for use
			model.owner.callLater(unlock);
			// update handler for unit tests
			var completeEvent:CompleteEvent = new CompleteEvent((_event as BaseEvent).type + "Complete");
			completeEvent.status = CompleteEvent.FAULT;
			completeEvent.dispatch();
			trace("--> Event: " + completeEvent.type + " - dispatched" );
		}
		
		public function unlock(e:TimerEvent = null):void
		{
			tmrUnlock.removeEventListener(TimerEvent.TIMER_COMPLETE, unlock);
			tmrUnlock.stop();
			
			model.appEnabled--;
			CursorManager.removeBusyCursor();
		}
	}
}