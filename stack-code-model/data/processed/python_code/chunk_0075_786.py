package services.vo.checkOut.itemRouting
{
	[RemoteClass(alias="MapAccountAddress")]
	public class AccountAddressVO
	{
		public static const TYPE_ADDRESS:int = 1;
		public static const TYPE_CARD:int = 2;
		/**
		 *  This property is id of address account.
		 */
		public var lId:Number;
		/**
		 *  This property is type of address account.
		 */
		public var iType:int;
		/**
		 *  This property address type.
		 */
		public var sAddressType:String;
		/**
		 *  This property is address account.
		 */
		public var sAddress:String;
	}
}