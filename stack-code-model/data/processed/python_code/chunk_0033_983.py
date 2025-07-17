package masputih.patterns.commands {
	import flash.events.Event;
	import org.casalib.collection.UniqueList;

	/**
	 * ...
	 * @author Anggie Bratadinata
	 */
	public class MacroCommand extends SimpleCommand implements ICommand {

		public static const NAME:String = "MacroCommand";

		protected var _subCommands:UniqueList = new UniqueList();

		public function MacroCommand(){

		}
		
		/**
		 * Add a subcommand
		 * @param	cmd
		 */
		public function addCommand(cmd:ICommand):void {
			_subCommands.addItem(cmd);
		}

		override public function execute(params:Array = null, event:Event = null):void {
			
			var subs:Array = _subCommands.toArray();
			for (var i:int = 0, len:int = subs.length; i < len; i++) {
				var cmd:ICommand = subs[i];
				cmd.execute(params, event);
			}
		}
		
		override public function get name():String { return MacroCommand.NAME; }
		
		

	}

}