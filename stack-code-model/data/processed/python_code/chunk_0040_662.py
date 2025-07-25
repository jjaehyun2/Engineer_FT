﻿package com.createjs.soundjs {

	import flash.display.Sprite;
	import flash.external.ExternalInterface;
	import flash.events.Event;
	import flash.media.Sound;
	import flash.net.URLRequest;
	import flash.events.ProgressEvent;
	import flash.events.IOErrorEvent;
	import flash.events.ErrorEvent;
	import flash.utils.Dictionary;
	import flash.utils.Timer;
	import flash.events.TimerEvent;
	import flash.system.Security;

	public class FlashAudioPlugin extends Sprite {

	// Constants:
		/** The maximum concurrent sounds that can play */
		public static const MAX_INSTANCES:uint = 255;

		/** Generic ExternalInterface callback string to Flash. */
		public static const FLASH_CALLBACK:String = "createjs.Sound.activePlugin.handleEvent";
		/** Generic ExternalInterface error callback string to Flash. */
		public static const ERROR_CALLBACK:String = "createjs.Sound.activePlugin.handleErrorEvent";
		/** Generic ExternalInterface preload callback string to Flash. */
		public static const PRELOAD_CALLBACK:String = "createjs.Sound.activePlugin.handlePreloadEvent";
		/** Generic ExternalInterface sound instance callback string to Flash. */
		public static const SOUND_CALLBACK:String = "createjs.Sound.activePlugin.handleSoundEvent";
		/** Output method */
		public static const LOG_CALLBACK:String = "createjs.Sound.activePlugin.flashLog";


	// Public Properties:
		/** The list instance to log errors to. Will be removed for production. */
		public var list:*;

	// Protected Properties:
		protected var lookup:Object;
		protected var preloadLookup:Dictionary;
		protected var preloadHash:Object;
		protected var nextId:int = 0;
		protected var playbackTimer:Timer = new Timer(50);
		public var masterVolume:Number = 1;
		public var soundDurationHash:Object;
		public var soundHash:Object;

	// UI Elements:
	// ** AUTO-UI ELEMENTS **
	// ** END AUTO-UI ELEMENTS **

	// Initialization:
		public function FlashAudioPlugin() {
			Security.allowDomain("*");
			configUI();
			initializeInterface();
		}

		protected function configUI():void {
			lookup = {};
			preloadHash = {};
			soundDurationHash = {};
			soundHash = {};
			preloadLookup = new Dictionary();
		}

	// Protected Methods:
		/**
		 * Add callbacks for ExternalInterface communication
		 */
		protected function initializeInterface():void {
			var map:Object = {

				preload: handlePreload,
				cancelPreload: handleCancelPreload,

				playSound: handlePlaySound,
				stopAll: handleStopAll,
				stopSound: handleStopSound,
				interrupt: handleSoundInterrupt,
				pauseSound: handlePauseSound,
				resumeSound: handleResumeSound,
				muteSound: handleMuteSound,
				unmuteSound: handleUnmuteSound,

				setVolume: handleSetVolume,
				getVolume: handleGetVolume,
				setPan: handleSetPan,
				getPan: handleGetPan,
				setPosition: handleSetPosition,
				getPosition: handleGetPosition,
				getDuration: handleGetDuration,
				getDurationBySrc: handleGetDurationBySrc,
				setLoop: handleSetLoop,

				setMasterVolume: handleSetMasterVolume,

				command: handleCommand
			};

			if (!ExternalInterface.available) {
				handleError({message:"ExternalInterface is not available"});
				return;
			}

			// Usually happens when running locally, or cross-scripting
			try {
				for (var n:String in map) {
					ExternalInterface.addCallback(n, map[n]);
				}
				// NOTE this is in an ENTER_FRAME to deal with a race issue in IE caused by caching
				this.addEventListener(Event.ENTER_FRAME, handleReady, false, 0, true);
			} catch (e:*) {
				handleError(e);
			}
		}

		// call to let JS know we are ready
		protected function handleReady(evt) {
			this.removeEventListener(Event.ENTER_FRAME, handleReady);
			ExternalInterface.call(FLASH_CALLBACK, "ready");

			// using a timer to handle audio sprites playing expected duration
			playbackTimer.start();
			playbackTimer.addEventListener(TimerEvent.TIMER, timerHandler);
		}

		// General error handler.
		protected function handleError(e:Object):void {
			log("*** Error:", e.message);
		}

		// For now, spit out messages to a list.
		public function log(...args:Array):void {
			var str = args.join(" ");
			ExternalInterface.call(LOG_CALLBACK, str);
			if (list == null) { return; }
			list.addItem({label:str});
			list.verticalScrollPosition = list.maxVerticalScrollPosition;
		}


	/******** PRELOAD ********/
		protected function handlePreload(src:String):String {
			var id:String = "p"+nextId++;
			var sound:Sound = new Sound();
			sound.addEventListener(ProgressEvent.PROGRESS, handleLoadProgress, false, 0, true);
			sound.addEventListener(Event.COMPLETE, handleLoadComplete, false, 0, true);
			sound.addEventListener(IOErrorEvent.IO_ERROR, handleLoadError, false, 0, true);
			//TODO: Other Errors
			preloadLookup[sound] = id;
			preloadHash[id] = sound;
			soundDurationHash[id] = src;

			sound.load(new URLRequest(src));
			return id;
		}

		protected function handleCancelPreload(id:String):Boolean {
			var sound:Sound = preloadHash[id] as Sound;
			if (sound == null) { return false; }
			try {
				sound.close();
			} catch(error:Error) {}
			delete preloadLookup[sound];
			delete preloadHash[id];
			delete soundDurationHash[id];
			return true;
		}

		protected function handleLoadProgress(event:ProgressEvent):void {
			var id = preloadLookup[event.target];
			ExternalInterface.call(PRELOAD_CALLBACK, id, "handleProgress", event.bytesLoaded, event.bytesTotal);
		}

		protected function handleLoadComplete(event:Event):void {
			var id = preloadLookup[event.target];
			delete preloadLookup[event.target];
			var src = soundDurationHash[id];
			var sound = preloadHash[id];
			sound.removeEventListener(ProgressEvent.PROGRESS, handleLoadProgress, false);
			sound.removeEventListener(Event.COMPLETE, handleLoadComplete, false);
			sound.removeEventListener(IOErrorEvent.IO_ERROR, handleLoadError, false);
			soundHash[src] = sound;
			delete preloadHash[id];
			soundDurationHash[src] = event.target.length;
			delete soundDurationHash[id];
			ExternalInterface.call(PRELOAD_CALLBACK, id, "handleComplete");
			log("Preload Complete", id);
		}

		protected function handleLoadError(event:ErrorEvent):void {
			var id = preloadLookup[event.target];
			ExternalInterface.call(PRELOAD_CALLBACK, id, "handleError", event.text);
			delete preloadLookup[event.target];
			delete preloadHash[id];
			delete soundDurationHash[id];
			log("Error Loading", id, event.text);
		}

		protected function getWrapper(id:String, alwaysReturn:Boolean=false):SoundWrapper {
			var wrapper = lookup[id] as SoundWrapper;
			if (wrapper == null) { return null; }
			if (!alwaysReturn && wrapper.failed) { return null; }
			return wrapper;
		}

	/******** PLAYBACK ********/
		protected function handlePlaySound(src:String, offset:Number=0, loop:int=0, volume:Number=1, pan:Number=0, startTime:Number=0, duration:Number=0):String {
			var id:String = "s" + nextId++;

			var wrapper:SoundWrapper = new SoundWrapper(id, src, startTime, duration, this);
			wrapper.play(offset, loop, volume, pan);

			lookup[id] = wrapper;
			wrapper.addEventListener(Event.SOUND_COMPLETE, handleSoundFinished, false, 0, true);
			wrapper.addEventListener("loop", handleSoundLoop, false, 0, true);
			wrapper.addEventListener("interrupt", handleSoundInterrupt, false, 0, true);
			log("Play Sound", id, src, "o:",offset, "l:",loop, "v:",volume, "p:",pan, "sT:",startTime, "d:",duration, "mv:",masterVolume);
			return id;
		}

		// An instance completed playback.
		protected function handleSoundFinished(event:Event):void {
			var wrapper:SoundWrapper = event.target as SoundWrapper;
			delete(lookup[wrapper.id]);
			wrapper.destroy();
			ExternalInterface.call(SOUND_CALLBACK, wrapper.id, "handleSoundFinished");
			log("Complete", wrapper.id, "Remaining:", activeSoundCount);
		}

		// An instance loop callback.
		protected function handleSoundLoop(event:Event):void {
			var wrapper:SoundWrapper = event.target as SoundWrapper;
			ExternalInterface.call(SOUND_CALLBACK, wrapper.id, "handleSoundLoop");
			log("Loop", wrapper.id, "Remaining:", wrapper.loop);
		}

		protected function handleSoundInterrupt(id:String):void {
			var wrapper:SoundWrapper = getWrapper(id, true);
			if (wrapper != null) {
				log("Interrupted", wrapper.id);
				wrapper.interrupt();
				delete(lookup[wrapper.id]);
			}
		}

		// Stop all instances
		protected function handleStopAll():Boolean {
			log("Stop All");
			var list:Array = [];
			for (var n:String in lookup) { list.push(lookup[n]); }
			for (var i:uint=0, l:uint=list.length; i<l; i++) {
				var wrapper:SoundWrapper = list[i] as SoundWrapper;
				wrapper.stop();
			}
			return true;
		}

		// Stop a specific instance
		protected function handleStopSound(id:String):Boolean {
			var wrapper:SoundWrapper = getWrapper(id, true);
			if (wrapper == null) { return false; }
			log("Stop",wrapper.id);
			wrapper.stop();
			delete(lookup[wrapper.id]);
			wrapper.destroy();
			return true;
		}

		// Pause an instance
		protected function handlePauseSound(id:String):Boolean {
			var wrapper:SoundWrapper = getWrapper(id, true);
			if (wrapper == null) { return false; }
			log("Pause",wrapper.id);
			wrapper.pause();
			return true;
		}

		// Resume a paused instance
		protected function handleResumeSound(id:String):Boolean {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return false; }
			log("Resume",wrapper.id,wrapper.offset);
			wrapper.resume();
			return true;
		}

		// Mute an instance
		protected function handleMuteSound(id:String):Boolean {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return false; }
			log("Mute",wrapper.id);
			wrapper.mute(true);
			return true;
		}

		// Unmute an instance
		protected function handleUnmuteSound(id:String):Boolean {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return false; }
			log("Unmute",wrapper.id);
			wrapper.mute(false);
			return true;
		}

		// Get the master volume
		protected function handleGetMasterVolume():Number { return masterVolume; }

		// Set the master volume
		protected function handleSetMasterVolume(value:Number):Boolean {
			log("Set Master Volume", value);
			masterVolume = value;
			for (var n:String in lookup) {
				var wrapper:SoundWrapper = lookup[n] as SoundWrapper;
				wrapper.volume = wrapper.volume; // this forces the wrapper to call the updateVolume function, which applies the owner.masterVolume
			}
			return true;
		}

		// Set the volume of an instance
		protected function handleSetVolume(id:String, value:Number):Boolean {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return false; }
			log("SetVolume", wrapper.id, value);
			wrapper.volume = value;
			return true;
		}

		// Get the volume of an instance
		protected function handleGetVolume(id:String):Number {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return -1; }
			return wrapper.volume;
		}

		// Set the pan of an instance
		protected function handleSetPan(id:String, value:Number):Boolean {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return false; }
			log("SetPan", wrapper.id, value);
			wrapper.pan = value;
			return true;
		}

		// Get the pan of an instance
		protected function handleGetPan(id:String):Number {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return -1; }
			return wrapper.pan;
		}

		// Set the loop of an instance
		protected function handleSetLoop(id:String, value:Number):Boolean {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return false; }
			log("SetLoop", wrapper.id, value);
			wrapper.loop = value;
			return true;
		}

		// Set the playhead position of an instance
		protected function handleSetPosition(id:String, value:Number):Boolean {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return false; }
			log("SetPosition", wrapper.id, value);
			wrapper.position = value;
			return true;
		}

		// Get the playhead position of an instance
		protected function handleGetPosition(id:String):Number {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return -1; }
			return wrapper.position;
		}

		// Get the duration of an instance
		protected function handleGetDuration(id:String):Number {
			var wrapper:SoundWrapper = getWrapper(id);
			if (wrapper == null) { return -1; }
			return wrapper.duration || soundDurationHash[wrapper.src];
		}

		// Get the duration of a src, returns -1 if it does not exist
		protected function handleGetDurationBySrc(src:String):Number {
			return soundDurationHash[src] || -1;
		}

		// Call a command on an instance (currently N/A)
		protected function handleCommand(id:String, command:String, value:*):Boolean {
			log("Command", command, value);
			return false;
		}

		// Get the number of active sounds.
		protected function get activeSoundCount():uint {
			var count:uint = 0;
			var max:uint = 500;
			for (var n:String in lookup) {
				count++;
				if (count > max) { break; }
			}
			return count;
		}

		protected function timerHandler(event:Event):void {
			var list:Array = [];
			for (var n:String in lookup) { list.push(lookup[n]); }
			for (var i:uint=list.length; i--;) {
				var wrapper:SoundWrapper = list[i] as SoundWrapper;
				wrapper.handleAudioSprite();
			}

		}

		override public function toString():String { return "[FlashAudioPlugin]"; }

	}

}

import flash.media.Sound;
import flash.media.SoundChannel;
import flash.events.Event;
import flash.net.URLRequest;
import flash.utils.Timer;
import flash.events.TimerEvent;
import flash.events.EventDispatcher;
import flash.media.SoundTransform;
import flash.events.IOErrorEvent;
import flash.events.ErrorEvent;

import com.createjs.soundjs.FlashAudioPlugin;
import flash.events.SecurityErrorEvent;

/**
 * The SoundWrapper controls a single sound instance. Instances can be played, and then modified during playback.
 * Once an instance completes, it is cleaned up. Any attempt by JavaScript to replay the same instance, will result
 * in a new instance being created.
 */
class SoundWrapper extends EventDispatcher {

	/** The unique ID of an instance */
	public var id:String;
	/** The path the audio source */
	public var src:String;
	/** How far into the sound to start playback (milliseconds) */
	public var offset:Number = 0;
	/** Audio sprite start point */
	public var _startTime:Number = 0;
	/** Audio sprite length of clip */
	public var _duration:Number = 0;
	/** How many loops to play */
	public var loop:int = 0;
	/** A reference to the Plugin owner */
	public var owner:FlashAudioPlugin;

	/** Whether the audio is currently muted */
	public var muted:Boolean = false;
	/** If the sound failed. */
	public var failed:Boolean = false;

	protected var sound:Sound;
	protected var channel:SoundChannel;  // NOTE you can have a maximum of 32 sound channels at once
	protected var timer:Timer;
	protected var _volume:Number = 1;
	protected var _pan:Number = 0;
	protected var _paused:Boolean = false;

	/**
	 * SoundInstances are alive as long as they are playing.
	 * When they complete, or are stopped, they will be released for cleanup
	 * If a sound is re-played, a new instance is created. There is no need to
	 * keep them around once they are stopped, since the reference to the sound is
	 * maintained in JS.
	 *
	 * @param id The unique ID of the instance
	 * @param owner The owner of this sound instance
	 */
	public function SoundWrapper(id:String, src:String, startTime:Number, duration:Number, owner:FlashAudioPlugin) {
		this.id = id;
		this.src = src;
		this._startTime = startTime;
		this._duration = duration;
		this.owner = owner;
		
		if(owner.soundHash[src])
		{
			sound = owner.soundHash[src];
		}
		else
		{
			sound = new Sound();
			sound.addEventListener(IOErrorEvent.IO_ERROR, handleSoundError, false, 0, true);
			sound.addEventListener(SecurityErrorEvent.SECURITY_ERROR, handleSoundError, false, 0, true);
			sound.addEventListener(Event.COMPLETE, handleSoundLoaded, false, 0, true);
		}
	}

	/**
	 * Play the sound.
	 * @param src The path the the asset source
	 * @param offset How far in to the sound to begin playback
	 * @param loop How many times to loop the audio
	 * @param volume The starting volume of the audio
	 * @param pan The starting pan of the audio
	 */
	public function play(offset:Number, loop:int, volume:Number, pan:Number) {
		this.offset = offset;
		this.loop = loop;
		this._volume = volume;
		this._pan = pan;
		if(sound.bytesTotal > 0 && sound.bytesTotal == sound.bytesLoaded)
		{
			startSound(offset);
		}
		else
		{
			sound.load(new URLRequest(src));
		}
	}

	/**
	 * Clean up a sound instance.
	 */
	public function destroy():void {
		sound = null;
		channel = null;
	}

	/**
	 * Interrupt this instance
	 */
	public function interrupt():void {
		if (channel != null) {
			channel.stop();
		}
		destroy();
	}

	/**
	 * Determine if the audio is currently paused. It is always unpaused when started, even while delaying.
	 */
	public function get paused():Boolean {
		return _paused;
	}

	/**
	 * Pause sound playback.
	 */
	public function pause():void {
		_paused = true;
		if (channel != null) {
			offset = channel.position - _startTime;
			channel.stop();
		}
	}

	/**
	 * Resume sound playback.
	 */
	public function resume():void {
		_paused = false;
		startSound(offset, true);
	}

	/**
	 * Stop sound playback.
	 */
	public function stop():void {
		if (channel != null) {
			channel.stop();
		}
		offset = 0;
		destroy();
	}

	/**
	 * Mute playback.
	 * @param value if the audio should be muted or not.
	 */
	public function mute(value:Boolean):void {
		muted = value;
		updateVolume();
	}

	/** Get/Set the volume of the sound. */
	public function get volume():Number { return _volume; }
	/** @private */
	public function set volume(value:Number):void {
		_volume = value;
		updateVolume();
	}

	/** Get/Set the pan of the sound. */
	public function get pan():Number { return _pan; }
	/** @private */
	public function set pan(value:Number):void {
		_pan = value;
		updateVolume();
	}

	/** Get/Set the playhead position. */
	public function get position():Number {
		if (channel != null && !_paused) {
			return channel.position - this._startTime;
		}
		return offset;
	}

	/** @private */
	public function set position(value:Number):void {
		if (channel != null) {
			channel.stop();
		}
		startSound(value);
	}

	/** Get the duration of the sound. */
	public function get duration():Number {
		return this._duration || sound.length;
	}

	// Begin playing the sound at a certain position.
	protected function startSound(startAt:Number, isResuming:Boolean = false):void {
		startAt += this._startTime;
		if (startAt > sound.length) {
			owner.log("Can not play, out of range");
			dispatchEvent(new Event(Event.SOUND_COMPLETE));
			return;
		}
		if (!_paused) {
			//fixed resuming of looping audio, also made audio loop gaplessly if it will loop
			//infinitely anyway
			channel = sound.play(startAt, (loop == -1 && !isResuming) ? int.MAX_VALUE : 0);
			//fixed null ref errors from invalid audio or a lack of sound channels
			if(channel)
				channel.addEventListener(Event.SOUND_COMPLETE, handleSoundComplete, false, 0, true);
			else
			{
				owner.log("Error - could not play sound: " + id);
				dispatchEvent(new Event(Event.SOUND_COMPLETE));
			}
		} else {
			offset = startAt - this._startTime;  // allows you to set position on a paused or stopped sound
		}
		updateVolume();
	}

	// Update the sound volume based on the volume, masterVolume, and mute settings.
	protected function updateVolume():void {
		if (channel == null) { return; }
		var transform:SoundTransform = channel.soundTransform;
		transform.volume = muted ? 0 : owner.masterVolume * _volume;
		transform.pan = _pan;
		channel.soundTransform = transform;
	}

	// Sound has completed loading
	protected function handleSoundLoaded(event:Event):void {
		if (_paused) { return; }
		startSound(offset);
	}

	public function handleAudioSprite():void {
		if (this._duration > 0 && channel != null && (channel.position - this._startTime) >= this._duration) {
			channel.stop();
			channel = null;
			this.handleSoundComplete(new Event(Event.SOUND_COMPLETE));
		}
	}

	// Sound playback has completed.
	protected function handleSoundComplete(event:Event):void {
		offset = 0;  // have to set this as it can be set by pause during playback
		if (loop != 0) {
			//only decrement loop if it is not -1
			if(loop > 0) loop--;  // NOTE this introduces a theoretical limit on loops = float max size x 2 - 1

			startSound(offset);

			dispatchEvent(new Event("loop"));
		} else {
			dispatchEvent(event);
		}
	}

	// An error has occurred.
	protected function handleSoundError(event:ErrorEvent):void {
		owner.log("Error!", event.text);
		failed = true;
		dispatchEvent(new Event("playbackFailed"));
	}

}