package  {
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.media.Sound;
	import flash.geom.ColorTransform;
	import flash.media.Sound;
	import com.milkmangames.nativeextensions.ios.*; 
	import com.milkmangames.nativeextensions.ios.events.*;
	
	public class Store {
		private var permy:Permy;
		private var storeButton:MovieClip;
		
		private var player:MovieClip;
		
		private var boughtItems:Array;
		
		private var whiteTiresBought:Boolean;
		private var silverTiresBought:Boolean;
		private var goldTiresBought:Boolean;
		
		private var starsDecalBought:Boolean;
		private var stallionDecalBought:Boolean;
		private var lionDecalBought:Boolean;
		
		private var redTruckBought:Boolean;
		private var blackTruckBought:Boolean;
		private var goldTruckBought:Boolean;
		
		private var decalColorChange:ColorTransform;
		
		private var buySound:Sound;
		
		private var saveGame:Function;
		
		private var dCPrice:String;
		private var dTPrice:String;
		private var c2Price:String;
		private var c10Price:String;
		
		private var restoring:Boolean;
		
		private var hay:Hay;
		
		private var closeStoreOk:Boolean;
		
		public function Store(permy:Permy,storeButton:MovieClip,player:MovieClip) {
			dCPrice = "";
			dTPrice = "";
			c2Price = "";
			c10Price = "";
			
			this.closeStoreOk = true;
			
			this.restoring = false;
			
			StoreKit.create();
			
			//In App Purchases
			var productIdList:Vector.<String>=new Vector.<String>(); 
			productIdList.push("net.game103.duckinatruck.coins20000"); 
			productIdList.push("net.game103.duckinatruck.coins100000"); 
			productIdList.push("net.game103.duckinatruck.doublecoins"); 
			productIdList.push("net.game103.duckinatruck.doublepowerup"); 
			
			StoreKit.storeKit.loadProductDetails(productIdList); 
			
			// listen for a response from loadProductDetails(): 
			StoreKit.storeKit.addEventListener(StoreKitEvent.PRODUCT_DETAILS_LOADED,onProducts); 
			function onProducts(e:StoreKitEvent):void {
				for each(var product:StoreKitProduct in e.validProducts) {
					trace("ID: "+product.productId); 
					trace("Title: "+product.title); 
					trace("Description: "+product.description); 
					trace("String Price: "+product.localizedPrice);
					trace("Price: "+product.price); 
					if(product.productId.toString() == "net.game103.duckinatruck.coins20000") {
						c2Price = product.localizedPrice;
					}
					else if(product.productId.toString() == "net.game103.duckinatruck.coins100000") {
						c10Price = product.localizedPrice;
					}
					else if(product.productId.toString() == "net.game103.duckinatruck.doublecoins") {
						dCPrice = product.localizedPrice;
					}
					else if(product.productId.toString() == "net.game103.duckinatruck.doublepowerup") {
						dTPrice = product.localizedPrice;
					}
				} 
				trace("Loaded "+e.validProducts.length+" Products."); 
				if (e.invalidProductIds.length>0) { 
					trace("[ERR]: invalid product ids:"+e.invalidProductIds.join(","));
				} 
			}
			
			// listen for ERROR response from loadProductDetails(): 
			StoreKit.storeKit.addEventListener(StoreKitErrorEvent.PRODUCT_DETAILS_FAILED, onProductsFailed); 
			
			this.permy = permy;
			this.storeButton = storeButton;
			this.player = player;
			
			this.decalColorChange = new ColorTransform();
			
			this.buySound = new BuyItem();
			
			this.storeButton.coinsText.text = permy.getTotalCoins();
			
			//this.storeButton.backButton.visible = false;
			//this.storeButton.nextButton.addEventListener(MouseEvent.CLICK,nextStore);
			//this.storeButton.backButton.addEventListener(MouseEvent.CLICK,backStore);
			
			this.storeButton.whiteTiresText.mouseEnabled = false;
			this.storeButton.silverTiresText.mouseEnabled = false;
			this.storeButton.goldTiresText.mouseEnabled = false;
			this.storeButton.starsDecalText.mouseEnabled = false;
			this.storeButton.stallionDecalText.mouseEnabled = false;
			this.storeButton.lionDecalText.mouseEnabled = false;
			this.storeButton.redTruckText.mouseEnabled = false;
			this.storeButton.blackTruckText.mouseEnabled = false;
			this.storeButton.goldTruckText.mouseEnabled = false;
			
			this.boughtItems = this.permy.getBoughtItems();
			
			storeButton.addEventListener(Event.ENTER_FRAME,lowerCash);
			storeButton.addEventListener(Event.ENTER_FRAME,raiseCash);
			
			//fade out all and set details to invisible
			this.fadeAll();
			
			//set colors
			for(var i:Number = 0;i < this.boughtItems.length;i++) {
				if(this.boughtItems[i] == "White Tires") {
					this.storeButton.whiteTiresButton.gotoAndStop(2);
					this.whiteTiresBought = true;
				}
				if(this.boughtItems[i] == "Silver Tires") {
					this.storeButton.silverTiresButton.gotoAndStop(2);
					this.silverTiresBought = true;
				}
				if(this.boughtItems[i] == "Gold Tires") {
					this.storeButton.goldTiresButton.gotoAndStop(2);
					this.goldTiresBought = true;
				}
				if(this.boughtItems[i] == "Stars Decal") {
					this.storeButton.starsDecalButton.gotoAndStop(2);
					this.starsDecalBought = true;
				}
				if(this.boughtItems[i] == "Stallion Decal") {
					this.storeButton.stallionDecalButton.gotoAndStop(2);
					this.stallionDecalBought = true;
				}
				if(this.boughtItems[i] == "Lion Decal") {
					this.storeButton.lionDecalButton.gotoAndStop(2);
					this.lionDecalBought = true;
				}
				if(this.boughtItems[i] == "Red Truck") {
					this.storeButton.redTruckButton.gotoAndStop(2);
					this.redTruckBought = true;
				}
				if(this.boughtItems[i] == "Black Truck") {
					this.storeButton.blackTruckButton.gotoAndStop(2);
					this.blackTruckBought = true;
				}
				
				if(this.boughtItems[i] == "Gold Truck") {
					this.storeButton.goldTruckButton.gotoAndStop(2);
					this.goldTruckBought = true;
				}
			}
			
			this.setEquipIndication();
			
			this.storeButton.whiteTiresButton.addEventListener(MouseEvent.CLICK,whiteTiresSetUp);
			this.storeButton.silverTiresButton.addEventListener(MouseEvent.CLICK,silverTiresSetUp);
			this.storeButton.goldTiresButton.addEventListener(MouseEvent.CLICK,goldTiresSetUp);
			this.storeButton.starsDecalButton.addEventListener(MouseEvent.CLICK,starsDecalSetUp);
			this.storeButton.stallionDecalButton.addEventListener(MouseEvent.CLICK,stallionDecalSetUp);
			this.storeButton.lionDecalButton.addEventListener(MouseEvent.CLICK,lionDecalSetUp);
			this.storeButton.redTruckButton.addEventListener(MouseEvent.CLICK,redTruckSetUp);
			this.storeButton.blackTruckButton.addEventListener(MouseEvent.CLICK,blackTruckSetUp);
			
			this.storeButton.goldTruckButton.addEventListener(MouseEvent.CLICK,goldTruckSetUp);
			
			if( StoreKit.storeKit.isStoreKitAvailable()) {
				this.storeButton.inAppButton.addEventListener(MouseEvent.CLICK,goToInAppPurchases);
			}
			else {
				this.storeButton.inAppButton.visible = false;
			}
		}
		
		public function setHay(hay:Hay) {
			this.hay = hay;
		}
		
		function onProductsFailed(e:StoreKitErrorEvent):void {
			trace("error loading products: "+e.text); 
		}
		
		public function setAddFunction(funct:Function):void {
			this.saveGame = funct;
		}
		
		public function goToInAppPurchases(event:MouseEvent) {
			this.storeButton.gotoAndStop(2);
			
			this.storeButton.infoText.text = "";
			
			this.storeButton.doubleCoinsText.text = "Double every coin you earn! (lasts forever!)\n- " + dCPrice;
			this.storeButton.doubleTimeText.text = "Double time for all time-based powerups! (lasts forever!) - " + dTPrice;
			this.storeButton.smallCoinsText.text = "20,000 coins\n- " + c2Price;
			this.storeButton.bigCoinsText.text = "100,000 coins\n- " + c10Price;
			
			this.storeButton.coinsText.text = permy.getTotalCoins();
			if(permy.getCoinMulti() == 2) {
				this.storeButton.doubleCoinsButton.gotoAndStop(2);
				this.storeButton.doubleCoinsText.text = "Double Coins Bought! Thanks!";
				this.storeButton.doubleCoinsText.y = 151.65;
			}
			else {
				this.storeButton.doubleCoinsButton.addEventListener(MouseEvent.CLICK,buyDoubleCoins);
			}
			if(permy.getPowerUpMulti() == 2) {
				this.storeButton.doubleTimeButton.gotoAndStop(2);
				this.storeButton.doubleTimeText.text = "Double Power Up Time Bought! Thanks!";
				this.storeButton.doubleTimeText.y = 151.65;
			}
			else {
				this.storeButton.doubleTimeButton.addEventListener(MouseEvent.CLICK,buyDoubleTime);
			}
			this.storeButton.doubleCoinsText.mouseEnabled = false;
			this.storeButton.doubleTimeText.mouseEnabled = false;
			this.storeButton.smallCoinsText.mouseEnabled = false;
			this.storeButton.bigCoinsText.mouseEnabled = false;
			this.storeButton.doubleCoinsButton.indicationBall.visible = false;
			this.storeButton.doubleTimeButton.indicationBall.visible = false;
			this.storeButton.smallCoinsButton.indicationBall.visible = false;
			this.storeButton.bigCoinsButton.indicationBall.visible = false;
			this.storeButton.backToStoreButton.addEventListener(MouseEvent.CLICK,goBackToStore);
			
			this.storeButton.smallCoinsButton.addEventListener(MouseEvent.CLICK,buySmallCoins);
			this.storeButton.bigCoinsButton.addEventListener(MouseEvent.CLICK,buyBigCoins);
			
			this.storeButton.restorePurchasesButton.addEventListener(MouseEvent.CLICK,restorePurchases);
		}
		
		public function restorePurchases(event:MouseEvent) {
			this.restoring = true;
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,doubleCoinsSuccess);
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,doubleTimeSuccess);
			StoreKit.storeKit.addEventListener(StoreKitEvent.TRANSACTIONS_RESTORED, onTransactionsRestoreComplete);
			StoreKit.storeKit.addEventListener(StoreKitErrorEvent.TRANSACTION_RESTORE_FAILED, onPurchaseFailed); 
			StoreKit.storeKit.restoreTransactions();
			this.storeButton.infoText.text = "Please Wait";
			removeInAppListeners();
		}
		
		public function onTransactionsRestoreComplete(e:StoreKitEvent):void {
			this.restoring = false;
			removePurchaseListeners();
			saveGame();
			addInAppListeners();
			this.storeButton.infoText.text = "Transactions Restored!";
			StoreKit.storeKit.removeEventListener(StoreKitEvent.TRANSACTIONS_RESTORED, onTransactionsRestoreComplete);
		}
		
		public function removePurchaseListeners() {
			StoreKit.storeKit.removeEventListener(StoreKitErrorEvent.TRANSACTION_RESTORE_FAILED, onPurchaseFailed); 
			StoreKit.storeKit.removeEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,doubleCoinsSuccess);
			StoreKit.storeKit.removeEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,doubleTimeSuccess);
			StoreKit.storeKit.removeEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,smallCoinsSuccess);
			StoreKit.storeKit.removeEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,bigCoinsSuccess);
			StoreKit.storeKit.removeEventListener(StoreKitEvent.PURCHASE_CANCELLED,onPurchaseCancel);
			StoreKit.storeKit.removeEventListener(StoreKitErrorEvent.PURCHASE_FAILED, onPurchaseFailed);
			StoreKit.storeKit.removeEventListener(StoreKitEvent.PURCHASE_SUCCEEDED, restorePurchasesEvent);
		}
		
		public function buyDoubleCoins(event:MouseEvent) {
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,doubleCoinsSuccess);
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_CANCELLED,onPurchaseCancel);
			StoreKit.storeKit.addEventListener(StoreKitErrorEvent.PURCHASE_FAILED, onPurchaseFailed);
			StoreKit.storeKit.purchaseProduct("net.game103.duckinatruck.doublecoins",1);
			this.storeButton.infoText.text = "Please Wait";
			removeInAppListeners();
		}
		
		public function buyDoubleTime(event:MouseEvent) {
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,doubleTimeSuccess); 
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_CANCELLED,onPurchaseCancel);
			StoreKit.storeKit.addEventListener(StoreKitErrorEvent.PURCHASE_FAILED, onPurchaseFailed);
			StoreKit.storeKit.purchaseProduct("net.game103.duckinatruck.doublepowerup",1);
			this.storeButton.infoText.text = "Please Wait";
			removeInAppListeners();
		}
		
		public function buySmallCoins(event:MouseEvent) {
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,smallCoinsSuccess);
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_CANCELLED,onPurchaseCancel);
			StoreKit.storeKit.addEventListener(StoreKitErrorEvent.PURCHASE_FAILED, onPurchaseFailed);
			StoreKit.storeKit.purchaseProduct("net.game103.duckinatruck.coins20000",1);
			this.storeButton.infoText.text = "Please Wait";
			removeInAppListeners();
		}
		
		public function buyBigCoins(event:MouseEvent) {
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_SUCCEEDED,bigCoinsSuccess);
			StoreKit.storeKit.addEventListener(StoreKitEvent.PURCHASE_CANCELLED,onPurchaseCancel);
			StoreKit.storeKit.addEventListener(StoreKitErrorEvent.PURCHASE_FAILED, onPurchaseFailed);
			StoreKit.storeKit.purchaseProduct("net.game103.duckinatruck.coins100000",1);
			this.storeButton.infoText.text = "Please Wait";
			removeInAppListeners();
		}
		
		public function removeInAppListeners() {
			if(this.hay != null) {
				this.hay.setCloseStoreOk(false);
			}
			else {
				this.closeStoreOk = false;
			}
			this.storeButton.backToStoreButton.removeEventListener(MouseEvent.CLICK,goBackToStore);
			this.storeButton.restorePurchasesButton.removeEventListener(MouseEvent.CLICK,restorePurchases);
			this.storeButton.doubleCoinsButton.removeEventListener(MouseEvent.CLICK,buyDoubleCoins);
			this.storeButton.doubleTimeButton.removeEventListener(MouseEvent.CLICK,buyDoubleTime);
			this.storeButton.smallCoinsButton.removeEventListener(MouseEvent.CLICK,buySmallCoins);
			this.storeButton.bigCoinsButton.removeEventListener(MouseEvent.CLICK,buyBigCoins);
		}
		
		public function getStoreOk():Boolean {
			return this.closeStoreOk;
		}
		
		public function addInAppListeners() {
			if(this.hay != null) {
				this.hay.setCloseStoreOk(true);
			}
			else {
				this.closeStoreOk = true;
			}
			this.storeButton.backToStoreButton.addEventListener(MouseEvent.CLICK,goBackToStore);
			this.storeButton.restorePurchasesButton.addEventListener(MouseEvent.CLICK,restorePurchases);
			if(permy.getCoinMulti() == 1) {
				this.storeButton.doubleCoinsButton.addEventListener(MouseEvent.CLICK,buyDoubleCoins);
			}
			if(permy.getPowerUpMulti() == 1) {
				this.storeButton.doubleTimeButton.addEventListener(MouseEvent.CLICK,buyDoubleTime);
			}
			this.storeButton.smallCoinsButton.addEventListener(MouseEvent.CLICK,buySmallCoins);
			this.storeButton.bigCoinsButton.addEventListener(MouseEvent.CLICK,buyBigCoins);
		}
		
		
		public function onPurchaseCancel(e:StoreKitEvent) {
			this.removePurchaseListeners();
			addInAppListeners();
			this.storeButton.infoText.text = "Purchase cancelled.";
		}
		
		public function onPurchaseFailed(e:StoreKitErrorEvent) {
			this.removePurchaseListeners();
			addInAppListeners();
			this.storeButton.infoText.text = "Could not connect to the App Store.";
		}
		
		public function goBackToStore(event:MouseEvent) {
			goBackToStoreFunction();
		}
		
		public function restorePurchasesEvent(e:StoreKitEvent) {
			if(e.productId == "net.game103.duckinatruck.doublecoins") {
				this.permy.setCoinMulti(2);
				this.storeButton.doubleCoinsButton.gotoAndStop(2);
				this.storeButton.doubleCoinsText.text = "Double Coins Bought! Thanks!";
				this.storeButton.doubleCoinsText.y = 151.65;
			}
			if(e.productId == "net.game103.duckinatruck.doublepowerup") {
				this.permy.setPowerUpMulti(2);
				this.storeButton.doubleTimeButton.gotoAndStop(2);
				this.storeButton.doubleTimeText.text = "Double Power Up Time Bought! Thanks!";
				this.storeButton.doubleTimeText.y = 151.65;
			}
			if(this.restoring == false) {
				removePurchaseListeners();
				saveGame();
				addInAppListeners();
			}
		}
		
		public function doubleCoinsSuccess(e:StoreKitEvent) {
			if(e.productId == "net.game103.duckinatruck.doublecoins") {
				this.permy.setCoinMulti(2);
				this.storeButton.doubleCoinsButton.gotoAndStop(2);
				this.storeButton.doubleCoinsText.text = "Double Coins Bought! Thanks!";
				this.storeButton.doubleCoinsText.y = 151.65;
				this.storeButton.doubleCoinsButton.removeEventListener(MouseEvent.CLICK,buyDoubleCoins);
				this.storeButton.infoText.text = "Purchase of x2 coins was successful! Thank you!";
			}
			if(e.productId == "net.game103.duckinatruck.doublepowerup") {
				this.permy.setPowerUpMulti(2);
				this.storeButton.doubleTimeButton.gotoAndStop(2);
				this.storeButton.doubleTimeText.text = "Double Power Up Time Bought! Thanks!";
				this.storeButton.doubleTimeText.y = 151.65;
				this.storeButton.infoText.text = "Purchase of double time powerups was successful! Thank you!";
			}
			if(this.restoring == false) {
				removePurchaseListeners();
				saveGame();
				addInAppListeners();
			}
		}
		
		public function doubleTimeSuccess(e:StoreKitEvent) {
			if(e.productId == "net.game103.duckinatruck.doublecoins") {
				this.permy.setCoinMulti(2);
				this.storeButton.doubleCoinsButton.gotoAndStop(2);
				this.storeButton.doubleCoinsText.text = "Double Coins Bought! Thanks!";
				this.storeButton.doubleCoinsText.y = 151.65;
				this.storeButton.doubleCoinsButton.removeEventListener(MouseEvent.CLICK,buyDoubleCoins);
				this.storeButton.infoText.text = "Purchase of x2 coins was successful! Thank you!";
			}
			if(e.productId == "net.game103.duckinatruck.doublepowerup") {
				this.permy.setPowerUpMulti(2);
				this.storeButton.doubleTimeButton.gotoAndStop(2);
				this.storeButton.doubleTimeText.text = "Double Power Up Time Bought! Thanks!";
				this.storeButton.doubleTimeText.y = 151.65;
				this.storeButton.infoText.text = "Purchase of double time powerups was successful! Thank you!";
			}
			if(this.restoring == false) {
				removePurchaseListeners();
				saveGame();
				addInAppListeners();
			}
		}
		
		public function smallCoinsSuccess(e:StoreKitEvent) {
			this.permy.setTotalCoins(this.permy.getTotalCoins() + 20000 * this.permy.getCoinMulti());
			removePurchaseListeners();
			saveGame();
			addInAppListeners();
			this.storeButton.infoText.text = "Purchase of 20,000 coins was successful! Thank you!";
		}
			
		public function bigCoinsSuccess(e:StoreKitEvent) {
			this.permy.setTotalCoins(this.permy.getTotalCoins() + 100000 * this.permy.getCoinMulti());
			removePurchaseListeners();
			saveGame();
			addInAppListeners();
			this.storeButton.infoText.text = "Purchase of 100,000 coins was successful! Thank you!";
		}
		
		public function goBackToStoreFunction() {
			if(this.storeButton.currentFrame == 2) {
				this.storeButton.infoText.text = "";
			}
			this.storeButton.gotoAndStop(1);
			this.storeButton.coinsText.text = permy.getTotalCoins();
			
			this.storeButton.whiteTiresText.mouseEnabled = false;
			this.storeButton.silverTiresText.mouseEnabled = false;
			this.storeButton.goldTiresText.mouseEnabled = false;
			this.storeButton.starsDecalText.mouseEnabled = false;
			this.storeButton.stallionDecalText.mouseEnabled = false;
			this.storeButton.lionDecalText.mouseEnabled = false;
			this.storeButton.redTruckText.mouseEnabled = false;
			this.storeButton.blackTruckText.mouseEnabled = false;
			this.storeButton.goldTruckText.mouseEnabled = false;
			
			//fade out all and set details to invisible
			this.fadeAll();
			
			//set colors
			for(var i:Number = 0;i < this.boughtItems.length;i++) {
				if(this.boughtItems[i] == "White Tires") {
					this.storeButton.whiteTiresButton.gotoAndStop(2);
					this.whiteTiresBought = true;
				}
				if(this.boughtItems[i] == "Silver Tires") {
					this.storeButton.silverTiresButton.gotoAndStop(2);
					this.silverTiresBought = true;
				}
				if(this.boughtItems[i] == "Gold Tires") {
					this.storeButton.goldTiresButton.gotoAndStop(2);
					this.goldTiresBought = true;
				}
				if(this.boughtItems[i] == "Stars Decal") {
					this.storeButton.starsDecalButton.gotoAndStop(2);
					this.starsDecalBought = true;
				}
				if(this.boughtItems[i] == "Stallion Decal") {
					this.storeButton.stallionDecalButton.gotoAndStop(2);
					this.stallionDecalBought = true;
				}
				if(this.boughtItems[i] == "Lion Decal") {
					this.storeButton.lionDecalButton.gotoAndStop(2);
					this.lionDecalBought = true;
				}
				if(this.boughtItems[i] == "Red Truck") {
					this.storeButton.redTruckButton.gotoAndStop(2);
					this.redTruckBought = true;
				}
				if(this.boughtItems[i] == "Black Truck") {
					this.storeButton.blackTruckButton.gotoAndStop(2);
					this.blackTruckBought = true;
				}
				
				if(this.boughtItems[i] == "Gold Truck") {
					this.storeButton.goldTruckButton.gotoAndStop(2);
					this.goldTruckBought = true;
				}
			}
			
			this.setEquipIndication();
			
			this.storeButton.whiteTiresButton.addEventListener(MouseEvent.CLICK,whiteTiresSetUp);
			this.storeButton.silverTiresButton.addEventListener(MouseEvent.CLICK,silverTiresSetUp);
			this.storeButton.goldTiresButton.addEventListener(MouseEvent.CLICK,goldTiresSetUp);
			this.storeButton.starsDecalButton.addEventListener(MouseEvent.CLICK,starsDecalSetUp);
			this.storeButton.stallionDecalButton.addEventListener(MouseEvent.CLICK,stallionDecalSetUp);
			this.storeButton.lionDecalButton.addEventListener(MouseEvent.CLICK,lionDecalSetUp);
			this.storeButton.redTruckButton.addEventListener(MouseEvent.CLICK,redTruckSetUp);
			this.storeButton.blackTruckButton.addEventListener(MouseEvent.CLICK,blackTruckSetUp);
			
			this.storeButton.goldTruckButton.addEventListener(MouseEvent.CLICK,goldTruckSetUp);
			
			this.storeButton.inAppButton.addEventListener(MouseEvent.CLICK,goToInAppPurchases);
		}
		
		public function nextStore(event:MouseEvent) {
			
		}
		
		public function backStore(event:MouseEvent) {
			
		}
		
		public function stopTires() {
			this.player.inside.w1Out.w1.gotoAndStop(1);
			this.player.inside.w2Out.w1.gotoAndStop(1);
		}
		
		//BEGIN TIRE SETUPS
		public function whiteTiresSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.whiteTiresButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop("White Tires");
			this.player.inside.w2Out.gotoAndStop("White Tires");
			stopTires();
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.whiteTiresBought && this.permy.getTires() != "White Tires") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipTires);
			}
			else if(this.permy.getTires() == "White Tires") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTires);
			}
			else {
				if(this.permy.getTotalCoins() >= 2000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "2,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyTires);
			}
			
			this.setEquipIndication();
		}
		
		public function silverTiresSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.silverTiresButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop("Silver Tires");
			this.player.inside.w2Out.gotoAndStop("Silver Tires");
			stopTires();
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.silverTiresBought && this.permy.getTires() != "Silver Tires") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipTires);
			}
			else if(this.permy.getTires() == "Silver Tires") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTires);
			}
			else {
				if(this.permy.getTotalCoins() >= 7500) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "7,500 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyTires);
			}
			
			this.setEquipIndication();
		}
		
		public function goldTiresSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.goldTiresButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop("Gold Tires");
			this.player.inside.w2Out.gotoAndStop("Gold Tires");
			stopTires();
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.goldTiresBought && this.permy.getTires() != "Gold Tires") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipTires);
			}
			else if(this.permy.getTires() == "Gold Tires") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTires);
			}
			else {
				if(this.permy.getTotalCoins() >= 20000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "20,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyTires);
			}
			
			this.setEquipIndication();
		}
		
		//DECALS
		public function starsDecalSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.starsDecalButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			stopTires();
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop("Stars Decal");
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.starsDecalBought && this.permy.getDecal() != "Stars Decal") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipDecal);
			}
			else if(this.permy.getDecal() == "Stars Decal") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipDecal);
			}
			else {
				if(this.permy.getTotalCoins() >= 1000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "1,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyDecal);
			}
			
			this.setEquipIndication();
		}
		
		public function stallionDecalSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.stallionDecalButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			stopTires();
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop("Stallion Decal");
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.stallionDecalBought && this.permy.getDecal() != "Stallion Decal") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipDecal);
			}
			else if(this.permy.getDecal() == "Stallion Decal") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipDecal);
			}
			else {
				if(this.permy.getTotalCoins() >= 5000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "5,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyDecal);
			}
			
			this.setEquipIndication();
		}
		
		public function lionDecalSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.lionDecalButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			stopTires();
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop("Lion Decal");
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.lionDecalBought && this.permy.getDecal() != "Lion Decal") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipDecal);
			}
			else if(this.permy.getDecal() == "Lion Decal") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipDecal);
			}
			else {
				if(this.permy.getTotalCoins() >= 10000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "10,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyDecal);
			}
			
			this.setEquipIndication();
		}
		
		//redTruck setup
		public function redTruckSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.redTruckButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			stopTires();
			this.player.inside.body.gotoAndStop("Red Truck");
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			
				decalColorChange.color = 0x000000;
				
			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.redTruckBought && this.permy.getColor() != "Red Truck") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipTruck);
			}
			else if(this.permy.getColor() == "Red Truck") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTruck);
			}
			else {
				if(this.permy.getTotalCoins() >= 5000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "5,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyTruck);
			}
			
			this.setEquipIndication();
		}
		
		//pirate hat set up
		public function blackTruckSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.blackTruckButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			stopTires();
			this.player.inside.body.gotoAndStop("Black Truck");
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			
				decalColorChange.color = 0x333333;
			
			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.blackTruckBought && this.permy.getColor() != "Black Truck") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipTruck);
			}
			else if(this.permy.getColor() == "Black Truck") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTruck);
			}
			else {
				if(this.permy.getTotalCoins() >= 15000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "15,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyTruck);
			}
			
			this.setEquipIndication();
		}
		
		//END HAT SET UPS
		//BEGIN ACCESSORY SET UPS
		
		public function goldTruckSetUp(event:MouseEvent) {
			//remove event listeners
			this.removeOtherEventListeners();
			//
			this.fadeAll();
			
			this.storeButton.goldTruckButton.alpha = 1;
			this.storeButton.equipButton.visible = true;
			
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			stopTires();
			this.player.inside.body.gotoAndStop("Gold Truck");
			this.player.inside.decal.gotoAndStop(permy.getDecal());

				decalColorChange.color = 0xCC8504;

			player.inside.decal.transform.colorTransform = decalColorChange;
			this.storeButton.priceTag.text = "";
			
			if(this.goldTruckBought && this.permy.getColor() != "Gold Truck") {
				this.storeButton.equipButton.textDisplay.text = "Equip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,equipTruck);
			}
			else if(this.permy.getColor() == "Gold Truck") {
				this.storeButton.equipButton.textDisplay.text = "Unequip";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTruck);
			}
			else {
				if(this.permy.getTotalCoins() >= 50000) {
					this.storeButton.equipButton.textDisplay.text = "Buy";
				}
				else {
					this.storeButton.equipButton.visible = false;
				}
				this.storeButton.priceTag.text = "50,000 Coins";
				this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,buyTruck);
			}
			
			this.setEquipIndication();
		}
		
		
		public function buyTires(event:MouseEvent) {
			if(this.storeButton.whiteTiresButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 2000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.whiteTiresBought = true;
					
					this.permy.setTires("White Tires");
					this.permy.addBoughtItem("White Tires");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 2000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyTires);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTires);
					this.storeButton.whiteTiresButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.silverTiresButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 7500) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.silverTiresBought = true;
					
					this.permy.setTires("Silver Tires");
					this.permy.addBoughtItem("Silver Tires");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 7500);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyTires);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTires);
					this.storeButton.silverTiresButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.goldTiresButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 20000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.goldTiresBought = true;
					
					this.permy.setTires("Gold Tires");
					this.permy.addBoughtItem("Gold Tires");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 20000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyTires);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTires);
					this.storeButton.goldTiresButton.gotoAndStop(2);
				}
			}
			
			this.setEquipIndication();
			this.updateMain();
		}
		public function buyDecal(event:MouseEvent) {
			if(this.storeButton.starsDecalButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 1000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.starsDecalBought = true;
					
					this.permy.setDecal("Stars Decal");
					this.permy.addBoughtItem("Stars Decal");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 1000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyDecal);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipDecal);
					this.storeButton.starsDecalButton.gotoAndStop(2);
				}
			}
			
			else if(this.storeButton.stallionDecalButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 5000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.stallionDecalBought = true;
					
					this.permy.setDecal("Stallion Decal");
					this.permy.addBoughtItem("Stallion Decal");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 5000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyDecal);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipDecal);
					this.storeButton.stallionDecalButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.lionDecalButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 10000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.lionDecalBought = true;
					
					this.permy.setDecal("Lion Decal");
					this.permy.addBoughtItem("Lion Decal");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 10000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyDecal);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipDecal);
					this.storeButton.lionDecalButton.gotoAndStop(2);
				}
			}
			
			this.setEquipIndication();
			this.updateMain();
		}
		public function buyTruck(event:MouseEvent) {
			if(this.storeButton.redTruckButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 5000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.redTruckBought = true;
					
					this.permy.setColor("Red Truck");
					this.permy.addBoughtItem("Red Truck");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 5000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyTruck);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTruck);
					this.storeButton.redTruckButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.blackTruckButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 15000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.blackTruckBought = true;
					
					this.permy.setColor("Black Truck");
					this.permy.addBoughtItem("Black Truck");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 15000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyTruck);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTruck);
					this.storeButton.blackTruckButton.gotoAndStop(2);
				}
			}
			else if(this.storeButton.goldTruckButton.alpha == 1 && this.storeButton.equipButton.textDisplay.text == "Buy") {
				if(this.permy.getTotalCoins() >= 50000) {
					
					if(permy.getMute() == false) {
						buySound.play();
					}
					
					this.goldTruckBought = true;
					
					this.permy.setColor("Gold Truck");
					this.permy.addBoughtItem("Gold Truck");
					this.permy.setTotalCoins(this.permy.getTotalCoins() - 50000);
					
					//this.storeButton.coinsText.text = this.permy.getTotalCoins();
					this.storeButton.priceTag.text = "";
					this.storeButton.equipButton.textDisplay.text = "Unequip";
					this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyTruck);
					this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTruck);
					this.storeButton.goldTruckButton.gotoAndStop(2);
				}
			}
			
			this.setEquipIndication();
			this.updateMain();
		}

		public function equipTires(event:MouseEvent) {
			if(this.storeButton.whiteTiresButton.alpha == 1) {
				this.permy.setTires("White Tires");
			}
			else if(this.storeButton.silverTiresButton.alpha == 1) {
				this.permy.setTires("Silver Tires");
			}
			else if(this.storeButton.goldTiresButton.alpha == 1) {
				this.permy.setTires("Gold Tires");
			}
			
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipTires);
			this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTires);
			this.storeButton.equipButton.textDisplay.text = "Unequip";
			
			this.setEquipIndication();
			this.updateMain();
		}
		public function equipDecal(event:MouseEvent) {
			if(this.storeButton.starsDecalButton.alpha == 1) {
				this.permy.setDecal("Stars Decal");
			}
			else if(this.storeButton.stallionDecalButton.alpha == 1) {
				this.permy.setDecal("Stallion Decal");
			}
			else if(this.storeButton.lionDecalButton.alpha == 1) {
				this.permy.setDecal("Lion Decal");
			}
			
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipDecal);
			this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipDecal);
			this.storeButton.equipButton.textDisplay.text = "Unequip";
			
			this.setEquipIndication();
			this.updateMain();
		}
		public function equipTruck(event:MouseEvent) {
			if(this.storeButton.redTruckButton.alpha == 1) {
				this.permy.setColor("Red Truck");
			}
			else if(this.storeButton.blackTruckButton.alpha == 1) {
				this.permy.setColor("Black Truck");
			}
			else if(this.storeButton.goldTruckButton.alpha == 1) {
				this.permy.setColor("Gold Truck");
			}
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipTruck);
			this.storeButton.equipButton.addEventListener(MouseEvent.CLICK,unequipTruck);
			this.storeButton.equipButton.textDisplay.text = "Unequip";
			
			this.setEquipIndication();
			this.updateMain();
		}
		
		
		public function unequipTires(event:MouseEvent) {
			this.fadeAll();
			this.permy.setTires("None");
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			stopTires();
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipTires);
			
			this.setEquipIndication();
			this.updateMain();
		}
		
		public function unequipDecal(event:MouseEvent) {
			this.fadeAll();
			this.permy.setDecal("None");
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			stopTires();
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipDecal);
			
			this.setEquipIndication();
			this.updateMain();
		}
		
		public function unequipTruck(event:MouseEvent) {
			this.fadeAll();
			this.permy.setColor("None");
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			stopTires();
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipTruck);
			
			this.setEquipIndication();
			this.updateMain();
		}
		
		
		public function removeOtherEventListeners() {
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipTruck);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipTruck);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipDecal);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipDecal);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,unequipTires);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,equipTires);
		}
		
		public function removeBuyEventListeners() {
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyTruck);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyTires);
			this.storeButton.equipButton.removeEventListener(MouseEvent.CLICK,buyDecal);
		}
		
		public function fadeAll() {
			this.storeButton.whiteTiresButton.alpha = .5;
			this.storeButton.silverTiresButton.alpha = .5;
			this.storeButton.goldTiresButton.alpha = .5;
			this.storeButton.starsDecalButton.alpha = .5;
			this.storeButton.stallionDecalButton.alpha = .5;
			this.storeButton.lionDecalButton.alpha = .5;
			this.storeButton.redTruckButton.alpha = .5;
			this.storeButton.blackTruckButton.alpha = .5;
			this.storeButton.goldTruckButton.alpha = .5;
			
			this.storeButton.equipButton.visible = false;
			this.storeButton.priceTag.text = "";
		}
		
		public function setEquipIndication() {
			this.storeButton.whiteTiresButton.indicationBall.visible = false;
			this.storeButton.silverTiresButton.indicationBall.visible = false;
			this.storeButton.goldTiresButton.indicationBall.visible = false;
			this.storeButton.starsDecalButton.indicationBall.visible = false;
			this.storeButton.stallionDecalButton.indicationBall.visible = false;
			this.storeButton.lionDecalButton.indicationBall.visible = false;
			this.storeButton.redTruckButton.indicationBall.visible = false;
			this.storeButton.blackTruckButton.indicationBall.visible = false;
			this.storeButton.goldTruckButton.indicationBall.visible = false;
			
			if(this.permy.getTires() == "White Tires") {
				this.storeButton.whiteTiresButton.indicationBall.visible = true;
			}
			else if(this.permy.getTires() == "Silver Tires") {
				this.storeButton.silverTiresButton.indicationBall.visible = true;
			}
			else if(this.permy.getTires() == "Gold Tires") {
				this.storeButton.goldTiresButton.indicationBall.visible = true;
			}
			if(this.permy.getDecal() == "Stars Decal") {
				this.storeButton.starsDecalButton.indicationBall.visible = true;
			}
			else if(this.permy.getDecal() == "Stallion Decal") {
				this.storeButton.stallionDecalButton.indicationBall.visible = true;
			}
			else if(this.permy.getDecal() == "Lion Decal") {
				this.storeButton.lionDecalButton.indicationBall.visible = true;
			}
			if(this.permy.getColor() == "Red Truck") {
				this.storeButton.redTruckButton.indicationBall.visible = true;
			}
			else if(this.permy.getColor() == "Black Truck") {
				this.storeButton.blackTruckButton.indicationBall.visible = true;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				this.storeButton.goldTruckButton.indicationBall.visible = true;
			}
		}
		
		public function lowerCash(event:Event) {
			if(Number(this.storeButton.coinsText.text) - 500 > this.permy.getTotalCoins()) {
				this.storeButton.coinsText.text = (Number(this.storeButton.coinsText.text) - 500).toString();
			}
			else {
				this.storeButton.coinsText.text = this.permy.getTotalCoins().toString();
			}
		}
		public function raiseCash(event:Event) {
			if(Number(this.storeButton.coinsText.text) + 500 < this.permy.getTotalCoins()) {
				this.storeButton.coinsText.text = (Number(this.storeButton.coinsText.text) + 500).toString();
			}
			else {
				this.storeButton.coinsText.text = this.permy.getTotalCoins().toString();
			}
		}
		
		public function removeEventListeners() {
			removeOtherEventListeners();
			
			this.storeButton.nextButton.removeEventListener(MouseEvent.CLICK,nextStore);
			this.storeButton.backButton.removeEventListener(MouseEvent.CLICK,backStore);
			
			this.storeButton.removeEventListener(Event.ENTER_FRAME,lowerCash);
			
			this.storeButton.whiteTiresButton.removeEventListener(MouseEvent.CLICK,whiteTiresSetUp);
			this.storeButton.silverTiresButton.removeEventListener(MouseEvent.CLICK,silverTiresSetUp);
			this.storeButton.goldTiresButton.removeEventListener(MouseEvent.CLICK,goldTiresSetUp);
			this.storeButton.starsDecalButton.removeEventListener(MouseEvent.CLICK,starsDecalSetUp);
			this.storeButton.stallionDecalButton.removeEventListener(MouseEvent.CLICK,stallionDecalSetUp);
			this.storeButton.lionDecalButton.removeEventListener(MouseEvent.CLICK,lionDecalSetUp);
			this.storeButton.redTruckButton.removeEventListener(MouseEvent.CLICK,redTruckSetUp);
			this.storeButton.blackTruckButton.removeEventListener(MouseEvent.CLICK,blackTruckSetUp);
			this.storeButton.goldTruckButton.removeEventListener(MouseEvent.CLICK,goldTruckSetUp);
		}
		
		public function updateMain() {
			this.player.inside.w1Out.gotoAndStop(permy.getTires());
			this.player.inside.body.gotoAndStop(permy.getColor());
			this.player.inside.decal.gotoAndStop(permy.getDecal());
			this.player.inside.w2Out.gotoAndStop(permy.getTires());
			if(this.permy.getColor() == "None") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Red Truck") {
				decalColorChange.color = 0x000000;
			}
			else if(this.permy.getColor() == "Black Truck") {
				decalColorChange.color = 0x333333;
			}
			else if(this.permy.getColor() == "Gold Truck") {
				decalColorChange.color = 0xCC8504;
			}
			player.inside.decal.transform.colorTransform = decalColorChange;
			stopTires();
		}

	}
	
}