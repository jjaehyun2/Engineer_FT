////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2008 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package core.timeline
{
	import flash.utils.getTimer;
	
	/**
	 * The Timeline class is an internal utility used by Animation to
	 * keep a single pulse for animations. This ensures that all animations
	 * run off a single timer, rather than individually calling getTimer().
	 * This approach means that effects that are set up to end/start at the same
	 * time, through use of duration and startDelay properties, will be
	 * synchronized.
	 *
	 *  @langversion 3.0
	 *  @playerversion Flash 10
	 *  @playerversion AIR 1.5
	 *  @productversion Flex 4
	 */
	public class Timeline
	{
		// TODO (chaase): This class is internal for now, but it may eventually
		// make sense to make it public and accessible outside of just the
		// Animation class. For example, effects may want to access the global
		// animation time. Also, we  may want to have child timelines, or expose
		// other capabilities such as speeding up and slowing down time.
		// Note that the static methods may instead become instance methods
		// on a singleton.
		
		private static var prevTime:int = -1;
		private static var _currentTime:int = -1;
		private static var _tickSpeed:Number = 1;
		
		public function Timeline()
		{
		}
		
		public static function pulse():int
		{
			if (_currentTime == -1)
			{
				_currentTime = 0;
				prevTime = getTimer()
				return _currentTime;
			}
			var current:int = getTimer();
			_currentTime = _currentTime + (current - prevTime) * _tickSpeed;
			prevTime = current;
			return _currentTime;
		}
		
		public static function get currentTime():int
		{
			if (_currentTime < 0)
			{
				var retVal:int = pulse();
				return pulse();
			}
			return _currentTime;
		}
		
		public static function set tickSpeed(value:Number):void{
			_tickSpeed = value;
		}
	}
}