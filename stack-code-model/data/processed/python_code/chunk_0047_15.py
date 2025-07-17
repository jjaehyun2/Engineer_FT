package services.vo.frontend
{
	import mx.messaging.management.ObjectInstance;
	
	[RemoteClass(alias="MapAddress")]
	[Bindable]
	public class AddressVO extends ObjectInstance
	{
		/**
		 *  This property contain id of the street by zip code.
		 */
		public var lZipStreetId:Number;
		/**
		 *  This property contain id of zip code.
		 */
		public var lZipId:Number;
		/**
		 *  This property contain view of zip code.
		 */
		public var sZipCode:String;
		/**
		 *  This property contain id of the street.
		 */
		public var lStreetId:Number;
		/**
		 *  This property contain name of the street.
		 */
		public var sStreet:String;
		/**
		 *  This property contain id of the city.
		 */
		public var lCityId:Number;
		/**
		 *  This property contain name of the city.
		 */
		public var sCity:String;
		/**
		 *  This property contain id of the region.
		 */
		public var lRegionId:Number;
		/**
		 *  This property contain name of the region.
		 */
		public var sRegion:String;
		/**
		 *  This property contain id of the country.
		 */
		public var lCountryId:Number;
		/**
		 *  This property contain name of the country.
		 */
		public var sCountry:String;
		/**
		 *  This property contain detailed adress id. For example,
		 *  house, street, room, etc.
		 *  <p><b>Note:</b>it needs for server.
		 */
		public var lAddressDetailedId:Number;
		/**
		 *  This property contain additional information of the address.
		 */
		public var sAddressInfo:String;
		/**
		 *  This property contain extended information of the address.
		 */
		public var sAddressInfoExt:String;
		
		public function get sFullAddress():String {
			var address:String = "";
			address += this.sZipCode + ",";
			address += this.sAddressInfo + ",";
			address += this.sCity + ",";
			address += this.sRegion + ",";
			address += this.sCountry;
			return address;
		}
	}
}