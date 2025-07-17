package  {
	import flash.display.MovieClip;
	import flash.text.TextField;
	import flash.events.Event;
	import flash.media.Sound;
	
	public class MissionHandler {
		private var coinsRound:Number;
		private var coinsSinceMission:Number;
		
		private var gamesSinceMission:Number;
		
		private var scoreRound:Number;
		private var scoreSinceMission:Number;
		
		private var topHitRound:Number;
		private var topHitRow:Number;
		private var topHitSinceMission:Number;
		
		private var backHitRound:Number;
		private var backHitRow:Number;
		private var backHitSinceMission:Number;
		
		private var frontHitRound:Number;
		private var frontHitRow:Number;
		private var frontHitSinceMission:Number;

		private var dropLandTopRound:Number;
		private var dropLandTopRow:Number;
		private var dropLandTopSinceMission:Number;
		
		private var bounceBackRound:Number;
		private var bounceBackRow:Number;
		private var bounceBackSinceMission:Number;
		
		private var missionLevel:Number;
		
		private var mission:Number;
		private var missionName:String;
		
		private var displayBox:TextField;
		private var currentBox:TextField;
		private var needBox:TextField;
		private var levelBox:TextField;
		private var slashBox:TextField;
		
		private var target:MovieClip;
		private var coin:Coin;
		
		private var levelLabel:TextField;
		
		private var permy:Permy;

		public function MissionHandler(permy:Permy) {
			resetAll();
			this.missionLevel = 1;
			this.mission = -1;
			this.permy = permy;
			newMission();
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
		
		public function setTarget(target:MovieClip,coin:Coin) {
			this.target = target;
			this.coin = coin;
			this.target.alpha = 0;
			this.target.addEventListener(Event.ENTER_FRAME,listen);
		}
		
		public function getTarget():MovieClip {
			return this.target;
		}
		
		public function newMission() {
			var oldMission:Number = this.mission;
			while(this.mission == oldMission) {
				this.mission = Math.floor(Math.random() * 20) + 1;
			}
			setMission(this.mission);
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
		public function getGamesSinceMission():Number {
			return this.gamesSinceMission;
		}
		public function setGamesSinceMission(u:Number) {
			this.gamesSinceMission = u;
		}
		public function getTopHitRow():Number {
			return this.topHitRow;
		}
		public function setTopHitRow(u:Number) {
			this.topHitRow = u;
		}
		public function getTopHitRound():Number {
			return this.topHitRound;
		}
		public function setTopHitRound(u:Number) {
			this.topHitRound = u;
		}
		public function getTopHitSinceMission():Number {
			return this.topHitSinceMission;
		}
		public function setTopHitSinceMission(u:Number) {
			this.topHitSinceMission = u;
		
		}
		public function getFrontHitRow():Number {
			return this.frontHitRow;
		}
		public function setFrontHitRow(u:Number) {
			this.frontHitRow = u;
		}
		public function getFrontHitRound():Number {
			return this.frontHitRound;
		}
		public function setFrontHitRound(u:Number) {
			this.frontHitRound = u;
		}
		public function getFrontHitSinceMission():Number {
			return this.frontHitSinceMission;
		}
		public function setFrontHitSinceMission(u:Number) {
			this.frontHitSinceMission = u;
		
		}
		public function getBackHitRow():Number {
			return this.backHitRow;
		}
		public function setBackHitRow(u:Number) {
			this.backHitRow = u;
		}
		public function getBackHitRound():Number {
			return this.backHitRound;
		}
		public function setBackHitRound(u:Number) {
			this.backHitRound = u;
		}
		public function getBackHitSinceMission():Number {
			return this.backHitSinceMission;
		}
		public function setBackHitSinceMission(u:Number) {
			this.backHitSinceMission = u;
		}
		public function getBounceBackRow():Number {
			return this.bounceBackRow;
		}
		public function setBounceBackRow(u:Number) {
			this.bounceBackRow = u;
		}
		public function getBounceBackRound():Number {
			return this.bounceBackRound;
		}
		public function setBounceBackRound(u:Number) {
			this.bounceBackRound = u;
		}
		public function getBounceBackSinceMission():Number {
			return this.bounceBackSinceMission;
		}
		public function setBounceBackSinceMission(u:Number) {
			this.bounceBackSinceMission = u;
		}
		public function getDropLandTopRow():Number {
			return this.dropLandTopRow;
		}
		public function setDropLandTopRow(u:Number) {
			this.dropLandTopRow = u;
		}
		public function getDropLandTopRound():Number {
			return this.dropLandTopRound;
		}
		public function setDropLandTopRound(u:Number) {
			this.dropLandTopRound = u;
		}
		public function getDropLandTopSinceMission():Number {
			return this.dropLandTopSinceMission;
		}
		public function setDropLandTopSinceMission(u:Number) {
			this.dropLandTopSinceMission = u;
		}
		
		public function setMission(mission:Number) {
			this.mission = mission;
			//coinsRound
			if(this.mission == 1) {
				//LISTENING VAR
				this.coinsRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Collect 50 coins in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Collect 100 coins in one round";
				}
				else {
					this.missionName = "Collect 150 coins in one round";
				}
			}
			//scoreRound
			else if(this.mission == 2) {
				//LISTENING VAR
				this.scoreRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Score 100 in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Score 200 in one round";
				}
				else {
					this.missionName = "Score 300 in one round";
				}
			}
			//coinsMission
			else if(this.mission == 3) {
				//LISTENING VAR
				this.coinsSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Collect 500 coins";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Collect 1,000 coins";
				}
				else {
					this.missionName = "Collect 1,500 coins";
				}
			}
			//scoreMission
			else if(this.mission == 4) {
				//LISTENING VAR
				this.scoreSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Score 1000 points";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Score 2000 points";
				}
				else {
					this.missionName = "Score 3000 points";
				}
			}
			//games
			else if(this.mission == 5) {
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
			//topHitRound
			else if(this.mission == 6) {
				//LISTENING VAR
				this.topHitRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the top of the truck 4 times in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the top of the truck 6 times in one round";
				}
				else {
					this.missionName = "Land on the top of the truck 8 times in one round";
				}
			}
			//topHitRow
			else if(this.mission == 7) {
				//LISTENING VAR
				this.topHitRow = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the top of the truck 3 times in a row";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the top of the truck 5 times in a row";
				}
				else {
					this.missionName = "Land on the top of the truck 7 times in a row";
				}
			}
			//topHitMission
			else if(this.mission == 8) {
				//LISTENING VAR
				this.topHitSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the top of the truck 15 times";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the top of the truck 25 times";
				}
				else {
					this.missionName = "Land on the top of the truck 35 times";
				}
			}
			//backHitRound
			else if(this.mission == 9) {
				//LISTENING VAR
				this.backHitRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the back of the truck 6 times in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the back of the truck 9 times in one round";
				}
				else {
					this.missionName = "Land on the back of the truck 12 times in one round";
				}
			}
			//backHitRow
			else if(this.mission == 10) {
				//LISTENING VAR
				this.backHitRow = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the back of the truck 4 times in a row";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the back of the truck 6 times in a row";
				}
				else {
					this.missionName = "Land on the back of the truck 8 times in a row";
				}
			}
			//backHitMission
			else if(this.mission == 11) {
				//LISTENING VAR
				this.backHitSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the back of the truck 25 times";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the back of the truck 35 times";
				}
				else {
					this.missionName = "Land on the back of the truck 45 times";
				}
			}
			//frontHitRound
			else if(this.mission == 12) {
				//LISTENING VAR
				this.frontHitRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the front of the truck 3 times in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the front of the truck 5 times in one round";
				}
				else {
					this.missionName = "Land on the front of the truck 7 times in one round";
				}
			}
			//frontHitRow
			else if(this.mission == 13) {
				//LISTENING VAR
				this.frontHitRow = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the front of the truck 2 times in a row";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the front of the truck 3 times in a row";
				}
				else {
					this.missionName = "Land on the front of the truck 4 times in a row";
				}
			}
			//frontHitMission
			else if(this.mission == 14) {
				//LISTENING VAR
				this.frontHitSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the front of the truck 10 times";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the front of the truck 20 times";
				}
				else {
					this.missionName = "Land on the front of the truck 30 times";
				}
			}
			//bounceBackRound
			else if(this.mission == 15) {
				//LISTENING VAR
				this.bounceBackRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 3 times in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 5 times in one round";
				}
				else {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 7 times in one round";
				}
			}
			//bounceBackRow
			else if(this.mission == 16) {
				//LISTENING VAR
				this.bounceBackRow = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 3 times in a row";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 4 times in a row";
				}
				else {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 5 times in a row";
				}
			}
			//bounceBackMission
			else if(this.mission == 17) {
				//LISTENING VAR
				this.bounceBackSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 15 times";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 25 times";
				}
				else {
					this.missionName = "Ricochet off the top of the truck into the back of the truck 35 times";
				}
			}
			//dropLandTopHitRound
			else if(this.mission == 18) {
				//LISTENING VAR
				this.dropLandTopRound = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the truck after dropping from the x3 zone 5 times in one round";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the truck after dropping from the x3 zone 8 times in one round";
				}
				else {
					this.missionName = "Land on the truck after dropping from the x3 zone 11 times in one round";
				}
			}
			//dropLandTopHitRow
			else if(this.mission == 19) {
				//LISTENING VAR
				this.dropLandTopRow = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the truck after dropping from the x3 zone 4 times in a row";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the truck after dropping from the x3 zone 6 times in a row";
				}
				else {
					this.missionName = "Land on the truck after dropping from the x3 zone 8 times in a row";
				}
			}
			//dropLandTopHitMission
			else if(this.mission == 20) {
				//LISTENING VAR
				this.dropLandTopSinceMission = 0;
				//END LISTENING VAR
				if(this.missionLevel < 6) {
					this.missionName = "Land on the truck after dropping from the x3 zone 30 times";
				}
				else if(this.missionLevel < 11) {
					this.missionName = "Land on the truck after dropping from the x3 zone 40 times";
				}
				else {
					this.missionName = "Land on the truck after dropping from the x3 zone 50 times";
				}
			}
			
			if(this.displayBox != null) {
				if(this.permy.getMute() == false) {
					var missionSound:Sound = new MissionComplete();
					missionSound.play();
				}
				setDisplayBox(this.displayBox,this.currentBox,this.needBox,this.levelBox,this.slashBox,this.levelLabel);
			}
			resetAll();
		}
		
		public function listen(event:Event) {
			if(this.target.alpha > 0) {
				this.target.alpha = this.target.alpha - 0.05;
			}
			if(this.levelBox.text.length == 1) {
				this.levelLabel.x = 101+30-10;
			}
			else if(this.levelBox.text.length == 2) {
				this.levelLabel.x = 101+15-10;
			}
			else {
				this.levelLabel.x = 101-10;
			}
			if(this.currentBox.text.length == 1) {
				this.currentBox.width = 68 - 52;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width;
			}
			else if(this.currentBox.text.length == 2) {
				this.currentBox.width = 68 - 39;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width;
			}
			else if(this.currentBox.text.length == 3) {
				this.currentBox.width = 68 - 26;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width;
			}
			else if(this.currentBox.text.length == 4) {
				this.currentBox.width = 68 - 13;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width;
			}
			else {
				this.currentBox.width = 68;
				this.slashBox.x = this.currentBox.x + this.currentBox.width;
				this.needBox.x = this.slashBox.x + this.slashBox.width;
			}
			this.levelBox.text = this.missionLevel.toString();
			//collect coins
			if(this.mission == 1) {
				this.currentBox.text = this.coinsRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '50';
					if(this.coinsRound >= 50) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						//reward
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '100';
					if(this.coinsRound >= 100) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '150';
					if(this.coinsRound >= 150) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//score
			else if(this.mission == 2) {
				this.currentBox.text = this.scoreRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '100';
					if(this.scoreRound >= 100) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '200';
					if(this.scoreRound >= 200) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '300';
					if(this.scoreRound >= 300) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//coins total
			else if(this.mission == 3) {
				this.currentBox.text = this.coinsSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '500';
					if(this.coinsSinceMission >= 500) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '1000';
					if(this.coinsSinceMission >= 1000) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '1500';
					if(this.coinsSinceMission >= 1500) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//scoreTotal
			else if(this.mission == 4) {
				this.currentBox.text = this.scoreSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '1000';
					if(this.scoreSinceMission >= 1000) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '2000';
					if(this.scoreSinceMission >= 2000) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '3000';
					if(this.scoreSinceMission >= 3000) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//gamesTotal
			else if(this.mission == 5) {
				this.currentBox.text = this.gamesSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '5';
					if(this.gamesSinceMission >= 5) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '10';
					if(this.gamesSinceMission >= 10) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '15';
					if(this.gamesSinceMission >= 15) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//topHitRound
			else if(this.mission == 6) {
				this.currentBox.text = this.topHitRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '4';
					if(this.topHitRound >= 4) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '6';
					if(this.topHitRound >= 6) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '8';
					if(this.topHitRound >= 8) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//topHitRow
			else if(this.mission == 7) {
				this.currentBox.text = this.topHitRow.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '3';
					if(this.topHitRow >= 3) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '5';
					if(this.topHitRow >= 5) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '7';
					if(this.topHitRow >= 7) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//topHitMission
			else if(this.mission == 8) {
				this.currentBox.text = this.topHitSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '15';
					if(this.topHitSinceMission >= 15) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '25';
					if(this.topHitSinceMission >= 25) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '35';
					if(this.topHitSinceMission >= 35) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//backHitRound
			else if(this.mission == 9) {
				this.currentBox.text = this.backHitRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '6';
					if(this.backHitRound >= 6) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '9';
					if(this.backHitRound >= 9) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '12';
					if(this.backHitRound >= 12) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//backHitRow
			else if(this.mission == 10) {
				this.currentBox.text = this.backHitRow.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '4';
					if(this.backHitRow >= 4) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '6';
					if(this.backHitRow >= 6) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '8';
					if(this.backHitRow >= 8) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//backHitMission
			else if(this.mission == 11) {
				this.currentBox.text = this.backHitSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '25';
					if(this.backHitSinceMission >= 25) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '35';
					if(this.backHitSinceMission >= 35) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '45';
					if(this.backHitSinceMission >= 45) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//frontHitRound
			else if(this.mission == 12) {
				this.currentBox.text = this.frontHitRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '3';
					if(this.frontHitRound >= 3) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '5';
					if(this.frontHitRound >= 5) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '7';
					if(this.frontHitRound >= 7) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//frontHitRow
			else if(this.mission == 13) {
				this.currentBox.text = this.frontHitRow.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '2';
					if(this.frontHitRow >= 2) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '3';
					if(this.frontHitRow >= 3) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '4';
					if(this.frontHitRow >= 4) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//frontHitMission
			else if(this.mission == 14) {
				this.currentBox.text = this.frontHitSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '10';
					if(this.frontHitSinceMission >= 10) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '20';
					if(this.frontHitSinceMission >= 20) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '30';
					if(this.frontHitSinceMission >= 30) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//bounceBackRound
			else if(this.mission == 15) {
				this.currentBox.text = this.bounceBackRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '3';
					if(this.bounceBackRound >= 3) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '5';
					if(this.bounceBackRound >= 5) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '7';
					if(this.bounceBackRound >= 7) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//bounceBackRow
			else if(this.mission == 16) {
				this.currentBox.text = this.bounceBackRow.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '3';
					if(this.bounceBackRow >= 3) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '4';
					if(this.bounceBackRow >= 4) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '5';
					if(this.bounceBackRow >= 5) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//bounceBackMission
			else if(this.mission == 17) {
				this.currentBox.text = this.bounceBackSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '15';
					if(this.bounceBackSinceMission >= 15) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '25';
					if(this.bounceBackSinceMission >= 25) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '35';
					if(this.bounceBackSinceMission >= 35) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			
			//dropLandTopRound
			else if(this.mission == 18) {
				this.currentBox.text = this.dropLandTopRound.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '5';
					if(this.dropLandTopRound >= 5) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '8';
					if(this.dropLandTopRound >= 8) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '11';
					if(this.dropLandTopRound >= 11) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//dropLandTopRow
			else if(this.mission == 19) {
				this.currentBox.text = this.dropLandTopRow.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '4';
					if(this.dropLandTopRow >= 4) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '6';
					if(this.dropLandTopRow >= 6) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '8';
					if(this.dropLandTopRow >= 8) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			//dropLandTopMission
			else if(this.mission == 20) {
				this.currentBox.text = this.dropLandTopSinceMission.toString();
				if(this.missionLevel < 6) {
					this.needBox.text = '30';
					if(this.dropLandTopSinceMission >= 30) {
						this.missionLevel ++;
						this.coin.addCoins(250);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel < 11) {
					this.needBox.text = '40';
					if(this.dropLandTopSinceMission >= 40) {
						this.missionLevel ++;
						this.coin.addCoins(500);
						this.target.alpha = 1;
						newMission();
					}
				}
				else if(this.missionLevel >= 11) {
					this.needBox.text = '50';
					if(this.dropLandTopSinceMission >= 50) {
						this.missionLevel ++;
						this.coin.addCoins(750);
						this.target.alpha = 1;
						newMission();
					}
				}
			}
			
		}
		
		public function setDisplayBox(displayBox:TextField,currentBox:TextField,needBox:TextField,levelBox:TextField,slashBox:TextField,levelLabel:TextField) {
			this.displayBox = displayBox;
			this.currentBox = currentBox;
			this.needBox = needBox;
			this.levelBox = levelBox;
			this.slashBox = slashBox;
			this.levelLabel = levelLabel;
			this.displayBox.text = this.missionName;
		}
		
		public function resetAll() {
			this.coinsRound = 0;
			this.coinsSinceMission = 0;
			this.gamesSinceMission = 0;
			this.scoreRound = 0;
			this.scoreSinceMission = 0;
			this.topHitRound = 0;
			this.topHitRow = 0;
			this.topHitSinceMission = 0;
			this.backHitRound = 0;
			this.backHitRow = 0;
			this.backHitSinceMission = 0;
			this.frontHitRound = 0;
			this.frontHitRow = 0;
			this.frontHitSinceMission = 0;
			this.dropLandTopRound = 0;
			this.dropLandTopRow = 0;
			this.dropLandTopSinceMission = 0;
			this.bounceBackRound = 0;
			this.bounceBackRow = 0;
			this.bounceBackSinceMission = 0;
		}
		
		public function resetRound() {
			this.coinsRound = 0;
			this.scoreRound = 0;
			this.topHitRow = 0;
			this.topHitRound = 0;
			this.backHitRow = 0;
			this.backHitRound = 0;
			this.frontHitRow = 0;
			this.frontHitRound = 0;
			this.dropLandTopRow = 0;
			this.dropLandTopRound = 0;
			this.bounceBackRound = 0;
			this.bounceBackRow = 0;
		}
		
		public function resetRow() {
			this.topHitRow = 0;
			this.backHitRow = 0;
			this.frontHitRow = 0;
			this.dropLandTopRow = 0;
			this.bounceBackRow = 0;
		}

	}
	
}