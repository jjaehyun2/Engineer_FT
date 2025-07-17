package vzw.menu.builder {
	import vzw.utils.StringUtils;
	import vzw.utils.URLUtils;
	
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	
	import utils.math.MathUtils;
	
	public class WmsAPI {
		private static var accessMode:Boolean = false; // true for external otherwise false for internal.
		public static var menuType:String = '';
		
		private static var _api_Get_Menu_Count:String = '';
		private static var _api_Delete_Menu_By_UUID:String = '';
		private static var _api_Get_Menu_By_UUID:String = '';
		private static var _api_Rename_Menu_by_UUID:String = '';
		private static var _api_Get_Menus:String = '';
		private static var _api_Set_Menu_by_UIUD:String = '';
		private static var _api_New_Menu:String = '';
		private static var _api_Set_Menu_Selection:String = '';
		private static var _api_Get_Menu_Selection:String = '';
		private static var _api_Publish_Menu:String = '';
		private static var _api_Keepalive:String = '';
		private static var _api_RegisterUser:String = '';
		
		private static var _api_Perform_Login:String = '';
		private static var _api_Perform_Logoff:String = '';
		
		public static var internal_domain:String = 'http://127.0.0.1:8888';
		private static var internal_prefix:String = '/rest';
		
		// The prefix override controls which servlet or other server thingy is being used...
		public static var external_domain:String = 'http://localhost:7001';
		private static var _external_prefix:String = '/WMSWeb';
		private static var external_prefix:String = WmsAPI._external_prefix+'/globalnav'; // loggedIn is handled by /WMSWeb/globalnav_loggedin
		
		private static var symbol_uuid_token:String = '%uuid%';
		private static var symbol_state_token:String = '%state%';
		private static var symbol_name_token:String = '%name%';
		private static var symbol_useruid_token:String = '%userid%';
		private static var symbol_username_token:String = '%username%';
		private static var symbol_password_token:String = '%password%';
		private static var symbol_fullname_token:String = '%fullname%';
		private static var symbol_menuType_token:String = '%menuType%';
		private static var symbol_envs_token:String = '%envs%';
		private static var symbol_cacheBuster_token:String = '%cb%';
		
		public static var symbol_loggedIn_token:String = 'loggedIn';
		public static var symbol_loggedOut_token:String = 'loggedOut';
		
		private static var internal_api_Get_Menu_Count:String = '/get/menu/count/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_useruid_token + '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_Delete_Menu_By_UUID:String = '/delete/menu/' + WmsAPI.symbol_uuid_token + '/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_useruid_token + '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_Get_Menu_By_UUID:String = '/get/menu/' + WmsAPI.symbol_uuid_token + '/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_useruid_token +  '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_Rename_Menu_by_UUID:String = '/rename/menu/' + WmsAPI.symbol_name_token + '/' + WmsAPI.symbol_uuid_token + '/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_useruid_token + '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_Get_Menus:String = '/get/menus/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_useruid_token + '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_Set_Menu_by_UIUD:String = '/set/menu/' + WmsAPI.symbol_uuid_token + '/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_useruid_token + '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_New_Menu:String = '/new/menu/' + WmsAPI.symbol_name_token + '/' + WmsAPI.symbol_uuid_token + '/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_useruid_token + '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_Set_Menu_Selection:String = '/set/menu-selection/' + WmsAPI.symbol_uuid_token + '/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_useruid_token + '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_Get_Menu_Selection:String = '/get/menu-selection/' + WmsAPI.symbol_useruid_token + '/' + WmsAPI.symbol_menuType_token + '/json/' + '?x=' + WmsAPI.symbol_cacheBuster_token;
		private static var internal_api_Publish_Menu:String = '/publish/menu/' + WmsAPI.symbol_uuid_token + '/' + WmsAPI.symbol_useruid_token + '/' + WmsAPI.symbol_menuType_token + '/' + WmsAPI.symbol_envs_token + '/json/';
		private static var internal_api_RegisterUser:String = '/users/register/' + WmsAPI.symbol_username_token + '/' + WmsAPI.symbol_password_token + '/' + WmsAPI.symbol_fullname_token + '/json/';
		private static var internal_api_Keepalive:String = '/keepalive/';
		
		private static var internal_api_Perform_Login:String = '/users/login/' + WmsAPI.symbol_name_token + '/' + WmsAPI.symbol_password_token + '/json/';
		private static var internal_api_Perform_Logoff:String = '/users/logout/' + WmsAPI.symbol_useruid_token + '/json/';
		
		private static var external_api_Get_Menu_Count:String = '?action=getMenuCount' + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Delete_Menu_By_UUID:String = '?action=deleteMenu&uuid=' + WmsAPI.symbol_uuid_token + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Get_Menu_By_UUID:String = '?action=getMenuByUuid&uuid=' + WmsAPI.symbol_uuid_token + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Rename_Menu_by_UUID:String = '?action=renameMenuByUuid&uuid=' + WmsAPI.symbol_uuid_token + '&name=' + WmsAPI.symbol_name_token + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Get_Menus:String = '?action=getMenus' + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Set_Menu_by_UIUD:String = '?action=setMenuByUuid&uuid=' + WmsAPI.symbol_uuid_token + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_New_Menu:String = '?action=newMenu' + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&uuid=' + WmsAPI.symbol_uuid_token + '&name=' + WmsAPI.symbol_name_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Set_Menu_Selection:String = '?action=setMenuSelection&uuid=' + WmsAPI.symbol_uuid_token + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Get_Menu_Selection:String = '?action=getMenuSelection&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Publish_Menu:String = '?action=publishMenu&uuid=' + WmsAPI.symbol_uuid_token + '&userid=' + WmsAPI.symbol_useruid_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&envs=' + WmsAPI.symbol_envs_token;
		private static var external_api_RegisterUser:String = '?action=registerUser&username=' + WmsAPI.symbol_username_token + '&password=' + WmsAPI.symbol_password_token + '&fullname=' + WmsAPI.symbol_fullname_token;
		private static var external_api_Keepalive:String = '/keepalive';
		
		private static var external_api_Perform_Login:String = '?action=login' + '&name=' + WmsAPI.symbol_name_token + '&password=' + WmsAPI.symbol_password_token + '&menuType=' + WmsAPI.symbol_menuType_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		private static var external_api_Perform_Logoff:String = '?action=logout' + '&userid=' + WmsAPI.symbol_useruid_token + '&x=' + WmsAPI.symbol_cacheBuster_token;
		
		public static var caption_Ready:String = 'Ready...';
		
		public static var caption_Get_Menus:String = 'Fetching Menus...';
		
		private static var _rollUpMenu_callback:Function = null;
		
		public static var _overrides:Object = null;
		
		public static var _disable_keepalive_timer:Boolean = false;
		
		private static var _keepalive_timer:Timer;
		private static var _keepalive_callback:Function = null;
		
		private static function perform_rollUpMenu_callback():void {
			if (WmsAPI._rollUpMenu_callback is Function) {
				try { WmsAPI._rollUpMenu_callback() } catch (e:Error) {trace('WmsAPI.perform_rollUpMenu_callback().ERROR='+e.toString())}
			}
		}
		
		private static function perform_keepalive_callback():void {
			if (WmsAPI._keepalive_callback is Function) {
				try { WmsAPI._keepalive_callback() } catch (e:Error) {trace('WmsAPI.perform_keepalive_callback().ERROR='+e.toString())}
			}
		}
		
		public static function api_Get_Menus(userid:String):String {
			var value:String = WmsAPI._api_Get_Menus.replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Get_Menu_Count:String = 'Fetching Menu Count...';
		
		public static function api_Get_Menu_Count(userid:String):String {
			var value:String = WmsAPI._api_Get_Menu_Count.replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Rename_Menu_by_UUID:String = 'Renaming Menu...';
		
		public static function api_Rename_Menu_by_UUID(userid:String,uuid:String,menuName:String):String {
			var value:String = WmsAPI._api_Rename_Menu_by_UUID.replace(WmsAPI.symbol_uuid_token,uuid).replace(WmsAPI.symbol_name_token,menuName).replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Get_Menu_By_UUID:String = 'Fetching Menu...';
		
		public static function api_Get_Menu_By_UUID(userid:String,uuid:String):String {
			WmsAPI.perform_rollUpMenu_callback();
			var value:String = WmsAPI._api_Get_Menu_By_UUID.replace(WmsAPI.symbol_uuid_token,uuid).replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Set_Menu_by_UIUD:String = 'Storing Menu...';
		
		public static function api_Set_Menu_by_UIUD(userid:String,uuid:String):String {
			WmsAPI.perform_rollUpMenu_callback();
			var value:String = WmsAPI._api_Set_Menu_by_UIUD.replace(WmsAPI.symbol_uuid_token,uuid).replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Delete_Menu_By_UUID:String = 'Deleting Menu...';
		
		public static function api_Delete_Menu_By_UUID(userid:String,uuid:String):String {
			var value:String = WmsAPI._api_Delete_Menu_By_UUID.replace(WmsAPI.symbol_uuid_token,uuid).replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_New_Menu_By_UUID:String = 'New Menu...';
		
		public static function api_New_Menu_By_UUID(userid:String,uuid:String,menuName:String):String {
			var value:String = WmsAPI._api_New_Menu.replace(WmsAPI.symbol_uuid_token,uuid).replace(WmsAPI.symbol_name_token,menuName).replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Perform_Login:String = 'Perform Login...';
		
		public static function api_Perform_Login(name:String,password:String):String {
			var value:String = WmsAPI._api_Perform_Login.replace(WmsAPI.symbol_name_token,name).replace(WmsAPI.symbol_password_token,password).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Perform_Logoff:String = 'Perform Logoff...';
		
		public static function api_Perform_Logoff(uid:String):String {
			var value:String = WmsAPI._api_Perform_Logoff.replace(WmsAPI.symbol_useruid_token,uid).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Set_Menu_Selection:String = 'Set Menu Selection...';
		
		public static function api_Set_Menu_Selection(uuid:String,userid:String):String {
			var value:String = WmsAPI._api_Set_Menu_Selection.replace(WmsAPI.symbol_uuid_token,uuid).replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Get_Menu_Selection:String = 'Get Menu Selection...';
		
		public static function api_Get_Menu_Selection(userid:String):String {
			var value:String = WmsAPI._api_Get_Menu_Selection.replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_cacheBuster_token,URLUtils.cacheBuster());
			return value;
		}
		
		public static var caption_Publish_Menu:String = 'Pubish Menu...';
		
		public static function api_Publish_Menu(userid:String,uuid:String,envs:String):String {
			WmsAPI.perform_rollUpMenu_callback();
			var _envs:String = StringUtils.urlEncode((envs is String) ? envs : '');
			var value:String = WmsAPI._api_Publish_Menu.replace(WmsAPI.symbol_uuid_token,uuid).replace(WmsAPI.symbol_useruid_token,userid).replace(WmsAPI.symbol_menuType_token,WmsAPI.menuType).replace(WmsAPI.symbol_envs_token,_envs);
			return value;
		}
		
		public static var caption_Register_User:String = 'Register User...';
		
		public static function api_RegisterUser(username:String,password:String,fullname:String):String {
			WmsAPI.perform_rollUpMenu_callback();
			var value:String = WmsAPI._api_RegisterUser.replace(WmsAPI.symbol_username_token,username).replace(WmsAPI.symbol_password_token,password).replace(WmsAPI.symbol_fullname_token,fullname);
			return value;
		}
		
		public static function api_Keepalive():String {
			var value:String = WmsAPI._api_Keepalive;
			return value;
		}
		
		public static function set_access_mode(accessMode:Boolean,menuType:String):Boolean {
			if (WmsAPI.external_domain.length == 0) {
				accessMode = false;
			}
			WmsAPI.accessMode = accessMode;
			
			var menuTypeChoices:Array = [WmsAPI.symbol_loggedIn_token,WmsAPI.symbol_loggedOut_token];
			
			WmsAPI.menuType = (menuTypeChoices.indexOf(menuType) > -1) ? menuType : WmsAPI.symbol_loggedOut_token;
			
			var urlDomainPrefix:String = '';
			urlDomainPrefix = (WmsAPI.accessMode) ? WmsAPI.external_domain + WmsAPI.external_prefix : WmsAPI.internal_domain + WmsAPI.internal_prefix;
			
			var _urlDomainPrefix:String = '';
			_urlDomainPrefix = (WmsAPI.accessMode) ? WmsAPI.external_domain + WmsAPI._external_prefix : WmsAPI.internal_domain + WmsAPI.internal_prefix;
			
			WmsAPI._api_Get_Menu_Count = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Get_Menu_Count : urlDomainPrefix + WmsAPI.internal_api_Get_Menu_Count;
			
			WmsAPI._api_Delete_Menu_By_UUID = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Delete_Menu_By_UUID : urlDomainPrefix + WmsAPI.internal_api_Delete_Menu_By_UUID;
			
			WmsAPI._api_Get_Menu_By_UUID = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Get_Menu_By_UUID : urlDomainPrefix + WmsAPI.internal_api_Get_Menu_By_UUID;
			
			WmsAPI._api_Rename_Menu_by_UUID = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Rename_Menu_by_UUID : urlDomainPrefix + WmsAPI.internal_api_Rename_Menu_by_UUID;
			
			WmsAPI._api_Get_Menus = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Get_Menus : urlDomainPrefix + WmsAPI.internal_api_Get_Menus;
			
			WmsAPI._api_Set_Menu_by_UIUD = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Set_Menu_by_UIUD : urlDomainPrefix + WmsAPI.internal_api_Set_Menu_by_UIUD;
			
			WmsAPI._api_New_Menu = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_New_Menu : urlDomainPrefix + WmsAPI.internal_api_New_Menu;
			
			WmsAPI._api_Set_Menu_Selection = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Set_Menu_Selection : urlDomainPrefix + WmsAPI.internal_api_Set_Menu_Selection;
			
			WmsAPI._api_Get_Menu_Selection = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Get_Menu_Selection : urlDomainPrefix + WmsAPI.internal_api_Get_Menu_Selection;
			
			WmsAPI._api_Perform_Login = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Perform_Login : urlDomainPrefix + WmsAPI.internal_api_Perform_Login;
			
			WmsAPI._api_Perform_Logoff = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Perform_Logoff : urlDomainPrefix + WmsAPI.internal_api_Perform_Logoff;
			
			WmsAPI._api_Publish_Menu = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_Publish_Menu : urlDomainPrefix + WmsAPI.internal_api_Publish_Menu;
			
			WmsAPI._api_RegisterUser = (WmsAPI.accessMode) ? urlDomainPrefix + WmsAPI.external_api_RegisterUser : urlDomainPrefix + WmsAPI.internal_api_RegisterUser;
			
			WmsAPI._api_Keepalive = (WmsAPI.accessMode) ? _urlDomainPrefix + WmsAPI.external_api_Keepalive : urlDomainPrefix + WmsAPI.internal_api_Keepalive;
			
			return WmsAPI.accessMode;
		}
		
		public static function initialize(application:*,isInternal:Boolean,_overrides:String,isWmsDev:Boolean,isDebugging:Boolean,callback:Function=null,keepalive_callback:Function=null):Boolean {
			try {
				isInternal = false;
				
				var url:String = application.url;
				
				var debugger:String = '';
				
				WmsAPI._overrides = URLUtils.parse_overrides(url);
				
				var over:Object = URLUtils.parse_overrides(_overrides);
				var skips:Array = ['domain','prefix'];
				for (var i:String in over) {
					if ( (!isDebugging) || (skips.indexOf(i) == -1) ) {
						WmsAPI._overrides[i] = ((over[i] is String) && (over[i].length > 0)) ? over[i] : WmsAPI._overrides[i];
					}
				}
				
				var domain:String = URLUtils.domain_with_port_and_protocol(url);
				var prefix:String = URLUtils.url_prefix_sans_domain_name_and_protocol(url);
				
				domain = ( (WmsAPI._overrides.domain is String) && (WmsAPI._overrides.domain.length > 0) ) ? WmsAPI._overrides.domain : domain;
				prefix = ( (WmsAPI._overrides.prefix is String) && (WmsAPI._overrides.prefix.length > 0) ) ? WmsAPI._overrides.prefix : prefix;
				
				var menuType:String = '';
				menuType = (WmsAPI._overrides.menuType != null) ? WmsAPI._overrides.menuType : WmsAPI.symbol_loggedOut_token;
				
				var isReallyInternal:Boolean = ( (domain.length == 0) || (isInternal) );
				
				WmsAPI.external_domain = (isReallyInternal) ? WmsAPI.internal_domain : domain;
				
				WmsAPI.external_prefix = (isReallyInternal) ? WmsAPI.internal_prefix : prefix;
				
				var access_mode:Boolean = (isReallyInternal) ? false : true;
				WmsAPI.set_access_mode(access_mode,menuType);
				
				if ( (!isReallyInternal) && (!WmsAPI._disable_keepalive_timer) ) {
					WmsAPI._keepalive_callback = keepalive_callback;
					WmsAPI._keepalive_timer = new Timer(MathUtils.randomNumberRange(1,4.95)*60*1000);
					WmsAPI._keepalive_timer.addEventListener(TimerEvent.TIMER,
						function (event:TimerEvent):void {
							if (!WmsAPI._disable_keepalive_timer) {
								WmsAPI.perform_keepalive_callback();
							}
						}
					);
					WmsAPI._keepalive_timer.start();
				}
				
				WmsAPI._rollUpMenu_callback = callback;
			} catch (e:Error) { return false; }
			return true;
		}
		
	}
}