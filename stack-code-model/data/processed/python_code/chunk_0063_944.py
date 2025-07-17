package dom.tidesdk
{
	import dom.tidesdk.api.TAPI;
	import dom.tidesdk.app.TApp;
	import dom.tidesdk.database.TDatabase;
	import dom.tidesdk.filesystem.TFilesystem;
	import dom.tidesdk.media.TMedia;
	import dom.tidesdk.misc.TBytes;
	import dom.tidesdk.misc.TCodec;
	import dom.tidesdk.misc.TCodecConstants;
	import dom.tidesdk.misc.TJSON;
	import dom.tidesdk.misc.TPlatform;
	import dom.tidesdk.misc.TUpdateManager;
	import dom.tidesdk.network.TNetwork;
	import dom.tidesdk.notification.TNotificationBase;
	import dom.tidesdk.process.TProcessBase;
	import dom.tidesdk.ui.TUI;
	import dom.tidesdk.worker.TWorkerBase;

	public class Ti
	{
		/** The ALL event constant. This can be used for listening for all events. */
		public static const ALL:String = "All";
		
		/** The APP_EXIT event constant, fired during host application exit. */
		public static const APP_EXIT:String = "AppExit";
			
		/** The CLOSE event constant */
		public static const CLOSE:String = "Close";
		
		/** The CLOSED event constant */
		public static const CLOSED:String = "Closed";

		/** The CREATE event constant */
		public static const CREATE:String = "Create";

		/** The EXIT event constant */
		public static const EXIT:String = "Exit";

		/** The FOCUSED event constant */
		public static const FOCUSED:String = "Focused";
		
		/** The FULLSCREENED event constant */
		public static const FULLSCREENED:String = "Fullscreened";

		/** The HIDDEN event constant */
		public static const HIDDEN:String = "Hidden";
		
		/** The HTTP request aborted event constant. */
		public static const HTTP_ABORT:String = "HttpAbort";

		/** The HTTP data received event constant */
		public static const HTTP_DATA_RECEIVED:String = "HttpDataReceived";

		/** The HTTP data sent event constant */
		public static const HTTP_DATA_SENT:String = "HttpDataSent";

		/** The HTTP request complete event constant */
		public static const HTTP_DONE:String = "HttpDone";

		/** The HTTP redirect event constant */
		public static const HTTP_REDIRECT:String = "HttpRedirect";

		/** The HTTP state changed event constant */
		public static const HTTP_STATE_CHANGED:String = "HttpStateChanged";

		/**The HTTP request timeout event constant */
		public static const HTTP_TIMEOUT:String = "HttpTimeout";

		/** The MAXIMIZED event constant */
		public static const MAXIMIZED:String = "Maximized";
		
		/** The MINIMIZED event constant */
		public static const MINIMIZED:String = "Minimized";
		
		/** The MOVED event constant */
		public static const MOVED:String = "Moved";

		/** The OPEN event constant */
		public static const OPEN:String = "Open";

		/** The OPENED event constant */
		public static const OPENED:String = "Opened";

		/** The OPEN request event constant */
		public static const OPEN_REQUEST:String = "OpenRequest";

		/** The PAGE_INITIALIZED event constant */
		public static const PAGE_INITIALIZED:String = "PageInitialized";

		/** The PAGE_LOADED event constant */
		public static const PAGE_LOADED:String = "PageLoaded";

		/** The READ event constant */
		public static const READ:String = "Read";

		/** The RESIZED event constant */
		public static const RESIZED:String = "Resized";

		/** The SHOWN event constant */
		public static const SHOWN:String = "Shown";

		/** The UNFOCUSED event constant */
		public static const UNFOCUSED:String = "Unfocused";
		
		/** The UNFULLSCREENED event constant */
		public static const UNFULLSCREENED:String = "Unfullscreened";

		/**
		 * Return the current platform.
		 * 
		 * @return A string with the current platform; either 'osx', 'win32' or 'linux'.
		 */
		public static function getPlatform():String { return null; }

		/**
		 * Return the Ti runtime version
		 * @return String
		 */
		public static function getVersion():String { return null; }
		
		/** A module for holding core TideSDK functionality */
		public static function get API():TAPI { return null; }
		
		/** A module for holding currently running application specific functionality */
		public static function get App():TApp { return null; }
		
		/**
		 * A module for dealing with Database storage. There are two ways to
		 * use databases in TideSDK - HTML5 Databases and the TideSDK Database
		 * API. Both API's make use of SQLite backends.
		 */
		public static function get Database():TDatabase { return null; }
		
		/** A module for accessing the Filesystem. */
		public static function get Filesystem():TFilesystem { return null; }
		
		/** A module for dealing with Media. */
		public static function get Media():TMedia { return null; }
		
		/** A module for network functionality. */
		public static function get Network():TNetwork { return null; }
		
		/**
		 * A module for displaying desktop notifications. TideSDK allows you to
		 * display notifications from your desktop apps using Growl on OS X,
		 * Snarl on Windows and libnotify on Linux. In the event of a
		 * notification provider being absent, notifications are shown using
		 * HTML/CSS.
		 */
		public static function get Notification():TNotificationBase { return null; }
		
		/** A module for creating processes. */
		public static function get Process():TProcessBase { return null; }
		
		/** A module for controlling the user interface. */
		public static function get UI():TUI { return null; }
		
		/** A module for creating Worker threads in TideSDK. */
		public static function get Worker():TWorkerBase { return null; }
		
		/** A module for dealing with encoding and decoding. */
		public static function get Codec():TCodecConstants { return null; }
		
		/** A module for serializing and deserializing JSON. */
		public static function get JSON():TJSON { return null; }
		
		/** A module for exposing platform-specific functionality. */
		public static function get Platform():TPlatform { return null; }
		
		/** A module for dealing with application and component updates in TideSDK. */
		public static function get UpdateManager():TUpdateManager { return null; }
		
		public function Ti()
		{
		}
	}
}