package services.vo.profiles
{
	[RemoteClass(alias="MapCompanyProfileView")]
	[Bindable]
	public class CompanyProfileViewVO
	{
		/**
		 *  This property contain id.
		 */
		public var lId:Number = 0;
		/**
		 *  This property contain main id.
		 */
		public var lMainId:Number = 0;
		/**
		 *  This property contain name.
		 */
		public var sName:String;
		/**
		 *  This property contain city.
		 */
		public var sCity:String;
		/**
		 *  This property contain country.
		 */
		public var sCountry:String;
		/**
		 *  This property contain phone number.
		 */
		public var sPhone:String;
		/**
		 *  This property contain e-mail
		 */
		public var sEmail:String;
		/**
		 *  This property contain list of sub companies of company.
		 *  
		 *  @default []
		 */
		public var aSubCompanies:Array = [];
		/**
		 *  This property is <code>true</code>, company is travel agency.
		 *  
		 *  @default fasle
		 */
		public var bIsTa:Boolean = false;
	}
}