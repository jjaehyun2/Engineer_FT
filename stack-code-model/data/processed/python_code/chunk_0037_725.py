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
import com.tuarua.iap.BillingClient;
import com.tuarua.iap.StoreKit;
import com.tuarua.iap.storekit.Purchase;
import com.tuarua.utils.os;

public class InAppPurchase {
    private static var _storeKit:StoreKit;
    private static var _billing:BillingClient;

    public function InAppPurchase() {
    }

    public static function storeKit():StoreKit {
        if (!os.isIos && !os.isOSX && !os.isTvos) {
            trace("StoreKit can only be created for iOS, macOS and tvOS");
            return null;
        }
        if (_storeKit == null) {
            var ret:* = InAppPurchaseANEContext.context.call("init");
            if (ret is ANEError) throw ret as ANEError;
            _storeKit = new StoreKit(ret as Vector.<Purchase>);
        }
        return _storeKit
    }

    public static function billing():BillingClient {
        if (!os.isAndroid) {
            trace("BillingClient can only be created for Android");
            return null;
        }
        if (_billing == null) {
            var ret:* = InAppPurchaseANEContext.context.call("init");
            if (ret is ANEError) throw ret as ANEError;
            _billing = new BillingClient();
        }
        return _billing
    }

    public static function dispose():void {
        if (InAppPurchaseANEContext.context) {
            InAppPurchaseANEContext.dispose();
        }
    }
}
}