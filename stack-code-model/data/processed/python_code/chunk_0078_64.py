package services.events.items.itemGroups
{
	import services.cairngorm.BaseEvent;
	import services.vo.items.ItemsGroupVO;
	
	public class SaveSystemSubGroupEvent extends BaseEvent
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  This property contain new adding sub groups or editing item of
		 *  sub group.
		 *  
		 *  @default new ItemsGroupVO()
		 *  
		 *  @see services.vo.backend.ItemsGroupVO
		 */
		private var _subGroups:ItemsGroupVO = new ItemsGroupVO();
		/**
		 *  This property contain index (position in the list) where needs
		 *  to add new system sub group or edited item of system sub group.
		 */
		private var _subGroupIndex:int;
		/**
		 *  This property contain id of main group for which will be added
		 *  new sub groups.
		 */
		private var _groupId:int;
		/**
		 *  This property contain index of the item in owner's group.
		 */
		private var _groupIndex:int;
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  SaveSystemSubGroupEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function SaveSystemSubGroupEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  New adding sub groups or editing item of system sub group.
		 */
		public function get subGroups():ItemsGroupVO
		{
			return _subGroups;
		}
		/**
		 *  @private
		 */
		public function set subGroups(value:ItemsGroupVO):void
		{
			_subGroups = value;
		}
		
		/**
		 *  The index (position in the list) where needs to add new
		 *  system sub group or edited item of system sub group.
		 */
		public function get subGroupIndex():int
		{
			return _subGroupIndex;
		}
		/**
		 *  @private
		 */
		public function set subGroupIndex(value:int):void
		{
			_subGroupIndex = value;
		}
		
		/**
		 *  Id of main group for which will be added new system
		 *  sub groups.
		 */
		public function get groupId():int
		{
			return _groupId;
		}
		/**
		 *  @private
		 */
		public function set groupId(value:int):void
		{
			_groupId = value;
		}
		
		/**
		 *  The index of the item in owner's group.
		 */
		public function get groupIndex():int
		{
			return _groupIndex;
		}
		/**
		 *  @private
		 */
		public function set groupIndex(value:int):void
		{
			_groupIndex = value;
		}
	}
}