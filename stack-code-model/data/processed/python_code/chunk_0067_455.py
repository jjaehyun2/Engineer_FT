package devoron.components.multicontainers.timeline
{
	import devoron.studio.modificators.timeline2.TimelineLabel;
	import flash.events.Event;
	
	/**
	 * TimelineEvent
	 * @author Devoron
	 */
	public class TimelineEvent extends Event
	{
		
		public static const LABEL_ADDED:String = "label_added";
		public static const LABEL_REMOVED:String = "label_removed";
		public static const LABEL_SELECTED:String = "label_selected";
		public static const LABEL_CHANGED:String = "label_changed";
		public static const TRACK_MOVED:String = "track_moved";
		public static const TRACK_SELECTED:String = "track_selected";
		
		private var _label:TimelineLabel;
		private var _track:*;
		
		public function TimelineEvent(object:*, type:String, bubbles:Boolean = false, cancelable:Boolean = false)
		{
			super(type, bubbles, cancelable);
			if (object is TimelineLabel)
			{
				_label = object;
			}
			/*else if (object is Track)
			{
				_track = object;
			}
			else
			{
				throw new Error("Unknown timeline component");
			}*/
		
		}
		
		override public function clone():Event
		{
			if (_label)
				return new TimelineEvent(_label, type, bubbles, cancelable);
			else if (_track)
				return new TimelineEvent(_track, type, bubbles, cancelable);
			return null;
		}
		
		public function get label():TimelineLabel
		{
			return _label;
		}
		
		/*public function get track():Track
		{
			return _track;
		}*/
	
	}

}