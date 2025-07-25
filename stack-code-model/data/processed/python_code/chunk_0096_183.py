package flixel.system
{
	import flixel.FlxG;
	import flixel.util.FlxPoint;
	import flixel.util.FlxTween;
	import flixel.FlxObject;
	import flixel.FlxBasic;
	import flash.events.Event;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.media.SoundTransform;
	import flash.net.URLRequest;
	
	/**
	 * This is the universal flixel sound object, used for streaming, music, and sound effects.
	 * 
	 * @author	Adam Atomic
	 */
	public class FlxSound extends FlxBasic
	{
		/**
		 * The X position of this sound in world coordinates.
		 * Only really matters if you are doing proximity/panning stuff.
		 */
		public var x:Number;
		/**
		 * The Y position of this sound in world coordinates.
		 * Only really matters if you are doing proximity/panning stuff.
		 */
		public var y:Number;
		/**
		 * Whether or not this sound should be automatically destroyed when you switch states.
		 */
		public var survive:Boolean;
		/**
		 * The ID3 song name.  Defaults to null.  Currently only works for streamed sounds.
		 */
		public var name:String;
		/**
		 * The ID3 artist name.  Defaults to null.  Currently only works for streamed sounds.
		 */
		public var artist:String;
		/**
		 * Stores the average wave amplitude of both stereo channels
		 */
		public var amplitude:Number;
		/**
		 * Just the amplitude of the left stereo channel
		 */
		public var amplitudeLeft:Number;
		/**
		 * Just the amplitude of the left stereo channel
		 */
		public var amplitudeRight:Number;
		/**
		 * Whether to call destroy() when the sound has finished.
		 */
		public var autoDestroy:Boolean;

		/**
		 * Internal tracker for a Flash sound object.
		 */
		protected var _sound:Sound;
		/**
		 * Internal tracker for a Flash sound channel object.
		 */
		protected var _channel:SoundChannel;
		/**
		 * Internal tracker for a Flash sound transform object.
		 */
		protected var _transform:SoundTransform;
		/**
		 * Internal tracker for whether the sound is paused or not (not the same as stopped).
		 */
		protected var _paused:Boolean;
		/**
		 * Internal tracker for the position in runtime of the music playback.
		 */
		protected var _position:Number;
		/**
		 * Internal tracker for how loud the sound is.
		 */
		protected var _volume:Number;
		/**
		 * Internal tracker for total volume adjustment.
		 */
		protected var _volumeAdjust:Number;
		/**
		 * Internal tracker for whether the sound is looping or not.
		 */
		protected var _looped:Boolean;
		/**
		 * Internal tracker for the sound's "target" (for proximity and panning).
		 */
		protected var _target:FlxObject;
		/**
		 * Internal tracker for the maximum effective radius of this sound (for proximity and panning).
		 */
		protected var _radius:Number;
		/**
		 * Internal tracker for whether to pan the sound left and right.  Default is false.
		 */
		protected var _pan:Boolean;
		/**
		 * Internal helper for fading sounds.
		 */
		protected var _fade:FlxTween;
		/**
		 * Internal flag for what to do when the sound is done fading out.
		 */
		protected var _onFadeComplete:Function;
		
		/**
		 * The FlxSound constructor gets all the variables initialized, but NOT ready to play a sound yet.
		 */
		public function FlxSound()
		{
			super();
			reset();
		}
		
		/**
		 * An internal function for clearing all the variables used by sounds.
		 */
		protected function reset():void
		{
			destroy();
			
			x = 0;
			y = 0;
			
			_position = 0;
			_paused = false;
			_volume = 1.0;
			_volumeAdjust = 1.0;
			_looped = false;
			_target = null;
			_radius = 0;
			_pan = false;
			_fade = null;
			_onFadeComplete = null;
			visible = false;
			amplitude = 0;
			amplitudeLeft = 0;
			amplitudeRight = 0;
			autoDestroy = false;
			
			if(_transform == null)
				_transform = new SoundTransform();
			_transform.pan = 0;
		}
		
		/**
		 * Clean up memory.
		 */
		override public function destroy():void
		{
			_transform = null;
			exists = false;
			active = false;
			_target = null;
			name = null;
			artist = null;
			
			if (_channel)
			{
				_channel.removeEventListener(Event.SOUND_COMPLETE,stopped);
				_channel.stop();
				_channel = null;
			}
			
			if (_sound)
			{
				_sound.removeEventListener(Event.ID3, gotID3);
				_sound = null;
			}
			
			super.destroy();
		}
		
		/**
		 * Handles fade out, fade in, panning, proximity, and amplitude operations each frame.
		 */
		override public function update():void
		{
			if(!playing)
				return;
			
			_position = _channel.position;
			
			var radialMultiplier:Number = 1.0;
			var fadeMultiplier:Number = 1.0;
			
			//Distance-based volume control
			if(_target != null)
			{
				radialMultiplier = FlxPoint.distance(new FlxPoint(_target.x,_target.y),new FlxPoint(x,y))/_radius;
				if(radialMultiplier < 0) radialMultiplier = 0;
				if(radialMultiplier > 1) radialMultiplier = 1;
				
				radialMultiplier = 1 - radialMultiplier;
				
				if(_pan)
				{
					var d:Number = (x-_target.x)/_radius;
					if(d < -1) d = -1;
					else if(d > 1) d = 1;
					_transform.pan = d;
				}
			}
			
			//Cross-fading volume control
			if(_fade)
			{
				_fade.progress += FlxG.elapsed;
				fadeMultiplier = _fade.value;
				
				if (_fade.finished)
				{
					_fade = null;
					if (_onFadeComplete != null) { _onFadeComplete.call(); }
				}
			}
			
			_volumeAdjust = radialMultiplier*fadeMultiplier;
			updateTransform();
			
			if(_transform.volume > 0)
			{
				amplitudeLeft = _channel.leftPeak/_transform.volume;
				amplitudeRight = _channel.rightPeak/_transform.volume;
				amplitude = (amplitudeLeft+amplitudeRight)*0.5;
			}
			else
			{
				amplitudeLeft = 0;
				amplitudeRight = 0;
				amplitude = 0;			
			}			
		}
		
		override public function kill():void
		{
			super.kill();
			cleanup(false);
		}
		
		/**
		 * One of two main setup functions for sounds, this function loads a sound from an embedded MP3.
		 * 
		 * @param	EmbeddedSound	An embedded Class object representing an MP3 file.
		 * @param	Looped			Whether or not this sound should loop endlessly.
		 * @param	AutoDestroy		Whether or not this <code>FlxSound</code> instance should be destroyed when the sound finishes playing.  Default value is false, but FlxG.play() and FlxG.stream() will set it to true by default.
		 * 
		 * @return	This <code>FlxSound</code> instance (nice for chaining stuff together, if you're into that).
		 */
		public function loadEmbedded(EmbeddedSound:Class, Looped:Boolean=false, AutoDestroy:Boolean=false):FlxSound
		{
			cleanup(true);
			
			_sound = new EmbeddedSound();
			//NOTE: can't pull ID3 info from embedded sound currently
			_looped = Looped;
			autoDestroy = AutoDestroy;
			updateTransform();
			exists = true;
			return this;
		}
		
		/**
		 * One of two main setup functions for sounds, this function loads a sound from a URL.
		 * 
		 * @param	EmbeddedSound	A string representing the URL of the MP3 file you want to play.
		 * @param	Looped			Whether or not this sound should loop endlessly.
		 * @param	AutoDestroy		Whether or not this <code>FlxSound</code> instance should be destroyed when the sound finishes playing.  Default value is false, but FlxG.play() and FlxG.stream() will set it to true by default.
		 * 
		 * @return	This <code>FlxSound</code> instance (nice for chaining stuff together, if you're into that).
		 */
		public function loadStream(SoundURL:String, Looped:Boolean=false, AutoDestroy:Boolean=false):FlxSound
		{
			cleanup(true);
			
			_sound = new Sound();
			_sound.addEventListener(Event.ID3, gotID3);
			_sound.load(new URLRequest(SoundURL));
			_looped = Looped;
			autoDestroy = AutoDestroy;
			updateTransform();
			exists = true;
			return this;
		}
		
		/**
		 * Call this function if you want this sound's volume to change
		 * based on distance from a particular FlxCore object.
		 * 
		 * @param	X		The X position of the sound.
		 * @param	Y		The Y position of the sound.
		 * @param	TargetObject	The object you want to track.
		 * @param	Radius	The maximum distance this sound can travel.
		 * @param	Pan		Whether the sound should pan in addition to the volume changes (default: true).
		 * 
		 * @return	This FlxSound instance (nice for chaining stuff together, if you're into that).
		 */
		public function proximity(X:Number,Y:Number,TargetObject:FlxObject,Radius:Number,Pan:Boolean=true):FlxSound
		{
			x = X;
			y = Y;
			_target = TargetObject;
			_radius = Radius;
			_pan = Pan;
			return this;
		}
		
		/**
		 * Call this function to play the sound - also works on paused sounds.
		 * 
		 * @param	ForceRestart	Whether to start the sound over or not.  Default value is false, meaning if the sound is already playing or was paused when you call <code>play()</code>, it will continue playing from its current position, NOT start again from the beginning.
		 */
		public function play(ForceRestart:Boolean=false):void
		{
			if(!exists)
				return;
		
			if(ForceRestart)
			{
				cleanup(false, true, true);
			} 
			else if(playing)
			{
				return;
			}
			
			if (_paused)
				resume();
			else
				startSound(0);
		}
		
		/**
		 * Unpause a sound. Only works on sounds that have been paused.
		 */
		public function resume():void
		{
			if (_paused)
				startSound(_position);
		}
		
		/**
		 * Call this function to pause this sound.
		 */
		public function pause():void
		{
			if(!playing)
				return;
			
			_position = _channel.position;
			_paused = true;
			cleanup(false, false, false);
		}
		
		/**
		 * Call this function to stop this sound.
		 */
		public function stop():void
		{
			cleanup(autoDestroy, true, true);
		}
		
		/**
		 * Call this function to make this sound fade out over a certain time interval.
		 * 
		 * @param	Seconds			The amount of time the fade out operation should take.
		 * @param	PauseInstead	Tells the sound to pause on fadeout, instead of stopping.
		 */
		public function fadeOut(Seconds:Number,PauseInstead:Boolean=false):void
		{
			if (!playing)
				{ return; }
			
			var fadeStartVolume:Number = (_fade ? _fade.value : 1);
			_fade = new FlxTween(fadeStartVolume, 0, Seconds);
			_onFadeComplete = (PauseInstead ? pause : stop);
		}
		
		/**
		 * Call this function to make a sound fade in over a certain
		 * time interval (calls <code>play()</code> automatically).
		 * 
		 * @param	Seconds		The amount of time the fade-in operation should take.
		 */
		public function fadeIn(Seconds:Number):void
		{
			if (playing && (!_fade))
				{ return; }
		
			var fadeStartVolume:Number = (_fade ? _fade.value : 0);
			_fade = new FlxTween(fadeStartVolume, 1, Seconds);
			_onFadeComplete = null;
			
			play();
		}
		
		/**
		 * Whether or not the sound is currently playing.
		 */
		public function get playing():Boolean
		{
			return (_channel != null);
		}
		
		/**
		 * Set <code>volume</code> to a value between 0 and 1 to change how this sound is.
		 */
		public function get volume():Number
		{
			return _volume;
		}
		
		/**
		 * @private
		 */
		public function set volume(Volume:Number):void
		{
			_volume = Volume;
			if(_volume < 0)
				_volume = 0;
			else if(_volume > 1)
				_volume = 1;
			updateTransform();
		}
		
		/**
		 * Returns the currently selected "real" volume of the sound (takes fades and proximity into account).
		 * 
		 * @return	The adjusted volume of the sound.
		 */
		public function getActualVolume():Number
		{
			return _volume*_volumeAdjust;
		}
		
		/**
		 * Call after adjusting the volume to update the sound channel's settings.
		 */
		internal function updateTransform():void
		{
			_transform.volume = (FlxG.mute?0:1)*FlxG.volume*_volume*_volumeAdjust;
			if(_channel != null)
				_channel.soundTransform = _transform;
		}
		
		/**
		 * An internal helper function used to attempt to start playing the sound and populate the <code>_channel</code> variable.
		 */
		protected function startSound(Position:Number):void
		{
			// See https://github.com/FlixelCommunity/flixel/issues/120
			var numLoops:int = (_looped && (Position == 0)) ? 9999 : 0;
			
			_position = Position;
			_paused = false;
			_channel = _sound.play(_position, numLoops, _transform);
			if(_channel != null)
			{
				_channel.addEventListener(Event.SOUND_COMPLETE, stopped);
				active = true;
			}
			else
			{
				exists = false;
				active = false;
			}
		}
		
		/**
		 * An internal helper function used to help Flash clean up finished sounds or restart looped sounds.
		 * 
		 * @param	event		An <code>Event</code> object.
		 */
		protected function stopped(event:Event=null):void
		{
			if (_looped)
			{
				cleanup(false);
				play();	
			}
			else
			{
				cleanup(autoDestroy);
			}
		}
		
		/**
		 * An internal helper function used to help Flash clean up (and potentially re-use) finished sounds. Will stop the current sound and destroy the associated <code>SoundChannel</code>, plus, any other commands ordered by the passed in parameters.
		 * 
		 * @param	destroySound		Whether or not to destroy the sound. If this is true, the position and fading will be reset as well.
		 * @param	resetPosition		Whether or not to reset the position of the sound.
		 * @param	resetFading		Whether or not to reset the current fading variables of the sound.
		 */
		protected function cleanup(destroySound:Boolean, resetPosition:Boolean = true, resetFading:Boolean = true):void
		{
			if (destroySound)
			{
				reset();
				return;
			}
		
			if (_channel)
			{
				_channel.removeEventListener(Event.SOUND_COMPLETE,stopped);
				_channel.stop();
				_channel = null;
			}
			
			active = false;
			
			if (resetPosition)
			{
				_position = 0;
				_paused = false;
			}
			
			if (resetFading)
			{
				_fade = null;
				_onFadeComplete = null;
			}
		}
		
		/**
		 * Internal event handler for ID3 info (i.e. fetching the song name).
		 * 
		 * @param	event	An <code>Event</code> object.
		 */
		protected function gotID3(event:Event=null):void
		{
			FlxG.log("got ID3 info!");
			name = _sound.id3.songName;
			artist = _sound.id3.artist;
			_sound.removeEventListener(Event.ID3, gotID3);
		}
	}
}