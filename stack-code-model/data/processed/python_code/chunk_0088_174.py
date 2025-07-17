package services.events.miscellaneous.countries
{
	import services.cairngorm.BaseEvent;
	/**
	 *  The event to get region by id of woner country.
	 *  
	 *  @author Artemyev Dmitriy
	 * 	@updater Potapov Viktor
	 *  @date 08.06.2009
	 *  
	 *  @see com.adobe.cairngorm.control.CairngormEvent
	 */
	public class GetRegionEvent extends BaseEvent
	{
		/**
		 *  This property contain id of owner country for 
		 *  neccessary region.
		 */
		public var countryId:Number;
		public var loadDefault:Boolean = true;
		/**
		 *  GetRegionEvent. Constructor.
		 */
		public function GetRegionEvent(type:String)
		{
			super(type);
		}
	}
}