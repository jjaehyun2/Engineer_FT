package services.controller
{
	import com.adobe.cairngorm.control.FrontController;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.business.common.CommonDelegate;
	import services.business.hotels.HotelsDelegate;
	import services.business.inHouse.InHouseDelegate;
	import services.business.items.ItemsDelegate;
	import services.business.profiles.ProfileDelegate;
	import services.command.BDC.CheckDepartureCommand;
	import services.command.BDC.CheckProfilesCommand;
	import services.command.BDC.CheckShiftsCommand;
	import services.command.BDC.GetAnnomalyPersonCommand;
	import services.command.BDC.PostTransactionsCommand;
	import services.command.BDC.RollBusinessDayCommand;
	import services.command.BDC.TotalLogoutCommand;
	import services.command.BDC.UpdateRoomStatesCommand;
	import services.command.backend.AddCityCommand;
	import services.command.backend.AddLocationCommand;
	import services.command.backend.GetCommonDictionariesCommand;
	import services.command.backend.GetHotelCommonRoomTypesCommand;
	import services.command.backend.GetHotelDictionariesCommand;
	import services.command.backend.GetRoomListCommand;
	import services.command.backend.GetStatusListCommand;
	import services.command.backend.LoginInHotelCommand;
	import services.command.backend.SetHotelRoomStatusCommand;
	import services.command.cashShift.CloseShiftCommand;
	import services.command.cashShift.GetDayShiftListCommand;
	import services.command.cashShift.GetLastOpenShiftCommand;
	import services.command.cashShift.GetShiftPaymentListCommand;
	import services.command.cashShift.OpenNextShiftCommand;
	import services.command.cashShift.ReopenShiftCommand;
	import services.command.cashShift.StartNewBusinessDayCommand;
	import services.command.checkIn.GetCheckInDataCommand;
	import services.command.checkIn.SaveCheckInDataCommand;
	import services.command.checkIn.SetAssignCheckInDataCommand;
	import services.command.checkOut.AcceptPaymentsCommand;
	import services.command.checkOut.AddDebitorPaymentCommand;
	import services.command.checkOut.AddNewItemsCommand;
	import services.command.checkOut.AddPaymentCommand;
	import services.command.checkOut.AddPaymentsCommand;
	import services.command.checkOut.AdjustItemCommand;
	import services.command.checkOut.AttachItemToAccountCommand;
	import services.command.checkOut.AttachPackageToAccountCommand;
	import services.command.checkOut.DeleteItemCommand;
	import services.command.checkOut.DeletePaymentCommand;
	import services.command.checkOut.DetachItemToAccountCommand;
	import services.command.checkOut.DetachPackageFromAccountCommand;
	import services.command.checkOut.DetachPaymentsFromAccountCommand;
	import services.command.checkOut.GetCheckoutStateCommand;
	import services.command.checkOut.GetCheckoutStateFromInHouseCommand;
	import services.command.checkOut.GetCheckoutStateFromInvoiceCommand;
	import services.command.checkOut.GetGuestListCommand;
	import services.command.checkOut.GetItemsRoutingCommand;
	import services.command.checkOut.GetReservationSummaryCommand;
	import services.command.checkOut.MergeItemsCommand;
	import services.command.checkOut.PrintActualReportCommand;
	import services.command.checkOut.PrintDebitReportCommand;
	import services.command.checkOut.SplitItemCommand;
	import services.command.checkOut.UnmergeItemCommand;
	import services.command.common.GetDataListByTypeCodeCommand;
	import services.command.common.GetDataListByTypeCommand;
	import services.command.common.GetMarketCodesCommand;
	import services.command.common.GetSourceCodesCommand;
	import services.command.common.GetSystemDateCommand;
	import services.command.frontend.CheckAnswerCommand;
	import services.command.frontend.CheckLoginCommand;
	import services.command.frontend.ConfirmFirstLoginCommand;
	import services.command.frontend.GetAddressByZipCommand;
	import services.command.frontend.GetCardOfCommand;
	import services.command.frontend.GetCityCommand;
	import services.command.frontend.GetCreditTypeCommand;
	import services.command.frontend.GetHotelChainCommand;
	import services.command.frontend.GetRoomListByOrderCommand;
	import services.command.frontend.LoginCommand;
	import services.command.frontend.SetNewPasswordCommand;
	import services.command.hotels.AddFloorCommand;
	import services.command.hotels.AddRoomCommand;
	import services.command.hotels.AddRoomListCommand;
	import services.command.hotels.DeleteHotelCommand;
	import services.command.hotels.DeleteHotelRoomCommand;
	import services.command.hotels.DeleteHotelStageCommand;
	import services.command.hotels.GetHotelRoomSettingsCommand;
	import services.command.hotels.GetHotelRoomTypesCommand;
	import services.command.hotels.GetHotelStageListCommand;
	import services.command.hotels.GetHotelsListCommand;
	import services.command.hotels.GetRealRoomTypeListCommand;
	import services.command.hotels.SaveHotelRoomSettingsCommand;
	import services.command.hotels.SaveHotelRoomTypesCommand;
	import services.command.hotels.SetFloorNameCommand;
	import services.command.hotels.UpdateHotelInfoCommand;
	import services.command.houseKeeper.SetOutOfServiceCommand;
	import services.command.inHouse.AttachConferenceRoomToAccountCommand;
	import services.command.inHouse.DeleteMessageCommand;
	import services.command.inHouse.GetAvailableRoomsListCommand;
	import services.command.inHouse.GetConferenceRoomStatusCommand;
	import services.command.inHouse.GetInHouseStateCommand;
	import services.command.inHouse.GetMessageHistoryCommand;
	import services.command.inHouse.GetPackagesCommand;
	import services.command.inHouse.GetVirtualRoutingCommand;
	import services.command.inHouse.MarkMessageAsReadCommand;
	import services.command.inHouse.MoveRoomCommand;
	import services.command.inHouse.SaveMessageCommand;
	import services.command.invoiceManagment.GetInvoiceFileCommand;
	import services.command.invoiceManagment.GetInvoiceListCommand;
	import services.command.items.arrangementCodes.DeleteArrangmentCommand;
	import services.command.items.arrangementCodes.GetArrangementsCommand;
	import services.command.items.arrangementCodes.SaveArrangmentsCommand;
	import services.command.items.itemGroups.ApplySystemGroupsToHotelCommand;
	import services.command.items.itemGroups.DeleteHotelGroupCommand;
	import services.command.items.itemGroups.DeleteHotelSubGroupCommand;
	import services.command.items.itemGroups.DeleteSystemGroupCommand;
	import services.command.items.itemGroups.DeleteSystemSubGroupCommand;
	import services.command.items.itemGroups.GetHotelItemsGroupsCommand;
	import services.command.items.itemGroups.GetSystemGroupsListCommand;
	import services.command.items.itemGroups.SaveSystemGroupCommand;
	import services.command.items.itemGroups.SaveSystemSubGroupCommand;
	import services.command.items.management.DeleteSystemArticleCommand;
	import services.command.items.management.DeleteSystemTransactionCommand;
	import services.command.items.management.GetAllowedHotelsCommand;
	import services.command.items.management.GetHotelTransactionsCommand;
	import services.command.items.management.GetSystemTransactionsCommand;
	import services.command.items.management.GetVatPeriodsCommand;
	import services.command.items.management.SaveHotelArticleCommand;
	import services.command.items.management.SaveHotelTransactionCommand;
	import services.command.items.management.SaveSystemArticleCommand;
	import services.command.items.management.SaveSystemTransactionCommand;
	import services.command.items.management.SaveVatPeriodCommand;
	import services.command.miscellaneous.countries.AddCountryCommand;
	import services.command.miscellaneous.countries.AddRegionCommand;
	import services.command.miscellaneous.countries.DeleteCountryCommand;
	import services.command.miscellaneous.countries.DeleteRegionCommand;
	import services.command.miscellaneous.countries.GetCountryCommand;
	import services.command.miscellaneous.countries.GetRegionCommand;
	import services.command.miscellaneous.langueges.AddLanguageCommand;
	import services.command.miscellaneous.langueges.DeleteLanguageCommand;
	import services.command.miscellaneous.langueges.GetLanguageCommand;
	import services.command.miscellaneous.loyaltyPrograms.AddLoyaltyProgramCommand;
	import services.command.miscellaneous.loyaltyPrograms.DeleteLoyaltyProgramCommand;
	import services.command.miscellaneous.loyaltyPrograms.GetLoyaltyProgramsCommand;
	import services.command.miscellaneous.nationalities.AddNationalitiesCommand;
	import services.command.miscellaneous.nationalities.DeleteNationalityCommand;
	import services.command.miscellaneous.nationalities.GetNationalityCommand;
	import services.command.miscellaneous.salutation.AddSalutationCommand;
	import services.command.miscellaneous.salutation.DeleteSalutationCommand;
	import services.command.miscellaneous.salutation.GetSalutationCommand;
	import services.command.miscellaneous.vat.AddVATCommand;
	import services.command.miscellaneous.vat.DeleteVATCommand;
	import services.command.miscellaneous.vat.EditVATCommand;
	import services.command.miscellaneous.vat.GetVATDataCommand;
	import services.command.profiles.company.DeleteCompanyCommand;
	import services.command.profiles.company.GetAllListCommand;
	import services.command.profiles.company.GetCompanyByIdComand;
	import services.command.profiles.company.GetCompanyListCommand;
	import services.command.profiles.company.GetMarketGroupListCommand;
	import services.command.profiles.company.GetSourceGroupListCommand;
	import services.command.profiles.company.SaveCompanyProfileCommand;
	import services.command.profiles.individual.DeletePersonalProfileCommand;
	import services.command.profiles.individual.FindProfileByNameCommand;
	import services.command.profiles.individual.FindProfileByNameForRsvCommand;
	import services.command.profiles.individual.FindProfileBySurnameCommand;
	import services.command.profiles.individual.FindProfileBySurnameForRsvCommand;
	import services.command.profiles.individual.GetProfileByIdCommand;
	import services.command.profiles.individual.GetProfilesPageCommand;
	import services.command.profiles.individual.GetWishesListCommand;
	import services.command.profiles.individual.SaveProfilesCommand;
	import services.command.profiles.travelAgency.DeleteTravelAgencyCommand;
	import services.command.profiles.travelAgency.GetTravelAgencyByIdComand;
	import services.command.profiles.travelAgency.GetTravelAgencyListCommand;
	import services.command.profiles.travelAgency.SaveTravelAgencyCommand;
	import services.command.rates.bar.GetBARsByDateCommand;
	import services.command.rates.bar.GetBarItemsInfoCommand;
	import services.command.rates.bar.GetHotelBarPriceCommand;
	import services.command.rates.bar.SaveBarItemsDataCommand;
	import services.command.rates.companyRates.DeleteCompanyRateCommand;
	import services.command.rates.companyRates.DeleteTransactionCompanyRateCommand;
	import services.command.rates.companyRates.GetCompanyRatesCountCommand;
	import services.command.rates.companyRates.GetCompanyRatesPageCommand;
	import services.command.rates.companyRates.GetGroupListCompanyRatesCommand;
	import services.command.rates.companyRates.GetItemCountCompanyRatesCommand;
	import services.command.rates.companyRates.GetItemPageCompanyRatesCommand;
	import services.command.rates.companyRates.GetTransactionListCompanyRateCommand;
	import services.command.rates.companyRates.SaveCompanyRateCommand;
	import services.command.rates.companyRates.SaveTransactionCompanyRateCommand;
	import services.command.rates.packages.DeletePackageCommand;
	import services.command.rates.packages.DeleteTransactionCommand;
	import services.command.rates.packages.GetPackagesCountCommand;
	import services.command.rates.packages.GetPackagesPageCommand;
	import services.command.rates.packages.GetTransactionGroupListCommand;
	import services.command.rates.packages.GetTransactionItemCountCommand;
	import services.command.rates.packages.GetTransactionItemPageCommand;
	import services.command.rates.packages.GetTransactionListCommand;
	import services.command.rates.packages.SavePackageCommand;
	import services.command.rates.packages.SaveTransactionCommand;
	import services.command.reports.GetItemTreeCommand;
	import services.command.reports.GetReportCommand;
	import services.command.reservation.GetComfLetterCommand;
	import services.command.reservation.GetCompanyRatesForReservationCommand;
	import services.command.reservation.GetGuestListForRsrvCommand;
	import services.command.reservation.GetOrderFutureInfoCommand;
	import services.command.reservation.GetPackagesRatesForReservationCommand;
	import services.command.reservation.GetPdfUrlFromHtmlCommand;
	import services.command.reservation.GetReservationCaledarDataCommand;
	import services.command.reservation.SaveReservationCommand;
	import services.command.roomSettings.AddRoomSettingCommand;
	import services.command.roomSettings.DeleteRoomSettingCommand;
	import services.command.roomSettings.EditRoomSettingCommand;
	import services.command.roomSettings.GetRoomSettingsDataCommand;
	import services.command.roomTypes.AddBedTypeCommand;
	import services.command.roomTypes.AddRoomTypeCommand;
	import services.command.roomTypes.DeleteBedTypeCommand;
	import services.command.roomTypes.DeleteRoomQualityCommand;
	import services.command.roomTypes.DeleteRoomTypeCommand;
	import services.command.roomTypes.EditRoomTypeCommand;
	import services.command.roomTypes.GetBedTypesListCommand;
	import services.command.roomTypes.GetRoomTypesDataCommand;
	import services.command.roomTypes.GetRoomTypesPageCommand;
	import services.command.roomTypes.SetRoomTypeCapacityCommand;
	import services.command.roomTypes.SetRoomTypeDescriptionCommand;
	import services.command.roomTypes.SetRoomTypeShortNameCommand;
	import services.command.search.CancelOrderCommand;
	import services.command.search.CancelReservationCommand;
	import services.command.search.ExecuteSearchCommand;
	import services.command.search.GetCancelationReasonsCommand;
	import services.command.search.GetReservationByIdCommand;
	import services.command.security.AddSystemUserCommand;
	import services.command.security.DeleteRoleCommand;
	import services.command.security.DeleteUserHotelRoleCommand;
	import services.command.security.GetRolesCommand;
	import services.command.security.GetSystemRoleListCommand;
	import services.command.security.GetUserListCommand;
	import services.command.security.GetUserListInHotelCommand;
	import services.command.security.SaveRoleCommand;
	import services.command.security.SetStatusSystemUserCommand;
	import services.command.security.SetUserHotelRoleCommand;
	import services.events.hotels.GetRealRoomTypeListEvent;
	import services.events.invoiceManagment.GetInvoiceFileEvent;
	import services.events.invoiceManagment.GetInvoiceListEvent;
	import services.events.reservation.GetComfLetterEvent;
	import services.events.reservation.GetCompanyRatesForReservationEvent;
	import services.events.reservation.GetGuestListForReservationEvent;
	import services.events.reservation.GetOrderFutureInfoEvent;
	import services.events.reservation.GetPackagesRatesForReservationEvent;
	import services.events.security.AddSystemUserEvent;
	import services.events.security.DeleteRoleEvent;
	import services.events.security.DeleteUserHotelRoleEvent;
	import services.events.security.GetRolesEvent;
	import services.events.security.GetSystemRoleListEvent;
	import services.events.security.GetUserListEvent;
	import services.events.security.GetUserListInHotelEvent;
	import services.events.security.SaveRoleEvent;
	import services.events.security.SetStatusSystemUserEvent;
	import services.events.security.SetUserHotelRoleEvent;
	import services.command.items.management.GetItemTypesCommand;
	import services.events.reservation.SaveGroupReservationEvent;
	import services.command.reservation.SaveGroupReservationCommand;

	public class AppController extends FrontController
	{
		//LOGIN
		public static const LOGIN_EVENT:String = "handleLogin";
		public static const LOGIN_IN_HOTEL_EVENT:String = "loginInHotelEvent";
		public static const CONFIRM_FIRST_LOGIN_EVENT:String = "confirmFirstTimeLoginEvent";

		public static const GET_PAGE_OF_START_HOTEL:String = "getPageOfStartHotel";
		//FORGOT PASSWORD
		public static const CHECK_LOGIN_EVENT:String = "checkLogin";
		public static const CHECK_ANSWER_EVENT:String = "checkAnswer";
		public static const SET_NEW_PASSWORD_EVENT:String = "setNewPassword";
		//VAT
		public static const GET_VAT_DATA_EVENT:String = "getVATData";
		public static const ADD_VAT_EVENT:String = "addVAT";
		public static const EDIT_VAT_EVENT:String = "editVAT";
		public static const DELETE_VAT_EVENT:String = "deleteVAT";
		
		//TRANSACTION TYPE
		public static const GET_ITEM_TYPE_DATA_EVENT:String = "getItemTypes";
		
		//ROOM SETTINGS
		public static const GET_ROOM_SETTINGS_DATA_EVENT:String = "getRoomSettings";
		public static const ADD_ROOM_SETTING_EVENT:String = "addRoomSetting";
		public static const EDIT_ROOM_SETIING_EVENT:String = "editRoomSetting";
		public static const DELETE_ROOM_SETTING_EVENT:String = "deleteRoomSetting";
		//ROOM TYPES
		public static const GET_ROOM_TYPES_DATA_EVENT:String = "getRoomTypesData";
		public static const GET_BED_TYPES_LIST_EVENT:String = "getBedTypesList";
		public static const ADD_BED_TYPE_EVENT:String = "addBedType";
		public static const DELETE_BED_TYPE_EVENT:String = "deleteBedType";
		public static const ADD_ROOM_TYPE_EVENT:String = "addRoomType";
		public static const DELETE_ROOM_TYPE_EVENT:String = "deleteRoomType";
		public static const DELETE_ROOM_QUALITY_EVENT:String = "deleteRoomQuality";
		public static const EDIT_ROOM_TYPE_EVENT:String = "editRoomType";
		public static const SET_ROOM_TYPE_DESCRIPTION_EVENT:String = "setRoomTypeDescription";
		public static const SET_ROOM_TYPE_CAPACITY_EVENT:String = "setRoomTypeCapacity";
		public static const SET_ROOM_TYPE_SHORT_NAME_EVENT:String = "setRoomTypeShortName";

		public static const GET_ROOM_TYPES_PAGE:String = "getPageRoomType";
		//HOTELS CONFIGURATION
		public static const UPDATE_HOTEL_INFO_EVENT:String = "updateHotelInfo";
		public static const ADD_FLOOR_EVENT:String = "addFloor";
		public static const ADD_ROOM_EVENT:String = "addRoom";
		public static const ADD_ROOM_LIST_EVENT:String = "addRoomList";
		public static const GET_HOTEL_ROOM_SETTINGS:String = "getHotelRoomsettings";
		public static const GET_HOTEL_ROOM_TYPES:String = "getHotelRoomTypes";
		public static const GET_HOTEL_COMMON_ROOM_TYPES:String = "getHotelCommonRoomTypes";
		public static const SAVE_HOTEL_ROOM_SETTINGS:String = "saveHotelRoomSettings";
		public static const SAVE_HOTEL_ROOM_TYPES:String = "saveHotelRoomTypes";
		public static const GET_HOTEL_STAGES:String = "getHotelStages";
		public static const GET_HOTEL_CHAINS:String = "getHotelChains";
		public static const DELETE_HOTEL_ROOM:String = "deleteHotelRoom";
		public static const DELETE_HOTEL_STAGE:String = "deleteHotelStage";
		public static const SET_HOTEL_FLOOR_NAME_EVENT:String="setFloorName";
		public static const ADD_CITY_EVENT:String = "addCityEvent";
		//BAR CONFIGURATION
		public static const GET_BAR_ITEMS_INFO_EVENT:String = "getBarItemsInfo";
		public static const SAVE_BAR_ITEMS_EVENT:String = "saveBarItems";
		public static const GET_HOTEL_BAR_PRICE_EVENT:String = "getHotelBarPrice";
		public static const GET_BARS_BY_DATE:String = "getBarsByDate";
		//RESERVATION
		public static const GET_RESERVATION_DATA_EVENT:String = "getReservationData";
		public static const SAVE_RESERVATION_EVENT:String = "saveReservation";

		public static const GET_VIP_TOTAL_LIST_EVENT:String = "getVipTotalList";
		public static const GET_VIP_2_STATUSES_EVENT:String = "getVipHotelList";

		public static const GET_PROFILES_EVENT:String = "getProfiles";
		public static const SAVE_CALLER_PROFILE_EVENT:String = "saveCallerProfile";
		public static const SAVE_PROFILE_ADDRESSES_EVENT:String = "saveProfileAddresses";

		public static const GET_RESERVATION_BY_ID:String = "getReservationById";
		

		//CREDITS
		public static const GET_CREDIT_TYPE_EVENT:String="getCreditTypeEvent";
		public static const GET_CARD_OF_EVENT:String="getCardOfEvent";

		//CHECK IN
		public static const GET_CHECK_IN_DATA_EVENT:String = "getCheckInData";
		public static const SAVE_CHECK_IN_DATA_EVENT:String = "saveCheckInData";
		public static const GET_ROOM_LIST_BY_ORDER_EVENT:String = "getRoomListByOrder";
		public static const SET_ASSIGN_CHECK_IN_DATA_EVENT:String = "setAssignCheckIn";

		/* Common events */
		public static const GET_SOURCE_GROUP_LIST:String = "getSourceGroupList";
		public static const GET_MARKET_GROUP_LIST:String = "getMarketGroupList";
		public static const GET_SOURCE_CODES:String = "getSourceCodes";
		public static const GET_MARKET_CODES:String = "getMarketCodes";
		public static const GET_DATA_LIST:String = "getDataList";

		/* Events for additional data */
		public static const GET_WISHES_LIST:String = "getWishesList";
		public static const GET_NATIONALITY_EVENT:String="getNationalityEvent";
		public static const GET_SALUTATION_EVENT:String="getSalutationEvent";
		public static const GET_LANGUAGE_EVENT:String="getLanguageEvent";

		//REPORTS
		public static const GET_ARRIVAL_REPORT_EVENT:String = "getArrivalReport";
		public static const GET_ITEM_TREE_EVENT:String = "getItemTree";

		/// COMMON
		public static const GET_MAILING_LIST:String="getMailingList";
		public static const GET_COUNTRY_EVENT:String="getCountryEvent";
		public static const GET_REGION_EVENT:String="getRegionEvent";
		public static const GET_CITY_EVENT:String="getCityEvent";
		public static const GET_STREET_EVENT:String="getStreetEvent";
		public static const GET_ZIP_BY_STREET_EVENT:String = "getZipByStreet";
		public static const GET_ADDRESS_BY_ZIP_EVENT:String = "getAddressByZipEvent";
		public static const ADD_LOCATION_EVENT:String = "addLocationEvent";

		public static const ADD_COUNTRY_EVENT:String="addCountryEvent";
		public static const ADD_REGION_EVENT:String="addRegionEvent";

		public static const DELETE_COUNTRY_EVENT:String="deleteCountryEvent";
		public static const DELETE_REGION_EVENT:String="deleteRegionEvent";

		public static const ADD_LANGUAGE_EVENT:String="addLangugeEvent";
		public static const DELETE_LANGUAGE_EVENT:String="deleteLangugeEvent";

		public static const ADD_NATIONALITIES_EVENT:String="addNationalitiesEvent";
		public static const DELETE_NATIONALITY_EVENT:String="deleteNationalityEvent";

		public static const GET_LOYALTY_PROGRAMS_EVENT:String="getLoyaltyProgramEvent";
		public static const ADD_LOYALTY_PROGRAMS_EVENT:String="addLoyaltyProgramEvent";
		public static const DELETE_LOYALTY_PROGRAMS_EVENT:String="deleteLoyaltyProgramEvent";

		public static const GET_DATA_LIST_BY_TYPE_CODE_EVENT:String="getDataListByTypeCodeEvent";

		public static const ADD_SALUTATION_EVENT:String="addSalutationEvent";
		public static const DELETE_SALUTATION_EVENT:String="deleteSalutationEvent";

		//RATES
		public static const RATES_COMPANY_GET_PAGE_EVENT:String = "ratesCompanyGetPageEvent";
		public static const RATES_COMPANY_SAVE_EVENT:String = "ratesCompanySaveEvent";
		public static const RATES_COMPANY_GET_COUNT_EVENT:String = "ratesCompanyGetCountEvent";
		public static const DELETE_COMPANY_RATE:String = "deleteCompanyRateEvent";
		public static const GET_TRANSACTION_LIST_COMPANY_RATE:String = "getTransactionListCompanyRate";
		public static const SAVE_TRANSACTION_COMPANY_RATE:String = "saveTransactionCompanyRate";
		public static const GET_GROUP_LIST_COMPANY_RATES:String = "getGroupListCompanyRate";
		public static const GET_ITEM_COUNT_COMPANY_RATES:String = "getItemCountCompanyRates";
		public static const GET_ITEM_PAGE_COMPANY_RATES:String = "getItemPageCompanyRates";
		public static const DELETE_TRANSACTION_COMPANY_RATES:String = "deleteTransactionCompanyRates";
		/* Packages */
		public static const PACKAGES_GET_PACKAGES_COUNT_EVENT:String = "packagesGetPackagesCountEvent";
		public static const PACKAGES_GET_PACKAGES_PAGE_EVENT:String = "packagesGetPackagesPageEvent";
		public static const PACKAGES_SAVE_PACKAGE_EVENT:String = "packagesSavePackageEvent";
		public static const PACKAGES_DELETE_PACKAGE_EVENT:String = "packagesDeletePackageEvent";
		public static const PACKAGES_GET_TRANSACTION_LIST_EVENT:String = "packagesGetTransactionListEvent";

		public static const PACKAGES_GET_TRANSACTION_GROUP_LIST_EVENT:String = "packagesGetTransactionGroupListEvent";
		public static const PACKAGES_GET_TRANSACTION_ITEM_COUNT_EVENT:String = "packagesGetTransactionItemCountEvent";
		public static const PACKAGES_GET_TRANSACTION_ITEM_PAGE_EVENT:String = "packagesGetTransactionItemPageEvent";
		public static const PACKAGES_SAVE_TRANSACTION_EVENT:String = "packagesSaveTransactionEvent";
		public static const PACKAGES_DELETE_TRANSACTION_EVENT:String = "packagesDeleteTransactionEvent";

		//HOUSE KEEPING
		public static const HOUSEKEEPING_GET_ROOM_LIST_EVENT:String="housekeepingGetRoomListEvent";
		public static const HOUSEKEEPING_GET_STATUS_LIST_EVENT:String="housekeepingGetStatusListEvent";
		public static const HOUSEKEEPING_SET_STATUS_EVENT:String="housekeepingSetStatusEvent";
		public static const HOUSEKEEPING_SET_OUT_OF_SERVICE_EVENT:String="housekeepingSetOutOfServiceEvent";

		//CHECK OUT
		public static const CHECK_OUT_GET_GUEST_LIST_EVENT:String = "checkOutGetGuestListEvent";

		//RESERVATION
		public static const GET_PDF_URL_FROM_HTML_EVENT:String = "getPdfUrlFromHtmlEvent";

		//RESERVATION SEARCH
		public static const EXECUTE_RESERVATION_SEARCH:String = "executReservationSearch";
		public static const GET_CANCELATION_REASONS:String = "getCancelationReasons";
		public static const CANCEL_ORDER:String = "cancelOrder";
		public static const CANCEL_RESERVATION:String = "cancelReservation";

		//CASH SHIFT
		public static const CASHSHIFT_GET_LAST_OPEN_SHIFT:String = "getLastOpenShift";
		public static const CASHSHIFT_CLOSE_SHIFT:String = "closeShift";
		public static const CASHSHIFT_OPEN_NEXT_SHIFT:String = "openNextShift";
		public static const CASHSHIFT_REOPEN_SHIFT:String = "reopenShift";
		public static const CASHSHIFT_GET_DAY_SHIFT_LIST:String = "getDayShiftList";
		public static const CASHSHIFT_GET_SHIFT_PAYMENT_LIST:String = "getShiftPaymentList";
		public static const CASHSHIFT_START_NEW_BUSINESS_DAY:String = "startNewBusinessDay";

		//BDC
		public static const BDC_CHECK_DEPARTURE:String = "checkDeparture";
		public static const BDC_CHECK_SHIFTS:String = "checkShifts";
		public static const BDC_GET_ANNOMALY_PERSON:String = "getAnnomalyPerson";
		public static const BDC_TOTAL_LOGOUT:String = "totalLogout";
		public static const BDC_CHECK_PROFILES:String = "checkProfiles";
		public static const BDC_POST_TRANSACTIONS:String = "postTransactions";
		public static const BDC_ROLL_BUSINESS_DAY:String = "rollBusinessDay";
		public static const BDC_UPDATE_ROOM_STATES:String = "updateRoomStates";

		public function AppController()
		{
			super();

			// --------------------------------------------------------------------- //
			//                          COMMON COMMANDS                              //
			// --------------------------------------------------------------------- //
			addCommand(CommonDelegate.GET_SYSTEM_DATE, GetSystemDateCommand);
			addCommand(CommonDelegate.GET_COMMON_DICTIONARY, GetCommonDictionariesCommand);
			addCommand(GET_PAGE_OF_START_HOTEL, GetHotelDictionariesCommand);

			addCommand(LOGIN_EVENT, LoginCommand);
			addCommand(LOGIN_IN_HOTEL_EVENT, LoginInHotelCommand);


			//addCommand(GET_ROOM_TYPES_DATA_EVENT, GetRoomTypesDataCommand)

			addCommand(CONFIRM_FIRST_LOGIN_EVENT, ConfirmFirstLoginCommand);

			addCommand(CHECK_LOGIN_EVENT, CheckLoginCommand);
			addCommand(CHECK_ANSWER_EVENT, CheckAnswerCommand);
			addCommand(SET_NEW_PASSWORD_EVENT, SetNewPasswordCommand);
			//VAT
			addCommand(GET_VAT_DATA_EVENT, GetVATDataCommand);
			addCommand(ADD_VAT_EVENT, AddVATCommand);
			addCommand(EDIT_VAT_EVENT, EditVATCommand);
			addCommand(DELETE_VAT_EVENT, DeleteVATCommand);
			//ROOM SETTINGS
			addCommand(GET_ROOM_SETTINGS_DATA_EVENT, GetRoomSettingsDataCommand);
			addCommand(ADD_ROOM_SETTING_EVENT, AddRoomSettingCommand);
			addCommand(EDIT_ROOM_SETIING_EVENT, EditRoomSettingCommand);
			addCommand(DELETE_ROOM_SETTING_EVENT, DeleteRoomSettingCommand);
			//Room Types
			addCommand(GET_ROOM_TYPES_DATA_EVENT, GetRoomTypesDataCommand);
			addCommand(GET_BED_TYPES_LIST_EVENT, GetBedTypesListCommand);
			addCommand(ADD_BED_TYPE_EVENT, AddBedTypeCommand);
			addCommand(DELETE_BED_TYPE_EVENT, DeleteBedTypeCommand);
			addCommand(ADD_ROOM_TYPE_EVENT, AddRoomTypeCommand);
			addCommand(DELETE_ROOM_TYPE_EVENT, DeleteRoomTypeCommand);
			addCommand(DELETE_ROOM_QUALITY_EVENT, DeleteRoomQualityCommand);
			addCommand(EDIT_ROOM_TYPE_EVENT, EditRoomTypeCommand);
			addCommand(SET_ROOM_TYPE_CAPACITY_EVENT, SetRoomTypeCapacityCommand);
			addCommand(SET_ROOM_TYPE_DESCRIPTION_EVENT, SetRoomTypeDescriptionCommand);
			addCommand(SET_ROOM_TYPE_SHORT_NAME_EVENT, SetRoomTypeShortNameCommand);
			addCommand(GET_ROOM_TYPES_PAGE, GetRoomTypesPageCommand);

			//Hotels Configuration
			addCommand(HotelsDelegate.GET_HOTELS_LIST, GetHotelsListCommand);
			addCommand(HotelsDelegate.REMOVE_HOTEL, DeleteHotelCommand);
			
			addCommand(UPDATE_HOTEL_INFO_EVENT, UpdateHotelInfoCommand);
			addCommand(ADD_FLOOR_EVENT, AddFloorCommand);
			addCommand(ADD_ROOM_EVENT, AddRoomCommand);
			addCommand(ADD_ROOM_LIST_EVENT, AddRoomListCommand);
			addCommand(GET_HOTEL_ROOM_SETTINGS, GetHotelRoomSettingsCommand);
			addCommand(GET_HOTEL_ROOM_TYPES, GetHotelRoomTypesCommand);
			addCommand(GET_HOTEL_COMMON_ROOM_TYPES, GetHotelCommonRoomTypesCommand);
			addCommand(SAVE_HOTEL_ROOM_SETTINGS, SaveHotelRoomSettingsCommand);
			addCommand(SAVE_HOTEL_ROOM_TYPES, SaveHotelRoomTypesCommand);
			addCommand(GET_HOTEL_STAGES, GetHotelStageListCommand);
			addCommand(GET_HOTEL_CHAINS, GetHotelChainCommand);
			addCommand(DELETE_HOTEL_ROOM, DeleteHotelRoomCommand);
			addCommand(DELETE_HOTEL_STAGE, DeleteHotelStageCommand);
			addCommand(SET_HOTEL_FLOOR_NAME_EVENT, SetFloorNameCommand);
			addCommand(ADD_CITY_EVENT, AddCityCommand);
			addCommand(GetRealRoomTypeListEvent.NAME, GetRealRoomTypeListCommand);
			//Bar Configuration
			addCommand(GET_BAR_ITEMS_INFO_EVENT, GetBarItemsInfoCommand);
			addCommand(SAVE_BAR_ITEMS_EVENT, SaveBarItemsDataCommand);
			addCommand(GET_HOTEL_BAR_PRICE_EVENT, GetHotelBarPriceCommand);
			addCommand(GET_BARS_BY_DATE, GetBARsByDateCommand);
			//Reservation
			addCommand(GET_RESERVATION_DATA_EVENT, GetReservationCaledarDataCommand);
			addCommand(SAVE_RESERVATION_EVENT, SaveReservationCommand);
			addCommand(GET_RESERVATION_BY_ID, GetReservationByIdCommand);
			addCommand(GetOrderFutureInfoEvent.NAME, GetOrderFutureInfoCommand);

			//CREDITS
			addCommand(GET_CREDIT_TYPE_EVENT, GetCreditTypeCommand);
			addCommand(GET_CARD_OF_EVENT, GetCardOfCommand);
			//CHECK IN
			addCommand(GET_CHECK_IN_DATA_EVENT, GetCheckInDataCommand);
			addCommand(SAVE_CHECK_IN_DATA_EVENT, SaveCheckInDataCommand);
			addCommand(GET_ROOM_LIST_BY_ORDER_EVENT, GetRoomListByOrderCommand);
			addCommand(SET_ASSIGN_CHECK_IN_DATA_EVENT, SetAssignCheckInDataCommand);

			/* Additional data */
			addCommand(GET_WISHES_LIST, GetWishesListCommand);
			/* Common */
			addCommand(GET_SOURCE_GROUP_LIST, GetSourceGroupListCommand);
			addCommand(GET_MARKET_GROUP_LIST, GetMarketGroupListCommand);
			addCommand(GET_SOURCE_CODES, GetSourceCodesCommand);
			addCommand(GET_MARKET_CODES, GetMarketCodesCommand);

			addCommand(GET_DATA_LIST, GetDataListByTypeCommand);
			addCommand(GET_NATIONALITY_EVENT, GetNationalityCommand);
			addCommand(GET_SALUTATION_EVENT, GetSalutationCommand);
			addCommand(GET_LANGUAGE_EVENT, GetLanguageCommand);

			//REPORTS
			addCommand(GET_ARRIVAL_REPORT_EVENT, GetReportCommand);
			addCommand(GET_ITEM_TREE_EVENT, GetItemTreeCommand);

			/// COMMON COMMANDS
			addCommand(GET_COUNTRY_EVENT, GetCountryCommand);
			addCommand(GET_REGION_EVENT, GetRegionCommand);
			addCommand(GET_CITY_EVENT, GetCityCommand);
			addCommand(GET_ADDRESS_BY_ZIP_EVENT, GetAddressByZipCommand);
			addCommand(ADD_LOCATION_EVENT, AddLocationCommand);

			addCommand(ADD_COUNTRY_EVENT, AddCountryCommand);
			addCommand(ADD_REGION_EVENT, AddRegionCommand);

			addCommand(DELETE_COUNTRY_EVENT, DeleteCountryCommand);
			addCommand(DELETE_REGION_EVENT, DeleteRegionCommand);

			addCommand(ADD_LANGUAGE_EVENT, AddLanguageCommand);
			addCommand(DELETE_LANGUAGE_EVENT, DeleteLanguageCommand);

			addCommand(ADD_NATIONALITIES_EVENT, AddNationalitiesCommand);
			addCommand(DELETE_NATIONALITY_EVENT, DeleteNationalityCommand);

			addCommand(GET_LOYALTY_PROGRAMS_EVENT, GetLoyaltyProgramsCommand);
			addCommand(ADD_LOYALTY_PROGRAMS_EVENT, AddLoyaltyProgramCommand);
			addCommand(DELETE_LOYALTY_PROGRAMS_EVENT, DeleteLoyaltyProgramCommand);

			addCommand(GET_DATA_LIST_BY_TYPE_CODE_EVENT, GetDataListByTypeCodeCommand);

			addCommand(ADD_SALUTATION_EVENT, AddSalutationCommand);
			addCommand(DELETE_SALUTATION_EVENT, DeleteSalutationCommand);

			//SECURITY
			addCommand(AddSystemUserEvent.NAME,AddSystemUserCommand);
			addCommand(GetSystemRoleListEvent.NAME,GetSystemRoleListCommand);
			addCommand(GetRolesEvent.NAME, GetRolesCommand);
			addCommand(SaveRoleEvent.NAME, SaveRoleCommand);
			addCommand(DeleteRoleEvent.NAME, DeleteRoleCommand);
			addCommand(GetUserListInHotelEvent.NAME, GetUserListInHotelCommand);
			addCommand(GetUserListEvent.NAME, GetUserListCommand);
			addCommand(SetStatusSystemUserEvent.NAME, SetStatusSystemUserCommand);
			addCommand(DeleteUserHotelRoleEvent.NAME,DeleteUserHotelRoleCommand);
			addCommand(SetUserHotelRoleEvent.NAME, SetUserHotelRoleCommand);

			//RATES
			addCommand(RATES_COMPANY_GET_PAGE_EVENT, GetCompanyRatesPageCommand);
			addCommand(RATES_COMPANY_SAVE_EVENT, SaveCompanyRateCommand);
			addCommand(RATES_COMPANY_GET_COUNT_EVENT, GetCompanyRatesCountCommand);
			addCommand(DELETE_COMPANY_RATE, DeleteCompanyRateCommand);
			addCommand(GET_TRANSACTION_LIST_COMPANY_RATE, GetTransactionListCompanyRateCommand);
			addCommand(SAVE_TRANSACTION_COMPANY_RATE, SaveTransactionCompanyRateCommand);
			addCommand(GET_GROUP_LIST_COMPANY_RATES, GetGroupListCompanyRatesCommand);
			addCommand(GET_ITEM_COUNT_COMPANY_RATES, GetItemCountCompanyRatesCommand);
			addCommand(GET_ITEM_PAGE_COMPANY_RATES, GetItemPageCompanyRatesCommand);
			addCommand(DELETE_TRANSACTION_COMPANY_RATES, DeleteTransactionCompanyRateCommand);

			/* Packages */
			addCommand(PACKAGES_GET_PACKAGES_COUNT_EVENT,GetPackagesCountCommand);
			addCommand(PACKAGES_GET_PACKAGES_PAGE_EVENT,GetPackagesPageCommand);
			addCommand(PACKAGES_SAVE_PACKAGE_EVENT, SavePackageCommand);
			addCommand(PACKAGES_DELETE_PACKAGE_EVENT, DeletePackageCommand);

			addCommand(PACKAGES_GET_TRANSACTION_LIST_EVENT, GetTransactionListCommand);
			addCommand(PACKAGES_GET_TRANSACTION_GROUP_LIST_EVENT, GetTransactionGroupListCommand);
			addCommand(PACKAGES_GET_TRANSACTION_ITEM_COUNT_EVENT, GetTransactionItemCountCommand);
			addCommand(PACKAGES_GET_TRANSACTION_ITEM_PAGE_EVENT, GetTransactionItemPageCommand);
			addCommand(PACKAGES_SAVE_TRANSACTION_EVENT, SaveTransactionCommand);
			addCommand(PACKAGES_DELETE_TRANSACTION_EVENT, DeleteTransactionCommand);

			//HOUSE KEEPING
			addCommand(HOUSEKEEPING_GET_ROOM_LIST_EVENT, GetRoomListCommand);
			addCommand(HOUSEKEEPING_GET_STATUS_LIST_EVENT,GetStatusListCommand);
			addCommand(HOUSEKEEPING_SET_STATUS_EVENT,SetHotelRoomStatusCommand);
			addCommand(HOUSEKEEPING_SET_OUT_OF_SERVICE_EVENT,SetOutOfServiceCommand);



			//RESERVATION
			addCommand(GetCompanyRatesForReservationEvent.NAME,GetCompanyRatesForReservationCommand);
			addCommand(GetPackagesRatesForReservationEvent.NAME,GetPackagesRatesForReservationCommand);
			
			addCommand(EXECUTE_RESERVATION_SEARCH ,ExecuteSearchCommand);
			addCommand(GET_CANCELATION_REASONS, GetCancelationReasonsCommand);
			addCommand(CANCEL_ORDER, CancelOrderCommand);
			addCommand(CANCEL_RESERVATION, CancelReservationCommand);
			addCommand(GetGuestListForReservationEvent.NAME,GetGuestListForRsrvCommand);
			addCommand(GET_PDF_URL_FROM_HTML_EVENT,GetPdfUrlFromHtmlCommand);
			
			addCommand(GetComfLetterEvent.NAME,GetComfLetterCommand);	
			
			addCommand(SaveGroupReservationEvent.NAME, SaveGroupReservationCommand);		

			// --------------------------------------------------------------------- //
			//                          CASH SHIFT MODULE                           //
			// --------------------------------------------------------------------- //
			/* Common */
			addCommand(CASHSHIFT_GET_LAST_OPEN_SHIFT, GetLastOpenShiftCommand);
			addCommand(CASHSHIFT_CLOSE_SHIFT, CloseShiftCommand);
			addCommand(CASHSHIFT_OPEN_NEXT_SHIFT, OpenNextShiftCommand);
			addCommand(CASHSHIFT_REOPEN_SHIFT, ReopenShiftCommand);
			addCommand(CASHSHIFT_GET_DAY_SHIFT_LIST, GetDayShiftListCommand);
			addCommand(CASHSHIFT_GET_SHIFT_PAYMENT_LIST, GetShiftPaymentListCommand);
			addCommand(CASHSHIFT_START_NEW_BUSINESS_DAY, StartNewBusinessDayCommand);

			// --------------------------------------------------------------------- //
			//                          BDC MODULE                           //
			// --------------------------------------------------------------------- //
			addCommand(BDC_CHECK_PROFILES, CheckProfilesCommand);
			addCommand(BDC_POST_TRANSACTIONS, PostTransactionsCommand);
			addCommand(BDC_ROLL_BUSINESS_DAY, RollBusinessDayCommand);
			addCommand(BDC_CHECK_DEPARTURE, CheckDepartureCommand);
			addCommand(BDC_CHECK_SHIFTS, CheckShiftsCommand);

			addCommand(BDC_GET_ANNOMALY_PERSON, GetAnnomalyPersonCommand);
			addCommand(BDC_TOTAL_LOGOUT, TotalLogoutCommand);
			addCommand(BDC_UPDATE_ROOM_STATES, UpdateRoomStatesCommand);

			// --------------------------------------------------------------------- //
			//                          TRANSACTION MODULE                           //
			// --------------------------------------------------------------------- //
			/* Common */
			addCommand(ItemsDelegate.GET_HOTEL_GROUPS, GetHotelItemsGroupsCommand);
			addCommand(ItemsDelegate.APPLY_SYSTEM_GROUPS_TO_HOTEL, ApplySystemGroupsToHotelCommand);
			addCommand(ItemsDelegate.GET_SYSTEM_GROUPS, GetSystemGroupsListCommand);
			/* System groups */
			addCommand(ItemsDelegate.SAVE_SYSTEM_GROUP, SaveSystemGroupCommand);
			addCommand(ItemsDelegate.DELETE_SYSTEM_GROUP, DeleteSystemGroupCommand);
			/* System sub groups */
			addCommand(ItemsDelegate.SAVE_SYSTEM_SUB_GROUP, SaveSystemSubGroupCommand);
			addCommand(ItemsDelegate.DELETE_SYSTEM_SUB_GROUP, DeleteSystemSubGroupCommand);
			/* Hotel's groups */
			addCommand(ItemsDelegate.GET_ALLOWED_HOTELS, GetAllowedHotelsCommand);
			addCommand(ItemsDelegate.GET_HOTEL_TRANSACTIONS, GetHotelTransactionsCommand);
			addCommand(ItemsDelegate.SAVE_HOTEL_TRANSACTION, SaveHotelTransactionCommand);
			addCommand(ItemsDelegate.SAVE_HOTEL_ARTICLE, SaveHotelArticleCommand);
			addCommand(ItemsDelegate.DELETE_HOTEL_GROUP, DeleteHotelGroupCommand);
			addCommand(ItemsDelegate.DELETE_HOTEL_SUB_GROUP, DeleteHotelSubGroupCommand);
			/* Transaction managment */
			addCommand(ItemsDelegate.GET_SYSTEM_TRANSACTIONS, GetSystemTransactionsCommand);
			addCommand(ItemsDelegate.SAVE_SYSTEM_TRANSACTIONS, SaveSystemTransactionCommand);
			addCommand(ItemsDelegate.SAVE_SYSTEM_ARTICLE, SaveSystemArticleCommand);
			addCommand(ItemsDelegate.DELETE_SYSTEM_TRANSACTION, DeleteSystemTransactionCommand);
			addCommand(ItemsDelegate.DELETE_SYSTEM_ARTICLE, DeleteSystemArticleCommand);

			addCommand(ItemsDelegate.SAVE_VAT_PERIOD, SaveVatPeriodCommand);
			addCommand(ItemsDelegate.GET_VAT_PERIODS, GetVatPeriodsCommand);
			/* Arrangemenmt codes */
			addCommand(ItemsDelegate.GET_ARRANGEMENTS_LIST, GetArrangementsCommand);
			addCommand(ItemsDelegate.SAVE_ARRANGEMENTS, SaveArrangmentsCommand);
			addCommand(ItemsDelegate.DELETE_ARRANGEMENT, DeleteArrangmentCommand);
			
			/* Transaction Types */
			addCommand(GET_ITEM_TYPE_DATA_EVENT, GetItemTypesCommand);

			// --------------------------------------------------------------------- //
			//                            PROFILES MODULE                            //
			// --------------------------------------------------------------------- //
			/* Individual profiles */
			addCommand(ProfileDelegate.GET_PROFILES_PAGE, GetProfilesPageCommand);
			addCommand(ProfileDelegate.GET_PROFILE_BY_ID, GetProfileByIdCommand);
			addCommand(ProfileDelegate.FIND_PROFILE_BY_SURNAME, FindProfileBySurnameCommand);
			addCommand(ProfileDelegate.FIND_PROFILE_BY_NAME, FindProfileByNameCommand);
			addCommand(ProfileDelegate.FIND_PROFILE_BY_SURNAME_FOR_RESERVATION, FindProfileBySurnameForRsvCommand);
			addCommand(ProfileDelegate.FIND_PROFILE_BY_NAME_FOR_RESERVATION, FindProfileByNameForRsvCommand);

			addCommand(ProfileDelegate.SAVE_PROFILE, SaveProfilesCommand);
			addCommand(ProfileDelegate.DELETE_PERSONAL_PROFILE, DeletePersonalProfileCommand);
			/* Company profiles */
			addCommand(ProfileDelegate.GET_COMPANY_LIST, GetCompanyListCommand);
			addCommand(ProfileDelegate.GET_COMPANY_PROFILE_BY_ID, GetCompanyByIdComand);
			addCommand(ProfileDelegate.SAVE_COMPANY_PROFILE, SaveCompanyProfileCommand);
			addCommand(ProfileDelegate.DELETE_COMPANY_PROFILE, DeleteCompanyCommand);
			/* Travel agency profiles */
			addCommand(ProfileDelegate.DELETE_TRAVEL_AGENCY, DeleteTravelAgencyCommand);
			addCommand(ProfileDelegate.GET_TRAVEL_AGENCY_LIST, GetTravelAgencyListCommand);
			addCommand(ProfileDelegate.GET_TRAVEL_AGENCY_BY_ID, GetTravelAgencyByIdComand);
			addCommand(ProfileDelegate.SAVE_TRAVEL_AGENCY, SaveTravelAgencyCommand);
			/* Common */
			addCommand(ProfileDelegate.GET_ALL_LIST, GetAllListCommand);

			// --------------------------------------------------------------------- //
			//                            IN HOUSE MODULE                            //
			// --------------------------------------------------------------------- //
			addCommand(InHouseDelegate.GET_IN_HOUSE_STATE, GetInHouseStateCommand);
			addCommand(InHouseDelegate.GET_VIRTUAL_ROUTING, GetVirtualRoutingCommand);
			addCommand(InHouseDelegate.GET_CONFERENCE_ROOM_STATUS, GetConferenceRoomStatusCommand);
			addCommand(InHouseDelegate.GET_MESSAGE_HISTORY, GetMessageHistoryCommand);
			addCommand(InHouseDelegate.GET_PACKAGES, GetPackagesCommand);
			addCommand(InHouseDelegate.SAVE_MESSAGES, SaveMessageCommand);
			addCommand(InHouseDelegate.DELETE_MESSAGES, DeleteMessageCommand);
			addCommand(InHouseDelegate.MARK_MESSAGE_AS_READ, MarkMessageAsReadCommand);
			addCommand(InHouseDelegate.GET_AVAILABLE_ROOM_LIST, GetAvailableRoomsListCommand);
			addCommand(InHouseDelegate.MOVE_ROOM, MoveRoomCommand);
			addCommand(InHouseDelegate.ATTACH_CONFERENCE_ROOM_TO_ACCOUNT, AttachConferenceRoomToAccountCommand);

			// --------------------------------------------------------------------- //
			//                           CHECK OUT MODULE                            //
			// --------------------------------------------------------------------- //
			addCommand(CHECK_OUT_GET_GUEST_LIST_EVENT, GetGuestListCommand);
			/* Item's routing commands */
			addCommand(CheckOutDelegate.GET_CHECKOUT_STATE, GetCheckoutStateCommand);
			addCommand(CheckOutDelegate.GET_CHECKOUT_STATE_FROM_INVOICE, GetCheckoutStateFromInvoiceCommand);
			addCommand(CheckOutDelegate.ADD_NEW_ITEMS, AddNewItemsCommand);
			addCommand(CheckOutDelegate.DELETE_ITEM, DeleteItemCommand);
			addCommand(CheckOutDelegate.SPLIT_ITEM, SplitItemCommand);
			addCommand(CheckOutDelegate.ADJUST_ITEM, AdjustItemCommand);
			addCommand(CheckOutDelegate.MERGE_ITEMS, MergeItemsCommand);
			addCommand(CheckOutDelegate.UNMERGE_ITEM, UnmergeItemCommand);
			addCommand(CheckOutDelegate.ATTACH_ITEMS_TO_ACCOUNT, AttachItemToAccountCommand);
			addCommand(CheckOutDelegate.DETACH_ITEMS_TO_ACCOUNT, DetachItemToAccountCommand);
			addCommand(CheckOutDelegate.ATTACH_PACKAGES_TO_ACCOUNT, AttachPackageToAccountCommand);
			addCommand(CheckOutDelegate.DETACH_PACKAGE_FROM_ACCOUNT, DetachPackageFromAccountCommand);
			addCommand(CheckOutDelegate.PRINT_ACTUAL_REPORT, PrintActualReportCommand);
			/* Payment's commands */
			addCommand(CheckOutDelegate.ADD_PAYMENT, AddPaymentCommand);
			addCommand(CheckOutDelegate.ADD_PAYMENTS, AddPaymentsCommand);
			addCommand(CheckOutDelegate.ADD_DEBITOR_PAYMENT, AddDebitorPaymentCommand);
			addCommand(CheckOutDelegate.DELETE_PAYMENT, DeletePaymentCommand);
			addCommand(CheckOutDelegate.PRINT_DEBIT_REPORT, PrintDebitReportCommand);
			addCommand(CheckOutDelegate.ACCEPT_PAYMENTS, AcceptPaymentsCommand);
			addCommand(CheckOutDelegate.DETACH_PAYMENTS_FROM_ACCOUNT, DetachPaymentsFromAccountCommand);
			/* Item's routing commands for In House */
			addCommand(CheckOutDelegate.GET_ITEMS_ROUTING, GetItemsRoutingCommand);
			addCommand(CheckOutDelegate.GET_RESERVATION_SUMMARY, GetReservationSummaryCommand);
			addCommand(CheckOutDelegate.GET_CHECK_OUT_STATE_IN_HOUSE, GetCheckoutStateFromInHouseCommand);




			//Invoice Managment
			addCommand(GetInvoiceListEvent.NAME,GetInvoiceListCommand);
			addCommand(GetInvoiceFileEvent.NAME,GetInvoiceFileCommand);
		}
	}
}