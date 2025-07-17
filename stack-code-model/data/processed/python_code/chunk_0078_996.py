package services.events.profiles.individual
{
	import services.cairngorm.BaseEvent;

	public class FindProfileByNameEvent extends BaseEvent
	{
		/**
		 *  This property contain pattern for search for profiles.
		 */
		private var _pattern:String;
		/**
		 *  This property contain index of page for get the sample
		 *  pages of profiles.
		 */
		private var _page:int;
		/**
		 *  This property contain count of profiles in the page.
		 */
		private var _count:int;
		/**
		 *  FindProfileByNameEvent. Constructor.
		 *  
		 *  @param type:String - The type of the event, accessible
		 *         as Event.type.
		 */
		public function FindProfileByNameEvent(type:String)
		{
			super(type);
		}
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  The pattern for search for profiles.
		 */
		public function get pattern():String
		{
			return _pattern;
		}
		/**
		 *  @private
		 */
		public function set pattern(value:String):void
		{
			_pattern = value;
		}
		
		
		/**
		 *  The index of page for get the sample pages of profiles.
		 */
		public function get page():Number
		{
			return _page;
		}
		/**
		 *  @private
		 */
		public function set page(value:Number):void
		{
			_page = value;
		}
		
		
		/**
		 *  The number of counts of profiles on the page.
		 */
		public function get count():Number
		{
			return _count;
		}
		/**
		 *  @private
		 */
		public function set count(value:Number):void
		{
			_count = value;
		}
	}
}