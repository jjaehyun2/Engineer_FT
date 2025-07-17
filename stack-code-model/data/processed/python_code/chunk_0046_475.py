package framework.module
{
	import services.vo.profiles.CompanyProfileVO;
	import services.vo.profiles.ProfilePersonalVO;
	
	import mx.collections.ArrayCollection;
	
	[Bindable]
	public class ProfilesModule implements IModule
	{
		// ----------------------------------------------------------------- //
		//                        COMMON VARIABLES                           //
		// ----------------------------------------------------------------- //
		/**
		 *  This property is type of module.
		 *  
		 *  @default -1
		 */
		private var _type:int = -1;
		/**
		 *  This property is index of current viewed page in Items
		 *  Groups module.
		 *  
		 *  @default 0
		 */
		private var _currPage:int = 0;
		/**
		 *  This property is all name of pages are existing in Items
		 *  Groups module.
		 *  
		 *  @default []
		 */
		private var _pageNames:/* String */Array = [];
		
		// ----------------------------------------------------------------- //
		//                  INDIVIDUAL PROFILES VARIABLES                    //
		// ----------------------------------------------------------------- //
		/**
		 *  This property contain current active individual profile by person.
		 *  
		 *  @see framework.vo.profiles.ProfilePersonalVO
		 *  
		 *  @default new ProfilePersonalVO()
		 */
		public var currentProfile:ProfilePersonalVO = new ProfilePersonalVO();
		
		/**
		 *  This property contain list of profiles by page.
		 *  
		 *  @see framework.vo.profiles.ProfilePersonViewVO
		 *  
		 *  @default new ArrayCollection()
		 */
		public var individualPageList:/* ProfilePersonViewVO */ArrayCollection = new ArrayCollection();
		/**
		 *  This property contain the count of profiles having got them last
		 *  time.
		 *  
		 *  @default 0
		 */
		public var individualProfilesCount:Number = 0;
		// ----------------------------------------------------------------- //
		//                     COMPANY PROFILES VARIABLES                    //
		// ----------------------------------------------------------------- //
		/**
		 *  This property contain current active profile by company.
		 *  
		 *  @see framework.vo.profiles.CompanyProfileVO
		 *  
		 *  @default new CompanyProfileVO()
		 */
		public var curCompanyProfile:CompanyProfileVO = new CompanyProfileVO();
		
		/**
		 *  This property contain list of company profiles by page.
		 *  
		 *  @see framework.vo.profiles.CompanyProfileViewVO
		 *  
		 *  @default new ArrayCollection()
		 */
		public var companyProfileList:/* CompanyProfileViewVO */ArrayCollection = new ArrayCollection();
		/**
		 *  This property contain the count of company profiles having got
		 *  them last time.
		 *  
		 *  @default 0
		 */
		public var companyProfileCount:Number = 0;
		
		
		
		
		public var wishesList:ArrayCollection= new ArrayCollection();
		
		public var currSearchField:String="";
		public var addressByZip:ArrayCollection = new ArrayCollection();
		public var travelAgencyList:ArrayCollection = new ArrayCollection();
		/**
		 *  This property contain the count of travel agencies profiles
		 *  having got them last time.
		 *  
		 *  @default 0
		 */
		public var travelAgencyProfileCount:Number = 0;
		/**
		 *  This property contain current active travel agency.
		 *  
		 *  @see framework.vo.profiles.CompanyProfileVO
		 *  
		 *  @default new CompanyProfileVO()
		 */
		public var curTravelAgency:CompanyProfileVO = new CompanyProfileVO();
		
		// ----------------------------------------------------------------- //
		//                          COMMON METHODS                           //
		// ----------------------------------------------------------------- //
		/**
		 *  TransactionModule. Constructor.
		 */
		public function ProfilesModule()
		{
			type = ModuleType.FRONTEND;
		}
		
		// ----------------------------------------------------------------- //
		//                        INTERFACE METHODS                          //
		// ----------------------------------------------------------------- //
		/**
		 *  Index of current viewed page.
		 */
		public function get currPage():int
		{
			return _currPage;
		}
		/**
		 *  @private
		 */
		public function set currPage(value:int):void
		{
			_currPage = value;
		}
		
		/**
		 *  Name of pages are existing in Items Groups module.
		 */
		public function get pageNames():Array
		{
			return _pageNames;
		}
		/**
		 *  @private
		 */
		public function set pageNames(value:Array):void
		{
			_pageNames = value;
		}
		
		/**
		 *  Type of the module.
		 */
		public function get type():int
		{
			return _type;
		}
		/**
		 *  @private
		 */
		public function set type(value:int):void
		{
			_type = value;
		}
		/**
		 *  Clear neccessary data.
		 */
		public function clear():void
		{
			
		}
	}
}