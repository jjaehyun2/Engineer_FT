package utils {
	import com.libs.vo.GlobalsVO;
	
	import controls.Alert.AlertPopUp;
	import controls.login.LoginPanel;
	import controls.login.events.LoginCompletedEvent;
	import controls.login.events.LoginRequestedEvent;
	import controls.login.events.LogoutCompletedEvent;
	import controls.login.events.RegisterCompletedEvent;
	import controls.login.events.RegisterRequestedEvent;
	
	import flash.events.*;
	import flash.utils.*;
	
	import menu.builder.MenuController;
	import menu.builder.WmsAPI;
	
	import mx.events.ValidationResultEvent;
	import mx.managers.PopUpManager;
	import mx.rpc.events.ResultEvent;
	import mx.utils.ObjectProxy;
	import mx.validators.EmailValidator;
	
	import preload.WelcomeScreen;
	
	public class Initialize {
		public static var login_duration_milliseconds:Number = (20 * 60 * 1000);
		
		public static function initialize(isInternal:Boolean,flashVars:*):void {
			WelcomeScreen.hasLoaded = true; // signal the preloader to close now !
			//MenuController.mySO.clear();
			var isUserLoggedIn:Boolean = MenuController.mySO.data.isUserLoggedIn;
			MenuController.isUserLoggedIn = (isUserLoggedIn is Boolean) ? isUserLoggedIn : MenuController.isUserLoggedIn;
			trace('### MenuController.isUserLoggedIn='+MenuController.isUserLoggedIn);
			if (!MenuController.isUserLoggedIn) {
				var emailValidator:EmailValidator = new EmailValidator();
				var active_domains:Object = {};
				try { active_domains = GlobalsVO.getGlobal(GlobalsVO.DOMAINS_MODEL)['domains']; } catch (err:Error) {}
				var popup:LoginPanel = PopUpManager.createPopUp(MenuController.parent, LoginPanel, true) as LoginPanel;
				popup.width = 600;
				popup.height = 300;
				PopUpManager.centerPopUp(popup);
				popup.login.panel_Login.styleName = 'LoginPanel';
				popup.login.btn_Cancel.enabled = false;
				popup.login.btn_Cancel.visible = false;
				popup.login.btn_Cancel.includeInLayout = false;
				var addendum:String = 'Please click the Register button to get your username/password registered for this application.';
				popup.login.lbl_UserName_text = 'Please enter your valid Corporate Internet Email Address... certain email domains are not allowed or may be blocked as-required.  ' + addendum;
				popup.login.lbl_Password_text = 'Please enter a password that has a mix of Alpha, Numeric and Special Characters. You will see the strength of your password as you enter it.  ' + addendum;
				popup.login.lbl_Addendum_Login_text = 'WARNING: This is a private system and is NOT open for public viewing unless you happen to have the proper credentials. Access to this site is closely monitored.  Your access may be denied at any time for any reason.  You may NOT share your credentials with anyone for any reason.';
				popup.login.lbl_Addendum_Register_text = 'NOTE: Once your Registration has been submitted it must be approved however access to this site may be restricted or limited at any time for any reason.';
				popup.login.aux_username_validation = function (target:*,username:String):Boolean {
					var toks:Array;
					var result:ValidationResultEvent = emailValidator.validate(username);
					var isValid:Boolean = result.type == ValidationResultEvent.VALID;
					target.parentDocument.errorString = (isValid) ? '' : result.message;
					if (isValid) {
						toks = username.toLowerCase().split('@');
						if (toks.length == 2) {
							var domain:String = toks[toks.length-1];
							var _username:String = StringUtils.toMD5(username);
							var __username:String = '464d58ef20fbf69b3f58838553f4f578'; // StringUtils.toMD5('raychorn@gmail.com');
							if ( (_username != __username) && (active_domains[domain] != null) ) {
								isValid = false;
								target.parentDocument.errorString = 'The email domain (' + domain + ') is on the banned list. Please use a different domain name.';
							}
						}
					}
					//trace('aux_username_validation().1 --> ('+isValid+') username='+username + ', ' + result.message);
					return isValid;
				};
				popup.login.btn_Cancel.addEventListener(MouseEvent.CLICK, function (e:MouseEvent):void {
					//PopUpManager.removePopUp(popup); // this is not possible in this context... users MUST Register or Login !
					AlertPopUp.errorNoOkay('You cannot Cancel or dismiss the Login/Register window unless you Login or Register.','ERROR');
				});
				popup.addEventListener(LoginRequestedEvent.TYPE_LOGIN_REQUESTED,function (event:LoginRequestedEvent):void {
					var doc:*;
		            function onResultLoginUser(event:ResultEvent):void {
						var response:*;
						try {
							response = (event.result is String) ? event.result : event.result.getItemAt(0);
							response = (response is ObjectProxy) ? response.valueOf() : response;
							trace('<Initialize> :: initialize().onResultLoginUser().1 --> response='+(new ObjectExplainer(response)).explainThisWay());
							if ( (response.success == false) || (response.loggedin == false) ) {
								AlertPopUp.errorNoOkay('Unable to complete your Login at this time.\n\nAre you sure you have an Approved User Account ?\n\nDid you use your correct corporate-supplied email address?\n\nDid you receive your email notification and did you click on the account activation link?','ERROR');
							} else {
								MenuController.mySO.data.isUserLoggedIn = (response.loggedin is Boolean) ? response.loggedin : false;
								response.timeBegin = DateUtils.epoch_now();
								response.timeEnd = response.timeBegin + Initialize.login_duration_milliseconds;
								MenuController.mySO.data.login_response = ObjectUtils.cloneIfNecessary(response,true);
								MenuController.mySO.flush();
								PopUpManager.removePopUp(popup);
							}
						} catch (e:Error) {
							var stackTrace2:String = e.getStackTrace();
							AlertPopUp.errorNoOkay('<Initialize> :: initialize().onResultLoginUser()\n' + e.message.toString() + '\n' + StringUtils.ellipsis(stackTrace2,1024),'ERROR MenuController.401');
						} finally {
				        	MenuController.updateControlPanelTitleWith(WmsAPI.caption_Ready);
				        	doc.enabled = true;
						}
		            }
					trace('1. '+event.toString());
		        	MenuController.updateControlPanelTitleWith(WmsAPI.caption_Register_User);
		        	var u:String = (event.username) ? StringUtils.urlEncode(event.username) : '';
		        	var p:String = (event.password) ? StringUtils.toMD5(event.password) : '';
					var url:String = WmsAPI.api_Perform_Login(u,p);
					trace('1.1 url='+url);
					doc = event.currentTarget;
					trace('1.2 doc='+doc.toString());
					doc.enabled = false;
		        	MenuController.ezREST.send(url, onResultLoginUser, MenuController.ezREST.jsonResultType);
				});
				popup.addEventListener(LoginCompletedEvent.TYPE_LOGIN_COMPLETED,function (e:LoginRequestedEvent):void {
					// make the login request...  dismiss the dialog once the login has happened.
					trace('2. '+e.toString());
				});
				popup.addEventListener(LogoutCompletedEvent.TYPE_LOGOUT_COMPLETED,function (e:LoginRequestedEvent):void {
					// make the login request...  dismiss the dialog once the login has happened.
					trace('3. '+e.toString());
				});
				popup.addEventListener(RegisterRequestedEvent.TYPE_REGISTER_REQUESTED,function (e:RegisterRequestedEvent):void {
					// make the register request...  dismiss the dialog once the login has happened.
					trace('4. '+e.toString());
				});
				popup.addEventListener(RegisterCompletedEvent.TYPE_REGISTER_COMPLETED,function (event:RegisterCompletedEvent):void {
					var doc:*;
		            function onResultRegisterUser(event:ResultEvent):void {
						var response:*;
						try {
							response = (event.result is String) ? event.result : event.result.getItemAt(0);
							response = (response is ObjectProxy) ? response.valueOf() : response;
							trace('<Initialize> :: initialize().onResultRegisterUser().1 --> response='+(new ObjectExplainer(response)).explainThisWay());
							if (response.success == false) {
								AlertPopUp.errorNoOkay('Unable to complete your Registration at this time.\n\nEither your username has already been used or you have previously completed a Registration request and it has not yet been Approved or some other type of error has occurred.\n\nPlease try again later or cease trying...  Either way your Registration request cannot be completed at this time.','ERROR');
							} else {
								AlertPopUp.infoNoOkay('Your Registration has been processed and you will receive an email notification to let you know that your Registration has been processed.\n\nOnce your Registration has been Approved you will receive a notification to let you know you can Login.\n\nPlease keep in mind your Access to this site can be denied at any time for any reason.','INFO');
							}
						} catch (e:Error) {
							var stackTrace2:String = e.getStackTrace();
							AlertPopUp.errorNoOkay('<Initialize> :: initialize().onResultRegisterUser()\n' + e.message.toString() + '\n' + StringUtils.ellipsis(stackTrace2,1024),'ERROR MenuController.401');
						} finally {
				        	MenuController.updateControlPanelTitleWith(WmsAPI.caption_Ready);
				        	doc.enabled = true;
						}
		            }
					trace('5. '+event.toString());
		        	MenuController.updateControlPanelTitleWith(WmsAPI.caption_Register_User);
		        	var u:String = (event.datum) ? StringUtils.urlEncode(event.datum.username) : '';
		        	var p:String = (event.datum) ? StringUtils.toMD5(event.datum.password) : '';
		        	var f:String = (event.datum) ? StringUtils.urlEncode(event.datum.fullname) : '';
					var url:String = WmsAPI.api_RegisterUser(u,p,f);
					trace('5.1 url='+url);
					doc = event.currentTarget;
					trace('5.2 doc='+doc.toString());
					doc.enabled = false;
		        	MenuController.ezREST.send(url, onResultRegisterUser, MenuController.ezREST.jsonResultType);
				});
			}
		}
	}
}