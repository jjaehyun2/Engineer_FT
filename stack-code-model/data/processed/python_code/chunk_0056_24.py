package dom.tidesdk.app
{
	/**
	 * <p>A module for holding currently running
	 * application specific functionality.</p>
	 */
	public class TApp
	{
		//
		// METHODS
		//

		/**
		 * <p>Convert the given app URL to a filesystem path.
		 * App URLs generally have the form
		 * 'app://subdir/resource.html' and resolve to a
		 * fileystem path rooted in the application resources
		 * directory.</p>
		 * 
		 * @return String   
		 */
		public function appURLToPath():String { return ""; }

		/**
		 * <p>Create a new App.Properties object.</p>
		 * 
		 * @param properties  Initial properties for the new App.Properties object. 
		 * 
		 * @return Ti.App.Properties   
		 */
		public function createProperties(properties:Object=null):TProperties { return null; }

		/**
		 * <p>Cause the application to exit after firing the
		 * <a href="#!/api/Ti-property-EXIT"
		 * rel="Ti-property-EXIT"
		 * class="docClass">Ti.EXIT</a> event. The
		 * application isn't gauaranteed to exit when this
		 * method is called, because an event handler may
		 * cancel the EXIT event by calling preventDefault or
		 * stopPropagation on it.</p>
		 */
		public function exit():void {}

		/**
		 * <p>Return the command-line arguments passed to
		 * this application, excluding the first which is the
		 * path to the application executable.</p>
		 * 
		 * @return Array   
		 */
		public function getArguments():Array { return null; }

		/**
		 * <p>Return the application's copyright information,
		 * defined in the tiapp.xml file.</p>
		 * 
		 * @return String   
		 */
		public function getCopyright():String { return ""; }

		/**
		 * <p>Return the application's description, defined
		 * in the tiapp.xml file.</p>
		 * 
		 * @return String   
		 */
		public function getDescription():String { return ""; }

		/**
		 * <p>Return the application's GUID, defined in the
		 * application manifest.</p>
		 * 
		 * @return String   
		 */
		public function getGUID():String { return ""; }

		/**
		 * <p>Return the full path to the application home
		 * directory. The application home or contents
		 * directory is the subdirectory within the
		 * application which contains the application
		 * Resources directory and bundled components. On OS
		 * X this is the directory "My App.app/Contents" and
		 * on Windows and Linux it is simply the path to the
		 * application.</p>
		 * 
		 * @return String   
		 */
		public function getHome():String { return ""; }

		/**
		 * <p>Get this human readable id defined in both the
		 * application manifest and the application's
		 * tiapp.xml file.</p>
		 * 
		 * @return String   
		 */
		public function getID():String { return ""; }

		/**
		 * <p>Return the full path to the application icon.
		 * The application icon path is specified in the
		 * application manifest and tiapp.xml relative to the
		 * application Resources directory.</p>
		 * 
		 * @return String   
		 */
		public function getIcon():String { return ""; }

		/**
		 * <p>Return the application name.</p>
		 * 
		 * @return String   
		 */
		public function getName():String { return ""; }

		/**
		 * <p>Return the full path to the application
		 * executable.</p>
		 * 
		 * @return String   
		 */
		public function getPath():String { return ""; }

		/**
		 * <p>Return the application publisher information
		 * specifiedi in the tiapp.xml file.</p>
		 * 
		 * @return String   
		 */
		public function getPublisher():String { return ""; }

		/**
		 * <p>Return the stream URL for the application's
		 * updates.</p>
		 * 
		 * @param multiple  Any number of String arguments which will be appended as path components of the stream URL. 
		 * 
		 * @return String   
		 */
		public function getStreamURL(multiple:Vector.<String>):String { return ""; }

		/**
		 * <p>Get the system properties defined in tiapp.xml
		 * (see App.Properties).</p>
		 * 
		 * @return Ti.App.Properties   
		 */
		public function getSystemProperties():TProperties { return null; }

		/**
		 * <p>Return the application URL definedin the
		 * tiapp.xml file.</p>
		 * 
		 * @return String   
		 */
		public function getURL():String { return ""; }

		/**
		 * <p>Return the application version defined in the
		 * tiapp.xml file.</p>
		 * 
		 * @return String   
		 */
		public function getVersion():String { return ""; }

		/**
		 * <p>Loads a properties list from a file path.</p>
		 * 
		 * @param path  Path to a properties file. 
		 * 
		 * @return Ti.Array&lt;App.Properties&gt;   
		 */
		public function loadProperties(path:String):Vector.<TProperties> { return null; }

		/**
		 * <p>Exit the application and restart it.</p>
		 */
		public function restart():void {}

		/**
		 * <p>Print a raw string to stderr without a trailing
		 * newline.</p>
		 * 
		 * @param data  The data to print. If not a String, it will be converted using the equivalent of String(data); 
		 */
		public function stderr(data:String):void {}

		/**
		 * <p>Reads from stdin</p>
		 * 
		 * @param prompt  "(optional) Text prompt for input. If not specified, no prompt will appear." 
		 * @param delimiter  "(optional) Will continue reading stdin until the delimiter character is reached. If no argument is specified, this method will continue reading until a newline." 
		 * 
		 * @return String   
		 */
		public function stdin(prompt:String, delimiter:String):String { return ""; }

		/**
		 * <p>Print a String to stdout including a trailing
		 * newline.</p>
		 * 
		 * @param data  The data to print. If not a String, it will be converted using the equivalent of String(data); 
		 */
		public function stdout(data:String):void {}

		public function TApp() {}
	}
}