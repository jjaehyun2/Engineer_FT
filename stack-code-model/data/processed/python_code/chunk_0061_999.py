package util.sound
{
	import flash.display.Sprite;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	
	public class ServerUnavailableSound extends Sprite
	{
		[Embed(source="assets/sounds/server_unavailable.mp3")]
		public var soundClass:Class;
		
		public function ServerUnavailableSound()
		{
			var smallSound:Sound = new soundClass() as Sound;
			smallSound.play();
		}
	}
	
}