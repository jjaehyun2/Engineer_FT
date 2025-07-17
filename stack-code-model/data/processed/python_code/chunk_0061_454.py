package {
	
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.media.SoundMixer;
	import flash.net.URLRequest;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class Main extends Sprite {
		private var channel:SoundChannel;
		
	private	const PLOT_HEIGHT:int = 200;
	private		const CHANNEL_LENGTH:int = 256;
	private var bytes:ByteArray;
		
		public function Main():void {
			if (stage)
				init();
			else
				addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			
			
			
			var snd:Sound = new Sound();
			var req:URLRequest = new URLRequest("s.mp3");
			snd.load(req);
			
			channel;
			channel = snd.play();
			addEventListener(Event.ENTER_FRAME, onEnterFrame);
			snd.addEventListener(Event.SOUND_COMPLETE, onPlaybackComplete);
			
			bytes = new ByteArray();
		}
		
		private function onEnterFrame(event:Event):void {
			SoundMixer.computeSpectrum(bytes, false, 0);
			
			var g:Graphics = this.graphics;
			
			g.clear();
			g.lineStyle(0, 0x6600CC);
			g.beginFill(0x6600CC);
			g.moveTo(0, PLOT_HEIGHT);
			
			var n:Number = 0;
			
			// left channel 
			for (var i:int = 0; i < CHANNEL_LENGTH; i++) {
				n = (bytes.readFloat() * PLOT_HEIGHT);
				g.lineTo(i * 2, PLOT_HEIGHT - n);
			}
			g.lineTo(CHANNEL_LENGTH * 2, PLOT_HEIGHT);
			g.endFill();
			
			// right channel 
			g.lineStyle(0, 0xCC0066);
			g.beginFill(0xCC0066, 0.5);
			g.moveTo(CHANNEL_LENGTH * 2, PLOT_HEIGHT);
			
			for (i = CHANNEL_LENGTH; i > 0; i--) {
				n = (bytes.readFloat() * PLOT_HEIGHT);
				g.lineTo(i * 2, PLOT_HEIGHT - n);
			}
			g.lineTo(0, PLOT_HEIGHT);
			g.endFill();
		}
		
		private function onPlaybackComplete(event:Event) {
			removeEventListener(Event.ENTER_FRAME, onEnterFrame);
		}
	
	}

}