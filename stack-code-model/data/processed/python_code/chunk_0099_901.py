package services.events.inHouse
{
	import services.cairngorm.BaseEvent;

	public class MarkMessageAsReadEvent extends BaseEvent
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  This property is id of message for person profile.
		 */
		private var _messageId:Number;
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  MarkMessageAsReadEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function MarkMessageAsReadEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Id of person profile who received messages.
		 */
		public function get messageId():Number
		{
			return _messageId;
		}
		/**
		 *  @private
		 */
		public function set messageId(value:Number):void
		{
			_messageId = value;
		}
	}
}