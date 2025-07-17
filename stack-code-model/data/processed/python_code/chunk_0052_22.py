package org.avManager.events
{
	import flash.events.Event;
	
	public final class VideoClassificationEvent extends Event
	{
		
		public static const SELECTED:String = "selected";
		
		private var _classificationName:String;
		
		public function VideoClassificationEvent(type:String, classificationName:String = null)
		{
			super(type);
			_classificationName = classificationName;
		}

		public function get classificationName():String
		{
			return _classificationName;
		}

	}
}