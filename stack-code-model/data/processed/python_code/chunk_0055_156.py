package  {
	
	public class Permy {
		private var totalCoins:Number;
		private var hiScore:Number;
		private var mute:Boolean;
		private var boughtItems:Array;
		private var tutSeen:Boolean;
		private var tires:String;
		private var decal:String;
		private var color:String;
		private var coinMulti:Number;
		private var powerUpMulti:Number;
		
		private var userId:String;
		private var userName:String;
		private var scoreQueue:Array;
		
		private static var permy:Permy;
		
		public static function getPermy() {
			if( permy == null ) {
				permy = new Permy();
			}
			return permy;
		}
		
		public function Permy() {
			this.hiScore = 0;
			this.totalCoins = 0;
			this.mute = false;
			this.tutSeen = false;
			this.boughtItems = new Array();
			this.tires = "None";
			this.decal = "None";
			this.color = "None";
			this.coinMulti = 1;
			this.powerUpMulti = 1;
			this.scoreQueue = new Array();
			this.userId = null;
			this.userName = null;
		}
		
		public function getTutSeen():Boolean {
			return this.tutSeen;
		}
		
		public function setTutSeen(tutSeen:Boolean):void {
			this.tutSeen = tutSeen;
		}
		
		public function setTutSeenSave(tutSeen:Boolean):void {
			this.tutSeen = tutSeen;
		}
		
		public function getHiScore():Number {
			return this.hiScore;
		}
		
		public function getTotalCoins():Number {
			return this.totalCoins;
		}

		public function setHiScore(hiScore:Number):void {
			this.hiScore = hiScore;
		}
		
		public function setTotalCoins(totalCoins:Number):void {
			this.totalCoins = totalCoins;
		}
		
		public function getMute():Boolean {
			return this.mute;
		}
		
		public function setMute(mute:Boolean) {
			this.mute = mute;
		}
		
		public function getBoughtItems():Array {
			return this.boughtItems;
		}
		
		public function setBoughtItems(boughtItems:Array) {
			this.boughtItems = boughtItems;
		}
		
		public function addBoughtItem(item:String) {
			this.boughtItems.push(item);
		}

		public function getTires():String {
			return this.tires;
		}
		
		public function setTires(tires:String):void {
			this.tires = tires;
		}
		
		public function setColor(color:String):void {
			this.color = color;
		}
		
		public function getColor():String {
			return this.color;
		}
		
		public function getDecal():String {
			return this.decal;
		}
		
		public function setDecal(decal:String):void {
			this.decal = decal;
		}
		
		public function getPowerUpMulti():Number {
			return powerUpMulti;
		}
		
		public function setPowerUpMulti(powerUpMulti:Number):void {
			this.powerUpMulti = powerUpMulti;
		}
		
		public function getCoinMulti():Number {
			return coinMulti;
		}
		
		public function setCoinMulti(coinMulti:Number):void {
			this.coinMulti = coinMulti;
		}
		
		public function getUserId():String {
			return this.userId;
		}
		
		public function setUserId(userId:String):void {
			this.userId = userId;
		}
		
		public function getUserName():String {
			return this.userName;
		}
		
		public function setUserName(userName:String):void {
			this.userName = userName;
		}
		
		public function getScoreQueue():Array {
			return this.scoreQueue;
		}
		
		public function setScoreQueue(scoreQueue:Array):void {
			this.scoreQueue = scoreQueue;
		}
		
		public function addScoreQueue(score:Number):void {
			if( this.scoreQueue == null ) {
				this.scoreQueue = new Array();
			}
			this.scoreQueue.push(score);
		}

	}
	
}