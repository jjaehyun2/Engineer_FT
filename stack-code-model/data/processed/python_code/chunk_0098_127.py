package ro.ciacob.desktop.windows.prompts {
	import flash.events.Event;
	import flash.geom.Rectangle;
	
	import ro.ciacob.desktop.signals.IObserver;
	import ro.ciacob.desktop.signals.Observer;
	import ro.ciacob.desktop.windows.IWindowsManager;
	import ro.ciacob.desktop.windows.WindowActivity;
	import ro.ciacob.desktop.windows.WindowStyle;
	import ro.ciacob.desktop.windows.prompts.constants.PromptDefaults;
	import ro.ciacob.utils.Strings;
	import ro.ciacob.utils.Time;

	public class PromptsManager implements IPromptsManager {

		/* @constructor */
		public function PromptsManager() {}

		private static const CHROME_PADDING:Number = 30;

		private var _alertIcon:Class;
		private var _cancelLabel:String;
		private var _confirmationIcon:Class;
		private var _currentPromptDetail:String;
		private var _currentPromptObserver:IObserver;
		private var _errorIcon:Class;
		private var _informationIcon:Class;
		private var _isInitialized:Boolean;
		private var _noLabel:String;
		private var _okLabel:String;

		private var _uid:String;
		private var _windowsManager:IWindowsManager;
		private var _yesLabel:String;
		private var _uiCallback:Function;

		public function alert(content:String, title:String = null):IObserver {
			return prompt(content, title || PromptDefaults.ALERT_TITLE, _alertIcon, Vector.<String>([_okLabel]));
		}

		public function clear():void {
			_clearExisting();
		}

		public function confirmation(content:String, title:String = null):IObserver {
			return prompt(content, title || PromptDefaults.CONFIRMATION_TITLE, _confirmationIcon, Vector.<String>([_yesLabel,
				_noLabel, _cancelLabel]));
		}
		
		public function yesNoConfirmation(content:String, title:String = null):IObserver {
			return prompt(content, title || PromptDefaults.CONFIRMATION_TITLE, _confirmationIcon, Vector.<String>([_yesLabel,
				_noLabel]));
		}

		public function error(content:String, title:String = null):IObserver {
			return prompt(content, title || PromptDefaults.ERROR_TITLE, _errorIcon, Vector.<String>([_okLabel]));
		}

		public function information(content:String, title:String = null):IObserver {
			return prompt(content, title || PromptDefaults.INFORMATION_TITLE, _informationIcon, Vector.<String>([_okLabel]));
		}

		public function init(
			windowsManager:IWindowsManager,
			alertIcon:Class = null,
			confirmationIcon:Class = null,
			errorIcon:Class = null,
			informationIcon:Class = null,
			yesLabel:String = null,
			noLabel:String = null,
			okLabel:String = null,
			cancelLabel:String = null,
			uiCallback:Function = null) : void {

			if (!_isInitialized) {
				if (windowsManager == null) {
					throw (new Error ('Prompt Library: no windows manager provided; aborting.'));
				}
				if (windowsManager.mainWindow == null) {
					throw (new Error ('Prompt Library: provided windows manager has no main window set; aborting.'));
				}
				_windowsManager = windowsManager;
				_alertIcon = alertIcon;
				_confirmationIcon = confirmationIcon;
				_errorIcon = errorIcon;
				_informationIcon = informationIcon;
				_yesLabel = yesLabel || PromptDefaults.YES_LABEL;
				_noLabel = noLabel || PromptDefaults.NO_LABEL;
				_okLabel = okLabel || PromptDefaults.OK_LABEL;
				_cancelLabel = cancelLabel || PromptDefaults.CANCEL_LABEL;
				_uiCallback = uiCallback;
				_isInitialized = true;
			}
		}

		public function prompt (content:String, title:String, image:Class = null, buttons:Vector.<String> = null, checkboxLabel:String =
			null, progressBarObserver:IObserver = null, centerToMainWindow : Boolean = true):IObserver {
			// MAKE THE CONTENT
			var component:PromptBaseUI = new PromptBaseUI;
			if (_uiCallback != null) {
				_uiCallback (component);
			}
			// Get text
			var textContent:String = Strings.trim(content as String);
			if (!Strings.isEmpty(textContent)) {
				component.text = textContent;
			}
			// Get image
			if (image != null) {
				component.iconClass = image;
			}
			// Buttons
			if (buttons == null) {
				buttons = Vector.<String>([PromptDefaults.OK_LABEL]);
			}
			for (var i:int = 0; i < buttons.length; i++) {
				var buttonLabel:String = buttons[i];
				component.createButton(buttonLabel);
			}
			// Checkbox
			if (checkboxLabel != null) {
				checkboxLabel = Strings.trim(checkboxLabel);
				if (!Strings.isEmpty(checkboxLabel)) {
					component.createCheckBox(checkboxLabel);
				}
			}
			// Progress bar
			if (progressBarObserver != null) {
				component.createProgressBar(progressBarObserver);
			}
			// MAKE THE WINDOW
			_clearExisting();
			
			// Create the new window as the child of last blocking modal window, if any; otherwise, the
			// window will be created as a child of the main window.
			var parentWindowId : String = _findTopmostParent ();
			
			_uid = _windowsManager.createWindow (component, WindowStyle.PROMPT, true, parentWindowId);
			if (_uid != null) {
				component.uid = _uid;
				_windowsManager.observeWindowActivity(_uid, WindowActivity.DESTROY, _onWindowDestroyed);
				_windowsManager.updateWindowTitle(_uid, title);
				_windowsManager.showWindow(_uid);
				if (centerToMainWindow) {
					_windowsManager.observeWindowActivity(_uid, WindowActivity.BEFORE_DESTROY, _removeCenteringListener);
					_windowsManager.observeWindowActivity (_uid, WindowActivity.RESIZE, _centeringListener);
				}
	
				// OBSERVE USER ACTIONS
				_currentPromptObserver = new Observer;
				component.addEventListener(PromptDefaults.USER_INTERRACTION, function(event:Event):void {
					var targetComponent:PromptBaseUI = (event.target as PromptBaseUI);
					_currentPromptDetail = targetComponent.interactionDetail;
					// For any other button than the checkbox, destroy the window, and have some callback code
					// executed AFTER - this is important.
					if (_currentPromptDetail != PromptDefaults.CHECKED && _currentPromptDetail != PromptDefaults.UNCHECKED) {
						_clearExisting();
					} else {
						// Otherwise, just send a notification that the checkbox was changed
						_currentPromptObserver.notifyChange(PromptDefaults.USER_INTERRACTION, _currentPromptDetail);
					}
				});
				return _currentPromptObserver;
			}
			return null;
		}
		
		/**
		 * Triggered when the window is resized in result to content being rendererd.
		 */
		private function _centeringListener (windowUid : String) : void {
			if (_windowsManager.isWindowAvailable(windowUid) &&
				_windowsManager.isWindowVisible(windowUid)) {
				var ownBounds : Rectangle = _windowsManager.retrieveWindowBounds (windowUid);
				var rootBounds : Rectangle = _windowsManager.retrieveWindowBounds (_windowsManager.mainWindow);
				var centeredBounds : Rectangle = new Rectangle (
					rootBounds.x + (rootBounds.width - ownBounds.width) * 0.5,
					rootBounds.y + (rootBounds.height - ownBounds.height) * 0.5
				);				
				_windowsManager.updateWindowBounds(windowUid, centeredBounds, true);
				
			}
		}
		
		/**
		 * Finds the last open modal window that can accept a child modal window. Returns the main window
		 * if there are no other modals open.
		 */
		private function _findTopmostParent () : String {
			var parentId  : String = _windowsManager.mainWindow;
			var allWindowIds : Vector.<String> = _windowsManager.availableWindows;
			for (var i : int = 0; i < allWindowIds.length; i++) {
				var windowId : String = allWindowIds[i];
				var isBlocking : Boolean = _windowsManager.isWindowBlocking (windowId);
				if (!isBlocking) {
					continue;
				}
				var hasChildren : Boolean = (_windowsManager.retrieveChildWindowsOf (windowId).length != 0);
				if (hasChildren) {
					continue;
				}
				parentId = windowId;
				break;
			}
			return parentId;			
		}
		
		private function _clearExisting():void {
			if (_uid != null) {
				_windowsManager.stopObservingWindowActivity(_uid, WindowActivity.DESTROY, _onWindowDestroyed);
				_windowsManager.destroyWindow(_uid);
				_onWindowDestroyed ();
			}
		}

		/**
		 * This method runs BEFORE an window is destroyed. This is the last chance for purging, releasing memory, etc.
		 */
		private function _removeCenteringListener (windowUid : String) : void {
			_windowsManager.stopObservingWindowActivity (_uid, WindowActivity.RESIZE, _centeringListener);
		}
		
		/**
		 * @private
		 * This method is run AFTER user causes the window of a prompt to close, whatever the means.
		 */
		private function _onWindowDestroyed(... etc):void {
			_uid = null;
			if (_currentPromptObserver != null) {
				if (_currentPromptDetail == null || _currentPromptDetail == PromptDefaults.CHECKED || _currentPromptDetail ==
					PromptDefaults.UNCHECKED) {
					_currentPromptDetail = PromptDefaults.X_LABEL;
				}
				Time.delay (0, _commitUserResponse);
				return;
			}
			_currentPromptDetail = null;
		}
		
		/**
		 * Sends out a notification containing user response. This approach ensures that the notification reaches out
		 * the host application AFTER the prompt window has been closed, and thus AFTER any windows that were blocked
		 * by the prompt have been unblocked. This is important in the event we need to manipulate those windows in
		 * response to the notification.
		 */
		private function _commitUserResponse () : void {
			_currentPromptObserver.notifyChange (PromptDefaults.USER_INTERRACTION, _currentPromptDetail);
			_currentPromptObserver = null;
			_currentPromptDetail = null;
		}
	}
}