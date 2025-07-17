/*

Copyright (c) 2009 Ronny Welter

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
 
*/

package com.nocreativity.playr{
	import flash.events.Event;
		/**
		 * Dedicated event class. These events are the only events you should be listening to. Built-in events from Flash will not be fired by Playr.
		 */
	public class PlayrEvent extends Event{
		
		
		private var _progress:Number= 0;
		
		public var totalTime:String="0:00";
		public var totalSeconds:Number = 0;
		public var currentTime:String="0:00";
		public var currentSeconds:Number = 0;
		public var volume:Number=0;
		public var playrState:String=PlayrStates.INIT;
		
		
		public static const SONGINFO:String = "songinfo";
		public static const MUTED:String = "muted";
		public static const UNMUTED:String = "unmuted";
		public static const VOLUME_SET:String = "volume_set";
		public static const TRACK_COMPLETE:String='track_complete';
		public static const NEXT_TRACK:String = "next_track";
		public static const PREV_TRACK:String = "prev_track";
		public static const TRACK_PROGRESS:String = "track_progress";
		public static const STREAM_PROGRESS:String = "stream_progress";
		public static const PLAYLIST_LOADED:String = "playlist_loaded";
		public static const PLAYRSTATE_CHANGED:String = "playrstate_changed";
		public static const PLAYR_SCROBBLED:String = "playr_scrobbled";
		public static const PLAYLIST_END_REACHED:String = "playlist_end_reached";
		public static const PLAYLIST_UPDATED:String='playlist_updated';
		public static const TRACK_REMOVED:String='track_removed';
		
		
		public function PlayrEvent(type:String){
			super(type,true);
		}
		public function get progress():Number{
			return _progress;
		}
		public function set progress(value:Number):void{
			if(value>1){
				_progress = 1;
			}
			else if(value<0){
				_progress = 0;
			}
			else{
				_progress  = value;
			}
		}
	}
}