package  {
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.text.TextField;
	import flash.media.Sound;
	import com.milkmangames.nativeextensions.ios.*; 
	import com.milkmangames.nativeextensions.ios.events.*; 
	
	
	public class MissionHandler {
		private var coinsRound:Number;
		private var coinsSinceMission:Number;
		private var jumpsRound:Number;
		private var jumpsSinceMission:Number;
		private var gamesSinceMission:Number;
		private var scoreRound:Number;
		private var scoreSinceMission:Number;
		
		private var missionLevel:Number;
		
		private var mission:Number;
		private var missionName:String;

		private var target:MovieClip;
		
		private var displayBox:TextField;
		private var currentBox:TextField;
		private var needBox:TextField;
		private var levelBox:TextField;
		private var slashBox:TextField;
		
		private var coin:Coin;
		
		private var permy:Permy;
		
		private var gameCenter:GameCenter;

		public function MissionHandler(permy:Permy,gameCenter:GameCenter) {
			resetAll();
			this.permy = permy;
			this.missionLevel =1;
			this.mission = -1;
			newMission();
			this.gameCenter = gameCenter;
		}
		
		public function getMissionLevel():Number {
			return this.missionLevel;
		}
		public function setMissionLevel(missionLevel:Number) {
			this.missionLevel = missionLevel;
		}
		public function getMission():Number {
			return this.mission;
		}
		public function setMission(mission:Number) {
			this.mission = mission;
			if(this.mission == 1) {
				//LISTENING VAR
				this.coinsRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Collect 100 coins in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Collect 200 coins in one round";
				}
				else {
					this.missionName = "Collect 300 coins in one round";
				}
			}
			else if(this.mission == 2) {
				//LISTENING VAR
				this.jumpsRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Jump 15 times in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Jump 20 times in one round";
				}
				else {
					this.missionName = "Jump 25 times in one round";
				}
			}
			else if(this.mission == 3) {
				//LISTENING VAR
				this.scoreRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Score 1,000 in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Score 2,000 in one round";
				}
				else {
					this.missionName = "Score 3,000 in one round";
				}
			}
			else if(this.mission == 4) {
				//LISTENING VAR
				this.coinsSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Collect 1,000 coins";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Collect 2,000 coins";
				}
				else {
					this.missionName = "Collect 3,000 coins";
				}
			}
			else if(this.mission == 5) {
				//LISTENING VAR
				this.jumpsSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Jump 50 times";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Jump 100 times";
				}
				else {
					this.missionName = "Jump 150 times";
				}
			}
			else if(this.mission == 6) {
				//LISTENING VAR
				this.scoreSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Score 10,000 points";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Score 20,000 points";
				}
				else {
					this.missionName = "Score 30,000 points";
				}
			}
			else if(this.mission == 7) {
				//LISTENING VAR
				this.gamesSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Play 5 games";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Play 10 games";
				}
				else {
					this.missionName = "Play 15 games";
				}
			}
			if(this.displayBox != null) {
				if(this.permy.getMute() == false) {
					var missionSound:Sound = new MissionComplete();
					missionSound.play();
				}
				setDisplayBox(this.displayBox,this.currentBox,this.needBox,this.levelBox,this.slashBox);
			}
			resetAll();
		}
		
		public function removeEventListeners():void {
			this.target.removeEventListener(Event.ENTER_FRAME,listen);
		}
		
		public function setTarget(target:MovieClip,coin:Coin) {
			this.target = target;
			this.coin = coin;
			this.target.alpha = 0;
			this.target.addEventListener(Event.ENTER_FRAME,listen);
		}
		
		public function setDisplayBox(displayBox:TextField,currentBox:TextField,needBox:TextField,levelBox:TextField,slashBox:TextField) {
			this.displayBox = displayBox;
			this.currentBox = currentBox;
			this.needBox = needBox;
			this.levelBox = levelBox;
			this.slashBox = slashBox;
			this.displayBox.text = this.missionName;
		}
		
		public function getTarget():MovieClip {
			return this.target;
		}
		
		public function listen(event:Event) {
			if(this.target.alpha > 0) {
				this.target.alpha = this.target.alpha - 0.05;
			}
			if(this.currentBox.text.length == 1) {
				this.currentBox.width = 108.4 - 80;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width + 10;
			}
			else if(this.currentBox.text.length == 2) {
				this.currentBox.width = 108.4 - 60;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width + 10;
			}
			else if(this.currentBox.text.length == 3) {
				this.currentBox.width = 108.4 - 40;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width + 10;
			}
			else if(this.currentBox.text.length == 4) {
				this.currentBox.width = 108.4 - 20;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width + 10;
			}
			else {
				this.currentBox.width = 108.4;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width + 10;
			}
			this.levelBox.text = this.missionLevel.toString();
			//collect coins
			if(this.mission == 1) {
				this.currentBox.text = this.coinsRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '100';
					if(this.coinsRound >= 100) {
						this.missionLevel ++;
						this.coin.addCoins(1000);
						this.target.alpha = 1;
						//reward
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '200';
					if(this.coinsRound >= 200) {
						this.missionLevel ++;
						this.coin.addCoins(2000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '300';
					if(this.coinsRound >= 300) {
						this.missionLevel ++;
						this.coin.addCoins(3000);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//collect jumps
			else if(this.mission == 2) {
				this.currentBox.text = this.jumpsRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '15';
					if(this.jumpsRound >= 15) {
						this.missionLevel ++;
						this.coin.addCoins(1000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '20';
					if(this.jumpsRound >= 20) {
						this.missionLevel ++;
						this.coin.addCoins(2000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '25';
					if(this.jumpsRound >= 25) {
						this.missionLevel ++;
						this.coin.addCoins(3000);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//score
			else if(this.mission == 3) {
				this.currentBox.text = this.scoreRound.toString();
				if(this.missionLevel < 6) {

					this.needBox.text = '1000';
					if(this.scoreRound >= 1000) {
						this.missionLevel ++;
						this.coin.addCoins(1000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '2000';
					if(this.scoreRound >= 2000) {
						this.missionLevel ++;
						this.coin.addCoins(2000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '3000';
					if(this.scoreRound >= 3000) {
						this.missionLevel ++;
						this.coin.addCoins(3000);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//coins total
			else if(this.mission == 4) {
				this.currentBox.text = this.coinsSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '1000';
					if(this.coinsSinceMission >= 1000) {
						this.missionLevel ++;
						this.coin.addCoins(1000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '2000';
					if(this.coinsSinceMission >= 2000) {
						this.missionLevel ++;
						this.coin.addCoins(2000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '3000';
					if(this.coinsSinceMission >= 3000) {
						this.missionLevel ++;
						this.coin.addCoins(3000);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//jumpsTotal
			else if(this.mission == 5) {
				this.currentBox.text = this.jumpsSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '50';
					if(this.jumpsSinceMission >= 50) {
						this.missionLevel ++;
						this.coin.addCoins(1000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '100';
					if(this.jumpsSinceMission >= 100) {
						this.missionLevel ++;
						this.coin.addCoins(2000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '150';
					if(this.jumpsSinceMission >= 150) {
						this.missionLevel ++;
						this.coin.addCoins(3000);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//scoreTotal
			else if(this.mission == 6) {
				this.currentBox.text = this.scoreSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '10000';
					if(this.scoreSinceMission >= 10000) {
						this.missionLevel ++;
						this.coin.addCoins(1000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '20000';
					if(this.scoreSinceMission >= 20000) {
						this.missionLevel ++;
						this.coin.addCoins(2000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '30000';
					if(this.scoreSinceMission >= 30000) {
						this.missionLevel ++;
						this.coin.addCoins(3000);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//gamesTotal
			else if(this.mission == 7) {
				this.currentBox.text = this.gamesSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '5';
					if(this.gamesSinceMission >= 5) {
						this.missionLevel ++;
						this.coin.addCoins(1000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '10';
					if(this.gamesSinceMission >= 10) {
						this.missionLevel ++;
						this.coin.addCoins(2000);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '15';
					if(this.gamesSinceMission >= 15) {
						this.missionLevel ++;
						this.coin.addCoins(3000);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
		}
		
		public function newMission() {
			var novicePercent:Number = this.missionLevel * 10;
			if(novicePercent > 100) {
				novicePercent = 100;
			}
			var proPercent:Number = this.missionLevel * 4;
			if(proPercent > 100) {
				proPercent = 100;
			}
			var masterPercent:Number = this.missionLevel * 2;
			if(masterPercent > 100) {
				masterPercent = 100;
			}
			//new mission means new level, so report to gamecenter
			GameCenter.gameCenter.reportAchievement("grp.levelNovice",novicePercent);
			GameCenter.gameCenter.reportAchievement("grp.levelPro",proPercent);
			GameCenter.gameCenter.reportAchievement("grp.levelMaster",masterPercent);
			//end report to gamecenter
			var oldMission:Number = this.mission;
			while(this.mission == oldMission) {
				this.mission = Math.floor(Math.random() * 7) + 1;
			}
			setMission(this.mission);
		}
	
		public function resetRound() {
			this.coinsRound = 0;
			this.jumpsRound = 0;
			this.scoreRound = 0;
		}
		
		public function resetAll() {
			this.coinsRound = 0;
			this.coinsSinceMission = 0;
			this.jumpsRound = 0;
			this.jumpsSinceMission = 0;
			this.gamesSinceMission = 0;
			this.scoreRound = 0;
			this.scoreSinceMission = 0;
		}
		
		public function getCoinsRound():Number {
			return this.coinsRound;
		}
		public function setCoinsRound(u:Number) {
			this.coinsRound = u;
		}
		public function getCoinsSinceMission():Number {
			return this.coinsSinceMission;
		}
		public function setCoinsSinceMission(u:Number) {
			this.coinsSinceMission = u;
		}
		
		public function getJumpsRound():Number {
			return this.jumpsRound;
		}
		public function setJumpsRound(u:Number) {
			this.jumpsRound = u;
		}
		public function getJumpsSinceMission():Number {
			return this.jumpsSinceMission;
		}
		public function setJumpsSinceMission(u:Number) {
			this.jumpsSinceMission = u;
		}
		
		public function getScoreRound():Number {
			return this.scoreRound;
		}
		public function setScoreRound(u:Number) {
			this.scoreRound = u;
		}
		public function getScoreSinceMission():Number {
			return this.scoreSinceMission;
		}
		public function setScoreSinceMission(u:Number) {
			this.scoreSinceMission = u;
		}
		
		public function getGamesSinceMission():Number {
			return this.gamesSinceMission;
		}
		public function setGamesSinceMission(u:Number) {
			this.gamesSinceMission = u;
		}
		
	}
	
}