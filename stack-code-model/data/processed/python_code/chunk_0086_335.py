package dom.tidesdk.ui
{
	import dom.domobjects.Window;

	/**
	 * <p>An object representing a top-level TideSDK
	 * window. All windows in TideSDK are <a
	 * href="#!/api/Ti.UI.UserWindow"
	 * rel="Ti.UI.UserWindow"
	 * class="docClass">Ti.UI.UserWindow</a> objects.   
	 * <br/> The current window can be accessed and
	 * modified as shown below:</p>
	 * 
	 *   <pre><code>var window = Ti.UI.currentWindow;
	 * window.setTitle('New Title'); // Will set window
	 * title to New Title </code></pre>
	 * 
	 *   <p>Once you open a window, you can close it at
	 * anytime. This will ensure that all resources
	 * attached to that window are freed up. However,
	 * this also means that the window cannot be opened
	 * again. If you need to hide a window , the
	 * following code can be used :</p>
	 * 
	 *   <pre><code>Ti.UI.currentWindow.hide(); //window
	 * hidden setTimeout(function() {    
	 * Ti.UI.currentWindow.show(); //window shown },
	 * 3000); </code></pre>
	 */
	public class TUserWindow
	{
		//
		// METHODS
		//

		/**
		 * <p>Registers a single event listener on the
		 * window. To register more than one event listener
		 * for the window, call
		 * <code>addEventListener()</code>
		 * 
		 *  multiple times but with different event
		 * types.</p>
		 * 
		 * @param type  A string representing the event type to listen for. 
		 * @param listener  The object that receives a notification when an event of the specified type occurs. This must be an object implementing the EventListener interface, or simply a JavaScript function. 
		 */
		public function addEventListener(type:String, listener:Function):void {}

		/**
		 * <p>Closes a window</p>
		 */
		public function close():void {}

		/**
		 * <p>Creates a new window as a child of the current
		 * window</p>
		 * 
		 * @param options  A string containing a url of the new window or an object containing properties for the new window 
		 * 
		 * @return Ti.UI.UserWindow   
		 */
		public function createWindow(options:Object=null):TUserWindow { return null; }

		/**
		 * <p>Focuses a window</p>
		 */
		public function focus():void {}

		/**
		 * <p>Return this window's bounds object. A bounds
		 * object is a simple JavaScript object containing
		 * four properties <tt>x</tt>, <tt>y</tt>,
		 * <tt>width</tt>, and <tt>height</tt> which
		 * correspond to the window geometry on the screen in
		 * pixels.</p>
		 * 
		 * @return object   
		 */
		public function getBounds():Object { return null; }

		/**
		 * <p>Get all children of this UI.UserWindow. All
		 * windows open from the context of this window are
		 * considered children. When a window is closed all
		 * of its children will also be closed
		 * automatically.</p>
		 * 
		 * @return Ti.Array&lt;UI.UserWindow&gt;   
		 */
		public function getChildren():Vector.<TUserWindow> { return null; }

		/**
		 * <p>Return the context menu set on this
		 * UI.Userwindow or null if none is set.</p>
		 * 
		 * @return Ti.UI.Menu|null   
		 */
		public function getContextMenu():TMenu { return null; }

		/**
		 * <p>Return the current window. This function does
		 * not exist outside of the context of a window.</p>
		 * 
		 * @return Ti.UI.UserWindow   
		 */
		public function getCurrentWindow():TUserWindow { return null; }

		/**
		 * <p>Return the WebKit DOMWindow of the page loaded
		 * in this window if one exists, otherwise return
		 * null. A DOMWindow object will not be available
		 * until a UI.UserWindow's PAGE_INITIALIZED event has
		 * fired.</p>
		 * 
		 * @return DOMWindow|null   
		 */
		public function getDOMWindow():Window { return null; }

		/**
		 * <p>Return this window's height in pixels.</p>
		 * 
		 * @return Number   
		 */
		public function getHeight():Number { return 0; }

		/**
		 * <p>Return this window's configuration id.</p>
		 * 
		 * @return String   
		 */
		public function getID():String { return ""; }

		/**
		 * <p>Return this window's icon, if one is set or
		 * null</p>
		 * 
		 * @return String|Null   
		 */
		public function getIcon():String { return null; }

		/**
		 * <p>Return this window's maximum height.</p>
		 * 
		 * @return Number   
		 */
		public function getMaxHeight():Number { return 0; }

		/**
		 * <p>Return this window's maximum height in
		 * pixels.</p>
		 * 
		 * @return Number   
		 */
		public function getMaxWidth():Number { return 0; }

		/**
		 * <p>Return the window menu set on this
		 * UI.UserWindow if one is set, otherwise return
		 * null.</p>
		 * 
		 * @return Ti.UI.Menu|null   
		 */
		public function getMenu():TMenu { return null; }

		/**
		 * <p>Return this window's minimum height.</p>
		 * 
		 * @return Number   
		 */
		public function getMinHeight():Number { return 0; }

		/**
		 * <p>Return this window's minimum width.</p>
		 * 
		 * @return Number   
		 */
		public function getMinWidth():Number { return 0; }

		/**
		 * <p>Return this window's parent window or null if
		 * it is a top-level window.</p>
		 * 
		 * @return Ti.UI.UserWindow|null   
		 */
		public function getParent():TUserWindow { return null; }

		/**
		 * <p>Return the title of this window.</p>
		 * 
		 * @return String   
		 */
		public function getTitle():String { return ""; }

		/**
		 * <p>Return this window's opacity.</p>
		 * 
		 * @return Number   
		 */
		public function getTransparency():Number { return 0; }

		/**
		 * <p>Return this window's current URL.</p>
		 * 
		 * @return String   
		 */
		public function getURL():String { return ""; }

		/**
		 * <p>Return this window's width in pixels.</p>
		 * 
		 * @return Number   
		 */
		public function getWidth():Number { return 0; }

		/**
		 * <p>Return this windows DOMWindow object.</p>
		 * 
		 * @return DOMWindow  the DOMWindow object of this window. 
		 */
		public function getWindow():Window { return null; }

		/**
		 * <p>Return a UI.UserWindow's horizontal (X-axis)
		 * position on the screen. The origin of the screen
		 * is considered to be the top-left on all
		 * platforms.</p>
		 * 
		 * @return Number   
		 */
		public function getX():Number { return 0; }

		/**
		 * <p>Return a UI.UserWindow's vertical (Y-axis)
		 * position on the screen. The origin of the screen
		 * is considered to be the top-left on all
		 * platforms.</p>
		 * 
		 * @return Number   
		 */
		public function getY():Number { return 0; }

		/**
		 * <p>Checks whether a window has a transparent
		 * background or not. If a window has a transparent
		 * background, transparent colors on the page will
		 * show through to windows underneath.</p>
		 * 
		 * @return bool   
		 */
		public function hasTransparentBackground():Boolean { return false; }

		/**
		 * <p>Hides a window</p>
		 * 
		 * @return String   
		 */
		public function hide():String { return ""; }

		/**
		 * <p>Return true if this window is active. An active
		 * window is one that has finished opening, but has
		 * not yet been closed.</p>
		 * 
		 * @return Boolean   
		 */
		public function isActive():Boolean { return false; }

		/**
		 * <p>Checks whether a window could be closed or
		 * not</p>
		 * 
		 * @return Boolean   
		 */
		public function isCloseable():Boolean { return false; }

		/**
		 * <p>Returns true if this window is a UI Dialog</p>
		 * 
		 * @return Boolean   
		 */
		public function isDialog():Boolean { return false; }

		/**
		 * <p>Checks whether a window is in an edited
		 * state</p>
		 * 
		 * @return Boolean   
		 */
		public function isDocumentEdited():Boolean { return false; }

		/**
		 * <p>Checks whether a window is in fullscreen</p>
		 * 
		 * @param chrome  true if the window is in fullscreen, false if otherwise 
		 * 
		 * @return String   
		 */
		public function isFullscreen(chrome:Boolean):String { return ""; }

		/**
		 * <p>Checks whether a window could be maximized or
		 * not</p>
		 * 
		 * @return String   
		 */
		public function isMaximizable():String { return ""; }

		/**
		 * <p>Checks whether a window is maximized</p>
		 * 
		 * @return Boolean   
		 */
		public function isMaximized():Boolean { return false; }

		/**
		 * <p>Checks whether a window could be minimized or
		 * not</p>
		 * 
		 * @return Boolean   
		 */
		public function isMinimizable():Boolean { return false; }

		/**
		 * <p>Checks whether a window is minimized</p>
		 * 
		 * @return Boolean   
		 */
		public function isMinimized():Boolean { return false; }

		/**
		 * <p>Checks whether a window is resizable</p>
		 * 
		 * @return Boolean   
		 */
		public function isResizable():Boolean { return false; }

		/**
		 * <p>Checks whether a window is a toolwindow</p>
		 * 
		 * @return Boolean   
		 */
		public function isToolWindow():Boolean { return false; }

		/**
		 * <p>Checks whether a window is top most</p>
		 * 
		 * @return Boolean   
		 */
		public function isTopMost():Boolean { return false; }

		/**
		 * <p>Checks whether a window uses system chrome</p>
		 * 
		 * @return Boolean   
		 */
		public function isUsingChrome():Boolean { return false; }

		/**
		 * <p>Checks whether a window is visible</p>
		 * 
		 * @return Boolean   
		 */
		public function isVisible():Boolean { return false; }

		/**
		 * <p>Maximizes a window</p>
		 */
		public function maximize():void {}

		/**
		 * <p>Minimizes a window</p>
		 */
		public function minimize():void {}

		/**
		 * <p>Moves the window to the specified position.</p>
		 * 
		 * @param x   
		 * @param y   
		 */
		public function moveTo(x:int, y:int):void {}

		/**
		 * <p>Opens a window</p>
		 */
		public function open():void {}

		/**
		 * <p> Displays a file chooser dialog. This is
		 * suitable for use cases where you need the user to
		 * select what file(s) to open or be saved. </p>
		 * 
		 *    <p> Available Options: <ul> <li>multiple:
		 * true/false - allow user to select multple files
		 * [default: true]</li>
		 *  <li>title: string used as the title of the dialog
		 * box</li>
		 *  <li>path: location where browsing of files should
		 * begin when dialog opens</li>
		 *  <li>types: list of allowable file types that user
		 * can pick (ex: js, html, txt)</li>
		 *  </ul>
		 *  </p>
		 * 
		 * @param callback  a callback function to fire after the user closes the dialog 
		 * @param options  additional options for the dialog 
		 */
		public function openFileChooserDialog(callback:Function, options:Object=null):void {}

		/**
		 * <p>Displays the folder chooser dialog</p>
		 * 
		 * @param callback  a callback function to fire after the user closes the dialog 
		 * @param options  additional options for the dialog 
		 */
		public function openFolderChooserDialog(callback:Function, options:Object=null):void {}

		/**
		 * <p>Displays the save as file dialog. Available
		 * options:</p>
		 * 
		 *   <ul> <li>title: string to use for dialog
		 * title</li>
		 *  <li>path: path to where the dialog should be
		 * opened at</li>
		 *  <li>types: array of file extensions that are
		 * allowed to be selected</li>
		 *  <li>multiple: if true, allow user to select more
		 * than one file [default: true]</li>
		 *  <li>defaultFile: default name to be used for
		 * saving</li>
		 *  </ul>
		 * 
		 * @param callback  a callback function to fire after the user closes the dialog 
		 * @param options  additional options for the dialog 
		 */
		public function openSaveAsDialog(callback:Function, options:Object=null):void {}

		/**
		 * <p>Allows the removal of eventlisteners from the
		 * window.</p>
		 * 
		 * @param type  A string representing the event type being removed. 
		 * @param listener  The listener object to be removed. 
		 */
		public function removeEventListener(type:String, listener:Function):void {}

		/**
		 * <p>Set this window's bounds object. A bounds
		 * object is a simple JavaScript object containing
		 * four properties <tt>x</tt>, <tt>y</tt>,
		 * <tt>width</tt>, and <tt>height</tt> which
		 * correspond to the window geometry on the screen in
		 * pixels.</p>
		 * 
		 * @param bounds  an object containing the value for the window bounds 
		 */
		public function setBounds(bounds:Object):void {}

		/**
		 * <p>Sets whether a window could be closed or
		 * not</p>
		 * 
		 * @param closeable  true if the window could be closed, false if otherwise 
		 */
		public function setCloseable(closeable:Boolean):void {}

		/**
		 * <p>Set the contents of the UserWindow, given an
		 * HTML string and a base URL. Relative links in the
		 * HTML will be resolved relatively to the base
		 * URL.</p>
		 * 
		 * @param contents  The HTML string to inject into the UserWindow. 
		 * @param baseURL  The base URL of the URL string. If omitted URLs will be resolved relative to the root of the app resources directory. 
		 */
		public function setContents(contents:String, baseURL:String=null):void {}

		/**
		 * <p>Set this window's context menu</p>
		 * 
		 * @param menu  The Menu object to use as the context menu or null to unset the menu. 
		 */
		public function setContextMenu(menu:TMenu):void {}

		/**
		 * <p>Set a window to the edited (a dot in the close
		 * button) or unedited state. OS X only.</p>
		 * 
		 * @param edited  true if the window is edited, false if not 
		 */
		public function setDocumentEdited(edited:Boolean):void {}

		/**
		 * <p>Makes a window fullscreen</p>
		 * 
		 * @param fullscreen  set to true for fullscreen, false if otherwise 
		 */
		public function setFullscreen(fullscreen:Boolean):void {}

		/**
		 * <p>Sets a window's height</p>
		 * 
		 * @param height  the height value of the window 
		 */
		public function setHeight(height:int):void {}

		/**
		 * <p>Sets a window's icon</p>
		 * 
		 * @param icon  path to the icon file 
		 */
		public function setIcon(icon:String):void {}

		/**
		 * <p>Sets a window's max-height</p>
		 * 
		 * @param height  the max-height value of the window 
		 */
		public function setMaxHeight(height:int):void {}

		/**
		 * <p>Sets a window's max-width</p>
		 * 
		 * @param width  the max-width value of the window 
		 */
		public function setMaxWidth(width:int):void {}

		/**
		 * <p>Sets whether a window could be maximized or
		 * not</p>
		 * 
		 * @param maximizable  true if the window could be maximized, false if otherwise 
		 */
		public function setMaximizable(maximizable:Boolean):void {}

		/**
		 * <p>Set this window's menu</p>
		 * 
		 * @param menu  The Menu object to use as the menu or null to unset the menu. 
		 */
		public function setMenu(menu:TMenu):void {}

		/**
		 * <p>Sets a window's min height</p>
		 * 
		 * @param height  the min-height value of the window 
		 */
		public function setMinHeight(height:int):void {}

		/**
		 * <p>Sets a window's min-width</p>
		 * 
		 * @param width  the min-width value of the window 
		 */
		public function setMinWidth(width:int):void {}

		/**
		 * <p>Sets whether a window could be maximized or
		 * not</p>
		 * 
		 * @param minimizable  true if the window could be minimized, false if otherwise 
		 */
		public function setMinimizable(minimizable:Boolean):void {}

		/**
		 * <p>Set if plugins are enabled</p>
		 * 
		 * @param enabled  true if plugins should be enabled 
		 */
		public function setPluginsEnabled(enabled:Boolean):void {}

		/**
		 * <p>Sets whether a window could be resized or
		 * not</p>
		 * 
		 * @param resizable  true if the window could be resized, false if otherwise 
		 */
		public function setResizable(resizable:Boolean):void {}

		/**
		 * <p>Sets a window's width and height.</p>
		 * 
		 * @param width  the width of the window 
		 * @param height  the height of the window 
		 */
		public function setSize(width:int, height:int):void {}

		/**
		 * <p>Sets the title of a window</p>
		 * 
		 * @param title  the title of the window 
		 */
		public function setTitle(title:String):void {}

		/**
		 * <p>Sets whether a window is top most (above other
		 * windows)</p>
		 * 
		 * @param topmost  true if top most, false if otherwise 
		 */
		public function setTopMost(topmost:Boolean):void {}

		/**
		 * <p>Sets a window's transparency value Note: this
		 * will make the window and ALL of its contents
		 * transparent.</p>
		 * 
		 * @param A  value between 0 and 1 where 0 is fully transparent. 
		 */
		public function setTransparency(A:Number):void {}

		/**
		 * <p>Sets the url for a window</p>
		 * 
		 * @param url  the url for the window 
		 */
		public function setURL(url:String):void {}

		/**
		 * <p>Sets whether a window should use system
		 * chrome</p>
		 * 
		 * @param chrome  set to true to use system chrome, false if otherwise 
		 */
		public function setUsingChrome(chrome:Boolean):void {}

		/**
		 * <p>Sets the visibility of the window</p>
		 * 
		 * @param visible  true if the window should be visible, false if otherwise 
		 */
		public function setVisible(visible:Boolean):void {}

		/**
		 * <p>Sets a window's width</p>
		 * 
		 * @param width  the width of the window 
		 */
		public function setWidth(width:int):void {}

		/**
		 * <p>Set a UI.UserWindow's horizontal (X-axis)
		 * position on the screen. The origin of the screen
		 * is considered to be the top-left on all
		 * platforms.</p>
		 * 
		 * @param x  the horizontal position 
		 */
		public function setX(x:int):void {}

		/**
		 * <p>Set a UI.UserWindow's vertical (Y-axis)
		 * position on the screen. The origin of the screen
		 * is considered to be the top-left on all
		 * platforms.</p>
		 * 
		 * @param y  the vertical position 
		 */
		public function setY(y:int):void {}

		/**
		 * <p>Shows a window</p>
		 */
		public function show():void {}

		/**
		 * <p>Show a UI.UserWindow's web inspector.</p>
		 * 
		 * @param console  Open the console along with the inspector (defaults to false). 
		 */
		public function showInspector(console:Boolean=false):void {}

		/**
		 * <p>Unfocuses a window</p>
		 */
		public function unfocus():void {}

		/**
		 * <p>Unmaximizes a window</p>
		 */
		public function unmaximize():void {}

		/**
		 * <p>Unminimizes a window</p>
		 */
		public function unminimize():void {}

		public function TUserWindow() {}
	}
}