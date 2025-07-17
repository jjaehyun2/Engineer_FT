package  {
	import flash.events.Event;
	import flash.display.MovieClip;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.display.Stage;
	
	public class Pup {
		private var pup:MovieClip;
		private var sound:Sound;
		//Will be used for getting sound volume
		private var channel:SoundChannel;
		//variables for keeping track of the current sound levels
		private var prevSoundLevel:Number;
		private var curSoundLevel:Number;
		
		private var changeLevel:Number;
		private var minimumLevel:Number;
		private var stage1:Number;
		private var stage2:Number;
		private var stage3:Number;
		private var stage4:Number;
		
		private var gameMode:Boolean;

		//Constructor
		public function Pup(pup:MovieClip,sound:Sound) {
			this.pup = pup;
			this.sound = sound;
			this.channel = new SoundChannel();
			this.channel = this.sound.play();
			this.prevSoundLevel = 0;
			this.curSoundLevel = 0;
			this.setMinLevel(0.2);
			this.gameMode = false;
			this.pup.addEventListener(Event.ENTER_FRAME, jazz);
		}
		
		//function to move pup based on music
		public function jazz(event:Event):void {
			var leftPeak:Number = this.channel.leftPeak;
			var rightPeak:Number = this.channel.rightPeak;
			var averagePeak:Number = (leftPeak + rightPeak) / 2;
			this.prevSoundLevel = this.curSoundLevel;
			this.curSoundLevel = averagePeak;
			if(this.curSoundLevel > this.minimumLevel) {
				if(Math.abs(this.curSoundLevel - this.prevSoundLevel) > this.changeLevel) {
					if(this.curSoundLevel < this.stage1) {
						this.pup.body.gotoAndPlay(10);
					}
					else if(this.curSoundLevel < this.stage2) {
						this.pup.body.gotoAndPlay(14)
					}
					else if(this.curSoundLevel < this.stage3) {
						this.pup.body.gotoAndPlay(2)
					}
					else {
						this.pup.body.gotoAndPlay(6)
					}
				}
			}
		}
		
		public function setMinLevel(level:Number) {
			//default 0.3
			this.changeLevel = level * 1.5;
			//default 0.2
			this.minimumLevel = level;
			this.stage1 = this.changeLevel/0.8;
			this.stage2 = this.changeLevel/0.6;
			this.stage3 = this.changeLevel/0.4;
			this.stage4 = this.changeLevel/0.3;
		}
		
		public function setSong(sound:Sound) {
			this.channel.stop();
			this.pup.removeEventListener(Event.ENTER_FRAME, jazz);
			this.pup.gotoAndStop(1)
			this.sound = sound;
			this.channel = sound.play();
			this.prevSoundLevel = 0;
			this.curSoundLevel = 0;
			this.pup.addEventListener(Event.ENTER_FRAME, jazz);
		}
		
		public function setGameMode(gameMode:Boolean) {
			this.gameMode = gameMode;
		}
		
	}
	
}