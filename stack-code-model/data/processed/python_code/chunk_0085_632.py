package services.vo.items
{
	import services.vo.MapValueObject;
	
	[RemoteClass(alias="MapItemsGroup")]
	[Bindable]
	public class ItemsGroupVO extends MapValueObject
	{
		/**
		 *  This property contain name of item.
		 */
		public var sName:String;
		/**
		 *  This property contain id of item.
		 *  
		 *  @default 0
		 */
		public var lId:int = 0;
		/**
		 *  This property contain id of hotel.
		 *  
		 *  @default 0
		 */
		public var lHotelId:int = 0;
		/**
		 *  This property contain sub group of item.
		 *  <p><b>Note:</b>the same sub groups can't have any 
		 *  subgroups.
		 *  
		 *  @deailt []
		 */
		public var aSubGroups:Array = [];
		/**
		 *  This property contain state of item. If it is <code>true</code>
		 *  than this item always choosed.
		 *  
		 *  @default false
		 */
		public var bIsDefault:Boolean = false;
		/**
		 *  This property is state of item. If it is <code>true</code>
		 *  than item is main group.
		 *  
		 *  @default false
		 */
		public var bIsGroup:Boolean = false;
		
		[Transient]
		/**
		 *  This property is <code>true</code> if item's state is check and
		 *  <code>false</code>  - if not.
		 *  <p><b>Note:</b>it needs for check state of item by update.
		 *  
		 *  @default false
		 */
		public var bSelected:Boolean = false;
		
		public function get children():Array
		{
			return aSubGroups.length == 0 ? null : aSubGroups;
		}
	}
}