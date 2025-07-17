package  {
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.media.Sound;
	
	public class Store {
		private var permy:Permy;
		private var storeButton:MovieClip;
		
		private var hat:MovieClip;
		private var accessory:MovieClip;
		
		private var boughtItems:Array;
		
		private var redCapBought:Boolean;
		private var topHatBought:Boolean;
		private var rainHatBought:Boolean;
		private var crownBought:Boolean;
		private var blueCapBought:Boolean;
		private var strawHatBought:Boolean;
		private var helmetBought:Boolean;
		private var pirateHatBought:Boolean;
		
		private var bowTieBought:Boolean;
		private var bandanaBought:Boolean;
		private var necklaceBought:Boolean;
		private var bellBought:Boolean;
		private var collarBought:Boolean;
		private var tieBought:Boolean;
		private var glassesBought:Boolean;
		private var eyepatchBought:Boolean;
		
		private var buySound:Sound;
		
		public function Store(permy:Permy,storeButton:MovieClip,hat:MovieClip,accessory:MovieClip) {
			this.permy = permy;
			this.storeButton = storeButton;
			this.hat = hat;
			this.accessory = accessory;
			
			this.buySound = new BuyItem();
			
			this.storeButton.coinsText.text = permy.getTotalCoins();
			
			this.storeButton.backButton.visible = false;
			this.storeButton.nextButton.addEventListener(MouseEvent.CLICK,nextStore);
			this.storeButton.backButton.addEventListener(MouseEvent.CLICK,backStore);
			
			this.storeButton.blueCapText.mouseEnabled = false;
			this.storeButton.redCapText.mouseEnabled = false;
			this.storeButton.topHatText.mouseEnabled = false;
			this.storeButton.rainHatText.mouseEnabled = false;
			this.storeButton.crownText.mouseEnabled = false;
			this.storeButton.strawHatText.mouseEnabled = false;
			this.storeButton.helmetText.mouseEnabled = false;
			this.storeButton.pirateHatText.mouseEnabled = false;
			this.storeButton.bowTieText.mouseEnabled = false;
			this.storeButton.bandanaText.mouseEnabled = false;
			this.storeButton.necklaceText.mouseEnabled = false;
			this.storeButton.bellText.mouseEnabled = false;
			this.storeButton.collarText.mouseEnabled = false;
			this.storeButton.tieText.mouseEnabled = false;
			this.storeButton.glassesText.mouseEnabled = false;
			this.storeButton.eyepatchText.mouseEnabled = false;
			
			this.storeButton.blueCapButton.visible = false;
			this.storeButton.blueCapText.visible = false;
			this.storeButton.strawHatButton.visible = false;
			this.storeButton.strawHatText.visible = false;
			this.storeButton.helmetButton.visible = false;
			this.storeButton.helmetText.visible = false;
			this.storeButton.pirateHatButton.visible = false;
			this.storeButton.pirateHatText.visible = false;
			
			this.storeButton.collarButton.visible = false;
			this.storeButton.collarText.visible = false;
			this.storeButton.tieButton.visible = false;
			this.storeButton.tieText.visible = false;
			this.storeButton.glassesButton.visible = false;
			this.storeButton.glassesText.visible = false;
			this.storeButton.eyepatchButton.visible = false;
			this.storeButton.eyepatchText.visible = false;
			
			this.storeButton.redCapButton.visible = true;
			this.storeButton.redCapText.visible = true;
			this.storeButton.topHatButton.visible = true;
			this.storeButton.topHatText.visible = true;
			this.storeButton.rainHatButton.visible = true;
			this.storeButton.rainHatText.visible = true;
			this.storeButton.crownButton.visible = true;
			this.storeButton.crownText.visible = true;
			
			this.storeButton.bowTieButton.visible = true;
			this.storeButton.bowTieText.visible = true;
			this.storeButton.bandanaButton.visible = true;
			this.storeButton.bandanaText.visible = true;
			this.storeButton.necklaceButton.visible = true;
			this.storeButton.necklaceText.visible = true;
			this.storeButton.bellButton.visible = true;
			this.storeButton.bellText.visible = true;
			
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			
			this.boughtItems = this.permy.getBoughtItems();
			
			storeButton.addEventListener(Event.ENTER_FRAME,lowerCash);
			
			//fade out all and set details to invisible
			this.fadeAll();
			
			//set colors
			for(var i:Number = 0;i < this.boughtItems.length;i++) {
				if(this.boughtItems[i] == "Red Cap") {
					this.storeButton.redCapButton.gotoAndStop(2);
					this.redCapBought = true;
				}
				if(this.boughtItems[i] == "Top Hat") {
					this.storeButton.topHatButton.gotoAndStop(2);
					this.topHatBought = true;
				}
				if(this.boughtItems[i] == "Rain Hat") {
					this.storeButton.rainHatButton.gotoAndStop(2);
					this.rainHatBought = true;
				}
				if(this.boughtItems[i] == "Crown") {
					this.storeButton.crownButton.gotoAndStop(2);
					this.crownBought = true;
				}
				if(this.boughtItems[i] == "Blue Cap") {
					this.storeButton.blueCapButton.gotoAndStop(2);
					this.blueCapBought = true;
				}
				if(this.boughtItems[i] == "Straw Hat") {
					this.storeButton.strawHatButton.gotoAndStop(2);
					this.strawHatBought = true;
				}
				if(this.boughtItems[i] == "Helmet") {
					this.storeButton.helmetButton.gotoAndStop(2);
					this.helmetBought = true;
				}
				if(this.boughtItems[i] == "Pirate Hat") {
					this.storeButton.pirateHatButton.gotoAndStop(2);
					this.pirateHatBought = true;
				}
				
				if(this.boughtItems[i] == "Bow Tie") {
					this.storeButton.bowTieButton.gotoAndStop(2);
					this.bowTieBought = true;
				}
				if(this.boughtItems[i] == "Bandana") {
					this.storeButton.bandanaButton.gotoAndStop(2);
					this.bandanaBought = true;
				}
				if(this.boughtItems[i] == "Necklace") {
					this.storeButton.necklaceButton.gotoAndStop(2);
					this.necklaceBought = true;
				}
				if(this.boughtItems[i] == "Bell") {
					this.storeButton.bellButton.gotoAndStop(2);
					this.bellBought = true;
				}
				if(this.boughtItems[i] == "Collar") {
					this.storeButton.collarButton.gotoAndStop(2);
					this.collarBought = true;
				}
				if(this.boughtItems[i] == "Tie") {
					this.storeButton.tieButton.gotoAndStop(2);
					this.tieBought = true;
				}
				if(this.boughtItems[i] == "Glasses") {
					this.storeButton.glassesButton.gotoAndStop(2);
					this.glassesBought = true;
				}
				if(this.boughtItems[i] == "Eyepatch") {
					this.storeButton.eyepatchButton.gotoAndStop(2);
					this.eyepatchBought = true;
				}
			}
			
			this.setEquipIndication();
			
			this.storeButton.redCapButton.addEventListener(MouseEvent.CLICK,redCapSetUp);
			this.storeButton.topHatButton.addEventListener(MouseEvent.CLICK,topHatSetUp);
			this.storeButton.rainHatButton.addEventListener(MouseEvent.CLICK,rainHatSetUp);
			this.storeButton.crownButton.addEventListener(MouseEvent.CLICK,crownSetUp);
			this.storeButton.blueCapButton.addEventListener(MouseEvent.CLICK,blueCapSetUp);
			this.storeButton.strawHatButton.addEventListener(MouseEvent.CLICK,strawHatSetUp);
			this.storeButton.helmetButton.addEventListener(MouseEvent.CLICK,helmetSetUp);
			this.storeButton.pirateHatButton.addEventListener(MouseEvent.CLICK,pirateHatSetUp);
			
			this.storeButton.bowTieButton.addEventListener(MouseEvent.CLICK,bowTieSetUp);
			this.storeButton.bandanaButton.addEventListener(MouseEvent.CLICK,bandanaSetUp);
			this.storeButton.necklaceButton.addEventListener(MouseEvent.CLICK,necklaceSetUp);
			this.storeButton.bellButton.addEventListener(MouseEvent.CLICK,bellSetUp);
			this.storeButton.collarButton.addEventListener(MouseEvent.CLICK,collarSetUp);
			this.storeButton.tieButton.addEventListener(MouseEvent.CLICK,tieSetUp);
			this.storeButton.glassesButton.addEventListener(MouseEvent.CLICK,glassesSetUp);
			this.storeButton.eyepatchButton.addEventListener(MouseEvent.CLICK,eyepatchSetUp);
		}
		
		public function nextStore(event:MouseEvent) {
			if(this.storeButton.nextButton.visible) {
				this.storeButton.nextButton.visible = false;
				this.storeButton.backButton.visible = true;
				
				this.storeButton.blueCapButton.y = this.storeButton.blueCapButton.y - 1000;
				this.storeButton.blueCapText.y = this.storeButton.blueCapText.y - 1000;
				this.storeButton.strawHatButton.y = this.storeButton.strawHatButton.y - 1000;
				this.storeButton.strawHatText.y = this.storeButton.strawHatText.y - 1000;
				this.storeButton.helmetButton.y = this.storeButton.helmetButton.y - 1000;
				this.storeButton.helmetText.y = this.storeButton.helmetText.y - 1000;
				this.storeButton.pirateHatButton.y = this.storeButton.pirateHatButton.y - 1000;
				this.storeButton.pirateHatText.y = this.storeButton.pirateHatText.y - 1000;
				
				this.storeButton.collarButton.y = this.storeButton.collarButton.y - 1000;
				this.storeButton.collarText.y = this.storeButton.collarText.y - 1000;
				this.storeButton.tieButton.y = this.storeButton.tieButton.y - 1000;
				this.storeButton.tieText.y = this.storeButton.tieText.y - 1000;
				this.storeButton.glassesButton.y = this.storeButton.glassesButton.y - 1000;
				this.storeButton.glassesText.y = this.storeButton.glassesText.y - 1000;
				this.storeButton.eyepatchButton.y = this.storeButton.eyepatchButton.y - 1000;
				this.storeButton.eyepatchText.y = this.storeButton.eyepatchText.y - 1000;
				
				this.storeButton.redCapButton.y = this.storeButton.redCapButton.y + 1000;
				this.storeButton.redCapText.y = this.storeButton.redCapText.y + 1000;
				this.storeButton.topHatButton.y = this.storeButton.topHatButton.y + 1000;
				this.storeButton.topHatText.y = this.storeButton.topHatText.y + 1000;
				this.storeButton.rainHatButton.y = this.storeButton.rainHatButton.y + 1000;
				this.storeButton.rainHatText.y = this.storeButton.rainHatText.y + 1000;
				this.storeButton.crownButton.y = this.storeButton.crownButton.y + 1000;
				this.storeButton.crownText.y = this.storeButton.crownText.y + 1000;
				
				this.storeButton.bowTieButton.y = this.storeButton.bowTieButton.y + 1000;
				this.storeButton.bowTieText.y = this.storeButton.bowTieText.y + 1000;
				this.storeButton.bandanaButton.y = this.storeButton.bandanaButton.y + 1000;
				this.storeButton.bandanaText.y = this.storeButton.bandanaText.y + 1000;
				this.storeButton.necklaceButton.y = this.storeButton.necklaceButton.y + 1000;
				this.storeButton.necklaceText.y = this.storeButton.necklaceText.y + 1000;
				this.storeButton.bellButton.y = this.storeButton.bellButton.y + 1000;
				this.storeButton.bellText.y = this.storeButton.bellText.y + 1000;
				
				this.storeButton.blueCapButton.visible = true;
				this.storeButton.blueCapText.visible = true;
				this.storeButton.strawHatButton.visible = true;
				this.storeButton.strawHatText.visible = true;
				this.storeButton.helmetButton.visible = true;
				this.storeButton.helmetText.visible = true;
				this.storeButton.pirateHatButton.visible = true;
				this.storeButton.pirateHatText.visible = true;
				
				this.storeButton.collarButton.visible = true;
				this.storeButton.collarText.visible = true;
				this.storeButton.tieButton.visible = true;
				this.storeButton.tieText.visible = true;
				this.storeButton.glassesButton.visible = true;
				this.storeButton.glassesText.visible = true;
				this.storeButton.eyepatchButton.visible = true;
				this.storeButton.eyepatchText.visible = true;
				
				this.storeButton.redCapButton.visible = false;
				this.storeButton.redCapText.visible = false;
				this.storeButton.topHatButton.visible = false;
				this.storeButton.topHatText.visible = false;
				this.storeButton.rainHatButton.visible = false;
				this.storeButton.rainHatText.visible = false;
				this.storeButton.crownButton.visible = false;
				this.storeButton.crownText.visible = false;
				
				this.storeButton.bowTieButton.visible = false;
				this.storeButton.bowTieText.visible = false;
				this.storeButton.bandanaButton.visible = false;
				this.storeButton.bandanaText.visible = false;
				this.storeButton.necklaceButton.visible = false;
				this.storeButton.necklaceText.visible = false;
				this.storeButton.bellButton.visible = false;
				this.storeButton.bellText.visible = false;
			}
		}
		
		public function backStore(event:MouseEvent) {
			if(this.storeButton.backButton.visible) {
				this.storeButton.backButton.visible = false;
				this.storeButton.nextButton.visible = true;
				
				this.storeButton.blueCapButton.y = this.storeButton.blueCapButton.y + 1000;
				this.storeButton.blueCapText.y = this.storeButton.blueCapText.y + 1000;
				this.storeButton.strawHatButton.y = this.storeButton.strawHatButton.y + 1000;
				this.storeButton.strawHatText.y = this.storeButton.strawHatText.y + 1000;
				this.storeButton.helmetButton.y = this.storeButton.helmetButton.y + 1000;
				this.storeButton.helmetText.y = this.storeButton.helmetText.y + 1000;
				this.storeButton.pirateHatButton.y = this.storeButton.pirateHatButton.y + 1000;
				this.storeButton.pirateHatText.y = this.storeButton.pirateHatText.y + 1000;
				
				this.storeButton.collarButton.y = this.storeButton.collarButton.y + 1000;
				this.storeButton.collarText.y = this.storeButton.collarText.y + 1000;
				this.storeButton.tieButton.y = this.storeButton.tieButton.y + 1000;
				this.storeButton.tieText.y = this.storeButton.tieText.y + 1000;
				this.storeButton.glassesButton.y = this.storeButton.glassesButton.y + 1000;
				this.storeButton.glassesText.y = this.storeButton.glassesText.y + 1000;
				this.storeButton.eyepatchButton.y = this.storeButton.eyepatchButton.y + 1000;
				this.storeButton.eyepatchText.y = this.storeButton.eyepatchText.y + 1000;
				
				this.storeButton.redCapButton.y = this.storeButton.redCapButton.y - 1000;
				this.storeButton.redCapText.y = this.storeButton.redCapText.y - 1000;
				this.storeButton.topHatButton.y = this.storeButton.topHatButton.y - 1000;
				this.storeButton.topHatText.y = this.storeButton.topHatText.y - 1000;
				this.storeButton.rainHatButton.y = this.storeButton.rainHatButton.y - 1000;
				this.storeButton.rainHatText.y = this.storeButton.rainHatText.y - 1000;
				this.storeButton.crownButton.y = this.storeButton.crownButton.y - 1000;
				this.storeButton.crownText.y = this.storeButton.crownText.y - 1000;
				
				this.storeButton.bowTieButton.y = this.storeButton.bowTieButton.y - 1000;
				this.storeButton.bowTieText.y = this.storeButton.bowTieText.y - 1000;
				this.storeButton.bandanaButton.y = this.storeButton.bandanaButton.y - 1000;
				this.storeButton.bandanaText.y = this.storeButton.bandanaText.y - 1000;
				this.storeButton.necklaceButton.y = this.storeButton.necklaceButton.y - 1000;
				this.storeButton.necklaceText.y = this.storeButton.necklaceText.y - 1000;
				this.storeButton.bellButton.y = this.storeButton.bellButton.y - 1000;
				this.storeButton.bellText.y = this.storeButton.bellText.y - 1000;
				
				this.storeButton.blueCapButton.visible = false;
				this.storeButton.blueCapText.visible = false;
				this.storeButton.strawHatButton.visible = false;
				this.storeButton.strawHatText.visible = false;
				this.storeButton.helmetButton.visible = false;
				this.storeButton.helmetText.visible = false;
				this.storeButton.pirateHatButton.visible = false;
				this.storeButton.pirateHatText.visible = false;
				
				this.storeButton.collarButton.visible = false;
				this.storeButton.collarText.visible = false;
				this.storeButton.tieButton.visible = false;
				this.storeButton.tieText.visible = false;
				this.storeButton.glassesButton.visible = false;
				this.storeButton.glassesText.visible = false;
				this.storeButton.eyepatchButton.visible = false;
				this.storeButton.eyepatchText.visible = false;
				
				this.storeButton.redCapButton.visible = true;
				this.storeButton.redCapText.visible = true;
				this.storeButton.topHatButton.visible = true;
				this.storeButton.topHatText.visible = true;
				this.storeButton.rainHatButton.visible = true;
				this.storeButton.rainHatText.visible = true;
				this.storeButton.crownButton.visible = true;
				this.storeButton.crownText.visible = true;
				
				this.storeButton.bowTieButton.visible = true;
				this.storeButton.bowTieText.visible = true;
				this.storeButton.bandanaButton.visible = true;
				this.storeButton.bandanaText.visible = true;
				this.storeButton.necklaceButton.visible = true;
				this.storeButton.necklaceText.visible = true;
				this.storeButton.bellButton.visible = true;
				this.storeButton.bellText.visible = true;
			}
		}
		
		//BEGIN HAT SETUPS
		public function redCapSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.redCapButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.hat.gotoAndStop("Red Cap");
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.priceTag.text = "";
			
			if(this.redCapBought && this.permy.getHat() != "Red Cap") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipHat);
			}
			else if(this.permy.getHat() == "Red Cap") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			}
			else {
				if(this.permy.getTotalCoins() >= 4000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "4,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyHat);
			}
			
			this.setEquipIndication();
		}
		
		public function topHatSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.topHatButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.hat.gotoAndStop("Top Hat");
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.priceTag.text = "";
			
			if(this.topHatBought && this.permy.getHat() != "Top Hat") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipHat);
			}
			else if(this.permy.getHat() == "Top Hat") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			}
			else {
				if(this.permy.getTotalCoins() >= 10000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "10,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyHat);
			}
			
			this.setEquipIndication();
		}
		
		public function rainHatSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.rainHatButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.hat.gotoAndStop("Rain Hat");
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.priceTag.text = "";
			
			if(this.rainHatBought && this.permy.getHat() != "Rain Hat") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipHat);
			}
			else if(this.permy.getHat() == "Rain Hat") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			}
			else {
				if(this.permy.getTotalCoins() >= 14000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "14,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyHat);
			}
			
			this.setEquipIndication();
		}
		
		public function crownSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.crownButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.hat.gotoAndStop("Crown");
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.priceTag.text = "";
			
			if(this.crownBought && this.permy.getHat() != "Crown") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipHat);
			}
			else if(this.permy.getHat() == "Crown") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			}
			else {
				if(this.permy.getTotalCoins() >= 100000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "100,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyHat);
			}
			
			this.setEquipIndication();
		}
		
		//Blue cap set up
		public function blueCapSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.blueCapButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.hat.gotoAndStop("Blue Cap");
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.priceTag.text = "";
			
			if(this.blueCapBought && this.permy.getHat() != "Blue Cap") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipHat);
			}
			else if(this.permy.getHat() == "Blue Cap") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			}
			else {
				if(this.permy.getTotalCoins() >= 6000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "6,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyHat);
			}
			
			this.setEquipIndication();
		}
		
		//straw hat setup
		public function strawHatSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.strawHatButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.hat.gotoAndStop("Straw Hat");
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.priceTag.text = "";
			
			if(this.strawHatBought && this.permy.getHat() != "Straw Hat") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipHat);
			}
			else if(this.permy.getHat() == "Straw Hat") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			}
			else {
				if(this.permy.getTotalCoins() >= 12000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "12,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyHat);
			}
			
			this.setEquipIndication();
		}
		
		//helmet setup
		public function helmetSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.helmetButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.hat.gotoAndStop("Helmet");
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.priceTag.text = "";
			
			if(this.helmetBought && this.permy.getHat() != "Helmet") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipHat);
			}
			else if(this.permy.getHat() == "Helmet") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			}
			else {
				if(this.permy.getTotalCoins() >= 35000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "35,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyHat);
			}
			
			this.setEquipIndication();
		}
		
		//pirate hat set up
		public function pirateHatSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.pirateHatButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.hat.gotoAndStop("Pirate Hat");
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.priceTag.text = "";
			
			if(this.pirateHatBought && this.permy.getHat() != "Pirate Hat") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipHat);
			}
			else if(this.permy.getHat() == "Pirate Hat") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			}
			else {
				if(this.permy.getTotalCoins() >= 75000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "75,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyHat);
			}
			
			this.setEquipIndication();
		}
		
		//END HAT SET UPS
		//BEGIN ACCESSORY SET UPS
		
		public function bowTieSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.bowTieButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.accessory.gotoAndStop("Bow Tie");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.priceTag.text = "";
			
			if(this.bowTieBought && this.permy.getAccessory() != "Bow Tie") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipAccessory);
			}
			else if(this.permy.getAccessory() == "Bow Tie") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			}
			else {
				if(this.permy.getTotalCoins() >= 2000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "2,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyAccessory);
			}
			
			this.setEquipIndication();
		}
		
		public function bandanaSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.bandanaButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.accessory.gotoAndStop("Bandana");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.priceTag.text = "";
			
			if(this.bandanaBought && this.permy.getAccessory() != "Bandana") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipAccessory);
			}
			else if(this.permy.getAccessory() == "Bandana") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			}
			else {
				if(this.permy.getTotalCoins() >= 9000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "9,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyAccessory);
			}
			
			this.setEquipIndication();
		}
		
		public function necklaceSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.necklaceButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.accessory.gotoAndStop("Necklace");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.priceTag.text = "";
			
			if(this.necklaceBought && this.permy.getAccessory() != "Necklace") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipAccessory);
			}
			else if(this.permy.getAccessory() == "Necklace") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			}
			else {
				if(this.permy.getTotalCoins() >= 24000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "24,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyAccessory);
			}
			
			this.setEquipIndication();
		}
		
		public function bellSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.bellButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.accessory.gotoAndStop("Bell");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.priceTag.text = "";
			
			if(this.bellBought && this.permy.getAccessory() != "Bell") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipAccessory);
			}
			else if(this.permy.getAccessory() == "Bell") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			}
			else {
				if(this.permy.getTotalCoins() >= 40000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "40,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyAccessory);
			}
			
			this.setEquipIndication();
		}
		
		public function collarSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.collarButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.accessory.gotoAndStop("Collar");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.priceTag.text = "";
			
			if(this.collarBought && this.permy.getAccessory() != "Collar") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipAccessory);
			}
			else if(this.permy.getAccessory() == "Collar") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			}
			else {
				if(this.permy.getTotalCoins() >= 4000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "4,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyAccessory);
			}
			
			this.setEquipIndication();
		}
		
		public function tieSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.tieButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.accessory.gotoAndStop("Tie");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.priceTag.text = "";
			
			if(this.tieBought && this.permy.getAccessory() != "Tie") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipAccessory);
			}
			else if(this.permy.getAccessory() == "Tie") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			}
			else {
				if(this.permy.getTotalCoins() >= 7000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "7,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyAccessory);
			}
			
			this.setEquipIndication();
		}
		
		public function glassesSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.glassesButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.accessory.gotoAndStop("Glasses");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.priceTag.text = "";
			
			if(this.glassesBought && this.permy.getAccessory() != "Glasses") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipAccessory);
			}
			else if(this.permy.getAccessory() == "Glasses") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			}
			else {
				if(this.permy.getTotalCoins() >= 15000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "15,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyAccessory);
			}
			
			this.setEquipIndication();
		}
		
		public function eyepatchSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.eyepatchButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.storeButton.accessory.gotoAndStop("Eyepatch");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.priceTag.text = "";
			
			if(this.eyepatchBought && this.permy.getAccessory() != "Eyepatch") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipAccessory);
			}
			else if(this.permy.getAccessory() == "Eyepatch") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			}
			else {
				if(this.permy.getTotalCoins() >= 30000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "30,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyAccessory);
			}
			
			this.setEquipIndication();
		}
		//END ACCESSORY SET UPS
		
		//ACCESSORY
		public function buyAccessory(event:MouseEvent) {
			if(this.storeButton.bowTieButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 2000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.bowTieBought = true;
					
					this.permy.setAccessory("Bow Tie");
					this.permy.addBoughtItem("Bow Tie");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 2000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyAccessory);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
					this.storeButton.bowTieButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.bandanaButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 9000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.bandanaBought = true;
					
					this.permy.setAccessory("Bandana");
					this.permy.addBoughtItem("Bandana");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 9000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyAccessory);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
					this.storeButton.bandanaButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.necklaceButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 24000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.necklaceBought = true;
					
					this.permy.setAccessory("Necklace");
					this.permy.addBoughtItem("Necklace");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 24000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyAccessory);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
					this.storeButton.necklaceButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.bellButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 40000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.bellBought = true;
					
					this.permy.setAccessory("Bell");
					this.permy.addBoughtItem("Bell");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 40000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyAccessory);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
					this.storeButton.bellButton.gotoAndStop(2);
				}
			}
			
			else if(this.storeButton.collarButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 4000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.collarBought = true;
					
					this.permy.setAccessory("Collar");
					this.permy.addBoughtItem("Collar");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 4000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyAccessory);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
					this.storeButton.collarButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.tieButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 7000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.tieBought = true;
					
					this.permy.setAccessory("Tie");
					this.permy.addBoughtItem("Tie");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 7000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyAccessory);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
					this.storeButton.tieButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.glassesButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 15000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.glassesBought = true;
					
					this.permy.setAccessory("Glasses");
					this.permy.addBoughtItem("Glasses");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 15000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyAccessory);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
					this.storeButton.glassesButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.eyepatchButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 30000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.eyepatchBought = true;
					
					this.permy.setAccessory("Eyepatch");
					this.permy.addBoughtItem("Eyepatch");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 30000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyAccessory);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
					this.storeButton.eyepatchButton.gotoAndStop(2);
				}
			}
			this.setEquipIndication();
			this.updateMain();
			
		}
		public function equipAccessory(event:MouseEvent) {
			if(this.storeButton.bowTieButton.alpha == 1) {
				this.permy.setAccessory("Bow Tie");
			}
			else if(this.storeButton.bandanaButton.alpha == 1) {
				this.permy.setAccessory("Bandana");
			}
			else if(this.storeButton.necklaceButton.alpha == 1) {
				this.permy.setAccessory("Necklace");
			}
			else if(this.storeButton.bellButton.alpha == 1) {
				this.permy.setAccessory("Bell");
			}
			else if(this.storeButton.collarButton.alpha == 1) {
				this.permy.setAccessory("Collar");
			}
			else if(this.storeButton.bellButton.alpha == 1) {
				this.permy.setAccessory("Collar");
			}
			else if(this.storeButton.tieButton.alpha == 1) {
				this.permy.setAccessory("Tie");
			}
			else if(this.storeButton.glassesButton.alpha == 1) {
				this.permy.setAccessory("Glasses");
			}
			else if(this.storeButton.eyepatchButton.alpha == 1) {
				this.permy.setAccessory("Eyepatch");
			}
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipAccessory);
			this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipAccessory);
			this.storeButton.equipButton.textDisplay.text = "Unequip";
			
			this.setEquipIndication();
			this.updateMain();
		}
		public function unequipAccessory(event:MouseEvent) {
			this.fadeAll();
			this.permy.setAccessory("None");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipAccessory);
			
			this.setEquipIndication();
			this.updateMain();
		}
		//END ACCESSORY
		
		//HAT
		public function buyHat(event:MouseEvent) {
			if(this.storeButton.redCapButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 4000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.redCapBought = true;
					
					this.permy.setHat("Red Cap");
					this.permy.addBoughtItem("Red Cap");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 4000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyHat);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
					this.storeButton.redCapButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.topHatButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 10000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.topHatBought = true;
					
					this.permy.setHat("Top Hat");
					this.permy.addBoughtItem("Top Hat");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 10000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyHat);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
					this.storeButton.topHatButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.rainHatButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 14000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.rainHatBought = true;
					
					this.permy.setHat("Rain Hat");
					this.permy.addBoughtItem("Rain Hat");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 14000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyHat);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
					this.storeButton.rainHatButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.crownButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 100000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.crownBought = true;
					
					this.permy.setHat("Crown");
					this.permy.addBoughtItem("Crown");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 100000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyHat);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
					this.storeButton.crownButton.gotoAndStop(2);
				}
			}
			
			else if(this.storeButton.blueCapButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 6000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.blueCapBought = true;
					
					this.permy.setHat("Blue Cap");
					this.permy.addBoughtItem("Blue Cap");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 6000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyHat);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
					this.storeButton.blueCapButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.strawHatButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 12000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.strawHatBought = true;
					
					this.permy.setHat("Straw Hat");
					this.permy.addBoughtItem("Straw Hat");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 12000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyHat);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
					this.storeButton.strawHatButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.helmetButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 35000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.helmetBought = true;
					
					this.permy.setHat("Helmet");
					this.permy.addBoughtItem("Helmet");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 35000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyHat);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
					this.storeButton.helmetButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.pirateHatButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 75000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.pirateHatBought = true;
					
					this.permy.setHat("Pirate Hat");
					this.permy.addBoughtItem("Pirate Hat");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 75000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyHat);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
					this.storeButton.pirateHatButton.gotoAndStop(2);
				}
			}
			
			this.setEquipIndication();
			this.updateMain();
		}
		public function equipHat(event:MouseEvent) {
			if(this.storeButton.redCapButton.alpha == 1) {
				this.permy.setHat("Red Cap");
			}
			else if(this.storeButton.topHatButton.alpha == 1) {
				this.permy.setHat("Top Hat");
			}
			else if(this.storeButton.rainHatButton.alpha == 1) {
				this.permy.setHat("Rain Hat");
			}
			else if(this.storeButton.crownButton.alpha == 1) {
				this.permy.setHat("Crown");
			}
			else if(this.storeButton.blueCapButton.alpha == 1) {
				this.permy.setHat("Blue Cap");
			}
			else if(this.storeButton.strawHatButton.alpha == 1) {
				this.permy.setHat("Straw Hat");
			}
			else if(this.storeButton.helmetButton.alpha == 1) {
				this.permy.setHat("Helmet");
			}
			else if(this.storeButton.pirateHatButton.alpha == 1) {
				this.permy.setHat("Pirate Hat");
			}
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipHat);
			this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipHat);
			this.storeButton.equipButton.textDisplay.text = "Unequip";
			
			this.setEquipIndication();
			this.updateMain();
		}
		public function unequipHat(event:MouseEvent) {
			this.fadeAll();
			this.permy.setHat("None");
			this.storeButton.hat.gotoAndStop(this.permy.getHat());
			this.storeButton.accessory.gotoAndStop(this.permy.getAccessory());
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipHat);
			
			this.setEquipIndication();
			this.updateMain();
		}
		
		
		
		
		public function removeOtherEventListeners() {
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipHat);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipHat);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipAccessory);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipAccessory);
		}
		
		public function fadeAll() {
			this.storeButton.redCapButton.alpha = .5;
			this.storeButton.topHatButton.alpha = .5;
			this.storeButton.rainHatButton.alpha = .5;
			this.storeButton.crownButton.alpha = .5;
			this.storeButton.blueCapButton.alpha = .5;
			this.storeButton.strawHatButton.alpha = .5;
			this.storeButton.helmetButton.alpha = .5;
			this.storeButton.pirateHatButton.alpha = .5;
			
			this.storeButton.bowTieButton.alpha = .5;
			this.storeButton.bandanaButton.alpha = .5;
			this.storeButton.necklaceButton.alpha = .5;
			this.storeButton.bellButton.alpha = .5;
			this.storeButton.collarButton.alpha = .5;
			this.storeButton.tieButton.alpha = .5;
			this.storeButton.glassesButton.alpha = .5;
			this.storeButton.eyepatchButton.alpha = .5;
			
			this.storeButton.equipButton.visible = false;
			this.storeButton.priceTag.text = "";
		}
		
		public function setEquipIndication() {
			this.storeButton.redCapButton.indicationBall.visible = false;
			this.storeButton.topHatButton.indicationBall.visible = false;
			this.storeButton.rainHatButton.indicationBall.visible = false;
			this.storeButton.crownButton.indicationBall.visible = false;
			this.storeButton.blueCapButton.indicationBall.visible = false;
			this.storeButton.strawHatButton.indicationBall.visible = false;
			this.storeButton.helmetButton.indicationBall.visible = false;
			this.storeButton.pirateHatButton.indicationBall.visible = false;
			
			this.storeButton.bowTieButton.indicationBall.visible = false;
			this.storeButton.bandanaButton.indicationBall.visible = false;
			this.storeButton.necklaceButton.indicationBall.visible = false;
			this.storeButton.bellButton.indicationBall.visible = false;
			this.storeButton.collarButton.indicationBall.visible = false;
			this.storeButton.tieButton.indicationBall.visible = false;
			this.storeButton.glassesButton.indicationBall.visible = false;
			this.storeButton.eyepatchButton.indicationBall.visible = false;
			if(this.permy.getHat() == "Red Cap") {
				this.storeButton.redCapButton.indicationBall.visible = true;
			}
			else if(this.permy.getHat() == "Top Hat") {
				this.storeButton.topHatButton.indicationBall.visible = true;
			}
			else if(this.permy.getHat() == "Rain Hat") {
				this.storeButton.rainHatButton.indicationBall.visible = true;
			}
			else if(this.permy.getHat() == "Crown") {
				this.storeButton.crownButton.indicationBall.visible = true;
			}
			else if(this.permy.getHat() == "Blue Cap") {
				this.storeButton.blueCapButton.indicationBall.visible = true;
			}
			else if(this.permy.getHat() == "Straw Hat") {
				this.storeButton.strawHatButton.indicationBall.visible = true;
			}
			else if(this.permy.getHat() == "Helmet") {
				this.storeButton.helmetButton.indicationBall.visible = true;
			}
			else if(this.permy.getHat() == "Pirate Hat") {
				this.storeButton.pirateHatButton.indicationBall.visible = true;
			}
			
			if(this.permy.getAccessory() == "Bow Tie") {
				this.storeButton.bowTieButton.indicationBall.visible = true;
			}
			else if(this.permy.getAccessory() == "Bandana") {
				this.storeButton.bandanaButton.indicationBall.visible = true;
			}
			else if(this.permy.getAccessory() == "Necklace") {
				this.storeButton.necklaceButton.indicationBall.visible = true;
			}
			else if(this.permy.getAccessory() == "Bell") {
				this.storeButton.bellButton.indicationBall.visible = true;
			}
			else if(this.permy.getAccessory() == "Collar") {
				this.storeButton.collarButton.indicationBall.visible = true;
			}
			else if(this.permy.getAccessory() == "Tie") {
				this.storeButton.tieButton.indicationBall.visible = true;
			}
			else if(this.permy.getAccessory() == "Glasses") {
				this.storeButton.glassesButton.indicationBall.visible = true;
			}
			else if(this.permy.getAccessory() == "Eyepatch") {
				this.storeButton.eyepatchButton.indicationBall.visible = true;
			}
		}
		
		public function lowerCash(event:Event) {
			if(Number(this.storeButton.coinsText.text) > this.permy.getTotalCoins()) {
				this.storeButton.coinsText.text = (Number(this.storeButton.coinsText.text) - 500).toString();
			}
		}
		
		public function removeEventListeners() {
			removeOtherEventListeners();
			
			this.storeButton.nextButton.removeEventListener(MouseEvent.CLICK,nextStore);
			this.storeButton.backButton.removeEventListener(MouseEvent.CLICK,backStore);
			
			this.storeButton.removeEventListener(Event.ENTER_FRAME,lowerCash);
			
			this.storeButton.redCapButton.removeEventListener(MouseEvent.CLICK,redCapSetUp);
			this.storeButton.topHatButton.removeEventListener(MouseEvent.CLICK,topHatSetUp);
			this.storeButton.rainHatButton.removeEventListener(MouseEvent.CLICK,rainHatSetUp);
			this.storeButton.crownButton.removeEventListener(MouseEvent.CLICK,crownSetUp);
			this.storeButton.blueCapButton.removeEventListener(MouseEvent.CLICK,blueCapSetUp);
			this.storeButton.strawHatButton.removeEventListener(MouseEvent.CLICK,strawHatSetUp);
			this.storeButton.helmetButton.removeEventListener(MouseEvent.CLICK,helmetSetUp);
			this.storeButton.pirateHatButton.removeEventListener(MouseEvent.CLICK,pirateHatSetUp);
			
			this.storeButton.bowTieButton.removeEventListener(MouseEvent.CLICK,bowTieSetUp);
			this.storeButton.bandanaButton.removeEventListener(MouseEvent.CLICK,bandanaSetUp);
			this.storeButton.necklaceButton.removeEventListener(MouseEvent.CLICK,necklaceSetUp);
			this.storeButton.bellButton.removeEventListener(MouseEvent.CLICK,bellSetUp);
			this.storeButton.collarButton.removeEventListener(MouseEvent.CLICK,collarSetUp);
			this.storeButton.tieButton.removeEventListener(MouseEvent.CLICK,tieSetUp);
			this.storeButton.glassesButton.removeEventListener(MouseEvent.CLICK,glassesSetUp);
			this.storeButton.eyepatchButton.removeEventListener(MouseEvent.CLICK,eyepatchSetUp);
		}
		
		public function updateMain() {
			this.hat.gotoAndStop(this.permy.getHat());
			this.accessory.gotoAndStop(this.permy.getAccessory());
		}

	}
	
}