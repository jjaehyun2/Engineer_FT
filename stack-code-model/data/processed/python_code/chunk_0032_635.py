dynamic class gfx.managers.FocusHandler
{
	static var _instance = gfx.managers.FocusHandler.instance;
	var inited: Boolean = false;
	var actualFocusLookup;
	var currentFocusLookup;
	var inputDelegate;

	function FocusHandler()
	{
		Selection.addListener(this);
		_global.gfxExtensions = 1;
		Selection.alwaysEnableArrowKeys = true;
		Selection.disableFocusKeys = true;
		Selection.disableFocusAutoRelease = true;
		Selection.disableFocusRolloverEvent = true;
		_root._focusrect = false;
		this.currentFocusLookup = [];
		this.actualFocusLookup = [];
	}

	static function get instance()
	{
		if (_instance == null) 
		{
			_instance = new FocusHandler();
		}
		return _instance;
	}

	function initialize()
	{
		this.inited = true;
		this.inputDelegate = gfx.managers.InputDelegate.instance;
		this.inputDelegate.addEventListener("input", this, "handleInput");
	}

	function getFocus(focusIdx)
	{
		return this.currentFocusLookup[focusIdx];
	}

	function setFocus(focus, focusIdx)
	{
		if (!this.inited) 
		{
			this.initialize();
		}
		while (focus.focusTarget != null) 
		{
			focus = focus.focusTarget;
		}
		var __reg8 = this.actualFocusLookup[focusIdx];
		var __reg5 = this.currentFocusLookup[focusIdx];
		if (__reg5 != focus) 
		{
			__reg5.focused = __reg5.focused & ~(1 << focusIdx);
			__reg5 = focus;
			this.currentFocusLookup[focusIdx] = focus;
			__reg5.focused = __reg5.focused | 1 << focusIdx;
		}
		if (__reg8 != __reg5 && !(__reg8 instanceof TextField)) 
		{
			var __reg6 = Selection.getControllerMaskByFocusGroup(focusIdx);
			var __reg2 = 0;
			for (;;) 
			{
				if (__reg2 >= System.capabilities.numControllers) 
				{
					return;
				}
				var __reg4 = (__reg6 >> __reg2 & 1) != 0;
				if (__reg4) 
				{
					Selection.setFocus(__reg5, __reg2);
				}
				++__reg2;
			}
		}
	}

	function handleInput(event)
	{
		var controllerIdx = event.details.controllerIdx;
		var focusIdx = Selection.getControllerFocusGroup(controllerIdx);
		var path = this.getPathToFocus(focusIdx);
		if (path.length == 0 || path[0].handleInput == null || path[0].handleInput(event.details, path.slice(1)) != true) 
		{
			if (event.details.value != "keyUp") 
			{
				var nav = event.details.navEquivalent;
				if (nav != null) 
				{
					var focusedElem = eval(Selection.getFocus(controllerIdx));
					var actualFocus = this.actualFocusLookup[focusIdx];
					if (actualFocus instanceof TextField && focusedElem == actualFocus && this.textFieldHandleInput(nav, controllerIdx)) 
					{
						return undefined;
					}
					var dirH = nav == gfx.ui.NavigationCode.LEFT || nav == gfx.ui.NavigationCode.RIGHT;
					var dirV = nav == gfx.ui.NavigationCode.UP || nav == gfx.ui.NavigationCode.DOWN;
					var focusContext = focusedElem._parent;
					var focusMode = "default";
					if (dirH || dirV) 
					{
						var focusProp = dirH ? "focusModeHorizontal" : "focusModeVertical";
						while (focusContext) 
						{
							focusMode = focusContext[focusProp];
							if (focusMode && focusMode != "default") 
							{
								break;
							}
							focusContext = focusContext._parent;
						}
					}
					else 
					{
						focusContext = null;
					}
					var newFocus = Selection.findFocus(nav, focusContext, focusMode == "loop", null, false, controllerIdx);
					if (newFocus) 
					{
						Selection.setFocus(newFocus, controllerIdx);
					}
				}
			}
		}
	}

	function getPathToFocus(focusIdx)
	{
		var __reg5 = this.currentFocusLookup[focusIdx];
		var __reg3 = __reg5;
		var __reg4 = [__reg3];
		while (__reg3) 
		{
			__reg3 = __reg3._parent;
			if (__reg3.handleInput != null) 
			{
				__reg4.unshift(__reg3);
			}
			if (__reg3 == _root) 
			{
				break;
			}
		}
		return __reg4;
	}

	function onSetFocus(oldFocus, newFocus, controllerIdx)
	{
		if (oldFocus instanceof TextField && newFocus == null) 
		{
			return undefined;
		}
		var __reg2 = Selection.getControllerFocusGroup(controllerIdx);
		var __reg6 = this.actualFocusLookup[__reg2];
		if (__reg6 == newFocus) 
		{
			var __reg4 = newFocus instanceof TextField ? newFocus._parent : newFocus;
			var __reg5 = __reg4.focused;
			if (__reg5 & 1 << __reg2 == 0) 
			{
				__reg4.focused = __reg5 | 1 << __reg2;
			}
		}
		this.actualFocusLookup[__reg2] = newFocus;
		this.setFocus(newFocus, __reg2);
	}

	function textFieldHandleInput(nav, controllerIdx)
	{
		var __reg3 = Selection.getCaretIndex(controllerIdx);
		var __reg4 = Selection.getControllerFocusGroup(controllerIdx);
		var __reg2 = this.actualFocusLookup[__reg4];
		if ((__reg0 = nav) === gfx.ui.NavigationCode.UP) 
		{
			if (!__reg2.multiline) 
			{
				return false;
			}
			return __reg3 > 0;
		}
		else if (__reg0 === gfx.ui.NavigationCode.LEFT) 
		{
			return __reg3 > 0;
		}
		else if (__reg0 === gfx.ui.NavigationCode.DOWN) 
		{
			if (!__reg2.multiline) 
			{
				return false;
			}
			return __reg3 < TextField(__reg2).length;
		}
		else if (__reg0 === gfx.ui.NavigationCode.RIGHT) 
		{
			return __reg3 < TextField(__reg2).length;
		}
		return false;
	}

}