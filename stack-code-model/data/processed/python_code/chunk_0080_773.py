package services.vo.rates.bar
{
	import mx.collections.ArrayCollection;

	[RemoteClass(alias="MapBarHotel")]
	[Bindable]
	public class BARItemObjectVO
	{
		/**
		 *  This property contain id of hotel.
		 */
		public var iBarId:int;
		/**
		 *  This property contain minimum stay days.
		 */
		public var iMinStay:int;
		/**
		 *  This property contain count days before.
		 */
		public var iCnlPolicy:int;
		/**
		 *  This property contain some description.
		 */
		public var sCnlDesc:String;
		/**
		 *  This property contain some description of event.
		 */
		public var sCnlDescEvent:String;
		/**
		 *  This property contain guarantee type. For example,
		 *    <ul>
		 *       <li><code>true</code> is YES;</li>
		 *       <li><code>false</code> is NO.</li>
		 *    </ul>
		 */
		public var bIsGuarantee:Boolean;
		/**
		 *  This property contain state of close to arrival.
		 */
		public var bIsClosedToArrival:Boolean;
		/**
		 *  This property contain hash code.
		 */
		public var sHashCode:String;
	}
}