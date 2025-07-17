package masputih.patterns.commands 
{
	import flash.events.Event;
	import nl.demonsters.debugger.MonsterDebugger;
	import org.casalib.collection.List;
	/**
	 * ...
	 * @author Anggie Bratadinata
	 */
	public class CommandSequence extends SimpleCommand
	{
		public static const NAME:String = "CommandSequence";
		
		protected var _subCommands:List = new List();
		protected var _currentCommand:SimpleCommand;
		protected var _currentCommandIndex:int = 0;
		
		public function CommandSequence() 
		{
			
		}
		
		override public function setReceiver(receiver:* = null):void 
		{
			super.setReceiver(receiver);
			if (!_subCommands.isEmpty() && _receiver != null) {
				for (var i:int = 0, len:int = _subCommands.size; i < len; i++) {
					SimpleCommand(_subCommands.getItemAt(i)).setReceiver(_receiver);
				}
			}
		}
		
		public function addCommand(cmd:SimpleCommand):void {
			_subCommands.addItem(cmd);
			if (_receiver != null) cmd.setReceiver(_receiver);
		}
		
		override public function execute(params:Array = null, event:Event = null):void {
			if (_subCommands.isEmpty()) return;
			
			//MonsterDebugger.trace(this, "executing command #" + (_currentCommandIndex+1) + " of " + _subCommands.size);
			_currentCommand = _subCommands.getItemAt(_currentCommandIndex);
			
			MonsterDebugger.trace(this, _currentCommand);
			_currentCommand.addEventListener(CommandEvent.COMPLETE, onSubCommandComplete);
			_currentCommand.addEventListener(CommandEvent.ERROR, onSubCommandError);
			_currentCommand.execute();
		}
		
		private function onSubCommandError(e:CommandEvent):void {
			_currentCommandIndex = 0;
			_currentCommand = null;
			dispatchEvent(new CommandEvent(CommandEvent.ERROR));
		}
		
		private function onSubCommandComplete(e:CommandEvent):void {
			//MonsterDebugger.trace(this, "subcommand complete " + e.target);
			if (_currentCommandIndex < _subCommands.size-1 ) {
				MonsterDebugger.trace(this, "executing next command " );
				_currentCommandIndex++;
				execute();
			}else {
				dispatchEvent(new CommandEvent(CommandEvent.COMPLETE));
			}
			
			
		}
		
		override protected function onComplete(e:CommandEvent):void 
		{
			_currentCommand = null;
			_currentCommandIndex = 0;
			super.onComplete(e);
		}
		/**********************************************
		 * GETTERS/SETTERS
		 **********************************************/
		
		override public function get name():String { return CommandSequence.NAME; }
		
		public function get subCommands():List { return _subCommands; }
		
		
	}

}