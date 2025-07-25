package com.digitalstrawberry.nativeExtensions.anesounds
{
	import flash.errors.IllegalOperationError;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.ProgressEvent;
	import flash.events.StatusEvent;
	import flash.external.ExtensionContext;
	import flash.filesystem.File;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.media.SoundTransform;
	import flash.net.URLRequest;
	import flash.system.Capabilities;
	import flash.utils.Dictionary;

	public class ANESounds extends EventDispatcher
	{
		public static const VERSION:String = "1.11";
		private static var _instance:ANESounds;
		private static var sMaxStreams:int = 10;
		private static var sStreamId:int = 0;

		private var _extContext:ExtensionContext;

		// Sounds array used for Flash fallback
		private var _soundId:int;
		private var _sounds:Vector.<SoundInfo> = new <SoundInfo>[];
		private var _streams:Vector.<StreamInfo> = new <StreamInfo>[];

		// Sound id mapped to a list of stream ids
		private var _soundStreams:Dictionary = new Dictionary();

		// Stream id mapped to a SoundChannel
		private var _activeStreams:Dictionary = new Dictionary();

		// Stream id mapped to a sound position (for resuming sounds)
		private var _streamPositions:Dictionary = new Dictionary();

		public function ANESounds()
		{
			if(!_instance)
			{
				_instance = this;
			}
			else
			{
				throw new Error('Class is a singleton, use ANESounds.instance instead');
			}

			if(isSupportedNatively())
			{
				_extContext = ExtensionContext.createExtensionContext('com.digitalstrawberry.nativeExtensions.ANESounds', null);
				if(_extContext == null)
				{
					throw new Error('Extension context could not be created!');
				}

				_extContext.addEventListener(StatusEvent.STATUS, onStatus);
				_extContext.call('initialize', sMaxStreams);
			}
		}


		public static function setMaxStreams(value:int):void
		{
			if(value <= 0)
			{
				throw new ArgumentError("The number of streams must be greater than zero.")
			}
			if(_instance != null)
			{
				throw new IllegalOperationError("Maximum streams must be set before calling any other API.");
			}
			sMaxStreams = value;
		}


		public function loadSound(file:File):int
		{
			if(!file.exists)
			{
				throw new Error('Sound file ' + file.url + ' does not exist');
			}

			// Fallback to Flash
			if(_extContext == null)
			{
				var sound:Sound = new Sound();
				sound.addEventListener(ProgressEvent.PROGRESS, onSoundLoadProgress, false, 0, true);
				sound.load(new URLRequest(file.url));

				_sounds.push(new SoundInfo(_soundId, sound));
				return _soundId++;
			}
			// Load the file natively
			else
			{
				var returnObject:Object = _extContext.call('loadSound', getNativePath(file));
				if(returnObject == null)
				{
					return -1;
				}

				return int(returnObject);
			}
		}


		private function onSoundLoadProgress(event:ProgressEvent):void
		{
			var perc:Number = event.bytesLoaded / event.bytesTotal;
			if(perc >= 1.0)
			{
				var sound:Sound = event.currentTarget as Sound;
				sound.removeEventListener(ProgressEvent.PROGRESS, onSoundLoadProgress);

				var soundId:int = -1;
				for each(var soundInfo:SoundInfo in _sounds)
				{
					if(soundInfo.sound == sound)
					{
						soundId = soundInfo.id;
						break;
					}
				}

				if(soundId >= 0)
				{
					dispatchEvent(new SoundEvent(SoundEvent.LOAD, soundId));
				}
			}
		}


		private function getNativePath(file:File):String
		{
			// Files located in the Application directory need to be moved so they can be properly read by the ANE.
			// This is due to a bug in AIR that compresses embedded media assets in the Android package, even though
			// the Android documentation states that these assets should not be compressed.
			if(file.nativePath == "")
			{
				var newFilename:String = file.url;
				newFilename = newFilename.replace(/\//g, "_");
				newFilename = newFilename.replace(/:/g, "");

				var newFile:File = File.applicationStorageDirectory.resolvePath(newFilename);

				file.copyTo(newFile, true);
				return newFile.nativePath;
			}

			return file.nativePath;
		}


		public function playSound(soundId:int, leftVolume:Number = 1.0, rightVolume:Number = 1.0, loop:int = 0, playbackRate:Number = 1.0):int
		{
			if(_extContext == null)
			{
				for each(var soundInfo:SoundInfo in _sounds)
				{
					if(soundInfo.id == soundId)
					{
						var sound:Sound = soundInfo.sound;

						var totalVolume:Number = leftVolume + rightVolume;
						var volume:Number = totalVolume / 2;
						var pan:Number = (rightVolume / totalVolume) - (leftVolume / totalVolume);
						var soundTransform:SoundTransform = new SoundTransform(volume, pan);

						// Generate new stream for this sound
						var channel:SoundChannel = sound.play(0, loop, soundTransform);

						// Channel may not be created if playing too many sounds already
						if(channel == null)
						{
							return 0;
						}

						sStreamId++;
						channel.addEventListener(Event.SOUND_COMPLETE, onSoundChannelCompleted);
						setStream(sStreamId, channel);
						soundInfo.addStream(sStreamId);

						// Store the stream info to be able to pause/resume
						var streamInfo:StreamInfo = new StreamInfo(sStreamId, sound, soundTransform, loop);
						_streams[_streams.length] = streamInfo;

						// Store stream id for this sound
						var activeStreams:Array = _soundStreams[soundId];
						if(activeStreams == null)
						{
							activeStreams = [];
						}
						activeStreams[activeStreams.length] = sStreamId;
						_soundStreams[soundId] = activeStreams;

						return sStreamId;
					}
				}
				trace('[ANESounds] Sound with id', soundId, 'not found.');
				return 0;
			}

			return _extContext.call('playSound', soundId, leftVolume, rightVolume, loop, playbackRate) as int;
		}


		public function unloadSound(soundId:int):Boolean
		{
			if(_extContext == null)
			{
				var soundInfo:SoundInfo = getSoundInfo(soundId);
				if(soundInfo != null)
				{
					// Stop all streams for this sound
					for each(var streamId:int in soundInfo.streams)
					{
						if(hasStream(streamId))
						{
							trace("[ANESounds] Stopping", streamId, "for sound", soundId);
							stopStream(streamId);
						}
					}

					try
					{
						soundInfo.sound.close()
					}
					catch (error:Error) {}
					_sounds.removeAt(_sounds.indexOf(soundInfo));
				}
				return soundInfo != null;
			}
			else
			{
				return _extContext.call('unloadSound', soundId) as Boolean;
			}
		}


		public function stopAllStreams():void
		{
			if(_extContext == null)
			{
				for(var streamId:String in _activeStreams)
				{
					stopStream(int(streamId));
				}
			}
			else
			{
				_extContext.call('stopAllStreams');
			}
		}


		public function stopStreamsForSound(soundId:int):void
		{
			if(_extContext == null)
			{
				var streams:Array = _soundStreams[soundId];
				if(streams != null)
				{
					for each(var streamId:int in streams)
					{
						stopStream(streamId);
					}
				}
			}
			else
			{
				_extContext.call('stopStreamsForSound', soundId);
			}
		}


		public function stopStream(streamId:int):void
		{
			if(_extContext == null)
			{
				if(hasStream(streamId))
				{
					getStream(streamId).stop();
					deleteStream(streamId);
				}
			}
			else
			{
				_extContext.call('stopStream', streamId);
			}
		}


		public function pauseStream(streamId:int):void
		{
			if(_extContext == null)
			{
				if(hasStream(streamId))
				{
					// This channel will not be used anymore but keep it around in case the "stop" method is called
					var channel:SoundChannel = getStream(streamId);
					_streamPositions[streamId] = channel.position;
					channel.stop();
					channel.removeEventListener(Event.SOUND_COMPLETE, onSoundChannelCompleted);
				}
			}
			else
			{
				_extContext.call('pauseStream', streamId);
			}
		}


		public function resumeStream(streamId:int):void
		{
			if(_extContext == null)
			{
				if(hasStream(streamId) && streamId in _streamPositions)
				{
					var position:Number = _streamPositions[streamId];
					for each(var stream:StreamInfo in _streams)
					{
						var channel:SoundChannel = stream.sound.play(position, stream.loop, stream.transform);
						channel.addEventListener(Event.SOUND_COMPLETE, onSoundChannelCompleted);
						setStream(sStreamId, channel);
					}
				}
			}
			else
			{
				_extContext.call('resumeStream', streamId);
			}
		}
		
		
		public function setVolume(streamId:int, leftVolume:Number = 1, rightVolume:Number = 1):void
		{
			if(_extContext == null)
			{
				if(hasStream(streamId))
				{
					var totalVolume:Number = leftVolume + rightVolume;
					var volume:Number = totalVolume / 2;
					var pan:Number = (rightVolume / totalVolume) - (leftVolume / totalVolume);
					getStream(streamId).soundTransform = new SoundTransform(volume, pan);
				}
			}
			else
			{
				_extContext.call('setVolume', streamId, clampVolume(leftVolume), clampVolume(rightVolume));
			}
		}


		private function onStatus(event:StatusEvent):void
		{
			if(event.code == SoundEvent.LOAD)
			{
				var soundId:int = int(event.level);
				if(soundId >= 0)
				{
					dispatchEvent(new SoundEvent(SoundEvent.LOAD, soundId));
				}
			}
		}


		private function onSoundChannelCompleted(event:Event):void
		{
			var channel:SoundChannel = SoundChannel(event.currentTarget);
			for(var streamId:String in _activeStreams)
			{
				if(channel == _activeStreams[streamId])
				{
					deleteStream(int(streamId));
					return;
				}
			}
		}


		private function hasStream(id:int):Boolean
		{
			var idString:String = String(id);
			return _activeStreams[idString] != null;
		}


		private function getStream(id:int):SoundChannel
		{
			var idString:String = String(id);
			return _activeStreams[idString] as SoundChannel;
		}


		private function setStream(id:int, channel:SoundChannel):void
		{
			var idString:String = String(id);
			_activeStreams[idString] = channel;
		}


		private function deleteStream(streamId:int):void
		{
			var channel:SoundChannel = getStream(streamId);
			channel.removeEventListener(Event.SOUND_COMPLETE, onSoundChannelCompleted);

			var length:int = _streams.length;
			for(var i:int = 0; i < length; ++i)
			{
				var stream:StreamInfo = _streams[i];
				if(stream.id == streamId)
				{
					_streams.removeAt(i);
					break;
				}
			}

			delete _activeStreams[streamId];
			delete _streamPositions[streamId];
		}
		
		
		private function clampVolume(volume:Number):Number
		{
			if(volume > 1)
			{
				return 1;
			}
			if(volume < 0)
			{
				return 0;
			}
			return volume;
		}


		private function getSoundInfo(soundId:int):SoundInfo
		{
			for each(var soundInfo:SoundInfo in _sounds)
			{
			    if(soundInfo.id == soundId)
			    {
				    return soundInfo;
			    }
			}
			return null;
		}


		private static function get _android():Boolean
		{
			return Capabilities.manufacturer.indexOf("Android") > -1;
		}


		public static function isSupported():Boolean
		{
			return true;
		}


		public static function isSupportedNatively():Boolean
		{
			return _android;
		}


		public static function get instance():ANESounds
		{
			return _instance ? _instance : new ANESounds();
		}

	}
}