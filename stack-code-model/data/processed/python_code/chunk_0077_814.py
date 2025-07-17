package services.vo.common
{
	/**
	 *  Map class for communicate with server for get 
	 *  regions for necessary country.
	 *  
	 *  @author Artemyev Dmitriy
	 *  @date 04.06.2009
	 */
	[Bindable]
	[RemoteClass(alias="MapRegion")]
	public class RegionVO
	{
		/**
		 *  This property contain id of region.
		 */
		public var lId:Number = 0;
		/**
		 *  This property contain id of owner country
		 *  for region.
		 */
		public var lCountryId:Number;
		/**
		 *  This property contain name of region.
		 */
		public var sRegionName:String;
		/**
		 *  This property contain code of region.
		 */
		public var sRegionCode:String;
	}
}