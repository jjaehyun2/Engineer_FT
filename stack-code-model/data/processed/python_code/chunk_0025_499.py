package framework.managers
{
	import flash.display.DisplayObject;
	
	import mx.core.IFlexDisplayObject;
	import mx.managers.PopUpManager;
	import mx.managers.PopUpManagerChildList;

	public class PopUpManagerExt
	{
		/**
		 *  This property is list with popups.
		 *  
		 *  @default []
		 */
		private static var _popups:Array = [];
		
		public function PopUpManagerExt()
		{
			super();
		}
		/**
		 *  Creates a top-level window and places it above other windows
		 *  in the z-order. It is good practice to call the removePopUp()
		 *  method to remove popups created by using the createPopUp() method.
		 *  If the class implements IFocusManagerContainer, the window will
		 *  have its own FocusManager so that, if the user uses the TAB key
		 *  to navigate between controls, only the controls in the window will
		 *  be accessed.
		 *  
		 *  @example
		 *      pop = mx.managers.PopUpManager.createPopUp(pnl, TitleWindow, false);
		 *  
		 *  Creates a popup window based on the TitleWindow class, using pnl as the
		 *  MovieClip for determining where to place the popup. It is defined to be
		 *  a non-modal window meaning that other windows can receive mouse events
		 *  
		 *  @param parent:DisplayObject — DisplayObject to be used for determining
		 *         which SystemManager's layers to use and optionally the reference
		 *         point for centering the new top level window. It may not be the
		 *         actual parent of the popup as all popups are parented by the
		 *         SystemManager.
		 *  @param className:Class — Class of object that is to be created for the
		 *         popup. The class must implement IFlexDisplayObject.
		 *  @param modal:Boolean (default = false) — If true, the window is modal
		 *         which means that the user will not be able to interact with other
		 *         popups until the window is removed.
		 *  @param childList:String (default = null) — The child list in which to add
		 *         the popup. One of PopUpManagerChildList.APPLICATION,
		 *         PopUpManagerChildList.POPUP, or PopUpManagerChildList.PARENT (default).
		 *  
		 *  @result IFlexDisplayObject — Reference to new top-level window.
		 *  
		 *  @see mx.managers.PopUpManagerChildList
		 */
		public static function createPopUp(parent:DisplayObject, className:Class, modal:Boolean = true):IFlexDisplayObject
		{
			var pop:IFlexDisplayObject = PopUpManager.createPopUp(parent, className, modal, PopUpManagerChildList.POPUP);
			_popups.push(pop);
			return pop;
		}
		/**
		 *  Centers a popup window over whatever window was used in the
		 *  call to the createPopUp() or addPopUp() method.
		 *  
		 *  Note that the position of the popup window may not change
		 *  immediately after this call since Flex may wait to measure
		 *  and layout the popup window before centering it.
		 *  
		 *  @param popUp:IFlexDisplayObject — IFlexDisplayObject representing
		 *  the popup.  
		 */
		public static function centerPopUp(popUp:IFlexDisplayObject):void
		{
			PopUpManager.centerPopUp(popUp);
		}
		
		public static function removePopUp(popup:IFlexDisplayObject):void
		{
			for(var i:int = 0; i < _popups.length; i++)
			{
				var pop:IFlexDisplayObject = _popups[i];
				if (pop.name == popup.name)
				{
					_popups.splice(i, 1);
					break;
				}
			}
			PopUpManager.removePopUp(popup);
			popup = null;
		}
		
		public static function removeAll():void
		{
			for each(var pop:IFlexDisplayObject in _popups)
			{
				PopUpManager.removePopUp(pop);
			}
			_popups = [];
		}
		
	}
}