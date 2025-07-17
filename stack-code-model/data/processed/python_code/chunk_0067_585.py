package gs.audio
{
	import gs.events.AudioEvent;
	import gs.util.MathUtils;

	import com.greensock.TweenMax;

	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.TimerEvent;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.media.SoundTransform;
	import flash.utils.Dictionary;
	import flash.utils.Timer;

	/**
	 * Dispatched when the sound starts playing.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("start", type="gs.support.soundmanager.AudioEvent")]
	
	/**
	 * Dispatched when the sound stops playing.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("stop", type="gs.support.soundmanager.AudioEvent")]
	
	/**
	 * Dispatched for progress of the audio.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("progress", type="gs.support.soundmanager.AudioEvent")]
	
	/**
	 * Dispatched when the sound is paused.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("paused", type="gs.support.soundmanager.AudioEvent")]
	
	/**
	 * Dispatched when the sound is resumed.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("resumed", type="gs.support.soundmanager.AudioEvent")]
	
	/**
	 * Dispatched when the sound has looped.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("looped", type="gs.support.soundmanager.AudioEvent")]
	
	/**
	 * Dispatched when the sound is muted.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("mute", type="gs.support.soundmanager.AudioEvent")]
	
	/**
	 * Dispatched when the sound is un-muted.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("unmute", type="gs.support.soundmanager.AudioEvent")]
	
	/**
	 * Dispatched when the sound has completed playing.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("complete", type="gs.support.soundmanager.AudioEvent")]

	/**
	 * Dispatched when the volume changes
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("volumeChange", type="gs.support.soundmanager.AudioEvent")]

	/**
	 * Dispatched when the panning changes.
	 * 
	 * @eventType gs.support.soundmanager.AudioEvent
	 */
	[Event("panChange", type="gs.support.soundmanager.AudioEvent")]

	/**
	 * The AudioObject class controls any audible object.
	 * It can control a sound instance or any object with
	 * a <em><strong>soundTransform</strong></em> property.
	 * 
	 * <p><b>Examples</b> are in the guttershark repository.</p>
	 * 
	 * @see gs.audio.AudioGroup
	 */
	public class AudioObject extends EventDispatcher
	{
		
		/**
		 * Internal dictionary for audio objects.
		 */
		private static var _ao:Dictionary = new Dictionary();

		/**
		 * @private
		 * The id of this audible object.
		 */
		public var id:String;
		
		/**
		 * @private
		 * The object being controled.
		 */
		public var obj:*;
		
		/**
		 * @private
		 * The group this audible object belongs to if any.
		 */
		public var group:AudioGroup;
		
		/**
		 * The type of this audible object.
		 */
		private var type:String;
		
		/**
		 * The play options.
		 */
		private var ops:Object;
		
		/**
		 * The sound channel if this is controlling a Sound.
		 */
		private var channel:SoundChannel;
		
		/**
		 * A transform used to keep reference to the volume.
		 */
		private var transform:SoundTransform;
		
		/**
		 * A volume var holder for mute/unmute.
		 */
		private var vol:Number;
		
		/**
		 * Whether or not this audible object is muted.
		 */
		private var muted:Boolean;
		
		/**
		 * A sound loop watching timer.
		 */
		private var loopWatcher:Timer;
		
		/**
		 * How many loops have occured.
		 */
		private var loops:Number;

		/**
		 * Whether or not this audible object is playing.
		 */
		private var _isPlaying:Boolean;
		
		/**
		 * Whether ot not the object is paused.
		 */
		private var _isPaused:Boolean;
		
		/**
		 * A holder var for the pause position, which
		 * is used to resume to.
		 */
		private var pausePosition:Number;
		
		/**
		 * The pixels to fill for this audible object.
		 */
		private var _pixelsToFill:int;
		
		/**
		 * The timer used for progress events.
		 */
		private var progressTimer:Timer;
		
		/**
		 * Whether or not this instance will dispatch progress events.
		 */
		private var dispatchesProgress:Boolean;
		
		/**
		 * The progress timer interval.
		 */
		private var _progressTimerInterval:int;
		
		/**
		 * Get an audio object.
		 * 
		 * @param id The audio object id.
		 */
		public static function get(id:String):AudioObject
		{
			if(!id)return null;
			return _ao[id];
		}
		
		/**
		 * Save an audio object.
		 * 
		 * @param id The id of the audio group.
		 * @param ag The audio group.
		 */
		public static function set(id:String,ao:AudioObject):void
		{
			if(!id||!ao)return;
			if(!ao.id)ao.id=id;
			_ao[id]=ao;
		}
		
		/**
		 * Unset (delete) an audio object.
		 * 
		 * @param id The audio object id.
		 */
		public static function unset(id:String):void
		{
			if(!id)return;
			delete _ao[id];
		}
		
		/**
		 * Constructor for AudioObject instances.
		 * 
		 * @param obj The object to control.
		 */
		public function AudioObject(_obj:*):void
		{
			_progressTimerInterval=300;
			if(!_obj)throw new ArgumentError("ERROR: Parameter {_obj} cannot be null.");
			dispatchesProgress=false;
			obj=_obj;
			if(obj is Sound)type="s";
			else if("soundTransform" in obj)type="o";
			else throw new Error("The volume for the object added cannot be controled, it must be a Sound or contain a {soundTransform} property.");
			progressTimer=new Timer(300);
			transform=new SoundTransform();
			pausePosition=0;
			muted=false;
			ops={};
		}
		
		/**
		 * The interval for dispatching progress events.
		 */
		public function set progressTimerInterval(val:int):void
		{
			_progressTimerInterval=val;
			stopProgressEvents();
			progressTimer=new Timer(_progressTimerInterval);
			if(dispatchesProgress && _isPlaying)startProgressEvents();
		}
		
		/**
		 * The interval for dispatching progress events.
		 */
		public function get progressTimerInterval():int
		{
			return _progressTimerInterval;
		}
		
		/**
		 * @private
		 * Set the id and group.
		 */
		public function setIdAndGroup(_id:String,_group:AudioGroup):void
		{
			id=_id;
			group=_group;
		}

		/**
		 * Play this audio object.
		 * 
		 * <p>Available options:</p>
		 * <ul>
		 * <li>volume (Number) - The volume to play the audio at.</li>
		 * <li>startTime (Number) - A start offset in milliseconds to start playing the audio from.</li>
		 * <li>loops (Number) - The number of times to loop the sound.</li>
		 * <li>panning (Number) - A panning value for the audio.</li>
		 * <li>restartIfPlaying (Boolean) - If this audible object is playing, and you call play again, it will (by defualt) not do anything,
		 * unless this option is true, which will restart the playing sound.</li>
		 * </ul>
		 * 
		 * @param _ops Play options.
		 */
		public function play(_ops:Object=null):void
		{
			if(!_ops)_ops={};
			if(type=="o")
			{
				trace("WARNING: An audible object cannot 'play' a display object it's managing.");
				return;
			}
			ops=_ops;
			if((!ops&&_isPlaying) || (!ops.restartIfPlaying&&_isPlaying))return;
			if(_isPlaying)channel.stop();
			removeListeners();
			var startTime:Number=(ops.startTime)?ops.startTime:0;
			var loops:Number=(ops.loops)?ops.loops:0;
			var panning:Number=(ops.panning)?ops.panning:0;
			var volume:Number=(ops.volume)?ops.volume:1;
			if(transform.volume && !ops.volume)volume=transform.volume;
			transform=new SoundTransform(volume,panning);
			if(loops>0)loopWatcher=new Timer(obj.length);
			dispatchEvent(new AudioEvent(AudioEvent.START));
			channel=obj.play(startTime,loops,transform);
			addListeners();
			if(loopWatcher)loopWatcher.start();
			_isPlaying=true;
			if(dispatchesProgress)startProgressEvents();
		}
		
		/**
		 * Add listeners for loop and complete.
		 */
		private function addListeners():void
		{
			if(loopWatcher)loopWatcher.addEventListener(TimerEvent.TIMER,onLoop,false,0,true);
			if(channel)channel.addEventListener(Event.SOUND_COMPLETE,onComplete,false,0,true);
		}
		
		/**
		 * Remove listeners for loop and complete.
		 */
		private function removeListeners():void
		{
			if(loopWatcher)loopWatcher.removeEventListener(TimerEvent.TIMER,onLoop);
			if(channel)channel.removeEventListener(Event.SOUND_COMPLETE,onComplete);
		}
		
		/**
		 * Check whether or not the sound is playing.
		 */
		public function get isPlaying():Boolean
		{
			if(type=="o")return false;
			return _isPlaying;
		}
		
		/**
		 * Check whether or not the sound is paused.
		 */
		public function get isPaused():Boolean
		{
			if(type=="o")return false;
			return _isPaused;
		}
		
		/**
		 * When a loop occurs.
		 */
		private function onLoop(e:TimerEvent):void
		{
			loops++;
			dispatchEvent(new AudioEvent(AudioEvent.LOOPED));
		}
		
		/**
		 * On complete.
		 */
		private function onComplete(e:Event):void
		{
			if(loopWatcher)loopWatcher.stop();
			_isPlaying=false;
			dispatchEvent(new AudioEvent(AudioEvent.COMPLETE));
			if(group)
			{
				group.cleanupAudibleObject(this);
				dispose();
				return;
			}
			stopProgressEvents();
		}
		
		/**
		 * Stop playing.
		 */
		public function stop():void
		{
			if(type=="o")return;
			if(loopWatcher)loopWatcher.stop();
			channel.stop();
			_isPlaying=false;
			dispatchEvent(new AudioEvent(AudioEvent.STOP));
			if(group)
			{
				group.cleanupAudibleObject(this);
				dispose();
				return;
			}
			stopProgressEvents();
		}
		
		/**
		 * Pause playing.
		 */
		public function pause():void
		{
			if(type=="o"||_isPaused)return;
			_isPlaying=false;
			if(loopWatcher)loopWatcher.stop();
			dispatchEvent(new AudioEvent(AudioEvent.PAUSED));
			pausePosition=channel.position;
			channel.stop();
			stopProgressEvents();
			_isPaused=true;
		}
		
		/**
		 * Resume playing.
		 */
		public function resume():void
		{
			if(type=="o"||_isPlaying||!_isPaused)return;
			_isPlaying=true;
			_isPaused=false;
			removeListeners();
			var startTime:Number=pausePosition;
			var loops:Number=(ops.loops)?ops.loops:0;
			channel=obj.play(startTime,loops,transform);
			if(!muted)channel.soundTransform=transform;
			dispatchEvent(new AudioEvent(AudioEvent.RESUMED));
			addListeners();
			if(loopWatcher)loopWatcher.start();
			if(dispatchesProgress)startProgressEvents();
		}
		
		/**
		 * Accessor method to get the channel or obj variable.
		 * 
		private function getObj():*
		{
			if(type=="s")return channel;
			else if(type=="o")return obj;
			return null;
		}*/
		
		/**
		 * Updates the sound transform.
		 */
		private function updateTransform():void
		{
			if(type=="s" && channel)channel.soundTransform=transform;
			else if(type=="o" && obj)obj.soundTransform=transform;
		}

		/**
		 * Increase the volume.
		 * 
		 * @param step The amount to increase the volume by.
		 */
		public function increaseVolume(step:Number=.1):void
		{
			transform.volume+=step;
			updateTransform();
		}
		
		/**
		 * Decrease the volume.
		 * 
		 * @param step The amount to decrease the volume by.
		 */
		public function decreaseVolume(step:Number=.1):void
		{
			if(transform.volume==0)return;
			transform.volume-=step;
			updateTransform();
		}
		
		/**
		 * Mute.
		 */
		public function mute():void
		{
			if(muted||transform.volume==0)return;
			muted=true;
			vol=transform.volume;
			transform.volume=0;
			updateTransform();
			dispatchEvent(new AudioEvent(AudioEvent.MUTE));
		}
		
		/**
		 * Un-mute.
		 */
		public function unMute():void
		{
			if(!muted)return;
			muted=false;
			transform.volume=vol;
			updateTransform();
			dispatchEvent(new AudioEvent(AudioEvent.UNMUTE));
		}
		
		/**
		 * Toggle mute.
		 */
		public function toggleMute():void
		{
			if(muted)unMute();
			else mute();
		}
		
		/**
		 * Tween the panning.
		 * 
		 * @param pan The new pan level.
		 * @param duration The time it takes to tween the panning.
		 */
		public function panTo(pan:Number,duration:Number=.3):void
		{
			TweenMax.to(this,duration,{pn:pan});
		}
		
		/**
		 * Panning.
		 * 
		 * @param panning The new panning value.
		 */
		public function set panning(panning:Number):void
		{
			if(transform.pan!=panning)dispatchEvent(new AudioEvent(AudioEvent.PAN_CHANGE));
			if(transform.pan==panning)return;
			transform.pan=panning;
			updateTransform();
		}
		
		/**
		 * Panning.
		 * 
		 * @param panning The new panning value.
		 */
		public function get panning():Number
		{
			return transform.pan;
		}
		
		/**
		 * Set the panning.
		 */
		public function set pn(panning:Number):void
		{
			transform.pan=panning;
			updateTransform();
		}
		
		/**
		 * A tween property for panning.
		 */
		public function get pn():Number
		{
			return transform.pan;
		}
		
		/**
		 * Set the volume for this audible object.
		 * 
		 * @param level The volume level.
		 */
		public function set volume(level:Number):void
		{
			if(transform.volume!=level)dispatchEvent(new AudioEvent(AudioEvent.VOLUME_CHANGE));
			if(transform.volume==level)return;
			transform.volume=level;
			updateTransform();
		}
		
		/**
		 * Volume.
		 */
		public function get volume():Number
		{
			return transform.volume;
		}
		
		/**
		 * Tween the volume.
		 * 
		 * @param level The new volume level.
		 * @param duration The time it takes to tween to the new level.
		 */
		public function volumeTo(level:Number,duration:Number=.3):void
		{
			TweenMax.to(this,duration,{vl:level});
		}
		
		/**
		 * A tween property for volume.
		 */
		public function get vl():Number
		{
			return transform.volume;
		}
		
		/**
		 * Tween volume.
		 */
		public function set vl(level:Number):void
		{
			transform.volume=level;
			updateTransform();
		}
		
		/**
		 * Set the volume. This is a helper method in case you need to
		 * use setTimeout with volume.
		 * 
		 * @param level The volume level.
		 */
		public function setVolume(level:Number):void
		{
			volume=level;
		}
		
		/**
		 * Seek to a position in the sound.
		 * 
		 * @param position The position of the sound to seek to.
		 */
		public function seek(position:Number):void
		{
			if(type=="o")
			{
				trace("WARNING: Seek is not supported for non Sound instances.");
				return;
			}
			if(!position)return;
			removeListeners();
			channel.stop();
			var lps:int=(ops.loops)?ops.loops:0;
			if(lps>0 && loops>1) lps=loops-lps;
			if(lps<0)lps=0;
			channel=Sound(obj).play(position,lps,transform);
		}
		
		/**
		 * Seek to a percent of the sound.
		 * 
		 * @param percent The percent to seek to.
		 */
		public function seekToPercent(percent:Number):void
		{
			if(type=="o")
			{
				trace("WARNING: Seek to percent is not supported when managing display objects.");
				return;
			}
			seek(Sound(obj).length*percent/100);
		}
		
		/**
		 * Seek to a pixel (first set pixels to fill).
		 * 
		 * @param pixel The pixel to seek to.
		 */
		public function seekToPixel(pixel:Number):void
		{
			if(type=="o")
			{
				trace("WARNING: Seek to pixels is not supported when managing display objects.");
				return;
			}
			seek(MathUtils.spread(pixel,pixelsToFill,Sound(obj).length));
		}
		
		/**
		 * Get the percentage of the sound that has played.
		 */
		public function percentPlayed():Number
		{
			if(type=="o")
			{
				trace("WARNING: A display object does not have a percent played value.");
				return -1;
			}
			if(channel.position==0||!channel||!channel.position)return 0;
			return Sound(obj).length/channel.position;
		}
		
		/**
		 * Get the amount of pixels that have played.
		 */
		public function pixelsPlayed():int
		{
			if(type=="o")
			{
				trace("WARNING: A display object does not have a pixels played value.");
				return -1;
			}
			if(!_pixelsToFill)
			{
				trace("WARNING: The pixels to fill is not set. It must be set before using pixelsPlayed()");
				return -1;
			}
			return MathUtils.spread(channel.position,Sound(obj).length,_pixelsToFill);
		}
		
		/**
		 * The amount of pixels to fill for this audio object.
		 * 
		 * @param pixels The amount of pixels to fill.
		 */
		public function set pixelsToFill(pixels:int):void
		{
			_pixelsToFill=pixels;
		}
		
		/**
		 * The amount of pixels to fill for this audio object.
		 */
		public function get pixelsToFill():int
		{
			return _pixelsToFill;
		}
		
		/**
		 * Starts the progress logic.
		 */
		private function startProgressEvents():void
		{
			progressTimer.addEventListener(TimerEvent.TIMER,onTick,false,0,true);
			if(!_isPlaying)return;
			progressTimer.start();
		}
		
		/**
		 * Stops the progress logic.
		 */
		private function stopProgressEvents():void
		{
			progressTimer.stop();
			progressTimer.removeEventListener(TimerEvent.TIMER,onTick);
		}
		
		/**
		 * On tick for progres timer.
		 */
		private function onTick(ev:TimerEvent):void
		{
			if(!_isPlaying)return;
			var e:AudioEvent=new AudioEvent(AudioEvent.PROGRESS,false,true);
			e.pixelsPlayed=pixelsPlayed();
			e.percentPlayed=percentPlayed();
			dispatchEvent(e);
		}
		
		/**
		 * @private
		 */
		override public function addEventListener(type:String,listener:Function,useCapture:Boolean=false,priority:int=0,useWeakReference:Boolean=false):void
		{
			super.addEventListener(type,listener,useCapture,priority,useWeakReference);
			if(type==AudioEvent.PROGRESS)dispatchesProgress=true;
		}
		
		/**
		 * @private
		 */
		override public function removeEventListener(type:String,listener:Function,useCapture:Boolean=false):void
		{
			super.removeEventListener(type,listener,useCapture);
			if(type==AudioEvent.PROGRESS)dispatchesProgress=false;
		}
		
		/**
		 * Dispose of this audible object.
		 */
		public function dispose():void
		{
			removeListeners();
			stopProgressEvents();
			_progressTimerInterval=0;
			dispatchesProgress=false;
			id=null;
			obj=null;
			type=null;
			transform=null;
			vol=NaN;
			_isPlaying=false;
			loops=NaN;
			loopWatcher=null;
			ops=null;
			group=null;
			channel=null;
			muted=false;
			pausePosition=NaN;
			_pixelsToFill=0;
		}
	}
}