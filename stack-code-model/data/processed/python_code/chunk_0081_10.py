package classes 
{
	import flash.media.Sound;
	import flash.media.SoundMixer;
	import flash.utils.setTimeout;
	/**
	 * ...
	 * @author Lucas Moyano
	 */
	public class Sounds 
	{
		public static var flagSpecialMusic		:Boolean;
		
		public static var kickSound		:Sound;
		public static var takeSound		:Sound;
		public static var tileSound		:Sound;
		public static var tremorSound	:Sound;
		public static var audioFlash		:Sound;
		public static var music			:Sound;
		public static var musicB			:Sound;
		public static var circleDoor		:Sound;
		public static var metalDoor		:Sound;	
		public static var crash			:Sound;
		
		public static function play(sound:Sound, delay:Number = 0, infinite:Boolean = false):void
		{
			var loops:int;
			
			loops = 0;
			if (infinite)
				loops = int.MAX_VALUE;
				
			setTimeout(function() {
				sound.play(0, loops);
			}, delay * 1000);
		}
		
		public static function stopAllSounds():void
		{
			SoundMixer.stopAll();
		}
		
		public static function init():void
		{
			kickSound 	= new KickSound();
			takeSound 	= new TakeSound();
			tileSound 		= new TileSound();
			tremorSound  = new TremorSound();
			audioFlash 	= new AudioFlash();
			music 			= new Music();
			circleDoor		= new CircleDoor();
			musicB			= new MusicB();
			metalDoor		= new MetalDoor();
			crash 			= new Crash();
		}
	}

}