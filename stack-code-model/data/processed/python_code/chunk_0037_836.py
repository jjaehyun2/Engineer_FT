package services.vo.common
{
	[Bindable]
	[RemoteClass(alias="MapCountry")]
	public class CountryVO
	{
		/**
		 *  This property contain id of country.
		 */
		public var lId:Number = 0;
		/**
		 *  This property contain name of country.
		 */
		public var sCountryName:String;
		/**
		 *  This property short name of country. For example,
		 *  DE, UA, UK, etc.
		 */
		public var sCountryCode:String;
		/**
		 *  This property contain default of country.
		 */
		public var bIsDefault:Boolean = false;
	}
}