package services.events.items.itemGroups
{
	import services.cairngorm.BaseEvent;

	public class DeleteSystemSubGroupEvent extends BaseEvent
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  This property contain id of removing system sub group.
		 */
		private var _subGroupId:Number;
		/**
		 *  This property contain index of removing system sub group
		 *  in data provider.
		 */
		private var _subGroupIndex:int;
		/**
		 *  This property contain index of system main group, which
		 *  consist removing sub group.
		 */
		private var _groupIndex:int;
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  DeleteSystemSubGroupEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function DeleteSystemSubGroupEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Id of removing system sub group.
		 */
		public function get subGroupId():Number
		{
			return _subGroupId;
		}
		/**
		 *  @private
		 */
		public function set subGroupId(value:Number):void
		{
			_subGroupId = value;
		}
		
		/**
		 *  The index of removing system sub group in data provider.
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
		 *  The index of system main group, which consist removing sub
		 *  group.
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