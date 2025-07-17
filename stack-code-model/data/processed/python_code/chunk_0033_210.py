package services.vo.rates.bar
{
	[RemoteClass(alias="MapBarPrice")]
	[Bindable]
	public class BarPriceVO
	{
		public var iRateId:int;
		/**
		 *  This property contain id of room type.
		 */
		public var iRQualityId:int;
		/**
		 *  This property contain name of room type.
		 */
		public var sRQualityName:String;
		/**
		 *  This property contain
		 */
		public var fPriceOneAdult:Number;
		/**
		 *  This property contain
		 */
		public var fPriceTwoAdults:Number;
		/**
		 *  This property contain
		 */
		public var fPriceExtraAdult:Number;
		/**
		 *  This property contain
		 */
		public var fPriceChildAbove:Number;
		public var fPriceChildMiddle:Number;
		public var fPriceChildBefore:Number;
		/**
		 *  This property contain
		 */
		public var iMarkupDelta:int;
	}
}