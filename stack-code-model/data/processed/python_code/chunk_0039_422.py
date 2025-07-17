package framework.module
{
	import services.vo.cashShift.BusinessDayVO;
	import services.vo.cashShift.CashierVO;
	

	[Bindable]
	public class CashShiftModule implements IModule
	{
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
		 *  @default ["Cash Shift"]
		 */
		private var _pageNames:/* String */Array = ["Cash Shift"];
		
		public var currOpenShift:CashierVO = new CashierVO();
		public var selectedShift:CashierVO = new CashierVO();
		
		
		public var currBusinessDay: BusinessDayVO = new BusinessDayVO();
		public var cashShiftList:Array; //
		public var cashShiftPaymantList:Array; //
		
		
		/**
		 *  Clear neccessary data.
		 */
		public function clear():void
		{
			currOpenShift = new CashierVO();
			currBusinessDay = new BusinessDayVO();
			cashShiftList = [];
			cashShiftPaymantList = [];
		}
		// ----------------------------------------------------------------------- //
		//                           INTERFACE METHODS                             //
		// ----------------------------------------------------------------------- //
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
	}
}