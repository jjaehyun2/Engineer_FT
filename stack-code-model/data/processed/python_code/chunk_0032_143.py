package services.vo.common
{
	[RemoteClass(alias="MapVipHotel")]
	[Bindable]
	public class VipHotelVO
	{
		/**
		 *  This property contain id of VIP.
		 */
		public var lId:Number;
		/**
		 *  This property contain name of VIP.
		 */
		public var sName:String;
		/**
		 *  for interface.
		 */
		public var bIsSelected:Boolean = false;
	}
}