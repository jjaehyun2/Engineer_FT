package services.vo.profiles
{
	[RemoteClass(alias="MapProfileAddressPersonal")]
	public class ProfileAddressPersonalVO
	{
		/**
		 *  This property contain id.
		 *  
		 *  @default 0
		 */
		public var lId:Number = 0;
		/**
		 *  This property contain id of city.
		 */
		public var lCityId:Number = 0;
		/**
		 *  This property contain name of city.
		 */
		public var sCityName:String;
		/**
		 *  This property contain id of region.
		 */
		public var lRgnId:Number = 0;
		/**
		 *  This property contain name of region
		 */
		public var sRgnName:String;
		/**
		 *  This property contain id of country.
		 */
		public var lCountryId:Number = 0;
		/**
		 *  This property contain name of country.
		 */
		public var sCountryName:String;
		/**
		 *  This property contain line of address.
		 */
		public var sLine:String = "";
		/**
		 *  This property contain extended line of address.
		 */
		public var sLineExt:String = "";
		/**
		 *  This property contain zip or postal code.
		 */
		public var sZipCode:String = "";
		
		public function get sFullAddress():String {
			var address:String = "";
			address += this.sZipCode + ",";
			address += this.sLineExt + ",";
			address += this.sCityName + ",";
			address += this.sRgnName + ",";
			address += this.sCountryName;
			return address;
		}
		
	}
}