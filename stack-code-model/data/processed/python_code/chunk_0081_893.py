package masputih.patterns.mvc.controller {
	import masputih.patterns.commands.ICommand;
	import flash.events.Event;
	import flash.events.IEventDispatcher;
	import nl.demonsters.debugger.MonsterDebugger;
	import org.casalib.collection.UniqueList;
	

	/**
	 * ...
	 * @author Anggie Bratadinata
	 */
	public class Controller {

		private var _registeredCommands:UniqueList = new UniqueList([]);

		public function Controller(){

		}

		/**
		 * Register a command to handle event dispatched by the dispatcher
		 * @param dispatcher
		 * @param eventType
		 * @param commandObj	
		 * @param params		execution parameters
		 * @param onComplete	callback function 
		 * @param onError		callback function
		 */
		public function addCommand(dispatcher:IEventDispatcher, eventType:String, commandObj:ICommand, receiver:* = null, params:Array = null, onComplete:Function = null, onError:Function = null):void {
			var cmd:ICommand = commandObj;
			cmd.setOnComplete(onComplete);
			cmd.setOnError(onError);
			cmd.setReceiver(receiver);
			cmd.setParams(params);

			var cmdSet:Object = {d: dispatcher, e: eventType, c: cmd};

			//try to add the command set to the list
			//if the same set is already there
			if (!_registeredCommands.addItem(cmdSet)){
				//replace it with the new one
				_registeredCommands.setItem(cmdSet, _registeredCommands.indexOf(cmdSet));
			}

			dispatcher.addEventListener(eventType, handleEvent);
			MonsterDebugger.inspect(_registeredCommands.toArray());
		}

		/**
		 * Find a command by its name or instance and remove it
		 * @param cmd			command instance or name
		 * @param dispatcher
		 * @param eventType
		 */
		public function removeCommand(cmd:*, dispatcher:IEventDispatcher, eventType:String, callback:Function = null):void {

			var cmdSet:Object;

			if (cmd is ICommand){
				cmdSet = findCommandSet(ICommand(cmd), dispatcher, eventType);
			} else {
				cmdSet = findCommandSetByCommandName(cmd, dispatcher, eventType);
			}
			
			if (_registeredCommands.removeItem(cmdSet)) {
				if (callback != null) callback.call();
			}
			
			
		}
		
		/**
		 * Find a set of command-dispatcher-eventType by the command name
		 * @param name
		 * @param dispatcher
		 * @param eventType
		 * @return object 
		 */
		private function findCommandSetByCommandName(name:String, dispatcher:IEventDispatcher, eventType:String):Object {
			
			var cmds:Array = _registeredCommands.toArray();
			
			for (var i:int = 0, len:int = cmds.length; i < len; i++ ) {
				var cmdSet:Object = cmds[i];
				
				if (cmdSet.c.name == name && cmdSet.d === dispatcher && cmdSet.e == eventType){
					return cmdSet;
				}
			}

			return null;
		}
		
		/**
		 * Find a set of command-dispatcher-eventType by the command instance
		 * @param cmd
		 * @param dispatcher
		 * @param eventType
		 * @return Object		{ c:command instance, d:eventdispatcher, e:eventType }
		 * 
		 */
		private function findCommandSet(cmd:ICommand, dispatcher:IEventDispatcher, eventType:String):Object {
			for each (var cmdSet:Object in _registeredCommands.toArray()){
				if (cmdSet.c === cmd && cmdSet.d === dispatcher && cmdSet.e == eventType){
					return cmdSet;
				}
			}
			return null;
		}
		
		/**
		 * Handle event and delegate it to a specific command
		 * @param e
		 */
		private function handleEvent(e:Event):void {

			var cmdSets:Array = _registeredCommands.toArray();
			for (var i:int = 0, len:int = cmdSets.length; i < len; i++){
				var o:Object = cmdSets[i];
				if (o.e == e.type && o.d == e.target){
					MonsterDebugger.trace(this, "executing : " + o.c);
					o.c.execute(null ,e);
				}
			}
		}

	}

}