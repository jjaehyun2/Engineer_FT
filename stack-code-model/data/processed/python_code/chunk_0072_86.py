package libs.utils
{
	
	
	import libs.vo.GlobalsVO;
	
	import utils.strings.*;
	
	public class FilterURL
	{
		public function FilterURL()
		{
		}
		
		private static const STR1:String = "%5B%5BDYNAMIC%5D%5D/1";
		private static const STR2:String = "[[DYNAMIC]]/1";
		
		
		public static function filter(url:String, fileName:String):String {
			var _url:String = url;
			var domain:String = utils.strings.URLUtils.domain_with_port_and_protocol(_url);
			var prefix:String = utils.strings.URLUtils.url_prefix_sans_domain_name_and_protocol(_url);

			if ( (domain == null) || ((domain is String) && (domain.length == 0)) ) {
				domain = String(GlobalsVO.getGlobal(GlobalsVO.APP_URL_DOMAIN));
				prefix = String(GlobalsVO.getGlobal(GlobalsVO.APP_URL_PREFIX));
			}
			prefix += (prefix.charAt(prefix.length-1) == '/') ? '' : '/';
			if (fileName.indexOf('./') > -1) {
				_url = fileName.replace('./',domain+prefix);
			} else {
				_url = domain+prefix+((prefix.substr(prefix.length-1,1) == '/') ? '' : '/')+fileName;
			}

			return _url; 
		}


		
		
		
		public static function filter1(url:String):String {
			return analyze_or_rebuild_url(url,1);
		}




		private static function analyze_or_rebuild_url(bar:String,method:int=1):String {
			var _bar:String = bar;
			var toks:Array = bar.split("?");
			
			bar = toks[0];
			
			try {
				// Remove the extra characters from the URL
				bar = bar.replace(STR1,"").replace(STR2,"");
			} catch(e:Error) {
				//trace("ERROR 1: analyze_or_rebuild_url: "+e.message + e.getStackTrace());
			}
			
			// Split up the URL by "/"
			toks = bar.split("/");
			
			// If the ".swf" was found then remove it from the array
			if (toks[toks.length-1].toLowerCase().indexOf('.swf') > -1) {
				toks.pop();
			}
			
			// BEGIN: normalize the URL even when the 
			// framework has been split from the app.
			var _found:int = -1;
			for (var i:String in toks) {
				try {
					if (toks[i] is String) {
						if (toks[i].toLowerCase().indexOf('.swf') > -1) {
							_found = int(i);
							break;
						}
					}
				} catch(e:Error) {
					//trace("ERROR 2: analyze_or_rebuild_url: "+e.message + e.getStackTrace());
				}
			}
			if (_found > -1) {
				toks.splice(_found,1);
			}
			
			// END! normalize the URL even when 
			// the framework has been split from the app.
			_bar = bar = toks.join('/');						
			
			if (method == 2) {
				var domain:String = utils.strings.URLUtils.domain_with_port_and_protocol(bar);
				var prefix:String = utils.strings.URLUtils.url_prefix_sans_domain_name_and_protocol(bar);
				
				if ( (domain is String) && (domain.length > 0) && (domain == '.') ) {
					bar = bar.replace(domain, "");
				} else {
					if(domain is String && domain.length > 0) {
						bar = bar.replace(domain, "");
					}
					if(prefix is String && prefix.length > 0) {
						bar = bar.replace(prefix, "");
					}
				}
				_bar = bar;
			}
			return _bar;
		}
	}
}