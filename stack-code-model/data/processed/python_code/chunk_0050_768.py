package masputih.patterns.mvc.model 
{
	import flash.events.Event;
	
	/**
	 * ...
	 * @author Anggie Bratadinata
	 */
	public class ModelEvent extends Event 
	{
		
		public static const UPDATE:String = "modelUpdate";
		
		public function ModelEvent(type:String) 
		{ 
			super(type,true);
			
		} 
		
		public override function clone():Event 
		{ 
			return new ModelEvent(type);
		} 
		
		public override function toString():String 
		{ 
			return formatToString("ModelEvent", "type", "bubbles", "cancelable", "eventPhase"); 
		}
		
	}
	
}