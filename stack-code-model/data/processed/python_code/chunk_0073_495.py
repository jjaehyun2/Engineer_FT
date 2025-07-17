package framework.view.pages.items.data
{
	public class GroupData
	{
		/**
		 *  This property contain id of main group for view into popup
		 *  for add and edit modes.
		 *  
		 *  @default -1
		 */
		private var _mainGroupId:Number = -1;
		/**
		 *  This property contain id of sub group for view into popup
		 *  for add and edit modes.
		 *  
		 *  @default -1
		 */
		private var _subGroupId:Number = -1;
		
		public function GroupData(id:Number = -1, subId:Number = -1)
		{
			_mainGroupId = id;
			_subGroupId = subId;
		}
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Id of main group for view into popup for add and edit modes.
		 */
		public function get mainGroupId():Number
		{
			return _mainGroupId;
		}
		/**
		 *  @private
		 */
		public function set mainGroupId(value:Number):void
		{
			_mainGroupId = value;
		}
		
		/**
		 *  Id of sub group for view into popup for add and edit modes.
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
	}
}