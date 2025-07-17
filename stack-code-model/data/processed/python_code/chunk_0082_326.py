package services.vo.rates.bar
{
	[RemoteClass(alias="MapBarDate")]
	public class BARSaveItemVO
	{
		/**
		 *  This property contain date by string format.
		 */
		public var sBarDate:String;
		/**
		 *  This property contain id of owner hotel.
		 */
		public var lHotelId:Number;
		/**
		 *  This property contain info about BAR item.
		 *  
		 *  @see framework.vo.backend.BARItemObjectVO
		 */
		public var oBarHotel:BARItemObjectVO;
		/**
		 *  This property contain prices for all room types.
		 */
		public var aBarPrices:Array;
	}
}