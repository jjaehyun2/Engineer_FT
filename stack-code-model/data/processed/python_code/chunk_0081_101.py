package services
{
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.net.URLRequest;
	
	public class SoundPlayer
	{
		
		[Bindable] public var url:String;
		
		// the list of audio files to play
		private var playList:Array;
		
		private var mySound:Sound;
		private var mySoundChannel:SoundChannel;
		
		// are we currently playing
		private var playing:Boolean = false;
		
		// a random number to get always the recent audio files
		private var random:Number = Math.floor( Math.random() * 99);
		
		public function SoundPlayer()
		{
			playList = new Array();
		}
		
		private function soundCompleteHandler( event:Event ):void
		{
			// play the next audio file, if any
			playing = false;
			if (playList.length > 0) { 
				play();
			} 
			
		}
		
		// add a new song, strip number from Bubble to get the number
		public function addBubbleTitle( a:String ):void
		{
			var parts:Array = a.split(".");
			// split the number from String
			// add audio to the end of the Array
			// check if Production or Test
			
			var number:Number = parts[0];
			var numberString:String = "";
			
			if ( number > 300 ) { number -= 300; }
			if ( number > 200 ) { number -= 200; }
			if ( number > 100 ) { number -= 100; }
			
			if ( number < 10 ) { numberString = "0"+number.toString(); } else { numberString = number.toString(); }
			
			playList.push( numberString + "_name.mp3" );
			// play if there is something to play and currently not playing
			if (playList.length > 0 && playing == false) { 
				play();
			} 
		}

		public function addFile( a:String ):void
		{
			// add audio to the end of the Array
			playList.push( a );
			// play if there is something to play and currently not playing
			if (playList.length > 0 && playing == false) { 
				play();
			} 
		}

		
		private function play():void
		{
			//var request:URLRequest = new URLRequest( "assets/sounds/" + playList.shift() + "?" + random );
			var request:URLRequest = new URLRequest( "assets/sounds/" + playList.shift() );
			url = request.url;
			
			mySound = new Sound();
				
			// add IOErrorEvent Handler to skip invalid sound files
			mySound.addEventListener(IOErrorEvent.IO_ERROR, soundCompleteHandler);
			mySound.load(request);
				
			mySoundChannel = mySound.play();
			// avoid playing at the same time
			playing = true;
			mySoundChannel.addEventListener(Event.SOUND_COMPLETE, soundCompleteHandler);
		}
		
	}
}