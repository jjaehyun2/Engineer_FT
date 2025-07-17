package  {
	
	import com.milkmangames.nativeextensions.android.*;
	import com.milkmangames.nativeextensions.android.events.*;
	import starling.events.TouchEvent;
	
	
	public class StoreAndroid {
		
		static const PUBLIC_KEY:String="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
		static var myPurchases:Vector.<AndroidPurchase>;
		static var purchasesAllowed:Boolean;
		static var elimAmt:String;
		static var itemHasBeenPurchased:Boolean = false;
		
		
		static function setup() {
			if (!AndroidIAB.isSupported()) {
				purchasesAllowed = false;
				return;
			}
			purchasesAllowed = true;
			
			AndroidIAB.create();
			AndroidIAB.androidIAB.startBillingService(PUBLIC_KEY);
			
			AndroidIAB.androidIAB.addEventListener(AndroidBillingEvent.SERVICE_READY, onServiceReady);
			AndroidIAB.androidIAB.addEventListener(AndroidBillingEvent.PURCHASE_SUCCEEDED, onPurchaseSuccess);
			AndroidIAB.androidIAB.addEventListener(AndroidBillingErrorEvent.PURCHASE_FAILED, onPurchaseFailed);
			AndroidIAB.androidIAB.addEventListener(AndroidBillingEvent.INVENTORY_LOADED, onInventoryLoaded);
			AndroidIAB.androidIAB.addEventListener(AndroidBillingErrorEvent.LOAD_INVENTORY_FAILED, onInventoryFailed);
			AndroidIAB.androidIAB.addEventListener(AndroidBillingEvent.CONSUME_SUCCEEDED, onConsumed);
			AndroidIAB.androidIAB.addEventListener(AndroidBillingErrorEvent.CONSUME_FAILED, onConsumeFailed);
		}
		
		
		// SERVICE READY		
		static function onServiceReady(e:AndroidBillingEvent):void {
			AndroidIAB.androidIAB.loadPlayerInventory();
		}
		
		
		// INVENTORY		
		static function onInventoryLoaded(e:AndroidBillingEvent):void {
			for each (var id in e.purchases) {
				consumeElims(id.itemId);
			}
			
			if (!itemHasBeenPurchased) {
				if (Store.storeHeaderLarge) {
					Store.showItems();
				}
			}
		}
		
		static function onInventoryFailed(e:AndroidBillingErrorEvent):void {
			
		}
		
		
		// PURCHASE
		static function purchaseElims(id:String):void {
			AndroidIAB.androidIAB.purchaseItem(id);
		}
				
		static function onPurchaseSuccess(evt:AndroidBillingEvent):void {
			itemHasBeenPurchased = true;
			Store.showUpdating();
			AndroidIAB.androidIAB.loadPlayerInventory();
		}
		
		static function onPurchaseFailed(e:AndroidBillingErrorEvent):void {
			Store.resetItems();
		}
		
		
		// CONSUME
		static function consumeElims(id:String):void {
			AndroidIAB.androidIAB.consumeItem(id);
		}
		
		
		static function onConsumed(evt:AndroidBillingEvent):void {			
			if (evt.itemId == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") {
				Environment.totalRedux += 50;
				Data.saveObj.totalRedux += 50;
				Data.flushSave();
				elimAmt = "50";
			}
			
			if (evt.itemId == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") {
				Environment.totalRedux += 300;
				Data.saveObj.totalRedux += 300;
				Data.flushSave();
				elimAmt = "300";
			}
			
			if (evt.itemId == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") {
				Environment.totalRedux += 1000;
				Data.saveObj.totalRedux += 1000;
				Data.flushSave();
				elimAmt = "1,000";
			}
			
			if (Stats.statsSprite) {
				Stats.statsSprite.unflatten();
				Stats.totalElims.text = String(Score.addCommas(Environment.totalRedux));
				Stats.statsSprite.flatten();
			}
			
			itemHasBeenPurchased = false;
			Store.didPurchase = true;
			Store.showStatus(elimAmt);
		}
		
		static function onConsumeFailed(e:AndroidBillingErrorEvent):void {
			
		}
	}
}