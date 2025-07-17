/*
 * Copyright (c) 2011 Vyper Logix Corp., All Rights Reserved.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */
package com.vyperlogix {
    import flash.net.InterfaceAddress;
    import flash.net.NetworkInfo;
    import flash.net.NetworkInterface;
    import flash.net.URLRequestMethod;
    import flash.system.Capabilities;
    
    import mx.core.FlexGlobals;
    
    /**
     * Service which uses the Foursquare API.
     */
    public class GoogleCloudService {
		/**
		 * domain name.
		 */
		public static var domain:String = "";
		
		/**
		 * air_id for the Django Framework.
		 */
		public static var air_id:String = "";
		
		/**
		 * sub-domain name.
		 */
		public static var sub_domain:String = "";
		
		/**
		 * domain symbol.
		 */
		private static var domain_symbol:String = "{{domain}}";
		
		/**
		 * Local URL prefix to use for REST calls.
		 */
		public var url_local:String = "http://127.0.0.1:9000";
		
		/**
		 * Remote URL prefix to use for REST calls.
		 */
		public var url_remote:String = "https://"+domain_symbol+".appspot.com";
		
        /**
         * URL prefix to use for REST calls.
         */
        public var url:String;
        
        /**
         * The request format. <code>FoursquareRequestFormat.XML</code> or <code>FoursquareRequestFormat.JSON</code>.
         * 
         * @default <code>FoursquareRequestFormat.JSON</code>
         */
        public var format:String = GoogleCloudRequestFormat.JSON;
        
        /**
         * Request timeout in seconds. Value of -1 indicates no timeout.
         * 
         * @default -1
         */
        public var timeout:Number = -1;
		
		public function GoogleCloudService():void {
			var isDebugger:Boolean = false;
			try {isDebugger = FlexGlobals.topLevelApplication.app.isDebugger} 
				catch (err:Error) {
					try {isDebugger = FlexGlobals.topLevelApplication.isDebugger} catch (err:Error) {}
				}
			this.url = (isDebugger) ? this.url_local : this.url_remote;
			this.url = this.url.replace(domain_symbol,domain);
		}
        
		/**
		 * Return the ip address.
		 * 
		 */
		public function get ip_address():String {
			var interfaces:Vector.<NetworkInterface> = new Vector.<NetworkInterface>();
			interfaces = NetworkInfo.networkInfo.findInterfaces();

			var bucket:Array = [];
			
			for each (var netf:NetworkInterface in interfaces) {
				if (netf.active) {
					var addresses:Vector.<InterfaceAddress> = netf.addresses;
					for each(var interfaceAddress:InterfaceAddress in addresses) {
						if (interfaceAddress.ipVersion == 'IPv4') {
							bucket.push(interfaceAddress.address);
						}
					}
				}
			}
			bucket.sort();
			var i:int = bucket.indexOf('127.0.0.1');
			i = ((i > -1) ? i : 0);
			return bucket[i];                                      
		}
		
        /**
         * Returns the user record from the server. The user record has information about the status of the current sesstion including whether or not the user is logged in. 
         * 
         */
        public function get_user(geo:*=null):GoogleCloudOperation {
            var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/get/user/", {geo:geo}, air_id, sub_domain);
            operation.timeout = this.timeout;
            operation.method = URLRequestMethod.POST;
			operation.format = this.format;
            return operation;
        }
        
        /**
         * Perform a user login.
         * 
         * @param username string
         * @param password string
         */
        public function login(username:String, password:String,geo:*=null):GoogleCloudOperation {
            var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/login/user/", {username:username,password:password,geo:geo}, air_id, sub_domain);
            operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
            return operation;
        }
        
		/**
		 * Perform a user logout.
		 * 
		 */
		public function logout():GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/logout/user/", {}, air_id, sub_domain);
			operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
			return operation;
		}
		
		/**
		 * Perform a send email.
		 * 
		 * @param fromName string
		 * @param email string
		 */
		public function send_email(fromName:String, email:String):GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/send/email/", {fromName:fromName, email:email}, air_id, sub_domain);
			operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
			return operation;
		}
		
		/**
		 * Perform an adhoc send email.
		 * 
		 * @param from string
		 * @param to string
		 * @param subject string
		 * @param body string
		 */
		public function send_adhoc_email(_from:String,_to:String,_subject:String,_body:String):GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/send/email/", {from:_from,to:_to,subject:_subject,body:_body}, air_id, sub_domain);
			operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
			return operation;
		}
		
		/**
		 * Register a user.
		 * 
		 * @param username string
		 * @param password string
		 * @param password2 string
		 */
		public function register(username:String, password:String, password2:String):GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/register/user/", {username:username, password:password, password2:password2}, air_id, sub_domain);
			operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
			return operation;
		}
		
		/**
		 * Activate a user.
		 * 
		 * @param username string
		 * @param activation_key string
		 */
		public function activate(username:String, activation_key:String):GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/activate/", {username:username, activation_key:activation_key}, air_id, sub_domain);
			operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
			return operation;
		}
		
		/**
		 * Re-Activate a user.
		 * 
		 * @param username string
		 */
		public function reactivate(username:String):GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/reactivate/", {username:username}, air_id, sub_domain);
			operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
			return operation;
		}
		
		/**
		 * Change a user password.
		 * 
		 * @param username string
		 */
		public function chgpassword(username:String, password:String, password2:String):GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/chgpassword/", {username:username, password:password, password2:password2}, air_id, sub_domain);
			operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
			return operation;
		}
		
		/**
		 * Send an EMail.
		 * 
		 * @param username string
		 */
		public function sendemailto(from:String, to:String, msg:String):GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/sendemailto/", {from:from, to:to, msg:msg}, air_id, sub_domain);
			operation.timeout = timeout;
			operation.format = this.format;
			operation.method = URLRequestMethod.POST;
			return operation;
		}
		
		/**
		 * Returns an admob advert. 
		 * 
		 */
		public function get_admob(pub_id:String,site_id:String=null,is_test:Boolean=true):GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/get/admob/", {admob_site_id:pub_id,admob_siteID:site_id,admob_mode:((is_test) ? 'test' : null)}, air_id, sub_domain);
			operation.timeout = this.timeout;
			operation.method = URLRequestMethod.POST;
			operation.format = this.format;
			return operation;
		}
		
		/**
		 * Returns an smaato advert. 
		 * 
		 */
		public function get_smaato():GoogleCloudOperation {
			var operation:GoogleCloudOperation = new GoogleCloudOperation(this.url + "/get/smaato/", {}, air_id, sub_domain);
			operation.timeout = this.timeout;
			operation.method = URLRequestMethod.POST;
			operation.format = this.format;
			return operation;
		}
  }
}