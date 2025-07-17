/*
 * Class: Menu_Model (Data Model)
 * @author Ryan C. Knaggs
 * @since 1.0
 * @date 08/14/2009
 * @version 1.21 - RCK
 * @version 1.22 - Enhanced the getURL method
 * @date 11/19/2009
 * @description: This class object will access
 * and store the MenuBar JSON data.  Then
 * will send out an event to any other view
 * class objects for update purposes 
 */

package models
{
	import communication.WebServices;
	
	import flash.events.*;
	
	import libs.utils.ErrorMessages;
	import libs.utils.ExtendedChars;
	import libs.vo.GlobalsVO;
	
	import mx.collections.ArrayCollection;
	import mx.rpc.events.FaultEvent;
	
	import utils.strings.Strings;


	public class Menu_Model extends EventDispatcher
	{
		
		private var _menuData:Object;
		private var _metaData:Object;
		private var _headerData:Object;
		private var _metaDomain:Object;
		private var _metaDomainKey:Object;
		private var _url:String;
		private var _uuid:Object;
		
		private var _callback:Function;

		private const URL:String = "dataURL";
		private const PROPERTIES:String = "props";
		private const EXTERNALVARS:String = "externalVars";
		private const MBC:String = "MenuBarContainer";
		private const exceptions:ArrayCollection = new ArrayCollection(['secureDefault','vOrientation','hOrientation'])
		
		/**
		 * Constructor
		 */
		 
		public function Menu_Model() {
		}
		
		
		
		
		/**
		 * Call the WebServices to get the data
		 * for the data grid.  The Model should
		 * only get the data, access the encapsulated WebServices Class
		 */
		
		public function getMenuData(url:String=null,callback:Function=null):String {
			this._callback = callback;
			
			try {
				var mcr:Object = GlobalsVO.getGlobal("MenuController");
				mcr.deleteAndRemoveAllMenuChildren();
			} catch (e:Error) {}
			
			var domain:String = String(GlobalsVO.getGlobal(GlobalsVO.APP_URL_DOMAIN));
			var prefix:String = String(GlobalsVO.getGlobal(GlobalsVO.APP_URL_PREFIX));

			/* Assemble new URL for the data model, then, 
			 * If Cache Buster is true */
			
			_url = (url) ? url : GlobalsVO.getGlobal(EXTERNALVARS)[GlobalsVO.DATAFILE];				


			//new WebServices().getData(_url ,new JSONParser(onData,onFault),GlobalsVO.getGlobal(EXTERNALVARS)[GlobalsVO.CACHEBUSTER],callback);

			//trace("load data _url: "+_url);
			var ws:WebServices = new WebServices();
			ws.getData(_url,onReturn,GlobalsVO.getGlobal(EXTERNALVARS)[GlobalsVO.CACHEBUSTER]);
			
			// Access the web service for the new JSON data model 
			
			return _url;
		}


		private var initalLoadSuccess:Boolean = true;

		/**
		 * onReturn 
		 * @param o - Returned object from Webservices
		 * If o.success is true the data was
		 * successfully loaded.  False no data.
		 * 
		 */		
		public function onReturn(o:Object):void {
			
			if(!initalLoadSuccess) return;
			
			if(!o.success) {
				GlobalsVO.DATAMODEL_ERROR = "ERROR: 404 - Data model failed to load: "+_url;
				initalLoadSuccess = false;
				dispatchEvent(new Event(Event.CANCEL));
				return;
			}
				
			if(o.success) {
				var jsp:JSONParser = new JSONParser();
				//trace('### jsp.parse json='+o.data);
				jsp.parse(o.data,onData);
			}
			
			if (this._callback is Function) {
				this._callback(o);
			}
		}
		

		/**
		 * Returned data from the selected parser 
		 * @param obj - Data object that contains all
		 * information about the menu data model
		 */
		 		
		private function onData(data:Object):void {
			
			if(data == null) return;
			//var hello:Object = data.data.datafield;
			//trace("hello: "+hello);
			data = data.data;

			/* Get static constant for the field names 
			 * to look for in the data model to separate 
			 * the menu data from the meta data */
			 
			_menuData = {name:data[GlobalsVO.DATAFIELD],data:data[data[GlobalsVO.DATAFIELD]]};
			_metaData = {name:data[GlobalsVO.METAFIELD],data:data[data[GlobalsVO.METAFIELD]]};
			_headerData = {name:data[GlobalsVO.HEADERFIELD],data:data[data[GlobalsVO.HEADERFIELD]]};
			_metaDomain = {data:data[GlobalsVO.META_DOMAIN]};
			_metaDomainKey = {data:data[GlobalsVO.META_DOMAIN_KEY]};
			_uuid = {data:data[GlobalsVO.UUID]};
			
			// BEGIN:  This block of code makes it a bit easier to go from a non-human readable back to human readable... 
			_metaData.hash = {};
			var o:Object;
			for (var i:String in _metaData.data) {
				o = _metaData.data[i];
				for (var k:String in o) {
					if (this.exceptions.getItemIndex(k) > -1) {
						_metaData.hash[k] = o[k];
					} else { // this opens the door to the other way of looking at this data in case this ever becomes necessary...
						_metaData.hash[k] = o[k];
					}
				}
			}
			// END!  This block of code makes it a bit easier to go from a non-human readable back to human readable... 
			// Dispatch a load ready event
			dispatchEvent(new Event(Event.COMPLETE));
		}
		


		/**
		 * If Global Navigation Data Model
		 * JSON file is missing
		 */
		private function onFault(e:FaultEvent):void {
			/* Call the Error_View class and
			 * display the error message */
			 new ErrorMessages(GlobalsVO.getGlobal(GlobalsVO.APPLICATION),e.type+": "+_url);
			 dispatchEvent(new Event(Event.CANCEL));
		}
		
		
		
		/**
		 * Get the domain name object
		 * that is used in conjunction
		 * with the metaDomainKey
		 * @return 
		 */
		 		
		public function get metaDomain():Object {
			return _metaDomain;	
		}
		
		
		
		/**
		 * Get the domain key meta data object
		 * to lookup the correct URL for the
		 * Navigation
		 * @return - Domain Key 
		 */
		 
		public function get metaDomainKey():Object {
			return _metaDomainKey;	
		}
		
		
		
		
		/**
		 * Get the menu data array of objects 
		 * @return 
		 */
		 		
		public function get menuData():Object {
			return _menuData;
		}
		
		
		/**
		 * Get the menu uuid 
		 * @return 
		 */
		 		
		public function get uuid():Object {
			return _uuid;
		}
		
		
		
		
		/**
		 * Return meta data 
		 * @return 
		 */
		 		
		public function get metaData():Object {
			return _metaData;
		}
		
		
		
		/**
		 * Return header data 
		 * @return 
		 */
		 		
		public function get headerData():Object {
			return _headerData;
		}
		
		
		
		
		/**
		 * Get the value from the meta data item 
		 * @param name
		 * @return 
		 */
		 
		public function getMetaDataValue(name:String):* {
			
			// Get reference of symbol
			for(var item:Object in _metaData.data) {
				if(_metaData.data[item][name]!= null) {
					return _metaData.data[item][name];
				}
			}
			
			return null;
		}
		
		
		
		
		/**
		 * Get the metaData value 
		 * @param name
		 * @return 
		 * 
		 */		
		public function getMetaDataHash(name:String):* {
			return _metaData.hash[name];
		}
		
		
		
		
		
		/**
		 * Accessed by different class object's for
		 * getting the domain data when the file is compressed
		 * @param index
		 * @param keyName
		 * @return 
		 */
		 		
		public function getMetaDomain(index:int=-1,keyName:String=null):String {
			return _metaDomain.data[index];
		}
		
		
		
		
		
		/**
		 * Construct a new url for the category and menu items
		 * if domain key (aka. k) is a number then
		 * access the meta_domain_key for the value
		 *
		 * if properties file exists
		 * 		lookup the domain name from the meta_domain_key
		 * 			otherwise if properties file DOES NOT EXIST then
		 * 			access the "domain" (aka. d) for the number then
		 * 			Look up the meta_domain by the number and get the domain
		 * @param data:Object - The Current category or menuitem data object
		 * @return protocol + domain + path : String
		 */		
		 
		public function getUrl(data:Object):String {
			// Set the protocol		
			var protocol:String;
			var i_secure:int = (data != null) ? int(data[getMetaDataValue(GlobalsVO.META_SECURE)]) : 0;
			protocol = (i_secure==0) ? GlobalsVO.DEFAULT_PROTOCOL : GlobalsVO.SECURE_PROTOCOL;
			
			// Get the domain
			var domainName:String;
			var keyRef:String = (data != null) ? String(data[getMetaDataValue(GlobalsVO.DOMAIN_KEY)]) : "-1";
			
			// If there is a properties file
			var b_keyRef:Boolean = Strings.isStringNumeric(keyRef);
			domainName = (b_keyRef) ? getDomainFromProperties(_metaDomainKey.data[keyRef]) : getDomainFromProperties(keyRef);
			// If no properties file found, get the domain reference from the data model file
			if(domainName == null) {
				var domainRef:String = (data != null) ? String(data[getMetaDataValue(GlobalsVO.META_DOMAIN_INDEX)]) : "-1";
				domainName = '';
				if (int(domainRef) > -1) {
					//trace('###.1 domainRef='+domainRef);
					var b_domainRef:Boolean = Strings.isStringNumeric(domainRef);
					//trace('###.2 b_domainRef='+b_domainRef);
					domainName = (b_domainRef) ? this._metaDomain.data[domainRef] : domainRef;
					//trace('###.3 domainName='+domainName);
					domainName = ((domainName is String) && (domainName.length > 0)) ? domainName : '';
					//trace('###.4 domainName='+domainName);
				} else {
					var i:int = -1;
				}
			} else if ( (domainName.indexOf(GlobalsVO.DEFAULT_PROTOCOL) > -1) || (domainName.indexOf(GlobalsVO.SECURE_PROTOCOL) > -1) ) {
				protocol = ''; // sometimes the protocol can be supplied by the domainName... 
			}

			// Return protocol + domainName + path
			var s_url:String = (data != null) ? data[getMetaDataValue(GlobalsVO.META_URL)] : '';
			var showTraces:Boolean = true; //( (s_url is String) && (s_url.length > 0) && (s_url.indexOf('www.google.com') > -1) );
			if (showTraces) {
				//trace('###.5 protocol='+protocol);
				//trace('###.6 domainName='+domainName);
				//trace('###.7 s_url='+s_url);
			}
			var isDomainNameString:Boolean = (domainName is String) && (domainName.length > 0);
			var isUrlString:Boolean = (s_url is String) && (s_url.length > 0);
			var doesDomainNameHaveNoProtocol:Boolean = (!isDomainNameString) || ( (isDomainNameString) && (domainName.indexOf('://') == -1) );
			var doesUrlHaveNoProtocol:Boolean = (!isUrlString) || ( (isUrlString) && (s_url.indexOf('://') == -1) );
			var url:String = ((doesDomainNameHaveNoProtocol) && (doesUrlHaveNoProtocol) ? protocol : '') + (((domainName is String) && (domainName.length > 0)) ? domainName : '') + s_url;
			if (showTraces) {
				//trace('###.8 isDomainNameString='+isDomainNameString);
				//trace('###.9 isUrlString='+isUrlString);
				//trace('###.10 doesDomainNameHaveNoProtocol='+doesDomainNameHaveNoProtocol);
				//trace('###.11 doesUrlHaveNoProtocol='+doesUrlHaveNoProtocol);
			}
			//if ( (showTraces) || (url.indexOf('http://http://') == -1) ) {
			if (url.indexOf('http://http://') > -1) {
				//trace('###.12 url='+url);
			}
			return url;
		}
		
		
		
		
		
		/**
		 * Get the domain from the properties
		 * file by the key name 
		 * @param keyName
		 * @return 
		 */
		 
		private function getDomainFromProperties(keyName:String):String {
			
			/* If the properties file exists
			 * then get this key and props file
			 * for domain name */
			 
			var props:Object = GlobalsVO.getGlobal(PROPERTIES);
			if(props != null) {
				for(var i:Object in props) {
					//trace("props[i].name: "+props[i].name);
					if(props[i].name == keyName) {
						var domainName:String = props[i].value;
						return domainName;
					}
				}
			}
			
			return null;
		}
		
		
		
		
		
		/**
		 * Get the header data and repackage it
		 * back into an array
		 * @param name
		 * @param htmlFilter:Boolean - Default: False
		 * 		If false do not apply the regular expression
		 * 		to search and replace non-standard HTML Extended
		 * 		character set symbols
		 * 		If true, search and replace any non-standard
		 * 		HTML symbols
		 * 
		 * @return headerData:Array 
		 */
		
		public function getHeaderData(name:String,htmlFilter:Boolean=false,isAdmin:Boolean=false):Array {
			
			//trace("getHeaderData: "+ name);
			var arr:Array = new Array();
			var data:Array = new Array();
			
			var aaa:* = _headerData.data;
			
			
			/* Look for the data based on the
			 * header feature */
			for(var i:Object in _headerData.data) 
				if(i.toString().toLowerCase() == name.toLowerCase()) {
					var headerData:* = _headerData.data[i.toString()][_headerData.name];
					if(headerData is Array) {
						arr = headerData;
					} else {
						arr = [];
						arr.push(headerData);
					}
				}
			
			if (isAdmin || name=="welcome" || name=="home" || name=="logout") {
				data = arr;
			} else {
				// Filter any extra escaped characters
				for(var a:int=0;a<=arr.length-1; ++a) {
					try {
						var target:* = arr[a][_metaData.hash[GlobalsVO.META_TARGET]];
	 						if(target == undefined) {
							target = _metaData.hash[GlobalsVO.TARGET_DEFAULT];
						}
						
						var label:String = arr[a][_metaData.hash[GlobalsVO.META_LABEL]].toString();
						data.push({name:!htmlFilter ? label : 
						new ExtendedChars().convertHTML(label), 
						value:this.getUrl(arr[a]),target:target});
						
					} catch(e:Error) {
						data.push({name:null,target:target, value:this.getUrl(arr[a])});	
					}
				}
			}
			
			return data;
		}
	}
}