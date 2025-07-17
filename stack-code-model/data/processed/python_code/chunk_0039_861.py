package dom.tidesdk.network
{
	/**
	 * <p>An object representing a single HTTP server
	 * request.</p>
	 */
	public class THTTPServerRequest
	{
		//
		// METHODS
		//

		/**
		 * <p>the content length of this request</p>
		 * 
		 * @return Number   
		 */
		public function getContentLength():Number { return 0; }

		/**
		 * <p>get the content type of this request</p>
		 * 
		 * @return String   
		 */
		public function getContentType():String { return ""; }

		/**
		 * <p>get an HTTP header value from this request</p>
		 * 
		 * @param header  the header of the request 
		 * 
		 * @return String   
		 */
		public function getHeader(header:String):String { return ""; }

		/**
		 * <p>get an HTTP header value from this request</p>
		 * 
		 * @return String   
		 */
		public function getHeaders():String { return ""; }

		/**
		 * <p>get the HTTP method of this request</p>
		 * 
		 * @return String   
		 */
		public function getMethod():String { return ""; }

		/**
		 * <p>get the URI of this request</p>
		 * 
		 * @return String   
		 */
		public function getURI():String { return ""; }

		/**
		 * <p>get the HTTP version of this request</p>
		 * 
		 * @return String   
		 */
		public function getVersion():String { return ""; }

		/**
		 * <p>check to see if this request has an HTTP
		 * header</p>
		 * 
		 * @param header  the header of the request to check 
		 * 
		 * @return Boolean   
		 */
		public function hasHeader(header:String):Boolean { return false; }

		/**
		 * <p>read content from this request</p>
		 * 
		 * @param length  the number of bytes to read (default 8096) 
		 * 
		 * @return String   
		 */
		public function read(length:Number=0):String { return ""; }

		public function THTTPServerRequest() {}
	}
}