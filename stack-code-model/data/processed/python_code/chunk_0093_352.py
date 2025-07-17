/*
 * Static Class:Globals.as
 * @author Ryan C. Knaggs
 * @date 10/1/2009
 * @description: 
 * 1) Designed to store any type of object
 * for application scope
 * 2) Read an external CSS file for 
 * application configuration
 */

package libs.vo
{
	import flash.events.Event;
	
	import mx.core.UIComponent;
	import mx.events.ResizeEvent;
	
	import utils.css.CSSLoader;
	import utils.strings.Strings;
	import utils.window.OutputWindow;
	import flash.external.ExternalInterface;
	
	
	
	public class GlobalsVO extends UIComponent
	{
		
		public static var bStart:int = 0;
		public static var benchMark:int = 0;
		
		
		public static const VERSION:String = "Global Navigation 1.0.029.6";
		public static const APP_URL_DOMAIN:String = "domain";
		public static const APP_URL_PREFIX:String = "prefix";
		
		// Default Frames Per Second
		public static const DEFAULT_FPS:int=30;
		
		/* Display the optional diagnostics
		 * output window */
		private static var diagnosticsWindow:Object;
		
		/* If all loaded files have successfully loaded 
		 * then set this to true.  If the application
		 * is has dependence on something from one
		 * of the files, then check to make sure that
		 * everything is ok otherwise throw an error message */
		public static var ALLSYSTEMSGO:Boolean = false;
		public static var DATAMODEL_ERROR:String = "";
		/* Designed to allow the developer test
		 * the application from the flex developement
		 * enviornment or production */
		public static var DEVMODE:Boolean = false;

		public static var ISLoggedOut:Boolean = false; // when true this is the logged out case otherwise the logged in case...
		
		/* Used to switch on the diagnostics model 
		 * for displaying trace output information */
		public static var DIAG:Boolean = false;
		public static var DIAG_WINDOW_X:Number = 50;
		public static var DIAG_WINDOW_Y:Number = 200;
		
		// Main object container for all dynamic references
		private static var _global:Object;
		
		/* Missing Graphic Symbol
		 * This is required in case the graphics
		 * from the server don't load */
		[Embed(source="/assets/MissingGraphic.gif")]
		[Bindable] 
		public static var MissingImage:Class;
		
		[Embed(source="/assets/TextCursor.gif")]
		[Bindable] 
		public static var TextCursor:Class;

		// CSS
		private static var _onStyleLoaded:Function;
		private static var _cssStyleCount:Number = 0;
		private static const VALIDCSS:String = "image_arrowLNAsset";
		
		// Main application reference
		public static const APPLICATION:String = "Application";

		public static const APPLICATION_GUI:String = "Application_GUI";

		public static const WMS_KEEPALIVE:String = "Wms_Keepalive";
		
		// Main application reference
		public static const ISADMIN:String = "IsAdmin";
		public static const ISWMSDEV:String = "IsWmsDev";
		public static const ISDEBUGGING:String = "IsDebugging";
		public static const USERID:String = "UserId";
		public static const EDITABLELABEL_onClickHandler:String = 'EDITABLELABEL_onClickHandler';
		public static const EDITABLELABEL_onCreationComplete:String = 'EDITABLELABEL_onCreationComplete';
		public static const NONEDITABLELABEL_onCreationComplete:String = 'NONEDITABLELABEL_onCreationComplete';
		public static const EDITABLEICON_onClickHandler:String = 'EDITABLEICON_onClickHandler';
		public static const EDITABLEICON_onCreationComplete:String = 'EDITABLEICON_onCreationComplete';
		public static const EDITABLELOGOICON_onCreationComplete:String = 'EDITABLELOGOICON_onCreationComplete';
		public static const EDITABLELOBICON_onCreationComplete:String = 'EDITABLELOBICON_onCreationComplete';
		public static const EDITABLEGLINKS_onCreationComplete:String = 'EDITABLEGLINKS_onCreationComplete';
		public static const EDITABLELOCATION_onCreationComplete:String = 'EDITABLELOCATION_onCreationComplete';
		public static const EDITABLEHOUSEICON_onCreationComplete:String = 'EDITABLEHOUSEICON_onCreationComplete';
		public static const EDITABLESIGNOUTICON_onCreationComplete:String = 'EDITABLESIGNOUTICON_onCreationComplete';
		public static const EDITABLESEARCHICON_onCreationComplete:String = 'EDITABLESEARCHICON_onCreationComplete';
		
		// name of the data model
		public static const DATA_MODEL:String = "menuModel";
		
		public static const DOMAINS_MODEL:String = "domainsModel";
		
		// Name of JavaScript interface
		public static const JSINTERFACE:String = "JSINTERFACE";
		
		public static var USERNAME:String = 'UNDEFINED';
		
		// JSInterface Functions
		public static const JSKEYBOARD:String = "keyboard";		// JS keyboard listener
		public static const TOJS:String = "fromFlex";				// To JS function used for actions and other messages
		public static const FROMJS:String = "toFlex";			// Call Flex method from JS for actions and other messages
		public static const FLEXSTATUS:String = "flexStatus";	// Send flex status messages to JS
		public static const FLEXREADY:String = "flexReady";
		public static const TABOUT:String = "tabOut";
		public static const TALK:String = "talk";
		
		
		
		/* The JSON data model will need to have
		 * two main static names to define where
		 * the menu data and meta data exists */		
		public static const DATAFIELD:String = "datafield";
		public static const METAFIELD:String = "metafield";
		public static const HEADERFIELD:String = "headerfield";
		public static const UUID:String = "uuid";
		
		/* JSONP Filter */
		public static const JSONP_1:String = "xhr.fetchversion('";
		public static const JSONP_2:String = "')";
		
		/* The JSON data model will have meta tags
		 * that will be used to access the data
		 * then the body of the JSON data model
		 * meta data defination tags should not be
		 * altered */
		public static const META_LABEL:String = "label";
		public static const META_URL:String = "url";
		public static const META_BODY:String = "body";
		public static const META_TARGET:String = "target";
		public static const META_V_ORIENTATION:String = "vOrientation";
		public static const META_H_ORIENTATION:String = "hOrientation";
		public static const META_TYPE:String = "type";
		public static const META_DOMAIN:String = "meta_domain";
		public static const META_DOMAIN_INDEX:String = "domain";
		public static const META_DOMAIN_KEY:String = "meta_domain_key";
		public static const META_SECURE:String = "secure";
		public static const DOMAIN_KEY:String = "domain_key";
		

		// Used for setting up a url with the proper protocol
		public static const DEFAULT_PROTOCOL:String = "http://";
		public static const SECURE_PROTOCOL:String = "https://";
		
		// Used for sanity check for building a new url
		public static const IS_PROTOCOL:String = "://";
		
		// Default page type
		public static const PAGE_TYPE:String = "_top";
		public static const TARGET_DEFAULT:String = "targetDefault";
		
		
		/* Default file names and path(s) */
		public static const DEFAULT_CACHEBUSTER:Boolean = false;
		public static const DEFAULT_DIAGNOSTICS:Boolean = false;
		public static const DEFAULT_VERSION_FILE:String = "./gnversion.txt";
		public static const DEFAULT_CSS_FILE:String = "./css/globalnav-flex.css";
		public static const DEFAULT_PERPERTIES_FILE:String = "/globalnav.txt";
		public static const DEFAULT_DATA_FILE:String = "./globalnavmenu.txt";
		
		// Max width of menu bar if Error occured
		public static const MAX_ERROR_WIDTH:Number = 1000;
		
		
		/* External Flashvars and query string parameter names */
		public static const EXTERNALVARS:String = "externalVars";
		
		// Override cache for file access
		public static const CACHEBUSTER:String = "cb";
		
		// Diagnostics mode for display window output
		public static const DIAGNOSTICS:String = "diag";
		
		// Path for override of default file access
		public static const PROPERTIESFILE:String = "p";
		public static const CSSFILE:String = "css";
		public static const DATAFILE:String = "d";
		public static const IMAGEPATH:String = "img";
		
		// Required for the properties file
		public static const ORIGIN_SERVER:String = "originServer";
		
		// Highligh Category
		public static const STATICCATEGORY:String = "gn_category";
		
		// Current version
		public static const GN_VERSION:String = "gnversion";				// File name
		public static const GN_VERSION_COOKIE:String = "gnversioncookie";	// Flash var
		public static const GN_CARTSTATUS:String = "cartStatus";
		public static const GN_DISPLAY:String = "gnDisplay";
		public static const G_LINKS_DISPLAY:String = "gLinksDisplay";
		public static const ZIP_DISPLAY:String = "zipDisplay";
		public static const LOGO_DISPLAY:String = "logoDisplay";
		public static const LOB_DISPLAY:String = "lobDisplay";
		public static const SEARCH_DISPLAY:String = "searchDisplay";
		
		public static const LOGIN_URL:String = "loggedInURL";
		public static const CITY:String = "CITY";
		public static const STATE:String = "STATE";
		public static const ZIPCODE:String = "ZIPCODE";
		public static const COMPANY_NAME:String = "companyName";
		
		// Header items
		public static const GLINKS:String = "glinks";
		public static const CARTURL:String = "cart";
		public static const LINEOFBUSINESS:String = "lob";
		public static const LOGO:String = "logo";
		
		// If there is a problem witht he application, then send back to JS this status
		public static var status:int = 0;
		
		
		
		// Convertion
		public static var htmlSymbols:Array = [
			{ from:"&ntilde;",to:"&#0328;" },
		];
		
		
		public static var wordSymbols:Array = [
			{ from:"&amp;",to:"and" },
			{ from:"&#0328;",to:"n" },
		];
		
		
		
		public function GlobalsVO() {
		}
		
		
		
		
		private static var _focusObjects:Array = new Array();
		
		
		
		/**
		 * Add focus to any display object
		 * for the accessibility feature 
		 */
		 		
		public static function addFocus(displayObject:*,tabOrder:int=-1):void {
			if(tabOrder != -1) {
				_focusObjects[tabOrder] = {displayObject:displayObject,tabOrder:tabOrder};
			} else {
				/* If no tab order is supplied then push
				 * the tabable displayobject at the end of the array */
				_focusObjects.push({displayObject:displayObject,tabOrder:tabOrder});
			}
		}
		
		
		
		/* Tab order for all features
		 * HOW THIS WORKS
		 * The following static constant(s)
		 * have an initial value.
		 * EXAMPLE:
		 * INIT_TAB_GLINKS will be tabbed first
		 * so the initial starting tab value will be "0"
		 * The next tabable section will be the LOCATION
		 * Since there we're 6 tabbable links (Starting with 0 end a 5)
		 * the LOCATION "Will Start" will a 6 */
		 
		public static const INIT_TAB_GLINKS:int = 0;
		public static const INIT_TAB_LOCATION:int = 7;
		public static const INIT_TAB_LOGO:int = 9;
		public static const INIT_TAB_LOB:int = 10;
		public static const INIT_TAB_SEARCH:int = 13;
		/* Tab index will start the menu bar
		 * (Really being the 12th key pressed tab */
		public static const INIT_TAB_MENUBAR:int = 15;
		
		
		
		
		public static function get accessableTabList():Array {
			return _focusObjects;
		}
		
		
		
		
		
		/**
		 * @param name - String value of any datatype to store
		 * @param value - Any data type to store into the class var _global
		 */
		 
		public static function setGlobal(name:String,value:*):void {
			try {
				_global[name] = value;
			} catch(e:Error) {
				_global = {};
				_global[name] = value;
			}
		}
		
		
		
		/**
		 * This is to set the header height and
		 * the height of the menu component.
		 * It is used to call the external interface
		 * to JS to set the DIV tag
		 * @param componentHeight:Number - The total
		 * height of each component
		 */
		 
		public static function setMaxHeight(componentHeight:Number):void {
			isNaN(_global.maxHeight) ? _global.maxHeight = componentHeight :
										_global.maxHeight+=componentHeight;
		}
		
		
		/**
		 * Get the total height for all the
		 * components that have registered
		 * their height 
		 * @return 
		 */
		 		
		public static function getMaxHeight():Number {
			return Number(_global.maxHeight);
		}
		
		
		
		
		/**
		 * Get a new CSSLoader to read in the
		 * external CSS file 
		 * @param callBack
		 */
		 		
		public static function styleManager(callBack:Function):void {
			
			_onStyleLoaded = callBack;
			
			// Set global reference to the style loader
			_global.styleLoader = new CSSLoader();
			_global.styleLoader.addEventListener(CSSLoader.RESULT, onLoadFinished);
			_global.styleLoader.addEventListener(CSSLoader.FAULT, onLoadFault);
		}
		
		
		
		
		
		/**
		 * The diagnostics window 
		 * @param msg
		 * @return 
		 */
		 		
		public static function diagnostics(msg:String=null):Object {
			
			if(Strings.strToBool(getGlobal(EXTERNALVARS)[DIAGNOSTICS]) || DIAG) {
				if(diagnosticsWindow == null) {
					var layout:Object = GlobalsVO.getGlobal(APPLICATION);
					var output:OutputWindow = new OutputWindow();
					var setDimentions:Function = function(e:ResizeEvent=null):void {
						output.setDimentions(layout.stage.stageWidth,layout.stage.stageHeight);
					}
					layout.addChild(output);
					layout.addEventListener(ResizeEvent.RESIZE,setDimentions);
					setDimentions();
					// Set public reference for application
					diagnosticsWindow = output;
				} else if(msg != null) {
					diagnosticsWindow.msg(msg);
				}
			}
			return output;
		}
		
		
		
		
		/**
		 * Load the external CSS file 
		 * @param url
		 * @param type
		 */
		 		
		public static function loadStyle(url:String, cb:Boolean):void {
			_global.styleLoader.load(url,cb,VALIDCSS,"default");
			_cssStyleCount++;
		}
		
		
		
		/**
		 * Get all the properties from the CSS file
		 */
		 
		public static function getStyleProperties():* {
			return _global.styleLoader.getStyleProperties("default");
		}
		
		
		
		/**
		 * Style manager finished loading the styles 
		 * @param event
		 */
			
		private static function onLoadFinished (event:Event):void {
			if(--_cssStyleCount <= 0) {
				_onStyleLoaded(event);
			}
		}
		
		
		
		
		/**
		 * Sytle manager encountered a problem
		 * in loading the CSS 
		 * @param event
		 */
		 
		private static function onLoadFault(event:Event):void {
			_onStyleLoaded(event);
		}
		
		
		/**
		 * Set the display object to the
		 * CSS defined style 
		 * @param instance
		 */
		 		
		public static function setStyle(instance:*):void {
			_global.styleLoader.applyStyle("default", instance, true);
		}
		
		
		
		
		
		/**
		 * 
		 * @param propertyName
		 * @return 
		 * 
		 */	
		 	
		public static function getCSSProperty(propertyName:String):* {
			return _global.styleLoader.getStyleProperty("default",propertyName);
		}
		
		
		
		
		/**
		 * @param name - String value to access the 
		 * class var _global to return the datatype reference
		 * 
		 * @return - Any datatype that is stored into the classvar _global
		 * If object name doesn't exist then return null, 
		 * otherwise return the datatype from the class var _global
		 */
		 
		public static function getGlobal(name:String):* {
			try {
				return _global[name];
			} catch(e:Error) {
				return null;
			}	
		}
	}
}