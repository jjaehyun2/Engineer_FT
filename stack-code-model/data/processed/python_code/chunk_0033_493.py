package services.events.inHouse
{
	import services.cairngorm.BaseEvent;

	public class GetMessageHistoryEvent extends BaseEvent
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  This property is id of person profile who received messages
		 *  (for see message's history by guest).
		 */
		private var _profileId:Number;
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  GetMessageHistoryEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function GetMessageHistoryEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Id of person profile who received messages.
		 */
		public function get profileId():Number
		{
			return _profileId;
		}
		/**
		 *  @private
		 */
		public function set profileId(value:Number):void
		{
			_profileId = value;
		}
	}
}