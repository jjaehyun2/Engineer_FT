package services.events.profiles.individual
{
	import services.cairngorm.BaseEvent;

	public class DeletePersonalProfileEvent extends BaseEvent
	{
		/**
		 *  This property contain id of profile by person,
		 *  which will be removed.
		 */
		private var _id:Number;
		/**
		 *  This property contain index of profile into the
		 *  list of individual profiles.
		 */
		private var _index:Number;
		/**
		 *  DeletePersonalProfileEvent. Constructor.
		 *  
		 *  @param type:String - The type of the event, accessible
		 *         as Event.type.
		 */
		public function DeletePersonalProfileEvent(type:String, id:Number = -1, index:Number = -1)
		{
			super(type);
			_id = id;
			_index = index;
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Id of profile by person, which will be removed.
		 */
		public function get id():Number
		{
			return _id;
		}
		/**
		 *  @private
		 */
		public function set id(value:Number):void
		{
			_id = value;
		}
		
		/**
		 *  The index of profile into the list of individual profiles.
		 */
		public function get index():Number
		{
			return _index;
		}
		/**
		 *  @private
		 */
		public function set index(value:Number):void
		{
			_index = value;
		}
	}
}