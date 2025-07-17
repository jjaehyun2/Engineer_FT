package com.vyperlogix {
	import flash.net.URLRequestMethod;

	public class GoogleMapsService extends AdHocService {
		private const __address_token__:String = '{{address}}';
		private const __url_geocode__:String = 'http://maps.googleapis.com/maps/api/geocode/json?address='+__address_token__+'&sensor=false';
		
		public function GoogleMapsService() {
			super();
			this.format = GoogleCloudRequestFormat.JSON;
		}

		/**
		 * Returns the user record from the server. The user record has information about the status of the current sesstion including whether or not the user is logged in. 
		 *  
		 */
		public function geocode(address:String):GoogleMapsOperation {
			var url:String = this.__url_geocode__.replace(__address_token__,address);
			var operation:GoogleMapsOperation = new GoogleMapsOperation(url);
			operation.timeout = this.timeout;
			operation.method = URLRequestMethod.POST;
			operation.format = this.format;
			operation.params = {};
			return operation;
		}
	}
}