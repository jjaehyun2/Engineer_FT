package  {
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.utils.Timer;
	import flash.utils.getTimer;
	import flash.events.TimerEvent;
	import flash.display.DisplayObject;
	import flash.geom.Matrix;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.media.SoundChannel;
	import flash.media.SoundTransform;
	import flash.media.Sound;
	
	public class Hay {
		
		private var target:MovieClip;
		private var touchArea:MovieClip;
		private var hitTruck:MovieClip;
		private var fallSpeed:Number;
		private var falling:Boolean;
		private var player:Player;
		private var timer:Timer;
		private var timerTime:Number;
		private var scoreKeeper:ScoreKeeper;
		private var startTime:Number;
		private var currentTime:Number;
		
		private var rotationSpeed:Number;
		private var bounceSpeed:Number;
		
		private var changeOk:Boolean;
		private var changeOkTop:Boolean;
		private var changeOkFront:Boolean;
		
		private var hitTop:MovieClip;
		private var hitFront:MovieClip;
		
		private var dropHeight:Number;
		
		private var hitFrontAlready:Boolean;
		
		private var endGame:MovieClip;
		
		private var moveSpeed:Number;
		
		private var permy:Permy;
		
		private var coin:Coin;

		private var pausedTimerTime:Number;
		
		private var paused:Boolean;
		
		private var missionHandler:MissionHandler;
		
		private var bouncedOffTop:Boolean;
		
		private var grassBottom:MovieClip;
		
		private var hitGrass:Boolean;
		
		private var multiplier:Number;
		
		private var powerup:Powerup;
		
		private var tiers:MovieClip;
		private var x3:TextField;
		private var x2:TextField;
		private var x1:TextField;
		private var speedometer:MovieClip;
		private var pauseButton:MovieClip;
		private var timeLabel:TextField;
		private var timeField:TextField;
		
		private var scoreLabel:TextField;
		private var hiScoreLabel:TextField;
		private var coinsLabel:TextField;
		private var totalCoinsLabel:TextField;
		
		private var scoreMoveSpeed;
		
		private var moveSpeedF1:Number;
		
		private var storeMovie:MovieClip;
		
		private var store:Store;
		
		private var mainSound:SoundChannel;
		private var mainSoundSound:Sound;
		private var fadeTimer:Timer;
		private var pauseSoundPos:Number;
		private var fadeInTimer:Timer;
		
		private var gotHiScore:Boolean;
		
		private var acheivementsCheck:Function;
		private var submitScore:Function;
		
		private var tutTap:TextField;
		
		//private var viewLeaderBoardFadeIn2:Function;
		//private var viewLeaderBoardFadeOut2:Function;
		
		private var openStore:Function;
		
		private var closeStoreOk:Boolean;

		public function Hay(target:MovieClip,touchArea:MovieClip,hitTruck:MovieClip,hitTop:MovieClip,hitFront:MovieClip,player:Player,scoreKeeper:ScoreKeeper,endGame:MovieClip,permy:Permy,missionHandler:MissionHandler,grassBottom:MovieClip,tiers:MovieClip,x3:TextField,x2:TextField,x1:TextField,speedometer:MovieClip,pauseButton:MovieClip,timeLabel:TextField,timeField:TextField,scoreLabel:TextField,hiScoreLabel:TextField,coinsLabel:TextField,totalCoinsLabel:TextField,storeMovie:MovieClip,mainSound:SoundChannel,mainSoundSound:Sound,tutTap:TextField) {
			this.target = target;
			this.fallSpeed = 0;
			this.falling = false;
			this.touchArea = touchArea;
			this.hitTruck = hitTruck;
			this.player = player;
			this.scoreKeeper = scoreKeeper;
			this.touchArea.addEventListener(MouseEvent.CLICK,startFall);
			
			this.closeStoreOk = true;
			
			this.tutTap = tutTap;
			
			this.storeMovie = storeMovie;
			
			this.scoreMoveSpeed = 20;
			
			moveSpeedF1 = 14;
			
			this.scoreLabel = scoreLabel;
			this.hiScoreLabel = hiScoreLabel;
			this.coinsLabel = coinsLabel;
			this.totalCoinsLabel = totalCoinsLabel;
			
			this.tiers = tiers;
			this.x3 = x3;
			this.x2 = x2;
			this.x1 = x1;
			this.speedometer = speedometer;
			this.pauseButton = pauseButton;
			this.timeLabel = timeLabel;
			this.timeField = timeField;
			
			this.multiplier = 1;
			
			this.paused = false;
			
			this.hitGrass = false;
			
			this.bouncedOffTop = false;
			
			this.missionHandler = missionHandler;
			
			this.grassBottom = grassBottom;
			
			this.timerTime = 10000;
			this.timer = new Timer(timerTime,1);
			this.timer.addEventListener(TimerEvent.TIMER,autoDrop);
			this.timer.start();
			
			this.startTime = getTimer();
			
			this.changeOk = true;
			this.changeOkTop = true;
			this.changeOkFront = true;
			
			this.hitTop = hitTop;
			this.hitFront = hitFront;
			this.hitFrontAlready = false;
			
			this.endGame = endGame;
			endGame.alpha = 0;
			
			this.moveSpeed = 14;
			
			this.permy = permy;
			
			this.pausedTimerTime = -1;
			
			this.mainSound = mainSound;
			
			this.fadeTimer = new Timer(60);
			this.fadeTimer.addEventListener(TimerEvent.TIMER,fadeSound);
			
			this.pauseSoundPos = 0;
			this.mainSoundSound = mainSoundSound;
			
			this.scoreKeeper.setHiScoreField(this.permy.getHiScore());
			
			this.target.addEventListener(Event.ENTER_FRAME,keepTimeUpdated);
			this.touchArea.addEventListener(MouseEvent.MOUSE_DOWN,startMoveBail);
			
			this.gotHiScore = false;
		}
		
		public function setCloseStoreOk(boo:Boolean) {
			this.closeStoreOk = boo;
		}
		
		public function setAddFunction(funct:Function):void {
			this.acheivementsCheck = funct;
		}
		
		public function setScoreFunction(funct:Function):void {
			this.submitScore = funct;
		}
		
		public function fadeSound(event:Event) {
			var vol:Number = this.mainSound.soundTransform.volume;
			var soundT:SoundTransform = this.mainSound.soundTransform;
			vol = vol - 0.05;
			soundT.volume = vol;
			if(vol > 0) {
				this.mainSound.soundTransform = soundT; 
			}
			else {
				this.mainSound.stop();
				this.fadeTimer.stop();
				this.fadeTimer.removeEventListener(TimerEvent.TIMER,fadeSound);
			}
		}
		
		function restartSoundFromBeginning(event:Event) {
			mainSound.removeEventListener(Event.SOUND_COMPLETE,restartSoundFromBeginning);
			mainSound = mainSoundSound.play(0,999,new SoundTransform(0.4));
		}
		
		public function setPowerUp(powerup:Powerup) {
			this.powerup = powerup;
		}
		
		public function setMultiplier(multiplier:Number) {
			this.multiplier = multiplier;
		}
		
		public function startMoveBail(event:MouseEvent) {
			if(!this.paused) {
				this.target.x = touchArea.mouseX-this.target.width/2;
				this.target.y = touchArea.mouseY-this.target.height/2;
				this.touchArea.addEventListener(MouseEvent.MOUSE_MOVE,moveBail);
				this.touchArea.addEventListener(MouseEvent.MOUSE_UP,stopMoveBail);
				this.touchArea.removeEventListener(MouseEvent.MOUSE_DOWN,startMoveBail);
			}
		}
		
		public function moveBail(event:MouseEvent) {
			if(!this.paused) {
				this.target.x = touchArea.mouseX-this.target.width/2;
				this.target.y = touchArea.mouseY-this.target.height/2;
				touchArea.addEventListener(MouseEvent.ROLL_OUT,listenForRollOut);
			}
		}
		
		public function listenForRollOut(event:MouseEvent) {
			this.touchArea.removeEventListener(MouseEvent.MOUSE_DOWN,startMoveBail);
			this.touchArea.removeEventListener(MouseEvent.MOUSE_MOVE,moveBail);
			this.touchArea.removeEventListener(MouseEvent.MOUSE_UP,stopMoveBail);
			this.touchArea.addEventListener(MouseEvent.MOUSE_DOWN,startMoveBail);
			this.touchArea.removeEventListener(MouseEvent.ROLL_OUT,listenForRollOut);
		}
		
		public function stopMoveBail(event:MouseEvent) {
			this.target.x = touchArea.mouseX-this.target.width/2;
			this.target.y = touchArea.mouseY-this.target.height/2;
			this.touchArea.removeEventListener(MouseEvent.MOUSE_MOVE,moveBail);
			this.touchArea.removeEventListener(MouseEvent.MOUSE_UP,stopMoveBail);
		}
		
		public function setCoin(coin:Coin) {
			this.coin = coin;
		}
		
		public function getTimerTime():Number {
			return this.timerTime;
		}
		
		public function setTimerTime(time:Number) {
			this.timerTime = time;
			trace(this.timerTime);
		}
		
		public function keepTimeUpdated(event:Event) {
			if(!this.paused) {
				if(this.pausedTimerTime == -1) {
					this.currentTime = getTimer();
					if ((this.timerTime-(this.currentTime - this.startTime)) >= 0) {
						this.scoreKeeper.setTimeField(Math.round(((this.timerTime-(this.currentTime - this.startTime))/1000) * 10) / 10);
					}
					else {
						this.scoreKeeper.setTimeField(0);
					}
				}
				else {
					this.currentTime = getTimer();
					if ((this.pausedTimerTime-(this.currentTime - this.startTime)) >= 0) {
						this.scoreKeeper.setTimeField(Math.round(((this.pausedTimerTime-(this.currentTime - this.startTime))/1000) * 10) / 10);
					}
					else {
						this.scoreKeeper.setTimeField(0);
						this.pausedTimerTime = -1;
					}
				}
			}
		}
		
		
		
		public function pause() {
			this.pausedTimerTime = 	Number(this.scoreKeeper.getTimeField().text) * 1000;
			this.timer.removeEventListener(TimerEvent.TIMER,autoDrop);
			this.timer.stop();
		}
		
		public function unpause() {
			if(this.fallSpeed == 0) {
				var test:Number = this.pausedTimerTime;
				this.startTime = getTimer();
				this.timer = new Timer(test,1);
				this.timer.addEventListener(TimerEvent.TIMER,autoDrop);
				this.timer.start();
			}
		}
		
		public function autoDrop(event:TimerEvent) {
			if(!this.paused) {
				this.pausedTimerTime = -1;
				this.target.removeEventListener(Event.ENTER_FRAME,keepTimeUpdated);
				this.touchArea.removeEventListener(MouseEvent.MOUSE_DOWN,startMoveBail);
				this.touchArea.removeEventListener(MouseEvent.MOUSE_MOVE,moveBail);
				this.touchArea.removeEventListener(MouseEvent.MOUSE_UP,stopMoveBail);
				this.touchArea.removeEventListener(MouseEvent.ROLL_OUT,listenForRollOut);
				this.touchArea.removeEventListener(MouseEvent.CLICK,startFall);
				this.touchArea.addEventListener(Event.ENTER_FRAME,fall);
				this.target.addEventListener(Event.ENTER_FRAME,tutTapFadeOut);
				this.dropHeight = this.target.y;
			}
		}
		
		public function startFall(event:MouseEvent) {
			if(!this.paused) {
				this.pausedTimerTime = -1;
				this.target.x = touchArea.mouseX-this.target.width/2;
				this.target.y = touchArea.mouseY-this.target.height/2;
				this.touchArea.removeEventListener(MouseEvent.MOUSE_DOWN,startMoveBail);
				this.touchArea.removeEventListener(MouseEvent.MOUSE_MOVE,moveBail);
				this.touchArea.removeEventListener(MouseEvent.MOUSE_UP,stopMoveBail);
				this.touchArea.removeEventListener(MouseEvent.ROLL_OUT,listenForRollOut);
				this.timer.removeEventListener(TimerEvent.TIMER,autoDrop);
				this.target.removeEventListener(Event.ENTER_FRAME,keepTimeUpdated);
				this.touchArea.removeEventListener(MouseEvent.CLICK,startFall);
				this.touchArea.addEventListener(Event.ENTER_FRAME,fall);
				this.target.addEventListener(Event.ENTER_FRAME,tutTapFadeOut);
				this.dropHeight = this.target.y;
			}
		}
		
		public function rotateAround(event:Event) {
			if(!this.paused) {
				if(this.target.insideHay.rotation < 0) {
					this.target.insideHay.rotation = this.target.insideHay.rotation + rotationSpeed/3;
					if(this.target.insideHay.rotation >= 0) {
						this.target.removeEventListener(Event.ENTER_FRAME,rotateAround);
					}
				}
				if(this.target.insideHay.rotation > 0) {
					this.target.insideHay.rotation = this.target.insideHay.rotation - rotationSpeed/3;
					if(this.target.insideHay.rotation <= 0) {
						this.target.removeEventListener(Event.ENTER_FRAME,rotateAround);
					}
				}
			}
		}
		
		public function fall(event:Event) {
			if(!this.paused) {
				this.target.y = this.target.y + this.fallSpeed;
				this.fallSpeed ++;
				
				if(this.target.hitTestObject(this.grassBottom)) {
					if(this.target.perfectHitTest(this.grassBottom,1)) {
						//grass
						this.hitGrass = true;
						this.target.y = this.grassBottom.y - this.target.insideHay.height - 1;
						this.target.removeEventListener(Event.ENTER_FRAME,bounceOffLeft);
						this.target.removeEventListener(Event.ENTER_FRAME,bounceOffRight);
						//this.target.y = this.hitTruck.y - this.target.height;
		
						this.fallSpeed = 0;
						
						trace(this.powerup.getInvincibleTimer());
						if(this.powerup.getInvincibleTimer() == 0) {
							this.player.stopMoving();
							this.lose();
						}
						else {
							scorePoint(0);
						}
						this.touchArea.removeEventListener(Event.ENTER_FRAME,fall);
						
					}
				}
				else if(this.target.hitTestObject(this.hitTruck) && !this.hitGrass) {
					if(this.target.perfectHitTest(this.hitTruck,1)) {
						//truck back
						if((this.target.x >= this.hitTruck.x - 26.25 && this.player.getDirection() == "Right") || (this.target.x <= this.hitTruck.x + this.hitTruck.width - 26.25 && this.player.getDirection() == "Left")) {
								this.target.y = this.hitTruck.y - this.target.insideHay.height - 1;
								this.target.removeEventListener(Event.ENTER_FRAME,bounceOffLeft);
								this.target.removeEventListener(Event.ENTER_FRAME,bounceOffRight);
								if(this.target.insideHay.rotation <= -1 || this.target.insideHay.rotation >= 1) {
									this.target.addEventListener(Event.ENTER_FRAME,rotateAround);
								}
								//this.target.y = this.hitTruck.y - this.target.height;
								this.fallSpeed = -this.fallSpeed/5;
								this.player.stopMoving();
								if(Math.abs(this.fallSpeed) < 1) {
									this.fallSpeed = 0;
									this.touchArea.removeEventListener(Event.ENTER_FRAME,fall);
									scorePoint(5);
								}
						}
						else if((this.target.x < this.hitTruck.x - 26.25 && this.player.getDirection() == "Right") || (this.target.x > this.hitTruck.x + this.hitTruck.width - 26.25 && this.player.getDirection() == "Left")) {
								this.target.y = this.hitTruck.y - this.target.insideHay.height - 1;
								this.player.stopMoving();
								this.target.removeEventListener(Event.ENTER_FRAME,bounceOffLeft);
								this.target.removeEventListener(Event.ENTER_FRAME,bounceOffRight);
								//this.touchArea.removeEventListener(Event.ENTER_FRAME,fall);
								if(this.player.getDirection() == "Right") {
									rotationSpeed = this.hitTruck.x - 26.25 - this.target.x;
									bounceSpeed = rotationSpeed/5 + fallSpeed/10;
									this.fallSpeed = -fallSpeed/5 + bounceSpeed;
									this.target.addEventListener(Event.ENTER_FRAME,bounceOffLeft);
								}
								else if(this.player.getDirection() == "Left") {
									rotationSpeed = this.target.x - this.hitTruck.x +26.25 - this.hitTruck.width;
									bounceSpeed = rotationSpeed/5 + fallSpeed/10;
									this.fallSpeed = -fallSpeed/5 + bounceSpeed ;
									this.target.addEventListener(Event.ENTER_FRAME,bounceOffRight);
								}
						}
							
						
					}
				}
				else if(this.target.hitTestObject(this.hitFront) && !this.hitGrass) {
					if(this.target.perfectHitTest(this.hitFront,1)) {
						this.hitFrontAlready = true;
						//truckfront
							if((this.target.x >= this.hitFront.x - 26.25 && this.player.getDirection() == "Left") || (this.target.x <= this.hitFront.x + this.hitFront.width - 26.25 && this.player.getDirection() == "Right")) {
								this.target.y = this.hitFront.y - this.target.insideHay.height - 1;
								this.fallSpeed = -fallSpeed/5;
								this.player.stopMoving();
								if(Math.abs(this.fallSpeed) < 1) {
									this.fallSpeed = 0;
									this.touchArea.removeEventListener(Event.ENTER_FRAME,fall);
									scorePoint(7);
								}
							}
							else if((this.target.x < this.hitFront.x - 26.25 && this.player.getDirection() == "Left") || (this.target.x > this.hitFront.x + this.hitFront.width - 26.25 && this.player.getDirection() == "Right")) {
								this.target.y = this.hitFront.y - this.target.insideHay.height - 1;
								this.player.stopMoving();
								this.target.removeEventListener(Event.ENTER_FRAME,bounceOffLeft);
								this.target.removeEventListener(Event.ENTER_FRAME,bounceOffRight);
								if(this.player.getDirection() == "Left") {
									rotationSpeed = this.hitFront.x - 26.25 - this.target.x;
									bounceSpeed = rotationSpeed/5 + fallSpeed/10;
									this.fallSpeed = -fallSpeed/5 + bounceSpeed;
									this.target.addEventListener(Event.ENTER_FRAME,bounceOffLeft);
								}
								else if(this.player.getDirection() == "Right") {
									rotationSpeed = this.target.x - this.hitFront.x +26.25 - this.hitFront.width;
									bounceSpeed = rotationSpeed/5 + fallSpeed/10;
									this.fallSpeed = -fallSpeed/5 + bounceSpeed ;
									this.target.addEventListener(Event.ENTER_FRAME,bounceOffRight);
								}
							}
					}
				}
				else if(this.target.hitTestObject(this.hitTop) && !this.hitGrass) {
					if(this.target.perfectHitTest(this.hitTop,1) && this.hitFrontAlready == false) {
						//trucktop
							if(this.target.x >= this.hitTop.x - 26.25 && this.target.x <= this.hitTop.x + this.hitTop.width - 26.25) {
								this.target.y = this.hitTop.y - this.target.insideHay.height - 1;
								this.fallSpeed = -fallSpeed/5;
								this.player.stopMoving();
								if(Math.abs(this.fallSpeed) < 1) {
									this.fallSpeed = 0;
									this.touchArea.removeEventListener(Event.ENTER_FRAME,fall);
									scorePoint(6);
								}
							}
							else if((this.target.x < this.hitTop.x - 26.25) || (this.target.x > this.hitTop.x + this.hitTop.width - 26.25)) {
								this.bouncedOffTop = true;
								this.target.y = this.hitTop.y - this.target.insideHay.height - 1;
								this.player.stopMoving();
								this.target.removeEventListener(Event.ENTER_FRAME,bounceOffLeft);
								this.target.removeEventListener(Event.ENTER_FRAME,bounceOffRight);
								//this.touchArea.removeEventListener(Event.ENTER_FRAME,fall);
								if(this.target.x < this.hitTop.x - 26.25) {
									rotationSpeed = this.hitTop.x - 26.25 - this.target.x;
									bounceSpeed = rotationSpeed/5 + fallSpeed/10;
									this.fallSpeed = -fallSpeed/5 + bounceSpeed;
									this.target.addEventListener(Event.ENTER_FRAME,bounceOffLeft);
								}
								else {
									rotationSpeed = this.target.x - this.hitTop.x +26.25 - this.hitTop.width;
									bounceSpeed = rotationSpeed/5 + fallSpeed/10;
									this.fallSpeed = -fallSpeed/5 + bounceSpeed ;
									//if(this.player.getDirection() == "Left") {
										//this.hitTruck.x = this.hitTruck.x + 50;
									//}
									this.target.addEventListener(Event.ENTER_FRAME,bounceOffRight);
								}
							}
					}
				}
			}
		}
		
		public function bounceOffLeft(event:Event) {
			if(!this.paused) {
				this.target.x = this.target.x - bounceSpeed/2;
				this.target.insideHay.rotation = this.target.insideHay.rotation - rotationSpeed/3;
			}
		}
		
		public function bounceOffRight(event:Event) {
			if(!this.paused) {
				this.target.x = this.target.x + bounceSpeed/2;
				this.target.insideHay.rotation = this.target.insideHay.rotation + rotationSpeed/3;
			}
		}

		public function scorePoint(points:Number) {
			if(points != 0) {
				if(this.permy.getMute() == false) {
					var quackSound:Sound = new Quack();
					quackSound.play();
				}
			}
			
			this.touchArea.addEventListener(MouseEvent.MOUSE_DOWN,startMoveBail);
			this.hitTruck.y = 902.2;
			this.hitFront.y = 879.2;
			this.hitGrass = false;
			this.target.visible = true;
			this.startTime = getTimer();
			
			this.pausedTimerTime = -1;
			
			//tophit
			if(points == 0) {
				this.missionHandler.setBackHitRow(0);
				this.missionHandler.setTopHitRow(0);
				this.missionHandler.setFrontHitRow(0);
				this.missionHandler.setBounceBackRow(0);
				this.missionHandler.setDropLandTopRow(0);
			}
			else if(points == 6) {
				this.missionHandler.setTopHitRound(this.missionHandler.getTopHitRound() + 1);
				this.missionHandler.setTopHitRow(this.missionHandler.getTopHitRow() + 1);
				this.missionHandler.setTopHitSinceMission(this.missionHandler.getTopHitSinceMission() + 1);
				//no more row for others
				this.missionHandler.setBackHitRow(0);
				this.missionHandler.setFrontHitRow(0);
				this.missionHandler.setBounceBackRow(0);
			}
			else if(points == 5) {
				this.missionHandler.setBackHitRound(this.missionHandler.getBackHitRound() + 1);
				this.missionHandler.setBackHitRow(this.missionHandler.getBackHitRow() + 1);
				this.missionHandler.setBackHitSinceMission(this.missionHandler.getBackHitSinceMission() + 1);
				//no more row for others
				this.missionHandler.setTopHitRow(0);
				this.missionHandler.setFrontHitRow(0);
				
				if(this.bouncedOffTop) {
					this.missionHandler.setBounceBackRound(this.missionHandler.getBounceBackRound() + 1);
					this.missionHandler.setBounceBackRow(this.missionHandler.getBounceBackRow() + 1);
					this.missionHandler.setBounceBackSinceMission(this.missionHandler.getBounceBackSinceMission() + 1);
					this.bouncedOffTop = false;
				}
				else {
					this.missionHandler.setBounceBackRow(0);
				}
			}
			else if(points == 7) {
				this.missionHandler.setFrontHitRound(this.missionHandler.getFrontHitRound() + 1);
				this.missionHandler.setFrontHitRow(this.missionHandler.getFrontHitRow() + 1);
				this.missionHandler.setFrontHitSinceMission(this.missionHandler.getFrontHitSinceMission() + 1);
				//no more row for others
				this.missionHandler.setBackHitRow(0);
				this.missionHandler.setTopHitRow(0);
				this.missionHandler.setBounceBackRow(0);
			}
			
			var bonusMultiplier:Number = 0;
			if(dropHeight <= 95.1 && points != 0) {
				bonusMultiplier = 3;
				this.missionHandler.setDropLandTopRound(this.missionHandler.getDropLandTopRound() + 1);
				this.missionHandler.setDropLandTopRow(this.missionHandler.getDropLandTopRow() + 1);
				this.missionHandler.setDropLandTopSinceMission(this.missionHandler.getDropLandTopSinceMission() + 1);
			}
			else if(dropHeight <=212.1) {
				bonusMultiplier = 2;
				this.missionHandler.setDropLandTopRow(0);
			}
			else {
				bonusMultiplier = 1;
				this.missionHandler.setDropLandTopRow(0);
			}
			
			var totalScore:Number = Math.round(points * bonusMultiplier) * multiplier;
			this.scoreKeeper.setScore(this.scoreKeeper.getScore() + totalScore);
			this.missionHandler.setScoreRound(this.missionHandler.getScoreRound() + totalScore);
			this.missionHandler.setScoreSinceMission(this.missionHandler.getScoreSinceMission() + totalScore);
			
			if(this.scoreKeeper.getScore() > this.permy.getHiScore()) {
				if(this.permy.getMute() == false && !this.gotHiScore) {
					if(this.permy.getHiScore() != 0) {
						var missionSound:Sound = new MissionComplete();
						missionSound.play();
					}
				}
				this.gotHiScore = true;
				this.permy.setHiScore(this.scoreKeeper.getScore());
			}
			this.scoreKeeper.setHiScoreField(this.permy.getHiScore());
			
			this.target.x = 293.75;
			this.target.y = 30.9;
			this.fallSpeed = 0;
			removeEventListeners();
			this.touchArea.addEventListener(MouseEvent.CLICK,startFall);
			
			if(this.player.getDirection() == "Left") {
				this.hitTruck.x = this.player.getTruck().x - 5 - this.hitTruck.width;
			}
			
			if(points > 0) {
				if(this.timerTime > 3000) {
					this.timerTime = this.timerTime - 500;
				}
				if(this.player.getSpeed() < 12) {
					this.player.setSpeed(this.player.getSpeed() + 0.5);
				}
			}
			
			var shouldIReset:Number = Math.floor(Math.random() * 5);
			if(shouldIReset == 0) {
				this.powerup.allSpawn();
			}
			if(points > 0) {
				this.player.quack();
			}
			this.timer.removeEventListener(TimerEvent.TIMER,autoDrop);
			this.timer.stop();
			this.timer = new Timer(timerTime,1);
			this.target.addEventListener(Event.ENTER_FRAME,keepTimeUpdated);
			this.timer.addEventListener(TimerEvent.TIMER,autoDrop);
			this.timer.start();
			this.target.insideHay.rotation = 0;
			trace(this.powerup.getStoppedTruckTimer());
			if(this.powerup.getStoppedTruckTimer() <= 0) {
				this.player.startMoving();
			}
		}
		
		public function getTarget():MovieClip {
			return this.target;
		}
		
		public function lose() {
			//endGame.viewLeaderBoardButton.addEventListener(Event.ENTER_FRAME,viewLeaderBoardFadeOut2);
			//endGame.viewLeaderBoardButton.addEventListener(Event.ENTER_FRAME,viewLeaderBoardFadeIn2);
			this.acheivementsCheck();
			this.permy.addScoreQueue(this.scoreKeeper.getScore());
			this.submitScore();
			if(this.permy.getMute() == false) {
				var dieSound:Sound = new Lose();
				dieSound.play();
			}
			this.gotHiScore = false;
			this.fadeTimer.addEventListener(TimerEvent.TIMER,fadeSound);
			this.fadeTimer.start();
			this.powerup.removeTimers();
			this.missionHandler.resetRound();
			this.player.stopMoving();
			this.player.moveTruckToStart();
			this.endGame.alpha = 0;
			this.endGame.y = 175;
			this.endGame.x = 320;
			this.endGame.addEventListener(Event.ENTER_FRAME,fadeIn);
			this.powerup.fadeOut();
			this.coin.fadeOut();
			this.endGame.playButton.addEventListener(MouseEvent.CLICK,fadeOutStart);
			endGame.storeIcon.addEventListener(MouseEvent.CLICK,openStore);
			this.target.addEventListener(Event.ENTER_FRAME,scoreStuffIn);
			removeEventListeners();
			this.target.addEventListener(Event.ENTER_FRAME,hayFadeOut);
		}
		
		public function scoreStuffIn(event:Event) {
			if(this.scoreMoveSpeed > 0) {
				this.coin.getCoinField().x = this.coin.getCoinField().x + scoreMoveSpeed*1.1;
				this.scoreKeeper.getHiScoreField().x = this.scoreKeeper.getHiScoreField().x + scoreMoveSpeed*.85;
				this.scoreKeeper.getScoreField().x = this.scoreKeeper.getScoreField().x + scoreMoveSpeed*1.1;
				this.coin.getTotalCoinsField().x = this.coin.getTotalCoinsField().x + scoreMoveSpeed*.85;
				this.scoreLabel.x += scoreMoveSpeed*1.1; 
				this.hiScoreLabel.x += scoreMoveSpeed*.85;
				this.coinsLabel.x += scoreMoveSpeed*1.1;
				this.totalCoinsLabel.x += scoreMoveSpeed*.85;
				scoreMoveSpeed --;
			}
			else {
				scoreMoveSpeed = 0;
				this.target.removeEventListener(Event.ENTER_FRAME,scoreStuffIn);
			}
		}
		
		public function getPaused():Boolean {
			return this.paused;
		}
		
		public function scoreStuffOut(event:Event) {
			this.target.removeEventListener(Event.ENTER_FRAME,scoreStuffIn);
			if(this.scoreMoveSpeed < 20) {
				this.coin.getCoinField().x = this.coin.getCoinField().x - scoreMoveSpeed*1.1;
				this.scoreKeeper.getHiScoreField().x = this.scoreKeeper.getHiScoreField().x - scoreMoveSpeed*.85;
				this.scoreKeeper.getScoreField().x = this.scoreKeeper.getScoreField().x - scoreMoveSpeed*1.1;
				this.coin.getTotalCoinsField().x = this.coin.getTotalCoinsField().x - scoreMoveSpeed*.85;
				this.scoreLabel.x -= scoreMoveSpeed*1.1; 
				this.hiScoreLabel.x -= scoreMoveSpeed*.85;
				this.coinsLabel.x -= scoreMoveSpeed*1.1;
				this.totalCoinsLabel.x -= scoreMoveSpeed*.85;
				scoreMoveSpeed ++;
			}
			else {
				scoreMoveSpeed = 20;
				this.coin.getCoinField().x = 84;
				this.scoreKeeper.getHiScoreField().x = 140.05;
				this.scoreKeeper.getScoreField().x = 84.1;
				this.coin.getTotalCoinsField().x = 140.05;
				this.scoreLabel.x = -127.95; 
				this.hiScoreLabel.x = -72;
				this.coinsLabel.x = -128.05;
				this.totalCoinsLabel.x = -72;
				this.target.removeEventListener(Event.ENTER_FRAME,scoreStuffOut);
			}
		}
		
		public function hayFadeOut(event:Event) {
			if(this.target.alpha > 0) {
				this.target.alpha = this.target.alpha - 0.05;
			}
			else {
				this.target.removeEventListener(Event.ENTER_FRAME,hayFadeOut);
			}
		}
		
		public function fadeIn(event:Event) {
			if(endGame.alpha < 1) {
				endGame.alpha = endGame.alpha + 0.05;
				this.tiers.alpha -= .05;
				this.x3.alpha -= .05;
				this.x2.alpha -= .05;
				this.x1.alpha -= .05;
				this.speedometer.alpha -= .05;
				this.pauseButton.alpha -= .05;
				this.timeLabel.alpha -= .05;
				this.timeField.alpha -= .05;
			}
			else {
				endGame.alpha = 1;
				this.tiers.alpha = 0;
				this.x3.alpha = 0;
				this.x2.alpha = 0;
				this.x1.alpha = 0;
				this.speedometer.alpha = 0;
				this.pauseButton.alpha = 0;
				this.timeLabel.alpha = 0;
				this.timeField.alpha = 0;
				endGame.removeEventListener(Event.ENTER_FRAME,fadeIn);
			}
		}
		public function fadeOut(event:Event) {
			if(endGame.alpha > 0) {
				endGame.alpha = endGame.alpha - 0.05;
				this.tiers.alpha += .05;
				this.x3.alpha += .05;
				this.x2.alpha += .05;
				this.x1.alpha += .05;
				this.speedometer.alpha += .05;
				this.pauseButton.alpha += .05;
				this.timeLabel.alpha += .05;
				this.timeField.alpha += .05;
			}
			else {
				this.tiers.alpha = 1;
				this.x3.alpha = 1;
				this.x2.alpha = 1;
				this.x1.alpha = 1;
				this.speedometer.alpha = 1;
				this.pauseButton.alpha = 1;
				this.timeLabel.alpha = 1;
				this.timeField.alpha = 1;
				trace(x3.alpha);
				endGame.alpha = 0;
				this.endGame.y = 2750;
				this.endGame.x = 320;
				this.reset();
				endGame.removeEventListener(Event.ENTER_FRAME,fadeOut);
			}
		}
		
		public function tutTapFadeOut(event:Event) {
			if(tutTap.alpha > 0) {
				tutTap.alpha -= 0.05;
			}
			else if(tutTap.alpha <= 0) {
				tutTap.visible = false;
				this.target.removeEventListener(Event.ENTER_FRAME,tutTapFadeOut);
			}
		}
		
		public function fadeOutStart(event:MouseEvent) {
			//endGame.viewLeaderBoardButton.removeEventListener(Event.ENTER_FRAME,viewLeaderBoardFadeOut2);
			//endGame.viewLeaderBoardButton.removeEventListener(Event.ENTER_FRAME,viewLeaderBoardFadeIn2);
			this.mainSound.stop();
			this.fadeTimer.stop();
			var transitionSound:Sound = new Transition();
			if(permy.getMute() == false) {
				transitionSound.play();
			}
			endGame.storeIcon.removeEventListener(MouseEvent.CLICK,openStore);
			endGame.removeEventListener(Event.ENTER_FRAME,fadeIn);
			endGame.addEventListener(Event.ENTER_FRAME,fadeOut);
			this.target.addEventListener(Event.ENTER_FRAME,scoreStuffOut);
			this.player.setSpeed(5);
			this.player.setRandomExtra();
			this.player.stopMoving();
			this.scoreKeeper.setScore(0);
			this.player.reset();
			this.player.resetSpeedometer();
			this.scoreKeeper.setTimeField(10);
			this.scoreKeeper.setScoreField(0);
			this.coin.setCoinField(0);
			this.powerup.removeTimers();
			this.powerup.allSpawn();
			coin.reset();
			this.endGame.playButton.removeEventListener(MouseEvent.CLICK,fadeOutStart);
		}
		
		function fadeInSound(event:Event) {
			if(permy.getMute() == false) {
				var vol:Number = mainSound.soundTransform.volume;
				var soundT:SoundTransform = mainSound.soundTransform;
				vol = vol + 0.025;
				soundT.volume = vol;
				if(vol < 0.4) {
					mainSound.soundTransform = soundT; 
				}
				else {
					this.fadeInTimer.removeEventListener(TimerEvent.TIMER,fadeInSound);
					fadeInTimer.stop();
				}
			}
			else {
				mainSound.stop();
				fadeInTimer.removeEventListener(TimerEvent.TIMER,fadeInSound);
				fadeInTimer.stop();
			}
		}
		
		public function reset() {
			mainSoundSound = new Music();
			var volumeSetter:SoundTransform = new SoundTransform(0.0);
			fadeInTimer = new Timer(60);
			mainSound = mainSoundSound.play(0,999, volumeSetter);
				//if come to end, also for restarting after new soundPosition
				fadeInTimer.addEventListener(TimerEvent.TIMER,fadeInSound);
			if(permy.getMute() == false) {

				fadeInTimer.start();
			}
			
			endGame.removeEventListener(Event.ENTER_FRAME,fadeOut);
			this.target.alpha = 1;
			this.target.removeEventListener(Event.ENTER_FRAME,hayFadeOut);
			this.hitGrass = false;
			this.touchArea.addEventListener(MouseEvent.MOUSE_DOWN,startMoveBail);
			this.hitTruck.y = 902.2;
			this.hitFront.y = 879.2;
			this.target.visible = true;
			this.startTime = getTimer();
			this.scoreKeeper.setScore(0);
			this.target.x = 293.75;
			this.target.y = 30.9;
			this.fallSpeed = 0;
			this.player.stopMoving();
			
			this.missionHandler.resetRound();
			this.missionHandler.setGamesSinceMission(this.missionHandler.getGamesSinceMission() + 1);
			
			this.pausedTimerTime = -1;
			
			this.touchArea.addEventListener(MouseEvent.CLICK,startFall);
			
			this.timerTime = 10000;
			
			this.timer = new Timer(timerTime,1);
			this.target.addEventListener(Event.ENTER_FRAME,keepTimeUpdated);
			this.timer.addEventListener(TimerEvent.TIMER,autoDrop);
			this.timer.start();
			this.target.insideHay.rotation = 0;
			this.player.reset();
			this.player.startMoving();
		}
		
		public function removeEventListeners() {
			this.hitFrontAlready = false;
			this.touchArea.removeEventListener(Event.ENTER_FRAME,fall);
			this.target.removeEventListener(Event.ENTER_FRAME,bounceOffLeft);
			this.target.removeEventListener(Event.ENTER_FRAME,bounceOffRight);
			this.target.removeEventListener(Event.ENTER_FRAME,rotateAround);
		}
		
		public function setPaused() {
			if(this.paused == false) {
				this.paused = true;
				this.pauseSoundPos = mainSound.position;
				mainSound.stop();
			}
			else {
				this.paused = false;
				if(this.permy.getMute() == false) {
					mainSound = mainSoundSound.play(this.pauseSoundPos,1,new SoundTransform(0.4));
					mainSound.addEventListener(Event.SOUND_COMPLETE,restartSoundFromBeginning);
				}
			}
		}
		
		public function setStore(store:Store) {
			this.store = store;
		}
		
		/*function openStore(event:MouseEvent) {
			storeMovie.x = 10;
			storeMovie.y = 95;
			if(endGame.alpha >= 0) {
				if(this.closeStoreOk) {
					endGame.storeIcon.play();
				}
				//open
				if(endGame.storeIcon.currentFrame == 1) {
					if(moveSpeedF1 < 14) {
						moveSpeedF1 = moveSpeedF1 - 1;
					}
					this.endGame.playButton.removeEventListener(MouseEvent.CLICK,fadeOutStart);
					storeMovie.addEventListener(Event.ENTER_FRAME,storeExpand);
					storeMovie.removeEventListener(Event.ENTER_FRAME,storeContract);
				}
				//close
				else if(endGame.storeIcon.currentFrame == 2) {
					if(this.closeStoreOk) {
						this.coin.setTotalCoinsField(this.permy.getTotalCoins());
						this.store.goBackToStoreFunction();
						this.store.fadeAll();
						this.store.removeOtherEventListeners();
						this.store.removeBuyEventListeners();
						this.store.setEquipIndication();
						this.store.updateMain();
						if(moveSpeedF1 > 0) {
							moveSpeedF1 = moveSpeedF1 + 1;
						}
						this.endGame.playButton.addEventListener(MouseEvent.CLICK,fadeOutStart);
						storeMovie.removeEventListener(Event.ENTER_FRAME,storeExpand);
						storeMovie.addEventListener(Event.ENTER_FRAME,storeContract);
					}
				}
			}
		}*/
		
		function storeExpand(event:Event) {
			if(storeMovie.scaleX < 0.99999) {
				storeMovie.scaleX = storeMovie.scaleX + (moveSpeedF1/1.05)/100;
				storeMovie.scaleY = storeMovie.scaleY + (moveSpeedF1/1.05)/100;
				if(moveSpeedF1 > 0) {
					moveSpeedF1 = moveSpeedF1 - 1;
				}
			}
			else {
				storeMovie.scaleX = 1;
				storeMovie.scaleY = 1;
				storeMovie.removeEventListener(Event.ENTER_FRAME,storeExpand);
			}
		}
		function storeContract(event:Event) {
			if(storeMovie.scaleX > 0) {
				storeMovie.scaleX = storeMovie.scaleX - (moveSpeedF1/1.05)/100;
				storeMovie.scaleY = storeMovie.scaleY - (moveSpeedF1/1.05)/100;
				if(moveSpeedF1 < 14) {
					moveSpeedF1 = moveSpeedF1 + 1;
				}
			}
			else {
				storeMovie.scaleX = 0;
				storeMovie.scaleY = 0;
				storeMovie.removeEventListener(Event.ENTER_FRAME,storeContract);
			}
		}
		
		/*public function setFadeIn(fade:Function) {
			this.viewLeaderBoardFadeIn2 = fade;
		}
		
		public function setFadeOut(fade:Function) {
			this.viewLeaderBoardFadeOut2 = fade;
		}*/
		
		public function setOpenStore( openStore:Function ) {
			this.openStore = openStore;
		}
	}
}