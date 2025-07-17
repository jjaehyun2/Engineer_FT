package
{
	import flash.desktop.NativeApplication;
	import flash.display.Bitmap;
	import flash.display.Shape;
	import flash.events.Event;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.media.Sound;
	import flash.text.TextFormat;
	import flash.ui.Multitouch;
	import flash.ui.MultitouchInputMode;
	import flash.display.SimpleButton;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.utils.Timer;
	
	/**
	 * ...
	 * @author Reece Clydesdale
	 */
	[SWF(height="800", width="480", backgroundColor="#363636")]
	public class Main extends Sprite 
	{
		[Embed(source = "/assets/bensound-goinghigher.mp3")]
		public var GoingHigherMp3 : Class;
		
		[Embed(source = "/assets/bensound-jazzyfrenchy.mp3")]
		public var JazzyFrenchyMp3 : Class;
		
		//[Embed(source = "/assets/bensound-scifi.mp3")]
		//public var SciFiMp3 : Class;
		
		[Embed(source = "/assets/bensound-anewbeginning.mp3")]
		public var ANewBeginningMp3 : Class;
		
		[Embed(source = "/assets/bensound-acousticbreeze.mp3")]
		public var AcousticBreezeMp3: Class;
		
		[Embed(source = "/assets/bensound-betterdays.mp3")]
		public var BetterDaysMp3 : Class;
		
		[Embed(source = "/assets/bensound-buddy.mp3")]
		public var BuddyMp3 : Class;
		
		[Embed(source = "/assets/bensound-epic.mp3")]
		public var EpicMp3 : Class;
		
		//[Embed(source = "/assets/bensound-extremeaction.mp3")]
		//public var ExtremeActionMp3 : Class;
		
		[Embed(source = "/assets/bensound-littleidea.mp3")]
		public var LittleIdeaMp3 : Class;
		
		[Embed(source = "/assets/bensound-ofeliasdream.mp3")]
		public var OfeliasDreamMp3 : Class;
		
		[Embed(source = "/assets/bensound-slowmotion.mp3")]
		public var SlowMotionMp3 : Class;
		
		public var mediaPlayer : MusicPlayer;
		
		public var track : Sound;
		
		public var textSongName : TextField;
		public var currentTextSongName : String;
		
		public var progressBar : Sprite;
		public var progressBarContainer : Sprite;
		public var progressBarFiller : Sprite;
		
		public var progressBarHeight : int = 6;
		
		public var buttonPlaySprite : Sprite;
		public var buttonStopSprite : Sprite;
		public var buttonPauseSprite : Sprite;
		public var buttonRandomSprite : Sprite;
		
		public var buttonPlayUnpushed : Bitmap;
		public var buttonPauseUnpushed : Bitmap;
		public var buttonStopUnpushed : Bitmap;
		public var buttonRandomUnpushed : Bitmap;
		
		public var buttonPlayPushed : Bitmap;
		public var buttonPausePushed : Bitmap;
		public var buttonStopPushed : Bitmap;
		public var buttonRandomPushed : Bitmap;
		
		[Embed(source = "/assets/UnpushedPlay.png")]
		public var PlayPng : Class;
		
		[Embed(source = "/assets/UnpushedStop.png")]
		public var StopPng : Class;
		
		[Embed(source = "/assets/UnpushedPause.png")]
		public var PausePng : Class;
		
		[Embed(source = "/assets/UnpushedRandom.png")]
		public var RandomPng : Class;
		
		[Embed(source = "/assets/PushedPlay.png")]
		public var PushedPlayPng : Class;
		
		[Embed(source = "/assets/PushedStop.png")]
		public var PushedStopPng : Class;
		
		[Embed(source = "/assets/PushedPause.png")]
		public var PushedPausePng : Class;
		
		[Embed(source = "/assets/PushedRandom.png")]
		public var PushedRandomPng : Class;
		
		[Embed(source = "/assets/EasterEgg.png")]
		public var EasterEggPng : Class;
		
		public function playAudio(e : Event) : void
		{
			mediaPlayer.play();
			buttonPlaySprite.visible = false;
		}
		
		public function stopAudio(e : Event) : void
		{
			mediaPlayer.stop();
			buttonPlaySprite.visible = true;
		}
		
		public function randomAudio(e : Event) : void
		{
			mediaPlayer.setRandomTrack();
		}
		
		public function pauseAudio(e : Event) : void
		{
			mediaPlayer.pause();
			buttonPlaySprite.visible = true;
		}
		
		public function animatePause(e : MouseEvent) : void
		{
			buttonPauseUnpushed.visible = (e.type != "mouseDown");
		}
		
		public function animatePlay(e : MouseEvent) : void
		{
			buttonPlayUnpushed.visible = (e.type != "mouseDown");
		}
		
		public function animateStop(e : MouseEvent) : void
		{
			buttonStopUnpushed.visible = (e.type != "mouseDown");
		}
		
		public function animateRandom(e : MouseEvent) : void
		{
			buttonRandomUnpushed.visible = (e.type != "mouseDown");
		}
		
		public function updateSongName() : void
		{
			var name : String = mediaPlayer.getTrackName();
			if (name == null)
			{
				return;
			}
			if (name == currentTextSongName)
			{
				return;
			}
			
			textSongName.text = name;
		}
		
		public function updateSongProgress() : void
		{
			progressBar.width = Math.floor(mediaPlayer.getProgress() * progressBarContainer.width);
			progressBar.height = progressBarHeight;
		}
		
		public function handleTimer(e : Event) : void
		{
			updateSongName();
			updateSongProgress();
		}
		
		public function Main() 
		{
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			stage.addEventListener(Event.DEACTIVATE, deactivate);
			
			// touch or gesture?
			Multitouch.inputMode = MultitouchInputMode.TOUCH_POINT;
			
			// Entry point
			
			mediaPlayer = new MusicPlayer();

            // These songs were used to test the program but have since been removed for copyright reasons.
			//mediaPlayer.addTrack(new AcousticBreezeMp3(), "Acoustic Breeze"); // OK
			//mediaPlayer.addTrack(new ANewBeginningMp3(), "A New Beginning"); // OK
			//mediaPlayer.addTrack(new BetterDaysMp3(), "Better Days"); // OK
			//mediaPlayer.addTrack(new BuddyMp3(), "Buddy"); // OK
			//mediaPlayer.addTrack(new EpicMp3(), "Epic"); // OK
			//mediaPlayer.addTrack(new GoingHigherMp3(), "Going Higher"); // OK
			//mediaPlayer.addTrack(new LittleIdeaMp3(), "Little Idea"); // OK
			//mediaPlayer.addTrack(new OfeliasDreamMp3(), "Ofelia's Dream"); // OK
			//mediaPlayer.addTrack(new SlowMotionMp3(), "Slow Motion"); // OK
			//mediaPlayer.addTrack(new JazzyFrenchyMp3(), "Jazzy Frenchy"); // OK
			
			// PNG assets.
			// Play
			buttonPlayUnpushed = new PlayPng();
			buttonPlayUnpushed.height = buttonPlayUnpushed.width = 50;
			
			buttonPlayPushed = new PushedPlayPng();
			buttonPlayPushed.height = buttonPlayPushed.width = 50;
			
			// Stop
			buttonStopUnpushed = new StopPng();
			buttonStopUnpushed.height = buttonStopUnpushed.width = 50;
			
			buttonStopPushed = new PushedStopPng();
			buttonStopPushed.height = buttonStopPushed.width = 50;
			
			// Random
			buttonRandomUnpushed = new RandomPng();
			buttonRandomUnpushed.height = buttonRandomUnpushed.width = 50;
			
			buttonRandomPushed = new PushedRandomPng();
			buttonRandomPushed.height = buttonRandomPushed.width = 50;
			
			// Pause
			buttonPauseUnpushed = new PausePng();
			buttonPauseUnpushed.height = buttonPauseUnpushed.width = 50;
			
			buttonPausePushed = new PushedPausePng();
			buttonPausePushed.height = buttonPausePushed.width = 50;
			
			
			var pngEasterEgg : Bitmap = new EasterEggPng();
			pngEasterEgg.height = (909 / 2);
			pngEasterEgg.width = (700 / 2);
			
			
			var btnWidth : int = 80;
			var btnHeight : int = 80;
			
			var btnNum : int = 0;
			// Pause is not counted as it shares a slot with play.
			var btnCount : int = 3; 
			
			var secWidth : Number = (stage.stageWidth / btnCount);
			var btnOffset : Number = ((secWidth - btnWidth) / 2);
			
			// Play button. When this is clicked, it becomes invisible and reveals the Pause button.
			buttonPlaySprite = new Sprite();
			buttonPlaySprite.addChild(buttonPlayPushed);
			buttonPlaySprite.addChild(buttonPlayUnpushed);
			// Pause button. Displays beneath 'Play', never visible (to the user) until Play sprite is invisible.
			buttonPauseSprite = new Sprite();
			buttonPauseSprite.addChild(buttonPausePushed);
			buttonPauseSprite.addChild(buttonPauseUnpushed);
			buttonPauseSprite.width = buttonPlaySprite.width = btnWidth;
			buttonPauseSprite.height = buttonPlaySprite.height = btnHeight;
			buttonPauseSprite.x = buttonPlaySprite.x = Math.floor((btnNum++) * secWidth) + btnOffset;;
			buttonPauseSprite.y = buttonPlaySprite.y = (btnHeight / 2);
			
			buttonPausePushed.x = buttonPlayPushed.x = buttonPauseUnpushed.x = buttonPlayUnpushed.x = 0;
			buttonPausePushed.y = buttonPlayPushed.y = buttonPauseUnpushed.y = buttonPlayUnpushed.y = 0;
			
			buttonPauseSprite.addEventListener(MouseEvent.CLICK, pauseAudio);
			buttonPlaySprite.addEventListener(MouseEvent.CLICK, playAudio);
			
			addChild(buttonPauseSprite);
			addChild(buttonPlaySprite);
			
			// Stop button.
			buttonStopSprite = new Sprite();
			buttonStopSprite.addChild(buttonStopPushed);
			buttonStopSprite.addChild(buttonStopUnpushed);
			buttonStopSprite.width = btnWidth;
			buttonStopSprite.height = btnHeight;
			buttonStopSprite.addEventListener(MouseEvent.CLICK, stopAudio);
			buttonStopSprite.x = Math.floor((btnNum++) * secWidth) + btnOffset;
			buttonStopSprite.y = (btnHeight / 2);
			buttonStopUnpushed.x = 0;
			buttonStopUnpushed.y = 0;
			addChild(buttonStopSprite);
			
			// Random button.
			buttonRandomSprite = new Sprite();
			buttonRandomSprite.addChild(buttonRandomPushed);
			buttonRandomSprite.addChild(buttonRandomUnpushed);
			buttonRandomSprite.width = btnWidth;
			buttonRandomSprite.height = btnHeight;
			buttonRandomSprite.addEventListener(MouseEvent.CLICK, randomAudio);
			buttonRandomSprite.x = Math.floor((btnNum++) * secWidth) + btnOffset;
			buttonRandomSprite.y = (btnHeight / 2);
			buttonRandomUnpushed.x = 0;
			buttonRandomUnpushed.y = 0;
			addChild(buttonRandomSprite);
			
			// Button animations
			buttonPauseSprite.addEventListener(MouseEvent.MOUSE_DOWN, animatePause);
			buttonStopSprite.addEventListener(MouseEvent.MOUSE_DOWN, animateStop);
			buttonPlaySprite.addEventListener(MouseEvent.MOUSE_DOWN, animatePlay);
			buttonRandomSprite.addEventListener(MouseEvent.MOUSE_DOWN, animateRandom);
			stage.addEventListener(MouseEvent.MOUSE_UP, animatePause);
			stage.addEventListener(MouseEvent.MOUSE_UP, animateStop);
			stage.addEventListener(MouseEvent.MOUSE_UP, animatePlay);
			stage.addEventListener(MouseEvent.MOUSE_UP, animateRandom);
			
			// Progress bar.
			progressBarContainer = new Sprite();
			progressBarContainer.x = 0;
			progressBarContainer.y = 200;
			progressBarContainer.graphics.moveTo(0, 0);
			progressBarContainer.graphics.lineStyle(1);
			progressBarContainer.graphics.beginFill(0x333333, 1);
			progressBarContainer.graphics.drawRect(0, 0, stage.stageWidth, progressBarHeight);
			progressBarContainer.graphics.endFill();
			
			progressBar = new Sprite();
			// For efficiency: draw the rectangle once,
			// adjust the width so only part of it displays.
			progressBar.graphics.moveTo(0, 0);
			progressBar.graphics.lineStyle(0);
			progressBar.graphics.beginFill(0xFF0000, 1);
			
			progressBar.graphics.drawRect(0, 0, stage.stageWidth, progressBarHeight);
			progressBar.graphics.endFill();
			
			progressBarContainer.addChild(progressBar);
			progressBarContainer.width = stage.stageWidth;
			progressBarContainer.height = progressBarHeight;
			
			addChild(progressBarContainer);
			
			// Song title.
			var tf : TextFormat = new TextFormat();
			tf.size = 46;
			tf.align = "center";
			tf.color = 0xd5d5d5;
			//tf.font = "Arial";
			
			textSongName = new TextField();
			textSongName.defaultTextFormat = tf;
			textSongName.text = "";
			textSongName.width = stage.stageWidth;
			textSongName.height = 56;
			
			textSongName.x = 0;
			textSongName.y = 156;
			
			addChild(textSongName);
			
			
			pngEasterEgg.x = (stage.stageWidth - pngEasterEgg.width) / 2;
			pngEasterEgg.y = 250;
			addChild(pngEasterEgg);
			
			var tfEgg : TextField = new TextField();
			var tffEgg : TextFormat = new TextFormat();
			tffEgg.color = 0xd5d5d5;
			tffEgg.align = "center";
			tffEgg.size = 36;
			
			tfEgg.defaultTextFormat = tffEgg;
			
			tfEgg.text = "Bailey's Easter Egg";
			tfEgg.width = stage.stageWidth;
			tfEgg.x = 0;
			tfEgg.y = 225;
			addChild(tfEgg);
			
			var timer : Timer = new Timer(1000);
			timer.addEventListener("timer", handleTimer);
			timer.start();
		}
		
		private function deactivate(e:Event):void 
		{
			// make sure the app behaves well (or exits) when in background
			//NativeApplication.nativeApplication.exit();
		}
		
	}
	
}