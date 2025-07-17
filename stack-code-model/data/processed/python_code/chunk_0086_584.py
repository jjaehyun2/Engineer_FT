package framework.model
{
	import flash.events.EventDispatcher;
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	import flash.utils.setTimeout;
	
	import framework.localization.Resources;
	import framework.managers.PopUpManagerExt;
	import framework.module.CashShiftModule;
	import framework.module.CheckInModule;
	import framework.module.CheckOutModule;
	import framework.module.CommonModule;
	import framework.module.DashboardModule;
	import framework.module.HotelsModule;
	import framework.module.HouseKeepingModule;
	import framework.module.InHouseModule;
	import framework.module.InvoiceManagmentModule;
	import framework.module.ProfilesModule;
	import framework.module.RatesModule;
	import framework.module.ReportsModule;
	import framework.module.ReservationCreateModule;
	import framework.module.ReservationEditModule;
	import framework.module.SecurityModule;
	import framework.module.TransactionModule;
	import framework.module.VATModule;
	import framework.view.pages.loader.LoaderPopupView;
	
	import mx.collections.ArrayCollection;
	import mx.containers.ViewStack;
	import mx.core.UIComponent;
	import mx.managers.PopUpManager;
	import mx.managers.PopUpManagerChildList;
	
	import services.data.RequestInfo;
	import services.vo.backend.MiscellaneousObjectVO;
	import services.vo.backend.RoomSettingsModuleVO;
	import services.vo.backend.RoomTypesModuleVO;
	import services.vo.businessDay.BusinessDayModule;
	import services.vo.frontend.LoggedInUserVO;
	import services.vo.frontend.LoginPageVO;
	import services.vo.response.ResponseVO;

	[Bindable]
	public class AppModelLocator extends EventDispatcher
	{
		// ===================================================================== //
		//                         VARIABLES AND CONSTANTS                       //
		// ===================================================================== //
		public var isTestShow:Boolean = false;
		/**
		 *  This property is <code>true</code> if user is log outed
		 *  from system.
		 *
		 *  @default false
		 */
		private var _isLogOut:Boolean = false;
		/**
		 *  This property is <code>false</code> if business day is close.
		 *
		 *  @default false
		 */
		private var _isBusinessDayOpen:Boolean = false;
		/**
		 *  This property is instance of blocked popup.
		 */
		private var progressPopup:LoaderPopupView;
		/**
		 *  This property is count of active remote calls. Also it is enable state
		 *  of system. If <code>value = 0</code>, system is enabled.
		 *
		 *  @default 0
		 */
		private var _appEnabled:int = 0;
		/**
		 *  This property is current business date in the system.
		 *
		 *  @default new Date()
		 */
		private var _businessDate:Date = new Date();
		/**
		 *  This property is current calendar date in the system.
		 *
		 *  @default new Date()
		 */
		private var _date:Date = new Date();
		/**
		 *  This property is last received response from server.
		 *
		 *  @default new ResponseVO()
		 *
		 *  @see services.vo.response.ResponseVO
		 */
		private var _lastResponse:ResponseVO = new ResponseVO();
		
		
		/**
		 *  This property is owner of system.
		 */
		private var _owner:UIComponent;

		private var _tmrCheckLock:Timer = new Timer(10000);

		private static var instance:AppModelLocator;

		/**
		 *  AppModelLocator. Constructor.
		 */
		public function AppModelLocator()
		{
			if(instance != null)
			{
				throw new Error("AppModelLocator is Singleton!");
			}
		}

		public static function getInstance():AppModelLocator
		{
			if(instance == null) 
			{
				instance = new AppModelLocator();
			}
			return instance;
		}
		
		// --------------------------------------------------------------------- //
		//                           -----------------                           //
		// --------------------------------------------------------------------- //

		public var workspaceViewList:Array = new Array();

		public var loginPage:LoginPageVO = new LoginPageVO();

		public var currentUser:LoggedInUserVO = new LoggedInUserVO();

		public var mainViewIndex:int = 0;

		public var frontendIndex:int = 0;

		public var backendIndex:int = 0;
		public var backendLabel:String = "";

		public var reportsList:Array = []; //one item - ReportVO

		public var isFrontend:Boolean;
		/**
		 *  This property contain current time by milliseconds.
		 *
		 *  @see Date#getTime()
		 */
		public var lCurrentTime:Number = (new Date()).getTime();
		
		/**
		 *  This property is information for last active request to server for get, save,
		 *  update, etc. operation.
		 *  
		 *  @see services.data.RequestInfo
		 */
		public var requestInfo:RequestInfo = new RequestInfo();
		
		// --------------------------------------------------------------------- //
		//                             SYSTEM MODULES                            //
		// --------------------------------------------------------------------- //
		/**
		 *  This property is common module.
		 *
		 *  @default new CommonModule()
		 *
		 *  @see framework.module.CommonModule
		 */
		private var _commonModule:CommonModule = new CommonModule();
		/**
		 *  This property is transaction module.
		 *
		 *  @default new TransactionModule()
		 *
		 *  @see framework.module.TransactionModule
		 */
		private var _transactionModule:TransactionModule = new TransactionModule();
		/**
		 *  This property is profiles module.
		 *
		 *  @default new ProfilesModule()
		 *
		 *  @see framework.module.ProfilesModule
		 */
		private var _profilesModule:ProfilesModule = new ProfilesModule();
		/**
		 *  This property is check out module.
		 *
		 *  @default new CheckOutModule()
		 *
		 *  @see framework.module.CheckOutModule
		 */
		private var _checkOutModule:CheckOutModule = new CheckOutModule();
		/**
		 *  This property is in house module.
		 *
		 *  @default new InHouseModuleVO()
		 *
		 *  @see framework.module.InHouseModuleVO
		 */
		private var _inHouseModule:InHouseModule = new InHouseModule();

		public var vatModule:VATModule = new VATModule();

		public var miscellaneousModule:MiscellaneousObjectVO = new MiscellaneousObjectVO();

		public var roomSettingsModule:RoomSettingsModuleVO = new RoomSettingsModuleVO();

		public var roomTypesModule:RoomTypesModuleVO = new RoomTypesModuleVO();

		public var dashboardModule:DashboardModule= new DashboardModule();

		public var hotelsModule:HotelsModule = new HotelsModule();

		public var ratesModule:RatesModule = new RatesModule();

		public var checkInModule:CheckInModule = new CheckInModule();

		public var reportsModule:ReportsModule = new ReportsModule();

		public var invoiceManagmentModule:InvoiceManagmentModule = new InvoiceManagmentModule();

		public var securityModule:SecurityModule = new SecurityModule();

		public var houseKeeperModule:HouseKeepingModule = new HouseKeepingModule();
		
		public var reservationCreateModule:ReservationCreateModule = new ReservationCreateModule();

		public var reservationEditModule:ReservationEditModule = new ReservationEditModule();

		public var cashShiftModule:CashShiftModule = new CashShiftModule();

		public var BDCModule:BusinessDayModule = new BusinessDayModule();
		
		// --------------------------------------------------------------------- //
		//                             VARs			                             //
		// --------------------------------------------------------------------- //		

		public var months:Array = [];
		public var days:ArrayCollection = new ArrayCollection();
		public var micellaneousModuleCurPage:int = 0;

		//public var backendPartNames:ArrayCollection = new ArrayCollection( ["Dashboard","Hotels", "Room Settings", "Room Types", "Transactions", "Rates", "Miscellaneous", "Reports", "Security", "Reservation", "Profiles", "Check In", "In House", "House Keeper"] );

		public var backendModuls:Array = [dashboardModule ,hotelsModule, roomSettingsModule, roomTypesModule, transactionModule, ratesModule.barModule, miscellaneousModule, reservationCreateModule, profilesModule, checkInModule, reportsModule, inHouseModule, securityModule, houseKeeperModule, reservationEditModule, cashShiftModule];

		public var currMonthIndex:Number;
		public var currYear:Number;

		public var maxDaysInMonth:Number;



		public var moduleView:ViewStack = new ViewStack();

		public var rhythmsList:ArrayCollection = new ArrayCollection(); //DataListVO

		public function isProduction():Boolean
		{
			return lastResponse.bIsProduction;
		}

		public function getLogin():String
		{
			return String(currentUser.cLogInUser.sUserLogin);
		}

		private function activateCheckLock():void
		{
			if (_tmrCheckLock.hasEventListener(TimerEvent.TIMER))
			{
				_tmrCheckLock.stop();
				_tmrCheckLock.removeEventListener(TimerEvent.TIMER, checkLock);
			}

			_tmrCheckLock.addEventListener(TimerEvent.TIMER, checkLock);
			_tmrCheckLock.reset();
			_tmrCheckLock.start();
		}

		private function checkLock(e:TimerEvent):void
		{
			_tmrCheckLock.removeEventListener(TimerEvent.TIMER, checkLock);
			_tmrCheckLock.stop();

		//	if ((progressPopup) && (appEnabled == 0))
			{
				PopUpManager.removePopUp(progressPopup);
				progressPopup = null;
			}
		}

		/**
		 *  Create/Remove progress bar pop up.
		 */
		private function popUpLoader():void
		{
			if (appEnabled != 0)
			{
				if (!progressPopup)
				{
					progressPopup = PopUpManager.createPopUp(owner, LoaderPopupView, true, PopUpManagerChildList.POPUP) as LoaderPopupView;
					PopUpManager.centerPopUp(progressPopup);
				}
			}
			else
			{
				PopUpManager.removePopUp(progressPopup);
				progressPopup = null;
			}
		}

		// ===================================================================== //
		//                       GETTER AND SETTER HANDLERS                      //
		// ===================================================================== //
		/**
		 *  This property is owner of system.
		 */
		public function get owner():UIComponent
		{
			return _owner;
		}
		/**
		 *  @private
		 */
		public function set owner(value:UIComponent):void
		{
			_owner = value;

			setTimeout(initialize, 500);
		}

		protected function initialize():void
		{
			// collect all months
			months = [locale.Global_Month_January,
					  locale.Global_Month_February,
					  locale.Global_Month_March,
					  locale.Global_Month_April,
					  locale.Global_Month_May,
					  locale.Global_Month_June,
					  locale.Global_Month_July,
					  locale.Global_Month_August,
					  locale.Global_Month_September,
					  locale.Global_Month_October,
					  locale.Global_Month_November,
					  locale.Global_Month_December];
			// collect all name of days
			days = new ArrayCollection(
				[locale.Global_Day_Sunday,
				 locale.Global_Day_Monday,
				 locale.Global_Day_Tuesday,
				 locale.Global_Day_Wednesday,
				 locale.Global_Day_Thursday,
				 locale.Global_Day_Friday,
				 locale.Global_Day_Saturday]);
			
		}

		/**
		 *  The state of user (log in/out) into the system.
		 */
		public function get isLogOut():Boolean
		{
			return _isLogOut;
		}
		/**
		 *  @private
		 */
		public function set isLogOut(value:Boolean):void
		{
			_isLogOut = value;
			// if user is log out from system - remove all popups
			if (!_isLogOut)
			{
				PopUpManagerExt.removeAll();
			}

			cashShiftModule.clear();
		}

		/**
		 *  The state of user (log in/out) into the system.
		 */
		public function get isBusinessDayOpen():Boolean
		{
			return _isBusinessDayOpen;
		}
		/**
		 *  @private
		 */
		public function set isBusinessDayOpen(value:Boolean):void
		{
			_isBusinessDayOpen = value;
		}

		/**
		 *  The count of active remote calls. Also it is enable state
		 *  of system.
		 */
		public function get appEnabled():int
		{
			return _appEnabled;
		}
		/**
		 *  @private
		 */
		public function set appEnabled(value:int):void
		{
			_appEnabled = Math.max(0, value);

			popUpLoader();

			if (_appEnabled == 0)
			{
				activateCheckLock();
			}
		}

		/**
		 *  The current business date in the system.
		 */
		public function get businessDate():Date
		{
			return _businessDate;
		}
		/**
		 *  @private
		 */
		public function set businessDate(value:Date):void
		{
			_businessDate = value;
		}

		/**
		 *  The current calendar date in the system.
		 */
		public function get date():Date
		{
			return _date;
		}
		/**
		 *  @private
		 */
		public function set date(value:Date):void
		{
			_date = value;
		}

		/**
		 *  The last received response from server by remote call.
		 */
		public function get lastResponse():ResponseVO
		{
			return _lastResponse;
		}
		/**
		 *  @private
		 */
		public function set lastResponse(value:ResponseVO):void
		{
			_lastResponse = value;
		}

		// --------------------------------------------------------------------- //
		//                             SYSTEM MODULES                            //
		// --------------------------------------------------------------------- //
		/**
		 *  The transaction module.
		 */
		public function get commonModule():CommonModule
		{
			return _commonModule;
		}
		/**
		 *  @private
		 */
		public function set commonModule(value:CommonModule):void
		{
			_commonModule = value;
		}

		/**
		 *  The transaction module.
		 */
		public function get transactionModule():TransactionModule
		{
			return _transactionModule;
		}
		/**
		 *  @private
		 */
		public function set transactionModule(value:TransactionModule):void
		{
			_transactionModule = value;
		}

		/**
		 *  The profiles module.
		 */
		public function get profilesModule():ProfilesModule
		{
			return _profilesModule;
		}
		/**
		 *  @private
		 */
		public function set profilesModule(value:ProfilesModule):void
		{
			_profilesModule = value;
		}

		/**
		 *  The check out module.
		 */
		public function get checkOutModule():CheckOutModule
		{
			return _checkOutModule;
		}
		/**
		 *  @private
		 */
		public function set checkOutModule(value:CheckOutModule):void
		{
			_checkOutModule = value;
		}

		/**
		 *  The in house module.
		 */
		public function get inHouseModule():InHouseModule
		{
			return _inHouseModule;
		}
		/**
		 *  @private
		 */
		public function set inHouseModule(value:InHouseModule):void
		{
			_inHouseModule = value;
		}
		
		
		private var _locale:Resources = new Resources();
		public function get locale():Resources
		{
			return _locale;
		}	
		public function set locale(value:Resources):void
		{
			_locale = value;
		}
	}
}