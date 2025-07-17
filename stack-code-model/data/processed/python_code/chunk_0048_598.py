/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/

package org.rapo.games.astro {
	
	import flash.display.Sprite;
	import flash.display.MovieClip;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.media.SoundTransform;
	import flash.events.*;
	import flash.net.URLRequest;
	
	import org.rapo.games.astro.managers.GameDepthManager;
	import org.rapo.games.astro.sounds.sndBase;
	
	public class AudioController extends Sprite {
	
		public var soundClip:MovieClip;
		public var soundList:Object;
		public var soundChannelList:Object;
		public var soundClipContainer:Object;
		
		public function AudioController() {
			
			soundList = new Object();
			soundChannelList = new Object();
		}
		
		public function registerSound(sound_id:String, sound:sndBase):void {
			
			soundList[sound_id] = sound;
		}
		
		public function loadSound(	sound_id:String, sound_url:String,
									is_streaming:Boolean,
									play_when_loaded:Boolean):sndBase {
	
			
			var request:URLRequest = new URLRequest(sound_url);
			var thisSound:sndBase = new sndBase();

            thisSound.addEventListener(Event.COMPLETE, soundCompleteHandler);
            thisSound.addEventListener(Event.ID3, id3Handler);
            thisSound.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
            thisSound.addEventListener(ProgressEvent.PROGRESS, progressHandler);
            thisSound.load(request);

			soundList[sound_id] = thisSound;
			
			/*
			thisSound.onLoad = function() {
			
				var tempSound:GameSound = GameSound(this);
				tempSound.stop();
				tempSound.AC.onSoundLoaded(tempSound.soundID);
			}
			
			thisSound.onID3 = function() {
				
				var tempSound:GameSound = GameSound(this);
				tempSound.AC.onID3Detected(this.soundID);
			}
			*/
					
			return thisSound;
		}
		

        private function soundCompleteHandler(event:Event):void {
            trace("soundCompleteHandler: " + event);
        }

        private function id3Handler(event:Event):void {
            trace("id3Handler: " + event);
        }

        private function ioErrorHandler(event:Event):void {
            trace("ioErrorHandler: " + event);
        }

        private function progressHandler(event:ProgressEvent):void {
            //trace("progressHandler: " + event);
        }

		
		public function onSoundLoaded(sound_id:String):void {
			
			var thisSound:sndBase = sndBase(soundList[sound_id]);
			
			//if (thisSound.playWhenLoaded) thisSound.start();
		}
		
		public function onID3Detected(sound_id:String):void {
			
			var thisSound:sndBase = sndBase(soundList[sound_id]);
			
			trace("onID3Detected: soundID: "  + sound_id);
			for (var prop in thisSound.id3) {
				trace(prop + ": " + thisSound.id3[prop]);
			}
		}
			
		public function playSound(sound_id:String, loop:Boolean):void {
			
			var thisSound:sndBase = sndBase(soundList[sound_id]);
			//first stop all sounds managed by this controller
			//for (var prop in soundList) {
			//	stopSoundNow(prop);
			//}
			
			if (loop) {
				thisSound.addEventListener(Event.SOUND_COMPLETE, loopSound);
			}
			soundChannelList[sound_id] = thisSound.play();
		}
		
		public function loopSound(event:Event):void
		{			
			trace("SoundInstance: looping: " + this);
			//tempSound.start();
		}
			
		public function stopSoundNow(sound_id:String):void {
	
			var thisSound:sndBase = sndBase(soundList[sound_id]);
	
			thisSound.removeEventListener(Event.COMPLETE, loopSound);
			
			var tempChannel:SoundChannel;
			
			if (soundChannelList[sound_id] != null) {
				tempChannel = SoundChannel(soundChannelList[sound_id]);
				tempChannel.stop();
			}
		}
/*	
		public function stopSoundAtEndOfLoop(sound_id:String):void {
	
			var thisSound:GameSound = GameSound(soundList[sound_id]);
	
			if (thisSound.onSoundComplete != undefined) {
				thisSound.onSoundComplete = undefined;
			} else {
				thisSound.stop();
			}
		}
*/
		public function setSoundVolume(sound_id:String, volume:Number):void {
			
			var tempChannel:SoundChannel;
			var tempTransform:SoundTransform;
			
			if (soundChannelList[sound_id] != null) {
				tempChannel = SoundChannel(soundChannelList[sound_id]);
				tempTransform = new SoundTransform(.30);
				tempChannel.soundTransform = tempTransform;
			}
		}
	}
}