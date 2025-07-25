/* Copyright 2019 Tua Rua Ltd.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */
package com.tuarua {
import com.tuarua.fre.ANEError;
import com.tuarua.fre.ANEUtils;
import com.tuarua.iap.billing.BillingResult;
import com.tuarua.iap.billing.Purchase;
import com.tuarua.iap.billing.PurchaseHistoryRecord;
import com.tuarua.iap.billing.PurchasesResult;
import com.tuarua.iap.billing.SkuDetails;
import com.tuarua.iap.billing.events.BillingEvent;
import com.tuarua.iap.storekit.FetchReceiptResult;
import com.tuarua.iap.storekit.PurchaseError;
import com.tuarua.iap.storekit.Receipt;
import com.tuarua.iap.storekit.ReceiptError;

import flash.events.StatusEvent;
import flash.external.ExtensionContext;
import flash.utils.Dictionary;

/** @private */
public class InAppPurchaseANEContext {
    internal static const NAME:String = "InAppPurchaseANE";
    internal static const TRACE:String = "TRACE";

    // storekit
    private static const PRODUCT_INFO:String = "StoreKitEvent.ProductInfo";
    private static const PURCHASE:String = "StoreKitEvent.Purchase";
    private static const RESTORE:String = "StoreKitEvent.Restore";
    private static const VERIFY_RECEIPT:String = "StoreKitEvent.VerifyReceipt";
    private static const FETCH_RECEIPT:String = "StoreKitEvent.FetchReceipt";
    //billing
    private static const ON_CONSUME:String = "BillingEvent.onConsume";
    private static const ON_ACKNOWLEDGE_PURCHASE:String = "BillingEvent.onAcknowledgePurchase";
    private static const ON_SETUP_FINISHED:String = "BillingEvent.onBillingSetupFinished";
    private static const ON_SERVICE_DISCONNECTED:String = "BillingEvent.onBillingServiceDisconnected";
    private static const ON_QUERY_SKU:String = "BillingEvent.onQuerySkuDetails";
    private static const ON_PURCHASE_HISTORY:String = "BillingEvent.onPurchaseHistory";
    private static const ON_PRICE_CHANGE:String = "BillingEvent.onPriceChange";

    public static var callbacks:Dictionary = new Dictionary();
    private static var _context:ExtensionContext;
    private static var _isDisposed:Boolean;

    public function InAppPurchaseANEContext() {
    }

    public static function get context():ExtensionContext {
        if (_context == null) {
            try {
                _context = ExtensionContext.createExtensionContext("com.tuarua." + NAME, null);
                _context.addEventListener(StatusEvent.STATUS, gotEvent);
                _isDisposed = false;
            } catch (e:Error) {
                trace("[" + NAME + "] ANE not loaded properly.  Future calls will fail.");
            }
        }
        return _context;
    }

    public static function createCallback(listener:Function):String {
        var id:String;
        if (listener != null) {
            id = context.call("createGUID") as String;
            callbacks[id] = listener;
        }
        return id;
    }

    public static function callCallback(callbackId:String, ...args):void {
        var callback:Function = callbacks[callbackId];
        if (callback == null) return;
        callback.apply(null, args);
        delete callbacks[callbackId];
    }

    private static function gotEvent(event:StatusEvent):void {
        var argsAsJSON:Object;
        var ret:* = null;
        var pErr:PurchaseError = null;
        var rErr:ReceiptError = null;
        switch (event.level) {
            case TRACE:
                trace("[" + NAME + "]", event.code);
                break;
            case PRODUCT_INFO:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    if (argsAsJSON.hasOwnProperty("error") && argsAsJSON.error) {
                        pErr = new PurchaseError(argsAsJSON.error.text, argsAsJSON.error.id);
                    } else {
                        ret = _context.call("getProductsInfo", argsAsJSON.callbackId);
                    }
                    if (ret is ANEError) {
                        printANEError(ret as ANEError);
                        return;
                    }
                    callCallback(argsAsJSON.callbackId, ret, pErr);
                } catch (e:Error) {
                    trace(PRODUCT_INFO, "parsing error", event.code, e.message);
                }
                break;
            case PURCHASE:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    if (argsAsJSON.hasOwnProperty("error") && argsAsJSON.error) {
                        pErr = new PurchaseError(argsAsJSON.error.text, argsAsJSON.error.id);
                    } else {
                        ret = _context.call("getPurchaseProduct", argsAsJSON.callbackId);
                    }
                    if (ret is ANEError) {
                        printANEError(ret as ANEError);
                        return;
                    }
                    callCallback(argsAsJSON.callbackId, ret, pErr);
                } catch (e:Error) {
                    trace(PURCHASE, "parsing error", event.code, e.message);
                }
                break;
            case RESTORE:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    ret = _context.call("getRestore", argsAsJSON.callbackId);
                    if (ret is ANEError) {
                        printANEError(ret as ANEError);
                        return;
                    }
                    callCallback(argsAsJSON.callbackId, ret);
                } catch (e:Error) {
                    trace(RESTORE, "parsing error", event.code, e.message);
                }
                break;
            case VERIFY_RECEIPT:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    if (argsAsJSON.hasOwnProperty("error") && argsAsJSON.error) {
                        var receipt_a:Receipt;
                        var status_a:int = 0;
                        if (argsAsJSON.error.hasOwnProperty("receipt")) receipt_a = ANEUtils.map(argsAsJSON.error.receipt, Receipt) as Receipt;
                        if (argsAsJSON.error.hasOwnProperty("status")) status_a = argsAsJSON.error.status;
                        rErr = new ReceiptError(argsAsJSON.error.text, argsAsJSON.error.type, receipt_a, status_a);
                    } else {
                        ret = ANEUtils.map(argsAsJSON.receipt, Receipt) as Receipt;
                    }
                    callCallback(argsAsJSON.callbackId, ret, rErr);
                } catch (e:Error) {
                    trace(VERIFY_RECEIPT, "parsing error", event.code, e.message);
                }
                break;
            case FETCH_RECEIPT:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    var receiptResult:FetchReceiptResult;
                    if (argsAsJSON.hasOwnProperty("error") && argsAsJSON.error) {
                        var receipt_b:Receipt;
                        var status_b:int = 0;
                        if (argsAsJSON.error.hasOwnProperty("receipt")) receipt_b = ANEUtils.map(argsAsJSON.error.receipt, Receipt) as Receipt;
                        if (argsAsJSON.error.hasOwnProperty("status")) status_b = argsAsJSON.error.status;
                        rErr = new ReceiptError(argsAsJSON.error.text, argsAsJSON.error.type, receipt_b, status_b);
                    } else {
                        receiptResult = new FetchReceiptResult(argsAsJSON.receiptData);
                    }
                    callCallback(argsAsJSON.callbackId, receiptResult, rErr);
                } catch (e:Error) {
                    trace(FETCH_RECEIPT, "parsing error", event.code, e.message);
                }
                break;
            case ON_CONSUME:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    callCallback(argsAsJSON.callbackId,
                            new BillingResult(argsAsJSON.data.billingResult.responseCode,
                                    argsAsJSON.data.billingResult.debugMessage),
                            argsAsJSON.data.purchaseToken);

                } catch (e:Error) {
                    trace(ON_CONSUME, "parsing error", event.code, e.message);
                }
                break;
            case ON_PRICE_CHANGE:
            case ON_ACKNOWLEDGE_PURCHASE:
            case ON_SETUP_FINISHED:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    callCallback(argsAsJSON.callbackId,
                            new BillingResult(argsAsJSON.data.billingResult.responseCode,
                                    argsAsJSON.data.billingResult.debugMessage));

                } catch (e:Error) {
                    trace(event.level, "parsing error", event.code, e.message);
                }
                break;
            case ON_SERVICE_DISCONNECTED:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    callCallback(argsAsJSON.callbackId);
                } catch (e:Error) {
                    trace(ON_SERVICE_DISCONNECTED, "parsing error", event.code, e.message);
                }
                break;
            case ON_QUERY_SKU:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    var skuDetailsList:Vector.<SkuDetails> = new Vector.<SkuDetails>();

                    for each(var j:String in argsAsJSON.data.skuDetailsList) {
                        skuDetailsList.push(new SkuDetails(j))
                    }
                    callCallback(argsAsJSON.callbackId, new BillingResult(argsAsJSON.data.billingResult.responseCode,
                            argsAsJSON.data.billingResult.debugMessage),
                            skuDetailsList);

                } catch (e:Error) {
                    trace(ON_QUERY_SKU, "parsing error", event.code, e.message);
                }
                break;
            case ON_PURCHASE_HISTORY:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    var purchasesList:Vector.<PurchaseHistoryRecord> = new Vector.<PurchaseHistoryRecord>();
                    for each(var j2:Object in argsAsJSON.data.purchasesList) {
                        purchasesList.push(new PurchaseHistoryRecord(j2.originalJson, j2.signature));
                    }
                    callCallback(argsAsJSON.callbackId, new BillingResult(argsAsJSON.data.billingResult.responseCode,
                            argsAsJSON.data.billingResult.debugMessage),
                            purchasesList);
                } catch (e:Error) {
                    trace(ON_PURCHASE_HISTORY, "parsing error", event.code, e.message);
                }
                break;
            case BillingEvent.ON_PURCHASES_UPDATED:
                try {
                    argsAsJSON = JSON.parse(event.code);
                    ret = InAppPurchaseANEContext.context.call("getOnPurchasesUpdates", argsAsJSON.callbackId);
                    if (ret is ANEError) {
                        printANEError(ret);
                        return;
                    }
                    InAppPurchase.billing().dispatchEvent(new BillingEvent(event.level, ret as PurchasesResult));
                } catch (e:Error) {
                    trace(BillingEvent.ON_PURCHASES_UPDATED, "parsing error", event.code, e.message);
                }
                break;
        }
    }

    /** @private */
    private static function printANEError(error:ANEError):void {
        trace("[" + NAME + "] Error: ", error.type, error.errorID, "\n", error.source, "\n", error.getStackTrace());
    }

    public static function dispose():void {
        if (_context == null) return;
        _isDisposed = true;
        trace("[" + NAME + "] Unloading ANE...");
        _context.removeEventListener(StatusEvent.STATUS, gotEvent);
        _context.dispose();
        _context = null;
    }

    public static function get isDisposed():Boolean {
        return _isDisposed;
    }

}
}