package services.vo.profiles
{
	import services.vo.common.ContactVO;
	
	[RemoteClass(alias="MapCompanyProfile")]
	[Bindable]
	public class CompanyProfileVO
	{
		/**
		 *  This property contain id
		 *  
		 *  @default 0
		 */
		public var lDataId:Number = 0;
		/**
		 *  This property contain main id.
		 *  
		 *  @default 0
		 */
		public var lMainId:Number = 0;
		/**
		 *  This property contain parent id. For example, for sub
		 *  companies it is id of company, who have this sub company.
		 *  
		 *  @default 0
		 */
		public var lParentId:Number = 0;
		/**
		 *  This property contain name.
		 */
		public var sName:String;
		/**
		 *  This property contain id of language.
		 */
		public var lLanguageId:Number = 0;
		/**
		 *  This property contain corporate ID.
		 */
		public var sCorporateId:String;
		/**
		 *  This property contain booking code.
		 */
		public var sBookingCode:String;
		/**
		 *  This property contain id of industry code.
		 */
		public var lMarketCodeId:Number = 0;
		/**
		 *  This property contain id of source code.
		 */
		public var lSourceCodeId:Number = 0;
		/**
		 *  This property contain state of guarantee
		 */
		public var bIsCanGuarantee:Boolean = false;
		/**
		 *  This property contain ...
		 */
		public var bIsTravelAgency:Boolean = false;
		/**
		 *  This property contain ...
		 *  
		 *  @see framework.vo.profiles.company.TACommissionVO
		 */
		public var aCommissions:/* TACommissionVO */Array = [];
		/**
		 *  This property contain ...
		 */
		public var sIataNumber:String;
		/**
		 *  This property contain list of callers.
		 *  
		 *  @default []
		 */
		public var aCallers:Array = [];
		/**
		 *  This property contain list of addresses of company.
		 *  
		 *  @default []
		 */
		public var aAddresses:Array = [];
		/**
		 *  This property contain list of contants of company.
		 *  
		 *  @default []
		 */
		public var aContacts:Array = [];
		/**
		 *  This property contain list of sub companies of company.
		 *  
		 *  @default []
		 */
		public var aSubCompanies:Array = [];
		
		private function checkTypeOfConfirmation(type:String,contactType:int):Boolean {
			var isNeededType:Boolean = false;
			switch(type){
				case 'SMS':
					if(contactType == 6) {
						isNeededType = true;
					}
					break;
				case 'Fax':
					if(contactType == 2) {
						isNeededType = true;
					}
					break;	
				case 'E-Mail':
					if(contactType == 3 || contactType == 7) {
						isNeededType = true;
					}
					break;
				}
			return isNeededType;
		}
		public function getDataForConfirmation(type:String):Array {
			var comfirmationData:Array = new Array();
			var i:int = 0;
			if(type == 'White') {
				for(i = 0; i < this.aAddresses.length; i++) {
					var address:CompanyAddressVO = this.aAddresses[i] as CompanyAddressVO;
					comfirmationData.push(address.sFullAddress);
				}
			}
			else {
				for(i = 0; i < this.aContacts.length; i++) {
					var contact:ContactVO = this.aContacts[i] as ContactVO;
					if(checkTypeOfConfirmation(type,contact.iContactType)) {
						comfirmationData.push(contact.sContactData);
					}
				} 
			}
			return comfirmationData;
		}
	}
}