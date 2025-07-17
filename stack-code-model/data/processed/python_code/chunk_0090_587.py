/* Class: URLUtils
 * @author Ryan C. Knaggs
 * @date 02/10/2010
 * @description: Designed to separate
 * the url into manageable information
 */


package utils.strings
{
    public class URLUtils1
    {
        private static const PATTERN:RegExp = /^([A-Za-z0-9_+.]{1,8}:\/\/)?([!-~]+@)?([^\/?#:]*)(:[0-9]*)?(\/[^?#]*)?(\?[^#]*)?(\#.*)?/i;
        private static const KEY:String = "./";
        private var _url:String;
        private var _scheme:String;
        private var _userinfo:String;
        private var _host:String;
        private var _port:String;
        private var _path:String;
        private var _query:String;
        private var _fragment:String;
        
        
        public function listAll():String {
        	var s:String = new String();
        	s+="\nurl -> "+this.url;
        	s+="\nscheme -> "+this.scheme;
        	s+="\nhost -> "+this.host;
        	s+="\npath -> "+this.path;
        	s+="\nport -> "+this.port;
        	s+="\nfragment -> "+this.fragment;
        	s+="\nuserinfo -> "+this.userinfo;
        	
        	for(var i:Object in this.query.parsed) s+="\n"+i+" -> "+this.query.parsed[i];
        	
        	return s;
        }
        
        
        
        /**
         * Create new URL Object
         * @param s The url
         */
         
        public function URLUtils1(url:String):void {
        	
            var result:Array = url.match(PATTERN);
            _url = result[0];      // http://user:pass@example.com:80/foo/bar.php?var1=foo&var2=bar#abc
            _scheme = result[1];   // http://
            _userinfo = result[2]; // user:pass@
            _host = result[3];     // example.com
            _port = result[4];     // :80
            _path = result[5];     // /foo/bar.php
            _query = result[6];    // ?var1=foo&var2=bar
            _fragment = result[7]; // #abc
        }
        
        /**
         * Get the url
         */
        public function get url():String {
        	if(_url is String && _url!=null && _url.length>0) return _url;
	        return new String();
        }
        
        /**
         * Get the scheme
         */
        public function get scheme():String { 
        	if(_scheme is String && _scheme!=null && _scheme.length>0) return _scheme;
	        return new String();
        }
        
        /**
         * Get the userinfo
         * Returns an object containing the user and/or password
         */
         
        public function get userinfo():Object { 
            var ret:Object = {user:undefined,pass:undefined};
            if(_userinfo){
                var arr:Array = _userinfo.substring(0,_userinfo.length-1).split(':');
                ret.user = arr[0]?arr[0]:ret.user;
                ret.pass = arr[1]?arr[1]:ret.pas;
            }
            return ret; 
        }
        
        /**
         * Get the host
         */
        public function get host():String {
            if(_host is String && _host!=null && _host.length>0) return _host;
	        return new String();
        }
        
        /**
         * Get the port
         */
        public function get port():int {
        	
        	if(_port is String && _port != null) return Number(_port.split(":")[1]);
        	return -1;
        }
        
        /**
         * Get the path
         */
        public function get path():String {
        	if(_path is String && _path!=null && _path.length>0) return _path;
            return new String();
        }
        
        /**
         * Get the query
         * Returns an object containing the raw and parsed query string
         */
        public function get query():Object {
            var ret:Object = {raw:undefined,parsed:undefined};
            if(_query && _query.length>0){
                ret.raw = _query;
                var _parse:String = _query.substring(1,_query.length);
                var _intovars:Array = _parse.split("&");
                ret.parsed = _intovars.length>0?{}:undefined;
                for(var i:int=0; i<_intovars.length; i++){
                    var _kv:Array = _intovars[i].split("=");
                    ret.parsed[_kv[0]] = _kv[1];
                }
            }
            return ret; 
        }
        
        /**
         * Get the fragment
         */
         
        public function get fragment():String {
        	if(_fragment is String && _fragment!=null && _fragment.length>0) return _fragment;
	        return new String();
        }
        
        
        
        public function validate(parms:Object,value:String,fileName:String):String {
        	trace("##: "+this._scheme);
        	trace("##: "+this._host);
        	trace("##: "+this._query);
        	
        	// If flashvars then  
        	 
        	if(parms != null) {
  
  				// If flashvar exists, how is it constructed
  				// Does it have a fully qualified path?
  				// Does it have a relitative path?
  				if(parms.value != undefined) {
  					var pv:String = String(parms.value);
  					// if it has a fully qualified path then
  					// return the fully qualifed path
  					// If ://
  					if(pv.indexOf("://") > -1) {
  						return pv;
  					}

					if(pv.indexOf("./") > -1) {
						// If there is a host name, then the SWF is running from a webserver
						// http://127.0.0.1/
						if(this._host != "") {
							trace("##: "+
						}
					}					  					
  					
  					// If ./
  					
  					// If /
  					
  				} else {
  					
  				}
  
  
  
        	}
        	
        	/* If flashvar parameters exist 
        	 * but no value, then return file name
        	 * from GlobalsVO */
        	if(parms.value == null) {
        		trace("1");
        	} else {
        		trace("2");
        	}
        	return "hello";
			//trace("#: "+this.listAll());
        	//var nv:String = new String();
//        	try {
//				if(parms.value == undefined) {
//					nv = "";
//				}
//			} catch(e:Error) {
//					nv = "";
//			}
//			
//			nv = String(value);
//			
//			if(nv is String && nv == "" && nv.length == 0) {
//				trace("Parms Unavailable");
//
//				/* If ./ then find out the path where
//				 * the path of the swf is */				
//				if(fileName.indexOf(KEY) > -1) {
//					
//					/* trace("YES: "+ 	_url.scheme+
//									_url.host+
//									_url.path+
//									_url.fragment); */
//									// + file.substr(file.indexOf(KEY)+KEY.length);
//				}
//				//_url.scheme+_url.host+ file;
//			} else {
//			// Otherwise use FlashVar override
//				//trace("2");
//			}
        }
    }
}