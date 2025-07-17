package framework.view.components.address.data
{
	import flash.utils.Dictionary;
	
	import mx.collections.ArrayCollection;
	
	import services.vo.common.CityVO;
	import services.vo.common.CountryVO;
	import services.vo.common.RegionVO;
	import services.vo.frontend.StreetVO;
	
	[Bindable]
	public class AddressStorage
	{
		/**
		 *  This country contain dictionary with countries.
		 *  
		 *  @default = new Dictionary(true)
		 */
		protected var _country:Dictionary = new Dictionary(true);
		/**
		 *  This country contain dictionary with all regions.
		 *  
		 *  @default = new Dictionary(true)
		 */
		protected var _region:Dictionary = new Dictionary(true);
		/**
		 *  This country contain dictionary with all cities.
		 *  
		 *  @default = new Dictionary(true)
		 */
		protected var _city:Dictionary = new Dictionary(true);
		/**
		 *  This country contain dictionary with all street.
		 *  
		 *  @default = new Dictionary(true)
		 */
		protected var _street:Dictionary = new Dictionary(true);
		
		
		public function AddressStorage()
		{
		}
		/**
		 *  Add new country into the cashe for address's information
		 *  
		 *  @param country:CountryVO - data for new adding country.
		 */
		public function addCountry(country:CountryVO):void
		{
			if ((!country) || (_country[country.lId] != null)) return;
			
			var storage:CountryStorage = new CountryStorage();
			
			storage.country = country;
			
			_country[country.lId] = storage;
		}
		
		/**
		 *  Add region into the cashe for address's information by
		 *  owner country.
		 *  
		 *  @param region:RegionVO - data for new adding region.
		 */
		public function addRegion(region:RegionVO):void
		{
			if ((!region) || (_region[region.lId] != null)) return;
			
			(_country[region.lCountryId] as CountryStorage).regions.addItem(region);
			
			var storage:RegionStorage = new RegionStorage();
			
			storage.region = region;
			
			_region[region.lId] = storage;
		}
		
		/**
		 *  Add new city into the cashe for address's information by
		 *  owner region.
		 *  
		 *  @param city:CityVO - data for new adding city.
		 */
		public function addCity(city:CityVO):void
		{
			if ((!city) || (_city[city.lId] != null)) return;
			
			(_region[city.lRegionId] as RegionStorage).cities.addItem(city);
			
			var storage:CityStorage = new CityStorage();
			
			storage.city = city;
			
			_city[city.lId] = storage;
		}
		
		/**
		 *  Add new street into the cashe for address's information by
		 *  owner city.
		 *  
		 *  @param street:StreetVO - data for new adding street.
		 */
		public function addStreet(street:StreetVO):void
		{
			if ((!street) || (_street[street.lId] != null)) return;
			
			(_city[street.lCityId] as CityStorage).streets.addItem(street);
			
			_street[street.lId] = street;
		}
		
		/**
		 *  Get all countries.
		 *  
		 *  @return view as ArrayCollection for countries.
		 */
		public function getCountries():ArrayCollection
		{
			var res:ArrayCollection = new ArrayCollection();
			
			for(var prop:String in _country)
			{
				res.addItem((_country[prop] as CountryStorage).country);
			}
			
			return res;
		}
		
		/**
		 *  Get country by id.
		 *  
		 *  @param countryId:Number - id of owner country for region which 
		 *  we have to get for view for active country.
		 *  
		 *  @return view as ArrayCollection for active country.
		 */
		public function getCountry(countryId:Number):CountryVO
		{
			return (_country[countryId] as CountryStorage).country;
		}
		/**
		 *  Get all regions by id of owner country.
		 *  <p>Check exist country by his id. If country is active - get 
		 *  all gis regions for view as ArrayCollection.
		 *  
		 *  @param countryId:Number - id of owner country for region which 
		 *  we have to get for view for active country.
		 *  
		 *  @return view as ArrayCollection for active country.
		 */
		public function getRegions(countryId:Number):ArrayCollection
		{
			if (_country[countryId] == null) return new ArrayCollection();
			
			return (_country[countryId] as CountryStorage).regions;
		}
		/**
		 *  Get region by id.
		 *  
		 *  @param regionId:Number - id of region.
		 *  
		 *  @return data of region.
		 */
		public function getRegion(regionId:Number):RegionVO
		{
			return (_region[regionId] as RegionStorage).region;
		}
		
		/**		  
		 *  Check exist country by his id. 
		 *  
		 *  @param countryId:Number - id of owner country for region which 
		 *  we have to get for view for active country.
		 *  
		 *  @return Boolean.
		 */
		public function isPresentRegions(countryId:Number):Boolean
		{	
			//Alert.show("countryId: " + countryId + ", (_country[countryId] as CountryStorage).regions.length: " + (_country[countryId] as CountryStorage).regions.length, "", mx.controls.Alert.OK);		
			if (_country[countryId] == null)
			{			
			 	return false;
			}
			else
			{
				if((_country[countryId] as CountryStorage).regions.length == 0)
				{
					return false;	
				}
				else
				{					
					return true;
				} 
			}
		}
		
		/**
		 *  Get all cities by id of owner region.
		 *  <p>Check exist region by his id. If region is existed - get 
		 *  all his cities for view as ArrayCollection.
		 *  
		 *  @param regionId:Number - id of owner region by have to get
		 *  for view for active region.
		 *  
		 *  @return view as ArrayCollection for active region.
		 */
		public function getCities(regionId:Number):ArrayCollection
		{
			if (_region[regionId] == null) return new ArrayCollection();
			
			return (_region[regionId] as RegionStorage).cities;
		}
		/**
		 *  Get city by id.
		 *  
		 *  @param cityId:Number - id of city.
		 *  
		 *  @return data of city.
		 */
		public function getCity(cityId:Number):CityVO
		{
			return (_city[cityId] as CityStorage).city;
		}
		
		public function isCitiesPresent(regionId:Number):Boolean
		{
			if (_region[regionId] == null)
			{			
			 	return false;
			}
			else
			{
				if((_region[regionId] as RegionStorage).cities.length == 0)
				{
					return false;	
				}
				else
				{					
					return true;
				} 
			}
		}
		
		/**
		 *  Get all streets by id of owner city.
		 *  <p>Check exist city by his id. If city is existed - get 
		 *  all his streets for view as ArrayCollection.
		 *  
		 *  @param cityId:Number - id of owner city by have to get
		 *  for view for active city.
		 *  
		 *  @return view as ArrayCollection for active city.
		 */
		public function getStreets(cityId:Number):ArrayCollection
		{
			if (_city[cityId] == null) return new ArrayCollection();
			
			return (_city[cityId] as CityStorage).streets;
		}
		/**
		 *  Get street by id.
		 *  
		 *  @param cityId:Number - id of city.
		 *  
		 *  @return data of city.
		 */
		public function getStreet(streetId:Number):StreetVO
		{
			return _street[streetId];
		}
		
		
	}
}
	
import flash.utils.Dictionary;
import mx.collections.ArrayCollection;
import services.vo.frontend.StreetVO;
import services.vo.common.CityVO;
import services.vo.common.RegionVO;
import services.vo.common.CountryVO;

[Bindable]
class CountryStorage
{
	public var country:CountryVO;
	public var regions:ArrayCollection = new ArrayCollection();
}
[Bindable]
class RegionStorage
{
	public var region:RegionVO;
	public var cities:ArrayCollection = new ArrayCollection();
}
[Bindable]
class CityStorage
{
	public var city:CityVO;
	public var streets:ArrayCollection = new ArrayCollection();
}