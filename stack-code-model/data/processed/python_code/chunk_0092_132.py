package flash.display
{
	import flash.events.Event;
	import flash.geom.Rectangle;
	
	public class InteractiveObject extends DisplayObject
	{
		private var _mouseEnabled:Boolean = true;
		private var _doubleClickEnabled:Boolean = false;
		public function InteractiveObject()
		{
			super();
		}
		
		public function get tabEnabled():Boolean  { return true }
		
		public function set tabEnabled(param1:Boolean):void  {/**/ }
		
		public function get tabIndex():int  { return 0 }
		
		public function set tabIndex(param1:int):void  {/**/ }
		
		public function get focusRect():Object  { return null }
		
		public function set focusRect(param1:Object):void  {/**/ }
		
		public function get mouseEnabled():Boolean  { return _mouseEnabled }
		
		public function set mouseEnabled(v:Boolean):void  { _mouseEnabled = v; }
		
		public function get doubleClickEnabled():Boolean  { return _doubleClickEnabled }
		
		public function set doubleClickEnabled(v:Boolean):void  { _doubleClickEnabled = v; }
		
		// public function get accessibilityImplementation() : AccessibilityImplementation;
		
		//public function set accessibilityImplementation(param1:AccessibilityImplementation) : void;
		
		public function get softKeyboardInputAreaOfInterest():Rectangle  { return null }
		
		public function set softKeyboardInputAreaOfInterest(param1:Rectangle):void  {/**/ }
		
		public function get needsSoftKeyboard():Boolean  { return false }
		
		public function set needsSoftKeyboard(param1:Boolean):void  {/**/ }
		
		public function requestSoftKeyboard():Boolean  { return false }
	
		//public function get contextMenu() : ContextMenu;
	
		//public function set contextMenu(param1:ContextMenu) : void;
	}
}