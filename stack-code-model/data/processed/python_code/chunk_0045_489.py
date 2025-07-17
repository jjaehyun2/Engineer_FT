package devoron.components.buttons
{
	import flash.events.Event;
	import flash.events.IEventDispatcher;
	import org.aswing.event.AWEvent;
	import org.aswing.Icon;
	import org.aswing.JToggleButton;
	
	/**
	 * StateToggleButton
	 * @author Devoron
	 */
	public class StateToggleButton extends JToggleButton
	{
		private var relatedObject:IEventDispatcher;
		private var stateAFunction:Function;
		private var stateAEvent:String;
		private var stateBEvent:String;
		private var stateBFunction:Function;
		
		public function StateToggleButton(text:String = "", icon:Icon = null, isSelected:Boolean = false)
		{
			super(text, icon, isSelected);
			super.addActionListener(changeState);
		}
		
		public function setRelatedObject(object:IEventDispatcher, stateAEvent:String = null, stateAFunction:Function = null, stateBEvent:String = null, stateBFunction:Function = null):void
		{
			if (relatedObject)
			{
				if (stateAEvent != null && stateAFunction != null)
					relatedObject.removeEventListener(stateAEvent, stateAFunctionInternal);
				if (stateBEvent != null && stateBFunction != null)
					relatedObject.removeEventListener(stateBEvent, stateBFunctionInternal);
			}
			
			this.relatedObject = object;
			this.stateAEvent = stateAEvent;
			this.stateAFunction = stateAFunction;
			this.stateBFunction = stateBFunction;
			this.stateBEvent = stateBEvent;
			
			if (stateAEvent != null && stateAFunction != null)
				relatedObject.addEventListener(stateAEvent, stateAFunctionInternal);
			if (stateBEvent != null && stateBFunction != null)
				relatedObject.addEventListener(stateBEvent, stateBFunctionInternal);
		}
		
		private function changeState(e:AWEvent):void
		{
			if (!relatedObject)
				return;
			
			if (isSelected() && stateAFunction != null)
				stateAFunction.call(null);
			else if (!isSelected() && stateBFunction != null)
				stateBFunction.call(null);
		}
		
		protected function stateAFunctionInternal(e:Event):void
		{
			if (!isSelected())
				setSelected(true);
		}
		
		protected function stateBFunctionInternal(e:Event):void
		{
			if (isSelected())
				setSelected(false);
		}
	
	}

}