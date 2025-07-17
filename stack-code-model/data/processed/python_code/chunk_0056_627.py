package services.vo.common
{
	[RemoteClass(alias="MapCity")]
	[Bindable]
	public class CityVO
	{
		/**
		 *  This property contain id of city.
		 */
		public var lId:Number;
		/**
		 *  This property contain id of owner region.
		 */
		public var lRegionId:Number;
		/**
		 *  This property contain name of city.
		 */
		public var sCityName:String;
	}
}