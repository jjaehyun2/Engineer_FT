package masputih.patterns.commands 
{
	import flash.events.Event;
	import flash.events.EventDispatcher;
	
	/**
	 * Null command. It does nothing but dispatches CommandEvent.COMPLETE.
	 * @author Anggie Bratadinata
	 */
	public class NullCommand extends EventDispatcher implements ICommand
	{
		
		public static const NAME:String = "NullCommand";
		
		public function NullCommand() 
		{
			
		}
		
		/* INTERFACE com.masputih.patterns.command.ICommand */
		
		public function execute(params:Array = null, event:Event = null):void
		{
			dispatchEvent(new CommandEvent(CommandEvent.COMPLETE));
		}
		
		public function setReceiver(receiver:* = null):void
		{
			
		}
		
		public function setOnComplete(callback:Function = null):void
		{
			
		}
		
		public function setOnError(callback:Function = null):void
		{
			
		}
		
		public function setParams(params:Array):void
		{
			
		}
		
		public function getParams():Array
		{
			return null;
		}
		
		public function get name():String
		{
			return NullCommand.NAME;
		}
		
	}

}