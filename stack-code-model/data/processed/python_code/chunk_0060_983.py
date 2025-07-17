package framework.module
{
	//import flash.utils.Dictionary;
	import flash.utils.Dictionary;
	
	import framework.view.pages.checkOut.data.AccountData;
	import framework.view.pages.checkOut.data.PaymentData;
	
	import mx.collections.ArrayCollection;
	
	import services.vo.checkOut.itemRouting.AccountAddressVO;
	import services.vo.checkOut.itemRouting.AppliedItemsVO;
	import services.vo.checkOut.itemRouting.ItemCheckOutVO;
	import services.vo.checkOut.itemRouting.ItemsRoutingVO;
	import services.vo.checkOut.itemRouting.PackageItemsVO;
	import services.vo.checkOut.itemRouting.PaymentVO;
	import services.vo.checkOut.itemRouting.PersonAccountsVO;
	import services.vo.checkOut.itemRouting.ReservationSummaryCheckOutVO;
	import services.vo.checkOut.payment.CheckoutPaymentVO;
	import services.vo.checkOut.payment.DebitorPaymentVO;
	import services.vo.inHouse.CheckOutReportsListVO;
	import services.vo.inHouse.InHouseViewVO;
	import services.vo.profiles.ProfilePersonalVO;
	
	[Bindable]
	public class CheckOutModule
	{
		// ================================================================= //
		//                           CONSTANTS                               //
		// ================================================================= //
		/**
		 *  These constants are indexes of pages used in module.
		 */
		public static const CHECKOUT_GUESTS_VIEW:int = 0;
		public static const CHECKOUT_ITEMS_ROUTING:int = 1;
		public static const CHECKOUT_PAYMENTS:int = 2;
		/**
		 *  This constant is payment types.
		 *  
		 *  @see framework.view.pages.checkOut.data.PaymentData
		 *  @see framework.vo.checkOut.itemRouting.PaymentVO
		 */
		public static const paymentTypes:ArrayCollection = new ArrayCollection(
			[new PaymentData("Cash", PaymentVO.TYPE_CASH, ""),
			 new PaymentData("Credit Card", PaymentVO.TYPE_CARD, "CreditCard"),
			 new PaymentData("Debitor", PaymentVO.TYPE_DEPOSIT)]);
		
		// ================================================================= //
		//                           VARIABLES                               //
		// ================================================================= //
		/**
		 *  This property is current active page or tab for CheckOut module.
		 *  
		 *  @default CHECKOUT_GUESTS_VIEW
		 *  
		 *  @see framework.module.CheckOutModule#CHECKOUT_GUESTS_VIEW
		 */
		private var _currPage:int = CHECKOUT_GUESTS_VIEW;
		/**
		 *  This property is previous active page or tab for CheckOut module.
		 *  
		 *  @default CHECKOUT_GUESTS_VIEW
		 *  
		 *  @see framework.module.CheckOutModule#CHECKOUT_GUESTS_VIEW
		 */
		private var _prevPage:int = CHECKOUT_GUESTS_VIEW;
		/**
		 *  List of guest CheckOutGuestListVO
		 *  
		 *  @default new ArrayCollection
		 *  
		 *  @see framework.vo.checkOut.CheckOutGuestListVO
		 */
		public var guestList:/* CheckOutGuestListVO */ArrayCollection = new ArrayCollection();		
		
		public var needGuestListUpdate:Boolean = false;
		
		/**
		 *  count guest
		 *  
		 *  
		 */
		public var totalPage:int;
		
		public var guest:ProfilePersonalVO;
		
		public var reservationSummary:ReservationSummaryCheckOutVO = new ReservationSummaryCheckOutVO();
		public var paymentLineId:Number = 0;
		/**
		 *  This property is type of room from which will check out guest.
		 *  Type of rooms are normal, virtual and conference.
		 *  
		 *  @defaut InHouseViewVO.TYPE_NORMAL
		 *  
		 *  @see framework.vo.inHouse.InHouseViewVO
		 */
		public var roomType:int = InHouseViewVO.TYPE_NORMAL;
		/**
		 *  This property is items added to guest who check out from hotel.
		 *  
		 *  @see framework.vo.checkOut.itemRouting.ItemCheckOutVO
		 */
		public var addedItems:/* ItemCheckOutVO */ArrayCollection = new ArrayCollection();
		public var appliedItems:/* AppliedItemsVO */ArrayCollection = new ArrayCollection();
		public var packages:/* PackageItemVO */ArrayCollection = new ArrayCollection();
		public var paymentItems:/* CheckoutPaymentVO */ArrayCollection = new ArrayCollection();
		public var routedPaymentItems:/* CheckoutPaymentVO */ArrayCollection = new ArrayCollection();
		public var routingItems:/* ItemCheckOutVO */ArrayCollection = new ArrayCollection();
		
		public var profileIds:/* ProfilePersonalVO */Array = new Array();
		
		/**
		 *  This property is items were attached to guest who check out from hotel.
		 *  
		 *  @see framework.vo.checkOut.itemRouting.ItemCheckOutVO
		 */
		public var attachedItems:Dictionary = new Dictionary(true);
		
		public var accounts:/* PersonAccountsVO */ArrayCollection = new ArrayCollection();
		
		public var invoiceURL:String = "";
		
		public var acceptPaymentData:CheckOutReportsListVO = new CheckOutReportsListVO();
		
		/**
		 *  This property is associate list with attached items views.
		 *  
		 *  @default new Dictionary(true)
		 */
		private var _attachedItemsView:Dictionary = new Dictionary(true);
		/**
		 *  This property is associate list with payment views.
		 *  
		 *  @default new Dictionary(true)
		 */
		private var _paymentItemsView:Dictionary = new Dictionary(true);
		
		/**
		 *  This property is special payments such as CASH, CREDIT CARD, etc.
		 *  
		 *  @default []
		 */
		private var _specialPaymentItems:/* DebitorPaymentVO */Array = [];
		
		public function CheckOutModule()
		{
			// make special global items for payments
			for(var i:int = 0; i < paymentTypes.length; i++)
			{
				var type:PaymentData = (paymentTypes.getItemAt(i) as PaymentData);
				var globalItem:DebitorPaymentVO = new DebitorPaymentVO();
				globalItem.lId = -i;
				globalItem.iPaymentType = type.type;
				globalItem.sDescription = type.name;
				
				_specialPaymentItems[i] = globalItem;
			}
		}
		
		public function updateCheckOutState(itemRoutingData:ItemsRoutingVO):void
		{
			if (!itemRoutingData) itemRoutingData = new ItemsRoutingVO();
			
			var appliedItem:AppliedItemsVO;
			
			paymentLineId = itemRoutingData.lPaymentLineId;
			// accounts to apply items from guest to some each of this account
			accounts = new ArrayCollection(itemRoutingData.aMapAccounts);
			//
			var aAddedItems:Array = itemRoutingData.aNotRoutedItems;
			var aAppliedItems:Array = itemRoutingData.aAppliedItems;
			var aPayments:Array = itemRoutingData.aPayments;
			var aRoutedPayments:Array = itemRoutingData.aRoutedPayments;
			var aPackages:Array = itemRoutingData.aPackages;
			
			var aRoutingItems:Array = aAddedItems.slice();
			for each(appliedItem in aAppliedItems)
			{
				// set applied state state
				for(var i:int = 0; i < appliedItem.aItems.length; i++)
				//for each(var item:ItemCheckOutVO in aAddedItems.aItems)
				{
					var item:ItemCheckOutVO = appliedItem.aItems[i] as ItemCheckOutVO;
					item.bIsChecked = true;
				}
				// grab all items to applied to guest (routed and not routed)
				aRoutingItems = aRoutingItems.concat(appliedItem.aItems);
			}
			
			var payment:CheckoutPaymentVO;
			var paymentItem:ItemCheckOutVO;
			// check payments
			for each(payment in aPayments)
			{
				paymentItem = new ItemCheckOutVO();
				paymentItem.lId = payment.lId;
				paymentItem.fPrice = payment.fValue;
				paymentItem.dDate = payment.dDate;
				paymentItem.sTransName = payment.sName;
				paymentItem.iPaymentType = payment.iType;
				paymentItem.bIsChecked = true;
				paymentItem.bIsPayment = true;
				
				aRoutingItems.push(paymentItem);
			}
			
			// check payments by accounts
			for each(payment in aRoutedPayments)
			{
				paymentItem = new ItemCheckOutVO();
				paymentItem.lId = payment.lId;
				paymentItem.fPrice = payment.fValue;
				paymentItem.dDate = payment.dDate;
				paymentItem.sTransName = payment.sName;
				paymentItem.iPaymentType = payment.iType;
				paymentItem.lAppliedPayment = payment.lAppliedPayment;
				paymentItem.bIsChecked = true;
				paymentItem.bIsPayment = true;
				
				aRoutingItems.push(paymentItem);
			}
			// check packages
			for each(var ipackage:PackageItemsVO in aPackages)
			{
				var packageItem:ItemCheckOutVO = new ItemCheckOutVO();
				
				packageItem.lId = ipackage.lPackageId;
				packageItem.fPrice = ipackage.fSum;
				packageItem.dDate = "";
				packageItem.sTransName = "[PACKAGE] " + ipackage.sPackageName;
				packageItem.aPackageItems = ipackage.aItems;
				packageItem.bIsPackage = true;
				packageItem.bIsChecked = (ipackage.lAppliedAccount && ipackage.lAppliedAccount > 0);
				
				aRoutingItems.push(packageItem);
				// check applying package to some account
				if ((ipackage.lPaymentId) && (ipackage.lPaymentId > 0))
				{
					var isAdded:Boolean = false;
					for each(appliedItem in aAppliedItems)
					{
						if (appliedItem.lAccountId == ipackage.lAppliedAccount)
						{
							appliedItem.aItems.push(packageItem);
							isAdded = true;
							break;
						}
					}
					if (!isAdded)
					{
						appliedItem = new AppliedItemsVO();
						appliedItem.lPaymentId = ipackage.lPaymentId;
						
						var accountData:AccountData = getAccountById(ipackage.lAppliedAccount);
						//var accountData:AccountData = new AccountData();
						
						appliedItem.lAccountId = accountData.id;
						appliedItem.iType = accountData.type;
						appliedItem.aItems.push(packageItem);
						
						aAppliedItems.push(appliedItem);
					}
				}
			}
			
			routingItems = new ArrayCollection(aRoutingItems);
			addedItems = new ArrayCollection(aAddedItems);
			appliedItems = new ArrayCollection(aAppliedItems);
			packages = new ArrayCollection(aPackages);
			routedPaymentItems = new ArrayCollection(aRoutedPayments);
		}
		
		public function clear():void
		{
			routingItems.removeAll();
			addedItems.removeAll();
			appliedItems.removeAll();
			packages.removeAll();
			routedPaymentItems.removeAll();
			
			//attachedItems = new Dictionary(true);
			//attachedItemsView = new Dictionary(true);
		}
		
		/**
		 *  Get account data by id such as company name or guest name and address by
		 *  name of owner account.
		 *  
		 *  @param id:Number - id of account.
		 *  
		 *  @return account data
		 */
		private function getAccountById(id:Number):AccountData
		{
			var accounts:ArrayCollection = accounts;
			for each(var account:PersonAccountsVO in accounts)
			{
				for each(var address:AccountAddressVO in account.aAddresses)
				{
					if (address.lId == id)
					{
						var res:AccountData = new AccountData(account.sCompanyName, account.sGuestName, address.sAddress);
						res.id = address.lId;
						res.type = account.iType;
						return res;
					}
				}
			}
			
			return new AccountData();
		}
		
		// ===================================================================== //
		//                       GETTER AND SETTER HANDLERS                      //
		// ===================================================================== //
		/**
		 *  The current active page or tab for CheckOut module.
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
			// save previous active page
			_prevPage = _currPage;
			// update page
			_currPage = value;
		}
		
		/**
		 *  The previous active page or tab for CheckOut module.
		 */
		public function get prevPage():int
		{
			return _prevPage;
		}
		/**
		 *  @private
		 */
		public function set prevPage(value:int):void
		{
			_prevPage = value;
		}
		
		/**
		 *  Associate list with attached items views.
		 */
		public function get attachedItemsView():Dictionary
		{
			return _attachedItemsView;
		}
		/**
		 *  @private
		 */
		public function set attachedItemsView(value:Dictionary):void
		{
			_attachedItemsView = value;
		}
		
		/**
		 *  Associate list with payment views.
		 */
		public function get paymentItemsView():Dictionary
		{
			return _paymentItemsView;
		}
		/**
		 *  @private
		 */
		public function set paymentItemsView(value:Dictionary):void
		{
			_paymentItemsView = value;
		}
		
		/**
		 *  Special payments such as CASH, CREDIT CARD, etc.
		 */
		public function get specialPaymentItems():Array
		{
			return _specialPaymentItems.slice();
		}
		/**
		 *  @private
		 */
		public function set specialPaymentItems(value:Array):void
		{
			_specialPaymentItems = value;
		}
	}
}