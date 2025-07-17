package models
{
	import communication.WebServices;
	
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.ProgressEvent;
	import flash.external.ExternalInterface;
	
	import libs.utils.*;
	import libs.vo.ErrorMessagesVO;
	import libs.vo.GlobalsVO;
	
	import mx.containers.Canvas;
	import mx.controls.Image;
	
	import sockets.WebService;
	
	import utils.displayObject.*;
	import utils.objects.ObjectUtils;
	import utils.strings.Strings;
	import utils.strings.URLUtils;
	
	public class LoadExternalData
	{
		private var _progressTracker:Object = {};

		private var _gAssets:Array;
		private var _gCatAssets:Array;
		private var _assetsRemaining:int = 0;
		private var _graphicPreloadContainer:Canvas;
		private var _checkSum:int;
		private var _callBack:Function;
		private var _domain:String;
		private var _prefix:String;
		private var _cb:Boolean;
		private var _versionFile:String;
		
		private var _socketExample:SocketLoadExample;
		
		private var ws:WebService;
		private var _data:Array = [];
			
		private const RANDOMNESS:int = 1000000000;
		private const PROPERTIES:String = "props";
		private const CSSFAULT:String = "onCSSFault";
		private const DELIMITER:String = "?";
		private const UNDEFINED:String = "undefined";
		private const FILEDIVIDER:String = "/";
		private const FILE_NOT_FOUND:String = "404";
		
		
		private const NOVERSIONFILE:int = -100;
		private const NOPROPSFILE:int = -200;
		private const NOCSSFILE:int = -300;
		private const NODATAFILE:int = -400;



		
		private const ERROR_MSG_01:String = "404 - Missing version file: ";
		
		/* Initialize and pass reference 
		 * of the data model to handle */
		private var menuModel:Menu_Model = new Menu_Model();
		
		
		// Used for testing the urls and paths
		private var testvars:Object = new Object();
		
		
		
		
		public function LoadExternalData() {
			
		}
		
		
		
		public function load(overRide:String,callBack:Function):void {
			getGnCategory();
			
			this._domain = String(GlobalsVO.getGlobal(GlobalsVO.APP_URL_DOMAIN));
			this._prefix = String(GlobalsVO.getGlobal(GlobalsVO.APP_URL_PREFIX));
			
			this._callBack = callBack;
			// Process all external vars
			processEvars(overRide);
		}
		
		
		public function getGnCategory():void {
			//GlobalsVO.setGlobal("gnCategory",int(ExternalInterface.call("getgnCategory")));
			//trace("################ gncategory: "+GlobalsVO.getGlobal("gnCategory"));
		}
		
		
		
		/** 
		 * Combine external parameters and
		 * override any repeated external parameters
		 * found in SWFObject flash vars with
		 * the query string parameters
		 */
		 
		public function processEvars(overRide:String):void {
			var processExternalVars:ProcessExternalVars = new ProcessExternalVars();
			
			// Define a global var holding all external vars
			GlobalsVO.setGlobal(GlobalsVO.EXTERNALVARS,processExternalVars.parse(overRide));
			
			
			var isAdmin:Boolean = GlobalsVO.getGlobal(GlobalsVO.ISADMIN);
			
			if(isAdmin) {
				_cb = true;
				// Load the optional properties file
				// BEGIN: This block of code was changed to allow it to work with the Admin Tool as well as the typical production setup...
				var gE:* = GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS);
				var oS:String = GlobalsVO.ORIGIN_SERVER;
				loadProps((gE[oS] != null) ? gE[oS]+GlobalsVO.DEFAULT_PERPERTIES_FILE : gE[GlobalsVO.PROPERTIESFILE]);
				// END!   This block of code was changed to allow it to work with the Admin Tool as well as the typical production setup...				
			
			} else {
				// Get the version file from the Webserver
				loadVersion();
			}
		}
		
		
		
		/**
		 * Load the version file from from
		 * the target Web Server and
		 * compair with the flash var
		 * gn_version to see if the values
		 * match.  If they don't match
		 * then load all files with the
		 * cache buster option to true
		 */
		 		
		private function loadVersion():void {
			this._versionFile = GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS)[GlobalsVO.GN_VERSION];
			// Get the WebServices
			var webService:WebServices = new WebServices();
			webService.getData(_versionFile, onVersion, true);
		}
		
		
		
		/**
		 * If the version file was present and successfully
		 * loaded, then continue onto load the reset of the
		 * data.  Otherwise, If the version file was
		 * not present then stop the application and
		 * display the error message.
		 * 
		 * If the admintool is using this application
		 * and the version file is not present
		 * keep running the application 
		 * @param e
		 */
		 		
		private function onVersion(o:Object):void {
			var cb_F:Boolean = false;
			var currentData:String = "";
			
			if(!o.success) {
				var isAdmin:Boolean = GlobalsVO.getGlobal(GlobalsVO.ISADMIN);
				if (isAdmin == false) {
					GlobalsVO.status = NOVERSIONFILE;
					cb_F = true;
				}
			}
				
			if(o.success) {
				currentData = o.data;
			}
			
			if(cb_F) {
				_cb = true;
			} else {
			/* Set cache buster based on 
			 * external flash vars (Default: False) */
				_cb = Boolean(GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS)[GlobalsVO.CACHEBUSTER]);
			}
			
			
			try {
				var a:String = String(GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS)[GlobalsVO.GN_VERSION_COOKIE]).toLowerCase();
				var b:String = String(currentData).toLowerCase();		// File contents
				
				// Get the Version information and remove the JSONP
				b = String(utils.strings.Strings.crop(b.toString(),"'","'"));
				
				
				trace("Version Content: "+b);
				ExternalInterface.call("setVersionCookie",b);
				
				if(a != b) {
					// Set cache buster
					_cb = true;
				} else {
					_cb = false;
				}
			} catch (e:Error) {
				_cb = true;
			}
			
			// Load the optional properties file
			// BEGIN: This block of code was changed to allow it to work with the Admin Tool as well as the typical production setup...
			var gE:* = GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS);
			var oS:String = GlobalsVO.ORIGIN_SERVER;
			loadProps((gE[oS] != null) ? gE[oS]+GlobalsVO.DEFAULT_PERPERTIES_FILE : gE[GlobalsVO.PROPERTIESFILE]);
			// END!   This block of code was changed to allow it to work with the Admin Tool as well as the typical production setup...
		}
		
		
		
		
		
		/**
		 * Load the optional properties file
		 * @param url
		 */
		 		
		private function loadProps(propsFile:String):void {
			var pp:PropParser = new PropParser();
			var s:String = ''; // ExternalInterface.call("getProperties");
			
			//trace("s: "+s);
			if(s==null || (s.length < 10 && s.indexOf("404") > -1)) {
				
				//trace("I DON'T HAVE PROPERTIES");
				GlobalsVO.setGlobal(PROPERTIES,null);
			} else {
				
				//trace("I HAVE PROPERTIES");
				GlobalsVO.setGlobal(PROPERTIES,pp.parse(s));
				// Testing
				var obj:Object = GlobalsVO.getGlobal(PROPERTIES);
			}
			
			loadCSS();
		}
		
		
		
		/**
		 * Load CSS 
		 */		
		 
		private function loadCSS():void {
			/* Initialize CSS Styles, 
			 * then call the next method (loadDataModel) */
			GlobalsVO.styleManager(loadDataModel);
			
			// Get css File
			var cssFile:String = GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS)[GlobalsVO.CSSFILE]; 
			GlobalsVO.loadStyle(cssFile,_cb);
		}
		
		
		
		
		/**
		 * If the CSS file failed to load 
		 * @param e
		 */
		private function onCSSFault(e:Event):void {
			GlobalsVO.status = NOCSSFILE;
			new ErrorMessages(GlobalsVO.getGlobal(GlobalsVO.APPLICATION),ErrorMessagesVO.ERROR3+GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS)[GlobalsVO.CSSFILE]);
		}
		
		
		
		
		
		
		/**
		 * Load JSON data model 
		 * @param e
		 */
		 		
		private function loadDataModel(e:Event):void {
			// If the CSS file failed
			if(e.type == CSSFAULT) {
				onCSSFault(e);
				return;
			}
			
			GlobalsVO.setGlobal(GlobalsVO.DATA_MODEL, menuModel);
			
			/* After the menu model has finished
			 * reading the data */
			menuModel.addEventListener(Event.COMPLETE, onMenuData);
			menuModel.addEventListener(Event.CANCEL, onMenuDataError);
			/* Get the url that was called to load the data model
			 * and load the data model */
			menuModel.getMenuData();
		}
		
		
		private function onMenuDataError(e:Event):void {
			GlobalsVO.status = NODATAFILE;
			new ErrorMessages(GlobalsVO.getGlobal(GlobalsVO.APPLICATION),GlobalsVO.DATAMODEL_ERROR);
		}
		
		
		
		private function onMenuData(e:Event):void {
			loadGraphics();
		}
		
		
		/**
		 * Check to see if the FlashVar setting
		 * has a cachebusting override
		 * If so, then concatenate a random number
		 * after the query string 
		 * @param str
		 * @return 
		 */
		 		
		private function ckCacheBuster(str:String):String {
			if(Boolean(GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS).cb)) {
				str+=DELIMITER+int(Math.random()*RANDOMNESS);
			}
			
			return str;
		}
		
		
		
		
		
		/**
		 * Check to see if the graphic image
		 * override setting has been set
		 * from the Flashvars, if so then
		 * substitute the override string as
		 * the path to locate and load the images 
		 * @param str origional path and graphic name
		 * @return:String the new URL path or the origional path
		 */
		 
		private function ckImgOverride(str:String):String {
			var overRide:String = String(GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS).img);
			
			// If an image path override exists
			if(overRide != UNDEFINED) {
				var ns:String = new String();
				
				// Check if last character of the override string has a "/"
				if(overRide.substring(overRide.length-1,overRide.length) == FILEDIVIDER) {
					overRide = overRide.substring(0,overRide.length-1);
				} 
			} else {
				return str;
			}
			
			return overRide+FILEDIVIDER+str.substring(str.lastIndexOf(FILEDIVIDER)+1,str.length);
			
		}
		
		
		
		
		
		

		
		
		
		
		
		
		
		/**
		 * Get a list of image names and values
		 * from CSS
		 */
		 
		public function getImageList():Array {
			var arr:Array = new Array();
			var cssProperties:XML = GlobalsVO.getStyleProperties()[0];
			var c:int = 0;
			var l:int = cssProperties.children().length();

			while(c < l) {
				var n:String = cssProperties.child(c).@name;
				if(n.indexOf("image_") > -1) {
					arr.push({name:n, filename:cssProperties.child(c).@value,error:null});
				}
				++c;
			}
			
			/* Return list of image names and values
			 * Array of object */
			return arr;
		}
		
		
		
		
		
		/**
		 * Load all graphics 
		 */
		
			private function loadGraphics():void {

			// Load all graphic assets from CSS name
			_gAssets = getImageList();

			/* Once all the assets have finished 
			 * loading then run the menubar */
			_assetsRemaining = _gAssets.length;

			// Get reference to the application layer
			var app:Object = GlobalsVO.getGlobal(GlobalsVO.APPLICATION);

			// Create a constainer to pre-load the graphics
			_graphicPreloadContainer = new Canvas();
			_graphicPreloadContainer.visible = false;
			app.addChild(_graphicPreloadContainer);

			// Setup initial check sum for graphic sanity check
			_checkSum = _gAssets.length;

			var loader:imgLoader;
			var imgSource:* = '';
			// Loop through all the assets to load
			for(var i:int=0; i<_gAssets.length; ++i) {
				/* If the css can't get the name of the
				 * graphic from the css file, it will return a type undefined
				 * If this happends, replace with a default missing
				 * graphic icon */
				var keys:Array = ObjectUtils.keys(_gAssets[i]);
				if(GlobalsVO.getCSSProperty(_gAssets[i].name) == undefined) {
					checkSum();
					imgSource = GlobalsVO.MissingImage;

					// Store the file reference from the CSS and GlobalsVO
					_gAssets[i].filename = _gAssets[i].name.toString();
					_gAssets[i].error = ErrorMessagesVO.ERROR1 +_gAssets[i].filename;
				} else {
					// If development
					if(_domain == "." || _domain == "" || _domain == null) {
						// Load all graphics with cachebuster or not
						imgSource = ckCacheBuster(ckImgOverride(_gAssets[i].filename));
					} else {
						try {
							var __domain:String = URLUtils.domain_with_port_and_protocol(_gAssets[i].filename);
							if (__domain.indexOf('://') == -1) {
								var e:Object = GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS);
								imgSource = FilterURL.filter(e.img,_gAssets[i].filename);
							} else {
								imgSource = _gAssets[i].filename;
							}
						} catch (e:Error) {
						}
					}

				}
				loader = new imgLoader(imgSource,_gAssets[i],this.onImageLoaded_handler);
			}
		}

		

		private function onImageLoaded_handler(image:*):void {
			
			var img:Image = DuplicateImage.copy(image.image,true,true);
			//trace("onImageLoade_handler: "+image);
			try {
				// Create a new child for the preload container
				if (image.container != null) {
					_graphicPreloadContainer.addChild(image.container.image = img);
	
					// Set the current image into global assets
					GlobalsVO.setGlobal(image.container.name,image.container);
				}
			} catch (e:Error) {}
			checkSum(); // this ensures this function fires at-least once per image so long as any progress was detected for that image regardless of whether or not all the expected bytes were actually received.
		}



		
		 		
		
		/**
		 * Verify that the graphic has really loaded
		 * If so, then set the _checkSum minus 1 
		 * @param e
		 */
		 		
		public function onProgress(e:ProgressEvent):void {
			if (GlobalsVO.DEVMODE) {
				// BEGIN:  The checkSum() function MUST fire for every single image or bad evil things may happen, such as no menu appears ever !
				if (this._progressTracker[e.currentTarget.source] == false) {
					this._progressTracker[e.currentTarget.source] = true;
					checkSum(); // this ensures this function fires at-least once per image so long as any progress was detected for that image regardless of whether or not all the expected bytes were actually received.
				}
				// END!    The checkSum() function MUST fire for every single image or bad evil things may happen, such as no menu appears ever !
			} else {
				if(e.bytesLoaded == e.bytesTotal) checkSum(); 
			}
		}
		
		
		/**
		 * If the graphic file is missing
		 * or the filename is incorrect 
		 * @param e
		 */
		 
		public function onFault(e:IOErrorEvent):void {
			for(var i:int = 0; i<_gAssets.length; ++i) {
				if(_gAssets[i].image.toString() == e.currentTarget.toString()) {
					_gAssets[i].error = ErrorMessagesVO.ERROR2 + _gAssets[i].filename;
				}
			}
			checkSum();
		}
		
		
		
		
		
		/**
		 * The check sum checks to see
		 * if all the graphics have loaded 
		 */
		 		
		public function checkSum():void {
			if(--_checkSum == 0) {
				/* If logged in state then
				 * process category images before
				 * application ready state */
				if(!GlobalsVO.ISLoggedOut) {
					getCatAssets();
				} else {
					//trace("#### ready");
					// Logged out state application ready
					_callBack(new Event(Event.COMPLETE));
				}
				
			
			}
		}
		
		
		
		/**
		 * Find the category images in _gAssets
		 * then process the images into a new array
		 * of category images
		 */
		 		
		public function getCatAssets():void {
			_gCatAssets = new Array();
			for(var i:int = 0; i<_gAssets.length; ++i) {
				if(_gAssets[i].name.toString().toLowerCase().indexOf("image_catb")>-1) {
					processCatAssets(i);
					return;
				}
			}
		}
		
		
		
		
		/**
		 *  
		 * @param i
		 * 
		 */
		 		
		public function processCatAssets(i:int):void {
			for(;i<_gAssets.length;i+=3) {	
				var obj:Object = new Object();
				for(var a:int = 0; a<3; ++a) {
					obj["button_"+a] = _gAssets[i+a];
				}
				_gCatAssets.push(obj);
			}
			
			/* Store just the category Images
			 * into a new array for the logged in state
			 * to display the categories as images */
			GlobalsVO.setGlobal("categoryImages",_gCatAssets);
			
			
			_callBack(new Event(Event.COMPLETE));
		}
	}
}