package masputih.patterns.commands {
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import nl.demonsters.debugger.MonsterDebugger;

	/**
	 * The base class for all commands. This class must not be used on its own and needs to be extended.
	 * @author Anggie Bratadinata
	 */
	public class SimpleCommand extends EventDispatcher implements ICommand {

		public static const NAME:String = "SimpleCommand";
		
		public static const START:String = "commandStart";
		public static const COMPLETE:String = "commandComplete";
		public static const ERROR:String = "commandError";
		
		protected var _receiver:*;
		protected var _onCompleteCallback:Function;
		protected var _onErrorCallback:Function;
		protected var _state:String;
		protected var _params:Array;

		public function SimpleCommand(){
			this.addEventListener(CommandEvent.COMPLETE, onComplete);
			this.addEventListener(CommandEvent.ERROR, onError);
		}

		
		/**********************************************
		 * INTERFACE IMPLEMENTATIONS
		 **********************************************/
		
		/* INTERFACE masputih.patterns.commands.ICommand */
		
		public function get name():String{
			return SimpleCommand.NAME;
		}
		
		/**
		 * Execute command, set the command state and apply last minute parameters. 
		 * @param	params	Dynamic parameter array. If not null, this overwrites the command's _params property that's set via setParams() before the execution. 
		 * 					If the command is registered to a controller, the controller will always send a null argument to retain the command's static parameters if any.
		 * @param	event	Event that triggers this command or a delegated event.
		 * @see		setParams()
		 */
		public function execute(params:Array = null, event:Event = null):void {
			MonsterDebugger.trace(this, 'execute ');
			setState(START);
			if (params != null) setParams(params);
			
		}
		
		public function setReceiver(receiver:* = null):void {
			_receiver = receiver;
		}
		
		public function setOnComplete(callback:Function = null):void {
			_onCompleteCallback = callback;
		}

		public function setOnError(callback:Function = null):void {
			_onErrorCallback = callback;

		}
		
		/**
		 * Set the command parameters.
		 * 
		 * @param	params
		 * @see		execute()
		 */
		public function setParams(params:Array):void {
			_params = params;
		}
		
		public function getParams():Array {
			return _params;
		}

		/**********************************************
		 * INTERNAL EVENT HANDLERS
		 **********************************************/
		protected function onError(e:CommandEvent):void {
			setState(ERROR);
		}

		protected function onComplete(e:CommandEvent):void {
			setState(COMPLETE);
		}
		
		/**********************************************
		 * GETTERS/SETTERS
		 **********************************************/
		
		public function getState():String { return _state; }
		
		/**
		 * Set command state and call designated callback
		 * @param	value
		 */
		protected function setState(value:String):void {
			_state = value;
			
			if (_state == COMPLETE) {
				if (_onCompleteCallback != null) _onCompleteCallback.call();
				return;
			}
			
			if (_state == ERROR ) {
				if (_onErrorCallback != null) _onErrorCallback.call();
			}
		}
		
	}

}