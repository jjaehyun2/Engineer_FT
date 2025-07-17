package gs.model
{
	import gs.soap.SoapService;
	import gs.http.HTTPService;
	import gs.remoting.RemotingService;
	import gs.http.HTTPCall;
	import gs.managers.AssetManager;
	import gs.preloading.Asset;
	import gs.remoting.RemotingCall;
	import gs.util.NavigateToURL;
	import gs.util.StringUtils;
	import gs.util.Strings;
	import gs.util.StyleSheetUtils;
	import gs.util.TextAttributes;
	import gs.util.XMLLoader;
	import gs.util.cache.Cache;
	
	import flash.net.URLRequest;
	import flash.system.Security;
	import flash.text.Font;
	import flash.text.StyleSheet;
	import flash.text.TextFormat;
	import flash.utils.Dictionary;
	
	/**
	 * The Model class contains shortcuts for parsing a model xml file.
	 * 
	 * @example Example model XML file:
	 * <listing>	
	 * &lt;?xml version="1.0" encoding="utf-8"?&gt;
	 * &lt;model&gt;
	 *    &lt;fonts&gt;
	 *        &lt;font libraryName="Arial_Test" inSWF="fonts" /&gt;
	 *        &lt;group id="myGroup"&gt;
	 *            &lt;font libraryName="Helvetica Neueu Bold Condensed" /&gt;
	 *        &lt;/group&gt;
	 *    &lt;/fonts&gt;
	 *    
	 *    &lt;assets&gt;
	 *        &lt;asset libraryName="clayBanner1" source="clay_banners_1.jpg" preload="true" /&gt;
	 *        &lt;asset libraryName="clayBanner2" source="clay_banners_2.jpg" /&gt;
	 *        &lt;asset libraryName="clayBanner3" source="clay_banners_3.jpg" forceReload="true" /&gt;
	 *        &lt;asset libraryName="clayWebpage" source="clay_webpage.jpg" /&gt;
	 *        &lt;asset libraryName="rssFeed" source="http://codeendeavor.com/feed" forceType="xml" /&gt;
	 *        &lt;asset libraryName="fonts" source="fonts.swf" preload="true" /&gt;
	 *        &lt;group id="sounds"&gt;
	 *            &lt;asset libraryName="thesound" source="sound.mp3" path="sounds" /&gt;
	 *        &lt;/group&gt;
	 *    &lt;/assets&gt;
	 *    
	 *    &lt;captions&gt;
	 *        &lt;group id="spiritVideo"&gt;
	 *             &lt;caption time="3" duration="3" bgcolor="0x222222"&gt;
	 *                  &lt;![CDATA[
	 *                      &lt;span class="body"&gt;bob lob law&lt;/span&gt;
	 *                  ]]&gt;
	 *             &lt;/caption&gt;
	 *             &lt;caption time="8" duration="3" bgcolor="0x222222"&gt;
	 *                  &lt;![CDATA[
	 *                      &lt;span class="body"&gt;bob lob law&lt;/span&gt;
	 *                  ]]&gt;
	 *             &lt;/caption&gt;
	 *        &lt;/group&gt;
	 *    &lt;/captions&gt;
	 *    
	 *    &lt;links&gt;
	 *        &lt;link id="google" url="http://www.google.com" /&gt;
	 *        &lt;link id="rubyamf" url="http://www.rubyamf.org" /&gt;
	 *        &lt;link id="guttershark" url="http://www.guttershark.net" window="_blank" /&gt;
	 *        &lt;link id="googleFromStringId" stringId="googleInStrings" /&gt;
	 *    &lt/links&gt;
	 *    
	 *    &lt;attributes&gt;
	 *        &lt;attribute id="someAttribute" value="the value" /&gt;
	 *        &lt;attribute id="someAttributeFromStrings" stringId="someAttributeValueStringId" /&gt;
	 *    &lt;/attributes&gt;
	 *    
	 *    &lt;textAttributes&gt;
	 *        &lt;attribute id="myTextAttribute1" autoSize="left" antiAliasType="advanced"
	 *            styleSheetId='someStyleSheetId' textFormatId='someTextFormatId'
	 *            stringId='someStringId' wrapInBodySpan='true' selectable='false' border='false'
	 *            multiline='false' embedFonts='true'
	 *        /&gt;
	 *        &lt;attribute id="myTextAttribute2" styleSheetId='someStyleSheetId' /&gt; &lt;!-- you don't have to use every attribute, it will only apply what's here. --&gt;
	 *    &lt/textAttributes&gt;
	 *    
	 *    &lt;services&gt;
	 *        &lt;http&gt;
	 *            &lt;service id="google" url="http://www.google.com/" retries="1" timeout="1500" &gt;
	 *                &lt;call id="home" url="" method="GET||POST" responseFormat="text" retries="1" timeout="1500" /&gt;
	 *            &lt;/service&gt;
	 *            &lt;service id="codeendeavor" url="http://www.codeendeavor.com/" retries="1" timeout="1500" &gt;
	 *                &lt;call id="article814" url="archives/814" method="GET||POST" responseFormat="text" retries="1" timeout="1500" /&gt;
	 *            &lt;/service&gt;
	 *        &lt;/http&gt;
	 *        &lt;remoting&gt;
	 *            &lt;service id="amfphp" gateway="http://guttershark_amfphp/gateway.php" encoding="3" timeout="3000" retries="1" &gt;
	 *                &lt;call id="Echoer.echoString" endpoint="Echoer" method="echoString" /&gt;
	 *                &lt;call id="Echoer.echoObject" endpoint="Echoer" method="echoObject" encoding="3" timeout="3000" retries="1" /&gt;
	 *            &lt;/service&gt;
	 *        &lt;/remoting&gt;
	 *        &lt;soap&gt;
	 *            &lt;service id="resolveIP" wsdl="http://ws.cdyne.com/ip2geo/ip2geo.asmx?WSDL" timeout="3000" retries="1" /&gt;
	 *        &lt;/soap&gt;
	 *    &lt;/services&gt;
	 *    
	 *    &lt;security&gt;
	 *        &lt;policyfiles&gt;
	 *            &lt;crossdomain url="http://www.codeendeavor.com/crossdomain.xml" /&gt;
	 *        &lt;/policyfiles&gt;
	 *        &lt;xscript&gt;
	 *            &lt;domain name="macromedia.com" /&gt;
	 *            &lt;domain name="\*" /&gt;
	 *            &lt;domain name="192.168.1.1" /&gt;
	 *        &lt;/xscript&gt;
	 *    &lt;/security&gt;
	 *    
	 *    &lt;stylesheets&gt;
	 *        &lt;stylesheet id="colors"&gt;
	 *            &lt;![CDATA[
	 *                .pink {
	 *            	      color:#FF0066
	 *                }
	 *            ]]&gt;
	 *        &lt;/stylesheet&gt;
	 *        &lt;stylesheet id="colors2"&gt;
	 *            &lt;![CDATA[
	 *                .some {
	 *            	      color:#FF8548
	 *                }
	 *            ]]&gt;
	 *        &lt;/stylesheet&gt;
	 *        &lt;stylesheet id="colors3" mergeStyleSheets="colors,colors2" /&gt;
	 *    &lt;/stylesheets&gt;
	 *    
	 *    &lt;textformats&gt;
	 *        &lt;textformat id="theTF" font="Arial" color="0xFF0066" bold="true" /&gt;
	 *    &lt;/textformats&gt;
	 *    
	 *    &lt;properties&gt;
	 *        &lt;-- See examples/model_properties for more information on cast types. --&gt;
	 *        &lt;clip x="[int]10" y="[int]10" alpha="[number]1"&gt;
	 *            &lt;clip2 x="[int]0" y="[int]0" alpha="[number]1" /&gt;
	 *            &lt;clip3 x="[int]200" y="[int]0" alpha="[number].5" visible="[bool]false" /&gt;
	 *        &lt;/clip&gt;
	 *    &lt;/properties&gt;
	 * &lt;/model&gt;
	 * </listing>
	 * 
	 * <p><b>Examples</b> are in the <a target="_blank" href="http://gitweb.codeendeavor.com/?p=guttershark.git;a=summary">guttershark</a>
	 * repository.</p>
	 */
	public class Model
	{
		
		/**
		 * Reference to the entire model XML.
		 */
		private var _model:XML;
		
		/**
		 * The id of this model.
		 */
		public var id:String;
		
		/**
		 * A placeholder for an instance of a Strings
		 * object. This is never set automatically, it's
		 * a placeholder to you to set it yourself.
		 */
		public var strings:Strings;
		
		/**
		 * Stores a reference to the <code>&lt;assets&gt;&lt;/assets&gt;</code>
		 * node in the model xml.
		 */
		public var assets:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;links&gt;&lt;/links&gt;</code>
		 * node in the model xml.
		 */
		public var links:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;attributes&gt;&lt;/attributes&gt;</code>
		 * node in the model xml.
		 */
		public var attributes:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;services&gt;&lt;/services&gt;</code>
		 * node in the model xml.
		 */
		public var services:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;stylesheets&gt;&lt;/stylesheets&gt;</code>
		 * node in the model xml.
		 */
		public var stylesheets:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;textformats&gt;&lt;/textformats&gt;</code>
		 */
		public var textformats:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;fonts&gt;&lt/fonts&gt;</code>
		 * node in the model xml.
		 */
		public var fonts:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;security&gt;&lt;/security&gt;</code>
		 * node in the model xml.
		 */
		public var security:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;textAttributes&gt;&lt;/textAttributes&gt;</code>
		 * node in the model xml.
		 */
		public var textAttributes:XMLList;
		
		/**
		 * Stores a reference to the <code>&lt;captions&gt;&lt;/captions&gt;</code>
		 * node in the model xml.
		 */
		public var captions:XMLList;
		
		/**
		 * If external interface is not available, all paths are stored here.
		 */
		private var paths:Dictionary;
		
		/**
		 * A cache for text formats and stylesheets.
		 */
		private var modelcache:Cache;
		
		/**
		 * Custom merged stylesheets.
		 */
		private var customStyles:Dictionary;

		/**
		 * xml loader used for loadModelXML;
		 */
		private var xmlLoader:XMLLoader;
		
		/**
		 * On complete handler for the xml loader.
		 */
		private var onComplete:Function;
		
		/**
		 * Cast type matcher for applying properties on
		 * object chains.
		 */
		private var castMatch:RegExp = /^\[([a-zA-Z]*)\](.*)/;
		
		/**
		 * Model lookup.
		 */
		private static var _models:Dictionary = new Dictionary(true);
		
		/**
		 * @private
		 * Constructor for Model instances.
		 */
		public function Model()
		{
			paths=new Dictionary();
			customStyles=new Dictionary();
			modelcache=new Cache();
		}
		
		/**
		 * Get a model instance.
		 * 
		 * @param id The id of the model.
		 */
		public static function get(id:String):Model
		{
			if(!id)
			{
				trace("WARNING: Parameter {id} was null, returning null");
				return null;
			}
			if(!_models[id])_models[id]=new Model();
			return _models[id];
		}
		
		/**
		 * Set a model instance.
		 * 
		 * @param id The model id.
		 * @param ml The model instance.
		 */
		public static function set(id:String,ml:Model):void
		{
			if(_models[id] && !Model(_models[id]).xml && ml.xml)
			{
				ml.id=null;
				Model(_models[id]).xml=ml.xml;
				Model(_models[id]).clearCache();
				return;
			}
			if(!ml.id)ml.id=id;
			_models[id]=ml;
		}
		
		/**
		 * Unsets (deletes) a model instance.
		 */
		public static function unset(id:String):void
		{
			if(!_models)return;
			delete _models[id];
		}
		
		/**
		 * Sets the model xml.
		 * 
		 * @param xml The xml content that is the model.
		 */
		public function set xml(xml:XML):void
		{
			if(!xml)throw new ArgumentError("Parameter xml cannot be null");
			_model=xml;
			if(_model.assets)assets=_model.assets;
			if(_model.links)links=_model.links;
			if(_model["attributes"])attributes=_model["attributes"];
			if(_model.stylesheets)stylesheets=_model.stylesheets;
			if(_model.service)services=_model.services;
			if(_model.textformats)textformats=_model.textformats;
			if(_model.fonts)fonts=_model.fonts;
			if(_model.security)security=_model.security;
			if(_model.textAttributes)textAttributes=_model.textAttributes;
			if(_model.captions)captions=_model.captions;
		}
		
		/**
		 * The XML used as the model.
		 */
		public function get xml():XML
		{
			return _model;
		}
		
		/**
		 * Load an xml file to use as the model xml.
		 * 
		 * @param model The model xml file name.
		 * @param complete A callback function for on complete of the xml load.
		 * @param ioerror A callback function to handle ioerrors.
		 * @param securityerror A callback function to handle security errors.
		 */
		public function load(model:String,complete:Function,ioerror:Function=null,securityerror:Function=null):void
		{
			onComplete=complete;
			xmlLoader=new XMLLoader();
			xmlLoader.load(new URLRequest(model),_onComplete);
		}
		
		/**
		 * On complete handler.
		 */
		private function _onComplete():void
		{
			xml=xmlLoader.data;
			if(onComplete!=null)onComplete();
		}
		
		/**
		 * Get an Asset instance by the library name.
		 * 
		 * @param libraryName The libraryName of the asset to create.
		 * @param prependSourcePath	The path to prepend to the source property of the asset.
		 */
		public function getAssetByLibraryName(libraryName:String, prependSourcePath:String=null):Asset
		{
			checkForXML();
			//var cacheKey:String="asset_"+libraryName;
			//if(modelcache.isCached(cacheKey))return modelcache.getCachedObject(cacheKey) as Asset;
			if(!libraryName)throw new ArgumentError("Parameter libraryName cannot be null");
			var node:XMLList=assets..asset.(@libraryName==libraryName);
			var ft:String=(node.@forceType!=undefined&&node.@forceType!="")?node.@forceType:null;
			var src:String=node.@source || node.@src;
			if(prependSourcePath)src=prependSourcePath+src;
			if(node.@path!=undefined)src=getPath(node.@path.toString())+src;
			var a:Asset=new Asset(src,libraryName,ft);
			//modelcache.cacheObject(cacheKey,a);
			return a;
		}
		
		/**
		 * Get an array of asset objects, from the provided library names.
		 * 
		 * @param ...libraryNames An array of library names.
		 */
		public function getAssetsByLibraryNames(...libraryNames:Array):Array
		{
			checkForXML();
			//var cacheKey:String="assets_"+libraryNames.join("");
			//if(modelcache.isCached(cacheKey))return modelcache.getCachedObject(cacheKey) as Array;
			var p:Array=[];
			var i:int=0;
			var l:int=libraryNames.length;
			for(;i<l;i++)p[int(i)]=getAssetByLibraryName(libraryNames[int(i)]);
			//modelcache.cacheObject(cacheKey,p);
			return p;
		}
		
		/**
		 * Get an array of asset objects, defined by a group node.
		 * 
		 * @param groupId The id of the group node.
		 */
		public function getAssetGroup(groupId:String):Array
		{
			checkForXML();
			//var cacheKey:String="assetGroup_"+groupId; 
			//if(modelcache.isCached(cacheKey))return modelcache.getCachedObject(cacheKey) as Array;
			var x:XMLList=assets..group.(@id==groupId)..asset;
			var payload:Array=[];
			var i:int=0;
			var l:int=x.length();
			var ln:String;
			var n:*;
			for(;i<l;i++) {
				n=x[int(i)];
				if(AssetManager.isAvailable(n.@libraryName) && n.@forceReload!=undefined && n.@forceReload!="true") continue;
				payload.push(getAssetByLibraryName(n.@libraryName));
			}
			//for each(n in x..asset)payload.push(getAssetByLibraryName(n.@libraryName));
			//modelcache.cacheObject(cacheKey,payload);
			return payload;
		}
		
		/**
		 * Returns a captioning set for flv captioning.
		 * 
		 * @param gruopId The captioning group id.
		 */
		public function getCaptionsByGroupId(groupId:String):*
		{
			if(!groupId) return null;
			return captions.group.(@id == groupId).caption;
		}
		
		/**
		 * Returns an array of Asset instances from the assets node,
		 * that has a "preload" attribute set to true (preload='true').
		 */
		public function getAssetsForPreload():Array
		{
			checkForXML();
			var a:XMLList=assets..asset;
			if(!a)
			{
				trace("WARNING: No assets were defined, not doing anything.");
				return null;
			}
			var payload:Array=[];
			for each(var n:XML in a)
			{
				if(n.@preload==undefined||n.@preload=="false")continue;
				var ft:String=(n.@forceType!=undefined&&n.@forceType!="")?n.@forceType:null;
				var src:String=n.@source||n.@src;
				if(AssetManager.isAvailable(n.@libraryName) && n.@forceReload!=undefined && n.@forceReload!="true") continue;
				if(n.attribute("path")!=undefined)src=getPath(n.@path.toString())+src;
				var ast:Asset=new Asset(src,n.@libraryName,ft);
				payload.push(ast);
			}
			return payload;
		}
		
		/**
		 * Creates and returns a URLRequest from a link node.
		 * 
		 * @param id The id of the link node.
		 */
		public function getLink(id:String):URLRequest
		{
			checkForXML();
			var key:String="link_"+id;
			if(modelcache.isCached(key))return URLRequest(modelcache.getCachedObject(key));
			var link:XMLList=links..link.(@id==id);
			if(!link) return null;
			var u:URLRequest;
			if(link.hasOwnProperty("@stringId"))u=new URLRequest(strings.getStringFromID(link.@stringId));
			else if(link.@url!=undefined)u=new URLRequest(link.@url);
			else if(link.@href!=undefined)u=new URLRequest(link.@href);
			modelcache.cacheObject(key,u);
			return u;
		}
		
		/**
		 * Check whether or not a link is defined in the model.
		 * 
		 * @param id The link id.
		 */
		public function doesLinkExist(id:String):Boolean
		{
			checkForXML();
			var link:XMLList=links..link.(@id==id);
			if(!link||link==null)return false;
			return true;
		}
		
		/**
		 * Get the window attribute value on a link node.
		 * 
		 * @param id The id of the link node.
		 */
		public function getLinkWindow(id:String):String
		{
			checkForXML();
			var key:String="window_"+id;
			if(modelcache.isCached(key))return String(modelcache.getCachedObject(key));
			var link:XMLList=links..link.(@id == id);
			if(!link)return null;
			var window:String=link.@window;
			if(window)modelcache.cacheObject(key,window);
			return window;
		}
		
		/**
		 * Navigates to a link.
		 * 
		 * @param id The link id.
		 */
		public function navigateToLink(id:String):void
		{
			var req:URLRequest=getLink(id);
			var w:String=getLinkWindow(id);
			NavigateToURL.navToURL(req,w);
			//navigateToURL(req,w);
		}
		
		/**
		 * Get the value from an attribute node.
		 * 
		 * @param attributeID The id of an attribute node.
		 */
		public function getAttribute(attributeID:String):String
		{
			checkForXML();
			var attr:XMLList=attributes..attribute.(@id==attributeID);
			if(!attr)return null;
			if(attr.hasOwnProperty("@stringId")) return strings.getStringFromID(attr.@stringId);
			return attr.@value;
		}
		
		/**
		 * Get a text attributes.
		 * 
		 * @param attributeID The id of a text attribute node.
		 */
		public function getTextAttributeById(id:String):TextAttributes
		{
			checkForXML();
			var cachekey:String = "textAttributes_"+id;
			if(modelcache.isCached(cachekey)) return modelcache.getCachedObject(cachekey);
			var ss:StyleSheet=null;
			var tf:TextFormat=null;
			var string:String=null;
			var anti:String=null;
			var auto:String=null;
			var sel:Boolean=false;
			var mult:Boolean=false;
			var embed:Boolean=true;
			var bord:Boolean=false;
			var attr:XMLList=textAttributes..attribute.(@id==id);
			if(!attr)return null;
			if(attr.hasOwnProperty("@embedFonts"))embed=StringUtils.toBoolean(attr.@embedFonts);
			if(attr.hasOwnProperty("@styleSheetId"))ss=getStyleSheetById(attr.@styleSheetId,embed);
			if(attr.hasOwnProperty("@textFormatId"))tf=getTextFormatById(attr.@textFormatId,embed);
			if(attr.hasOwnProperty("@stringId"))
			{
				if(!strings)
				{
					trace("WARNING: The {strings} property on the model is not setup. Not doing anything.");
					return null;
				}
				else string=strings.getStringFromID(attr.@stringId);
			}
			if(attr.hasOwnProperty("@antiAliasType"))anti=attr.@antiAliasType;
			if(attr.hasOwnProperty("@autoSize"))auto=attr.@autoSize;
			if(attr.hasOwnProperty("@autosize"))auto=attr.@autosize;
			if(attr.hasOwnProperty("@selectable"))sel=StringUtils.toBoolean(attr.@selectable);
			if(attr.hasOwnProperty("@border"))bord=StringUtils.toBoolean(attr.@border);
			if(attr.hasOwnProperty("@multiline"))mult=StringUtils.toBoolean(attr.@multiline);
			var ta:TextAttributes=new TextAttributes(ss,tf,anti,auto,string,sel,mult,bord,embed);
			if(attr.hasOwnProperty("@wrapInBodySpan"))ta.wrapInBodySpan=(attr.@wrapInBodySpan=="true")?true:false;
			if(attr.hasOwnProperty("@clearsTextAfterApply"))ta.clearsTextAfterApply=(attr.@clearsTextAfterApply=="true")?true:false;
			modelcache.cacheObject(cachekey,ta);
			return ta;
		}
		
		/**
		 * A shortcut method to get an attribute as a number.
		 * 
		 * @param attributeID The id of an attribute node.
		 */
		public function attrAsNumber(attributeID:String):Number
		{
			return Number(getAttribute(attributeID));
		}
		
		/**
		 * A shortcut method to get an attribute as an integer.
		 * 
		 * @param attributeID The id of an attribute node.
		 */
		public function attrAsInt(attributeID:String):int
		{
			return int(getAttribute(attributeID));
		}
		
		/**
		 * A shortcut method to get an attribute as a boolean.
		 * 
		 * @param attributeID The id of an attribute node.
		 */
		public function attrAsBool(attributeID:String):Boolean
		{
			return (getAttribute(attributeID)=="true"?true:false);
		}
		
		/**
		 * Check that the model xml was set on the singleton instance before any attempts
		 * to read the xml happens.
		 */
		protected function checkForXML():void
		{
			if(!_model) throw new Error("The model xml must be set on the model before attempting to read a property from it.");
		}

		/**
		 * Check whether or not a path has been defined.
		 */
		public function isPathDefined(path:String):Boolean
		{
			return !(paths[path]==false);
		}
		
		/**
		 * Add a path to the model.
		 * 
		 * @example Using path logic with the model.
		 * <listing>	
		 * public class Main extends DocumentController
		 * {
		 *     override protected function initPaths():void
		 *     {
		 *         ml.addPath("root","./");
		 *         ml.addPath("assets",ml.getPath("root")+"assets/");
		 *         ml.addPath("bitmaps",ml.getPath("root","assets")+"bitmaps/");
		 *         testPaths();
		 *     }
		 *     
		 *     //illustrates how the "getPath" function works.
		 *     private function testPaths():void
		 *     {
		 *         trace(ml.getPath("root")); // -> ./
		 *         trace(ml.getPath("assets")); // -> ./assets/
		 *         trace(ml.getPath("bitmaps")); // -> ./assets/bitmaps/
		 *     }
		 * }
		 * </listing>
		 * 
		 * @param pathId The path identifier.
		 * @param path The path.
		 */	
		public function addPath(pathId:String, path:String):void
		{
			paths[pathId]=path;
			return;
		}
		
		/**
		 * Get a path concatenated from the given pathIds.
		 * 
		 * @param ...pathIds An array of pathIds whose values will be concatenated together.
		 */
		public function getPath(...pathIds:Array):String
		{
			var fp:String="";
			var i:int=0;
			var l:int=pathIds.length;
			for(;i<l;i++)
			{
				if(!paths[pathIds[int(i)]])throw new Error("Path {"+pathIds[int(i)]+"} not defined.");
				fp+=paths[pathIds[int(i)]];
			}
			return fp;
		}
		
		/**
		 * Loads all the security policy files
		 * specified in the model.
		 */
		public function loadPolicyFiles():void
		{
			if(!security)return;
			var pf:XMLList=security.policyfiles.crossdomain;
			var s:XML;
			var sp:String;
			for each(s in pf)
			{
				if(s.hasOwnProperty("@url"))sp=s.@url;
				if(s.hasOwnProperty("src"))sp=s.@src;
				Security.loadPolicyFile(sp);
			}
		}
		
		/**
		 * Allows a domain for cross scripting this swf.
		 * 
		 * <p>This is specifically for cases where a swf needs to
		 * allow an outer swf access (Security.allowDomain()).
		 */
		public function allowCrossScriptingDomains():void
		{
			if(!security) return;
			var pf:XMLList=security.xscripting.children();
			var s:*;
			var sp:String;
			for each(s in pf)
			{
				if(s.hasOwnProperty("@name"))sp=s.@name;
				if(s.hasOwnProperty("@value"))sp=s.@value;
				if(s.hasOwnProperty("@domain"))sp=s.@domain;
				Security.allowDomain(sp);
				Security.allowInsecureDomain(sp);
			}
		}
		
		/**
		 * Get's a color defined in the "colors" stylesheet. There
		 * must be a stylesheet defined with the id of "colors".
		 * 
		 * @example A colors stylesheet definition:
		 * <listing>	
		 * &lt;stylsheets&gt;
		 *     &lt;stylesheet id="colors"&gt;
		 *     &lt;![CDATA[
		 *         .pink{color:#ff0066}
		 *     ]]&gt;
		 *     &lt;/stylesheet&gt;
		 * &lt;/stylesheets&gt;
		 * </listing>
		 * 
		 * @example Using this method:
		 * <listing>	
		 * var color:int=Model.gi().getColorAsInt(".pink");
		 * </listing>
		 * 
		 * @param selector The selector from "colors" the stylesheet.
		 */
		public function getColorAsInt(selector:String):int
		{
			if(!selector)return -1;
			var s:StyleSheet=getStyleSheetById("colors");
			if(!s)throw new Error("A stylesheet in the model name 'colors' must be defined.");
			var c:String=s.getStyle(selector).color;
			if(!c)trace("WARNING: The selector {"+selector+"} in the colors stylesheet wasn't found.");
			return StringUtils.styleSheetNumberToInt(c);
		}
		
		/**
		 * Get a color in hex with 0x, (0xff0066).
		 * 
		 * @param selector The select from the "colors" stylesheet.
		 * 
		 * @see #getColorAsInt The getColorAsInt function for more documentation.
		 */
		public function getColorAs0xHexString(selector:String):String
		{
			if(!selector)return "0x";
			var s:StyleSheet=getStyleSheetById("colors");
			if(!s)throw new Error("A stylesheet in the model name 'colors' must be defined.");
			var c:String=s.getStyle(selector).color;
			if(!c)trace("WARNING: The selector {"+selector+"} in the colors stylesheet wasn't found.");
			return StringUtils.styleSheetNumberTo0xHexString(c);
		}
		
		/**
		 * Get a color in hex with #, (#ff0066).
		 * 
		 * @param selector The select from the "colors" stylesheet.
		 * 
		 * @see #getColorAsInt The getColorAsInt function for more documentation.
		 */
		public function getColorAsPoundHexString(selector:String):String
		{
			var s:StyleSheet=getStyleSheetById("colors");
			if(!s)throw new Error("A stylesheet in the model name 'colors' must be defined.");
			var c:String=s.getStyle(selector).color;
			if(!c)
			{
				trace("WARNING: The selector {"+selector+"} in the colors stylesheet wasn't found.");
				return "#FFFFFF";
			}
			return c;
		}
		
		/**
		 * Get a StyleSheet object by the node id.
		 * 
		 * <p>There is one extra "feature" that this can do -
		 * setting the proper font names for you, based off of
		 * the "font" or "fontFamily".</p>
		 * 
		 * <p>If you specify a "font" style, this will look for
		 * a font defined in the model, grab it out of the library,
		 * and use font.fontName as the "fontFamily" style.</p>
		 * 
		 * <p>If you specify the "fontFamily" style, this will
		 * use the asset manager to try and grab your font out,
		 * and replace what you have defined for the "fontFamily"
		 * style with the proper name.</p>
		 * 
		 * @param id The id of the stylesheet node to grab from the model.
		 */
		public function getStyleSheetById(id:String, applyEmbeddedFonts:Boolean = true):StyleSheet
		{
			checkForXML();
			var cacheId:String="css_"+id;
			if(modelcache.isCached(cacheId))return StyleSheet(modelcache.getCachedObject(cacheId));
			if(customStyles[id])return StyleSheet(customStyles[id]);
			var n:XMLList=stylesheets.stylesheet.(@id==id);
			if(!n)return null;
			var s:StyleSheet;
			if(n.@mergeStyleSheets!=undefined)s=mergeStyleSheetsAs(n.@id,n.@mergeStyleSheets.toString().split(","));
			else
			{
				s=new StyleSheet();
				s.parseCSS(n.toString());
			}
			var names:Array=s.styleNames;
			var i:int=0;
			var l:int=names.length;
			var so:Object;
			var fc:Class;
			var f:Font;
			var finalFontFamily:String;
			if(applyEmbeddedFonts)
			{
				for(;i<l;i++)
				{
					so=s.getStyle(names[int(i)]);
					for(var key:String in so)
					{
						if(key=="font")
						{
							var fontNode:XMLList=fonts..font.(@libraryName==so[key]);
							if(fontNode.hasOwnProperty("@inSWF"))fc=AssetManager.getClassFromSWFLibrary(fontNode.@inSWF,so[key]);
							else fc=AssetManager.getClass(so[key]);
							Font.registerFont(fc);
							f=new fc();
							delete so[key];
							finalFontFamily=f.fontName;
						}
						else if(key=="fontFamily")
						{
							fc=AssetManager.getClass(so[key]);
							Font.registerFont(fc);
							f=new fc();
							finalFontFamily=f.fontName;
						}
					}
					if(finalFontFamily)so['fontFamily']=finalFontFamily;
					s.setStyle(names[int(i)],so);
				}
			}
			modelcache.cacheObject(cacheId,s);
			return s;
		}
		
		/**
		 * Merge any number of style sheets declared in the model as a new
		 * stylesheet with a unique id. The new stylesheet is returned to you,
		 * and can be accessed again through the <em>getStyleSheetById</em>
		 * method. You can also declare merged style sheets in the model
		 * through xml.
		 * 
		 * @param newStyleId The id to name the new merged stylesheet.
		 * @param styleId An array of style ids that are defined in the model.
		 */
		public function mergeStyleSheetsAs(newStyleId:String, ...styleIds:Array):StyleSheet
		{
			checkForXML();
			if(!newStyleId)throw new ArgumentError("Parameter {newStyleId} cannot be null.");
			if(!styleIds)throw new ArgumentError("Parameter {styleIds} cannot be null or empty");
			if(styleIds[0] is Array)styleIds=styleIds[0];
			var sheets:Array=[];
			var i:int=0;
			var l:int=styleIds.length;
			for(;i<l;i++)sheets.push(getStyleSheetById(styleIds[int(i)]));
			var newstyle:StyleSheet=StyleSheetUtils.mergeStyleSheets(sheets);
			customStyles[newStyleId]=newstyle;
			var cacheKey:String="css_"+newStyleId;
			modelcache.cacheObject(cacheKey,newstyle,-1,true);
			return newstyle;
		}
		
		/**
		 * Get a TextFormat object by the node id.
		 * 
		 * <p>Supports these attributes:</p>
		 * <ul>
		 * <li>align</li>
		 * <li>blockIndent</li>
		 * <li>bold</li>
		 * <li>bullet</li>
		 * <li>color</li>
		 * <li>font</li>
		 * <li>indent</li>
		 * <li>italic</li>
		 * <li>kerning</li>
		 * <li>leading</li>
		 * <li>leftMargin</li>
		 * <li>letterSpacing</li>
		 * <li>rightMargin</li>
		 * <li>size</li>
		 * <li>underline</li>
		 * </ul>
		 */
		public function getTextFormatById(id:String,applyEmbeddedFonts:Boolean = true):TextFormat
		{
			checkForXML();
			var cacheId:String="tf_"+id;
			if(modelcache.isCached(cacheId)) return modelcache.getCachedObject(cacheId) as TextFormat;
			var n:XMLList=textformats.textformat.(@id==id);
			var tf:TextFormat=new TextFormat();
			if(n.attribute("align")!=undefined) tf.align=n.@align;
			if(n.attribute("blockIndent")!=undefined) tf.blockIndent=int(n.@blockIndent);
			if(n.attribute("bold")!=undefined) tf.bold=n.@bold;
			if(n.attribute("bullet")!=undefined) tf.bullet=StringUtils.toBoolean(n.@bullet);
			if(n.attribute("color")!=undefined) tf.color=Number(n.@color);
			if(n.attribute("font")!=undefined)
			{
				if(applyEmbeddedFonts)
				{
					var fontNode:*;
					if(fonts)fontNode=fonts..font.(@libraryName==n.@font);
					if(fontNode==undefined) tf.font=AssetManager.getFont(n.@font).fontName;
					else
					{
						var klass:Class;
						var font:Font;
						if(fontNode.attribute("inSWF")!=undefined)
						{
							klass=AssetManager.getClassFromSWFLibrary(fontNode.@inSWF,fontNode.@libraryName);
							font=new klass();
						}
						else font=AssetManager.getFont(fontNode.@libraryName);
						tf.font=font.fontName;
					}
				} else {
					tf.font = n.@font.toString();
				}

			}
			if(n.attribute("indent")!=undefined) tf.indent=Number(n.@indent);
			if(n.attribute("italic")!=undefined) tf.italic=StringUtils.toBoolean(n.@italic);
			if(n.attribute("kerning")!=undefined) tf.kerning=StringUtils.toBoolean(n.@kerning);
			if(n.attribute("leading")!=undefined) tf.leading=Number(n.@leading);
			if(n.attribute("leftMargin")!=undefined) tf.leftMargin=Number(n.@leftMargin);
			if(n.attribute("letterSpacing")!=undefined) tf.letterSpacing=Number(n.@letterSpacing);
			if(n.attribute("rightMargin")!=undefined) tf.rightMargin=Number(n.@rightMargin);
			if(n.attribute("size")!=undefined) tf.size=Number(n.@size);
			if(n.attribute("underline")!=undefined) tf.underline=StringUtils.toBoolean(n.@underline);
			modelcache.cacheObject(cacheId,tf);
			return tf;
		}
		
		/**
		 * Register declared fonts from the model. If no group id is specified,
		 * all fonts declared are registered.
		 * 
		 * @param groupId Optionally register fonts that were declared as part of a specific group.
		 */
		public function registerFonts(groupId:String=null):void
		{
			var child:XML;
			if(groupId)
			{
				var group:XML=fonts.group.(@id==groupId);
				for each(child in group.font)
				{
					if(child.attribute("inSWF")!=undefined) Font.registerFont(AssetManager.getClassFromSWFLibrary(child.@inSWF,child.@libraryName));
					else Font.registerFont(AssetManager.getClass(child.@libraryName));
				}
			}
			else
			{
				for each(child in fonts.font)
				{
					if(child.attribute("inSWF")!=undefined) Font.registerFont(AssetManager.getClassFromSWFLibrary(child.@inSWF,child.@libraryName));
					else Font.registerFont(AssetManager.getClass(child.@libraryName));
				}
			}
		}
		
		/**
		 * Traces information about fonts that will be registered when calling
		 * the registerFont method.
		 * 
		 * @param groupId Optionally trace fonts that were declared as part of a specific group.
		 */
		public function traceFonts(groupId:String=null):void
		{
			var child:XML;
			var fc:Class;
			var f:Font;
			if(groupId)
			{
				var group:XML=fonts.group.(@id==groupId);
				for each(child in group.font)
				{
					if(child.attribute("inSWF")!=undefined) fc = AssetManager.getClassFromSWFLibrary(child.@inSWF,child.@libraryName);
					else fc = AssetManager.getClass(child.@libraryName);
					f = new fc();
					trace("---font---");
					trace("libraryName:",child.@libraryName);
					trace("fontName:",f.fontName);
					trace("fontStyle",f.fontStyle);
					trace("fontType",f.fontType);
				}
			}
			else
			{
				for each(child in fonts.font)
				{
					if(child.attribute("inSWF")!=undefined) fc = AssetManager.getClassFromSWFLibrary(child.@inSWF,child.@libraryName);
					else fc = AssetManager.getClass(child.@libraryName);
					f = new fc();
					trace("---font---");
					trace("libraryName:",child.@libraryName);
					trace("fontName:",f.fontName);
					trace("fontStyle",f.fontStyle);
					trace("fontType",f.fontType);
				}
			}
		}
		
		/**
		 * Get an HTTPService by id.
		 * 
		 * @param id The service id.
		 */
		public function getHTTPServiceById(id:String):HTTPService
		{
			var node:XMLList=services.http..service.(@id==id);
			if(node.toXMLString()=="")throw new Error("ERROR: Could not find the service node.");
			var url:String=node.@url;
			var timeout:int=3000;
			var retries:int=1;
			if(node.hasOwnProperty("@timeout"))timeout=int(node.@timeout);
			if(node.hasOwnProperty("@retries"))retries=int(node.@retries);
			return new HTTPService(url,timeout,retries);
		}
		
		/**
		 * Get an HTTPCall instance by id.
		 * 
		 * @param serviceId The service id.
		 * @param callId The call id.
		 */
		public function getHTTPCallById(serviceId:String,callId:String):HTTPCall
		{
			var snode:XMLList=services.http..service.(@id==serviceId);
			if(snode.toXMLString()=="")throw new Error("ERROR: Could not find the service node.");
			var cnode:XMLList=snode..call.(@id==callId);
			if(cnode.toXMLString()=="") throw new Error("ERROR: Could not find the call node.");
			var url:String=snode.@url;
			var path:String=cnode.@url;
			if(!path)path="";
			var absurl:String=url+path;
			var method:String="GET";
			var responseFormat:String="variables";
			var timeout:int=3000;
			var retries:int=1;
			if(snode.hasOwnProperty("@method"))method=snode.@method;
			if(snode.hasOwnProperty("@timeout"))timeout=int(snode.@timeout);
			if(snode.hasOwnProperty("@retries"))retries=int(snode.@retries);
			if(cnode.hasOwnProperty("@method"))method=cnode.@method;
			if(cnode.hasOwnProperty("@timeout"))timeout=int(cnode.@timeout);
			if(cnode.hasOwnProperty("@retries"))retries=int(cnode.@retries);
			if(cnode.hasOwnProperty("@responseFormat"))responseFormat=cnode.@responseFormat.toString();
			trace(responseFormat);
			return new HTTPCall(absurl,method,null,timeout,retries,responseFormat);
		}
		
		/**
		 * Get a remoting service by id.
		 * 
		 * @param id The service id.
		 */
		public function getRemotingServiceById(id:String):RemotingService
		{
			var node:XMLList=services.remoting..service.(@id==id);
			if(node.toXMLString()=="")throw new Error("ERROR: Could not find the service node.");
			var gateway:String=node.@gateway;
			var endpoint:String=node.@endpoint;
			var timeout:int=3000;
			var retries:int=1;
			var encoding:int=3;
			if(node.hasOwnProperty("@timeout"))timeout=int(node.@timeout);
			if(node.hasOwnProperty("@retries"))retries=int(node.@retries);
			if(node.hasOwnProperty("@encoding"))encoding=int(node.@encoding);
			return new RemotingService(gateway,endpoint,timeout,retries,encoding);
		}
		
		/**
		 * Get a remoting call by service, and call id.
		 * 
		 * @param id The id of the remoting call.
		 */
		public function getRemotingCallById(serviceId:String,callId:String):RemotingCall
		{
			var snode:XMLList=services.remoting..service.(@id==serviceId);
			if(snode.toXMLString()=="")throw new Error("ERROR: Could not find the service node.");
			var cnode:XMLList=snode..call.(@id==callId);
			if(cnode.toXMLString()=="") throw new Error("ERROR: Could not find the call node.");
			var gateway:String=snode.@gateway;
			var encoding:int=3;
			var timeout:int=3000;
			var retries:int=1;
			var endpoint:String;
			var method:String;
			if(snode.hasOwnProperty("@timeout"))timeout=int(snode.@timeout);
			if(snode.hasOwnProperty("@retries"))retries=int(snode.@retries);
			if(snode.hasOwnProperty("@encoding"))encoding=int(snode.@encoding);
			if(cnode.hasOwnProperty("@timeout"))timeout=int(cnode.@timeout);
			if(cnode.hasOwnProperty("@retries"))retries=int(cnode.@retries);
			if(cnode.hasOwnProperty("@encoding"))encoding=int(cnode.@encoding);
			if(cnode.hasOwnProperty("@endpoint"))endpoint=String(cnode.@endpoint);
			if(cnode.hasOwnProperty("@method"))method=String(cnode.@method);
			return new RemotingCall(gateway,endpoint,method,encoding,timeout,retries);
		}
		
		/**
		 * Get a soap service by id.
		 * 
		 * @param id The soap service id.
		 */
		public function getSoapServiceById(id:String):SoapService
		{
			var node:XMLList=services.soap..service.(@id==id);
			var wsdl:String=node.@wsdl;
			var timeout:int=3000;
			var retries:int=1;
			if(node.hasOwnProperty("@timeout"))timeout=int(node.@timeout);
			if(node.hasOwnProperty("@retries"))retries=int(node.@retries);
			return new SoapService(wsdl,timeout,retries);
		}
		
		/**
		 * Apply a hierarchy of property values to an object. The
		 * xml should be a reference to the root node that corresponds
		 * to the object provided, it recurses down the xml in parallel
		 * with the object chain and sets property values.
		 * 
		 * @param obj The root object.
		 * @param xml The root xml.
		 */
		public function applyProperties(obj:*,xml:*):void
		{
			var n:*;
			var children:*;
			var attr:*;
			var attrs:*;
			var prop:String;
			var value:String;
			var match:Array = null;
			var cast:String = null;
			if(xml.children().length() > 0) //recurse first
			{
				children=xml.children();
				for each(n in children)
				{
					prop=n.name();
					if(!(prop in obj)) continue;
					applyProperties(obj[prop],n);
				}
			}
			if(xml.attributes().length() > 0) //apply attributes
			{
				attrs=xml.attributes();
				for each(attr in attrs)
				{
					prop=attr.name();
					value=attr.toString();
					match=value.match(castMatch);
					if(match && match.length > 1)
					{
						cast=match[1].toLowerCase();
						value=match[2];
					}
					switch(cast)
					{
						case "bool":
						case "boolean":
							if(value=="1" || value=="yes" || value=="true") obj[prop] = true;
							if(value=="0" || value=="no" || value=="false") obj[prop] = false;
							break;
						case "int":
						case "integer":
							obj[prop]=int(match[2]);
							break;
						case "uint":
							obj[prop]=uint(match[2]);
							break;
						case "num":
						case "number":
							obj[prop]=Number(match[2]);
							break;
						case "string":
						case "str":
						case null:
						default:
							obj[prop]=value.toString();
							break;
					}
				}
			}
		}
		
		/**
		 * Clears the internal cache.
		 * 
		 * <p>The internal cache caches textformats and stylesheets.</p>
		 */
		public function clearCache():void
		{
			modelcache.purgeAll();
		}
		
		/**
		 * Dispose of this model.
		 */
		public function dispose():void
		{
			Model.unset(id);
			clearCache();
			modelcache.dispose();
			modelcache=null;
			xml=null;
		}
	}
}