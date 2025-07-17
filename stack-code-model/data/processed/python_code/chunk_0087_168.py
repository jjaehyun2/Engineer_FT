package services.vo.common.loyaltyPrograms
{
	[RemoteClass(alias="MapLoyaltyPrograms")]
	public class LoyaltyProgramsVO
	{
		/**
		 *  This property contain id of loyalty program
		 *  item.
		 */
		public var lId:Number = 0;
		/**
		 *  This property contain name of loyalty program
		 *  item.
		 */
		public var sName:String = '';
		/**
		 *  This property contain id of description for
		 *  loyalty program item.
		 */
		public var iDesc:int = 0;
		/**
		 *  This property contain description of loyalty
		 *  program item.
		 */
		public var sDesc:String = '';
		/**
		 *  For interface
		 */
		public var bIsSelected:Boolean = false;
	}
}