package services.vo.checkOut.itemRouting
{
	[RemoteClass(alias="MapAddedItem")]
	public class AddedItemVO
	{
		/**
		 *  This property is id of hotel item.
		 *  
		 *  @default 0
		 */
		public var lHotelItemId:Number = 0;
		/**
		 *  This property is price of hotel item.
		 *  
		 *  @default "0"
		 */
		public var fPrice:String = "0";
	}
}