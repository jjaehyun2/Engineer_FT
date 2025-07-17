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
	public class TUserWindowConstants
	{
		//
		// PROPERTIES
		//
		
		/**
		 * <p>The ALL event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;all&quot;</code>
		 * 
		 * </p>
		 */
		public static const ALL:String = "All";
		
		/**
		 * <p>The APP_EXIT event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;app.exit&quot;</code>
		 * 
		 * </p>
		 */
		public static const APP_EXIT:String = "AppExit";
		
		/**
		 * <p>The CLOSE event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;close&quot;</code>
		 * 
		 * </p>
		 */
		public static const CLOSE:String = "Close";
		
		/**
		 * <p>The CLOSED event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;closed&quot;</code>
		 * 
		 * </p>
		 */
		public static const CLOSED:String = "Closed";
		
		/**
		 * <p>The CREATED event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;create&quot;</code>
		 * 
		 * </p>
		 */
		public static const CREATED:String = "Created";
		
		/**
		 * <p>The EXIT event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;exit&quot;</code>
		 * 
		 * </p>
		 */
		public static const EXIT:String = "Exit";
		
		/**
		 * <p>The FOCUSED event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;focused&quot;</code>
		 * 
		 * </p>
		 */
		public static const FOCUSED:String = "Focused";
		
		/**
		 * <p>The FULLSCREENED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;fullscreened&quot;</code>
		 * 
		 * </p>
		 */
		public static const FULLSCREENED:String = "Fullscreened";
		
		/**
		 * <p>The HIDDEN event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;hidden&quot;</code>
		 * 
		 * </p>
		 */
		public static const HIDDEN:String = "Hidden";
		
		/**
		 * <p>The HTTP_ABORT event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;http.abort&quot;</code>
		 * 
		 * </p>
		 */
		public static const HTTP_ABORT:String = "HttpAbort";
		
		/**
		 * <p>The CLOSED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;http.datareceived&quot;</code>
		 * 
		 * </p>
		 */
		public static const HTTP_DATA_RECEIVED:String = "HttpDataReceived";
		
		/**
		 * <p>The HTTP_DATA_SENT event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;http.datasent&quot;</code>
		 * 
		 * </p>
		 */
		public static const HTTP_DATA_SENT:String = "HttpDataSent";
		
		/**
		 * <p>The HTTP_DONE event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;http.done&quot;</code>
		 * 
		 * </p>
		 */
		public static const HTTP_DONE:String = "HttpDone";
		
		/**
		 * <p>The HTTP_REDIRECT event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;http.redirect&quot;</code>
		 * 
		 * </p>
		 */
		public static const HTTP_REDIRECT:String = "HttpRedirect";
		
		/**
		 * <p>The HTTP_STATE_CHANGED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;http.statechanged&quot;</code>
		 * 
		 * </p>
		 */
		public static const HTTP_STATE_CHANGED:String = "HttpStateChanged";
		
		/**
		 * <p>The HTTP_TIMEOUT event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;http.timeout&quot;</code>
		 * 
		 * </p>
		 */
		public static const HTTP_TIMEOUT:String = "HttpTimeout";
		
		/**
		 * <p>The MAXIMIZED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;maximized&quot;</code>
		 * 
		 * </p>
		 */
		public static const MAXIMIZED:String = "Maximized";
		
		/**
		 * <p>The MINIMIZED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;minimized&quot;</code>
		 * 
		 * </p>
		 */
		public static const MINIMIZED:String = "Minimized";
		
		/**
		 * <p>The MOVED event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;moved&quot;</code>
		 * 
		 * </p>
		 */
		public static const MOVED:String = "Moved";
		
		/**
		 * <p>The OPEN event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;open&quot;</code>
		 * 
		 * </p>
		 */
		public static const OPEN:String = "Open";
		
		/**
		 * <p>The OPENED event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;opened&quot;</code>
		 * 
		 * </p>
		 */
		public static const OPENED:String = "Opened";
		
		/**
		 * <p>The OPEN_REQUEST event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;open.request&quot;</code>
		 * 
		 * </p>
		 */
		public static const OPEN_REQUEST:String = "OpenRequest";
		
		/**
		 * <p>The PAGE_INITIALIZED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;page.init&quot;</code>
		 * 
		 * </p>
		 */
		public static const PAGE_INITIALIZED:String = "PageInitialized";
		
		/**
		 * <p>The PAGE_LOADED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;page.load&quot;</code>
		 * 
		 * </p>
		 */
		public static const PAGE_LOADED:String = "PageLoaded";
		
		/**
		 * <p>The READ event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;read&quot;</code>
		 * 
		 * </p>
		 */
		public static const READ:String = "Read";
		
		/**
		 * <p>The RESIZED event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;resized&quot;</code>
		 * 
		 * </p>
		 */
		public static const RESIZED:String = "Resized";
		
		/**
		 * <p>The SHOWN event constant</p>
		 * 
		 *  <p>Defaults to: <code>&quot;shown&quot;</code>
		 * 
		 * </p>
		 */
		public static const SHOWN:String = "Shown";
		
		/**
		 * <p>The UNFOCUSED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;unfocused&quot;</code>
		 * 
		 * </p>
		 */
		public static const UNFOCUSED:String = "Unfocused";
		
		/**
		 * <p>The UNFULLSCREENED event constant</p>
		 * 
		 *  <p>Defaults to:
		 * <code>&quot;unfullscreened&quot;</code>
		 * 
		 * </p>
		 */
		public static const UNFULLSCREENED:String = "Unfullscreened";
		
		public function TUserWindowConstants() {}
	}
}