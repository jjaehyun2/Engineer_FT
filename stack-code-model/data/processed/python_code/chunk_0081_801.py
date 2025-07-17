package framework.view.components.address.data
{
	import services.vo.profiles.CompanyAddressVO;
	import services.vo.profiles.ProfileAddressPersonalVO;
	
	[Bindable]
	public class LocationData
	{
		/**
		 *  This property is id of address line.
		 *  
		 *  @default 0
		 */
		public var locationId:Number = 0;
		/**
		 *  This property is address line.
		 *  
		 *  @default ""
		 */
		public var addressLine:String = "";
		/**
		 *  This property is extended address line.
		 *  
		 *  @default ""
		 */
		public var addressLineExt:String = "";
		/**
		 *  This property is zip code.
		 *  
		 *  @default ""
		 */
		public var zipCode:String = "";
		/**
		 *  This property is id of selected country.
		 *  
		 *  @default 0
		 */
		public var countryId:Number = 0;
		/**
		 *  This property is name of selected country.
		 *  
		 *  @default ""
		 */
		public var countryName:String = "";
		/**
		 *  This property is id of selected region.
		 *  
		 *  @default 0
		 */
		public var regionId:Number = 0;
		/**
		 *  This property is name of selected region.
		 *  
		 *  @default ""
		 */
		public var regionName:String = "";
		/**
		 *  This property is id of selected city.
		 *  
		 *  @default 0
		 */
		public var cityId:Number = 0;
		/**
		 *  This property is name of selected city.
		 *  
		 *  @default ""
		 */
		public var cityName:String = "";
		
		public static function convert(input:Object):LocationData
		{
			var location:LocationData = new LocationData();
			// converter for profile address
			if (input is ProfileAddressPersonalVO)
			{
				var prfAddress:ProfileAddressPersonalVO = input as ProfileAddressPersonalVO;
				location.locationId = prfAddress.lId;
				location.addressLine = prfAddress.sLine;
				location.addressLineExt = prfAddress.sLineExt;
				location.zipCode = prfAddress.sZipCode;
				location.countryId = prfAddress.lCountryId;
				location.countryName = prfAddress.sCountryName;
				location.regionId = prfAddress.lRgnId;
				location.regionName = prfAddress.sRgnName;
				location.cityId = prfAddress.lCityId;
				location.cityName = prfAddress.sCityName;
			}
			// converter for company address
			if (input is CompanyAddressVO)
			{
				var cmpAddress:CompanyAddressVO = input as CompanyAddressVO;
				location.locationId = cmpAddress.lId;
				location.addressLine = cmpAddress.sLine;
				location.addressLineExt = cmpAddress.sLineExt;
				location.zipCode = cmpAddress.sZipCode;
				location.countryId = cmpAddress.lCountryId;
				location.countryName = cmpAddress.sCountryName;
				location.regionId = cmpAddress.lRgnId;
				location.regionName = cmpAddress.sRgnName;
				location.cityId = cmpAddress.lCityId;
				location.cityName = cmpAddress.sCityName;
			}
			
			return location;
		}
		/**
		 *  Make address for person profile by adderss fields.
		 *  
		 *  @result ProfileAddressPersonalVO - address for person profile.
		 *  
		 *  @see framework.vo.profiles.ProfileAddressPersonalVO
		 */
		public function toProfileAddress():ProfileAddressPersonalVO
		{
			var address:ProfileAddressPersonalVO = new ProfileAddressPersonalVO();
			
			address.lId = locationId;
			address.sLine = addressLine;
			address.sLineExt = addressLineExt;
			address.sZipCode = zipCode;
			address.lCountryId = countryId;
			address.sCountryName = countryName;
			address.lRgnId = regionId;
			address.sRgnName = regionName;
			address.lCityId = cityId;
			address.sCityName = cityName;
			
			return address;
		}
		
		/**
		 *  Make address for company profile by adderss fields.
		 *  
		 *  @result ProfileAddressPersonalVO - address for company profile.
		 *  
		 *  @see framework.vo.profiles.ProfileAddressPersonalVO
		 */
		public function toCompanyAddress(isPrimary:Boolean = false, isBilling:Boolean = false):CompanyAddressVO
		{
			var address:CompanyAddressVO = new CompanyAddressVO();
			
			address.bIsBilling = isBilling;
			address.bIsPrimary = isPrimary;
			address.lId = locationId;
			address.sLine = addressLine;
			address.sLineExt = addressLineExt;
			address.sZipCode = zipCode;
			address.lCountryId = countryId;
			address.sCountryName = countryName;
			address.lRgnId = regionId;
			address.sRgnName = regionName;
			address.lCityId = cityId;
			address.sCityName = cityName;
			
			return address;
		}
	}
}