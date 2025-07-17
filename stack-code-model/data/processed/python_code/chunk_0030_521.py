package com.illuzor.circles.tools {
	
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.media.SoundMixer;
	import flash.net.URLRequest;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class AudioManager {
		
		public static const CORRECT_SOUND:String = "../assets/sound_correct.mp3";
		public static const INCORRECT_SOUND:String = "../assets/sound_incorrect.mp3";
		public static const MUSIC:String = "../assets/music.mp3";
		
		private static var musicChannel:SoundChannel;
		private static var soundChannel:SoundChannel;
		
		public static function playSound(soundName:String):void {
			var sound:Sound = new Sound(new URLRequest(soundName));
			soundChannel = sound.play();
		}
		
		public static function playMusic():void {
			var sound:Sound = new Sound(new URLRequest(MUSIC));
			musicChannel = sound.play(0, 1000);
		}
		
		public static function stopMusic():void {
			musicChannel.stop();
		}
		
		public static function stopAll():void {
			SoundMixer.stopAll();
		}
		
	}
}