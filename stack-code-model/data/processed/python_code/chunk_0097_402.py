/* Copyright 2018 Tua Rua Ltd.

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

package com.tuarua.spotlight {
import com.tuarua.*;
import com.tuarua.fre.ANEError;

import flash.events.EventDispatcher;
import flash.system.Capabilities;
/** The on-device index.*/
public class SearchableIndex extends EventDispatcher {
    private var id:String;
    private static const platform:String = Capabilities.version.substr(0, 3).toLowerCase();
    private static const isOSX:Boolean = platform == "mac";
    private static const isIos:Boolean = platform == "ios" && Capabilities.os.toLowerCase().indexOf("tvos") == -1;

    public function SearchableIndex(name:String = null) {
        id = SpotlightANEContext.context.call("createGUID") as String;
        var ret:* = SpotlightANEContext.context.call("initIndex", id, name);
        if (ret is ANEError) throw ret as ANEError;
    }

    /** Not all devices support indexing.  Read this property to check if indexing is supported on the current device. */
    public static function get isIndexingAvailable():Boolean {
        if (!isOSX && !isIos) return false;
        var ret:* = SpotlightANEContext.context.call("isIndexingAvailable");
        if (ret is ANEError) throw ret as ANEError;
        return ret as Boolean;
    }

    /** Call this method to add or update items in the index. */
    public function indexSearchableItems(items:Vector.<SearchableItem>, completionHandler:Function):void {
        var ret:* = SpotlightANEContext.context.call("indexSearchableItems", id, items,
                SpotlightANEContext.createCallback(completionHandler));
        if (ret is ANEError) throw ret as ANEError;
    }

    /** Call this method on the index to remove any items from the index with the given identifiers or domain identifiers.
     * The delete is recursive so if domain identifiers are of the form account-id.mailbox-id, for example,
     * calling delete with account-id will delte all the searchable items with that account and any mailbox. */
    public function deleteSearchableItems(identifiers:Vector.<String> = null, domainIdentifiers:Vector.<String> = null,
                                          completionHandler:Function = null):void {
        if (identifiers == null && domainIdentifiers == null) {
            throw new ArgumentError("pass either identifiers or domainIdentifiers");
        }
        var ret:* = SpotlightANEContext.context.call("deleteSearchableItems", id, identifiers,
                domainIdentifiers, SpotlightANEContext.createCallback(completionHandler));
        if (ret is ANEError) throw ret as ANEError;
    }

    /** Call this method to delete all searchable items from the index. */
    public function deleteAllSearchableItems(completionHandler:Function = null):void {
        var ret:* = SpotlightANEContext.context.call("deleteAllSearchableItems", id,
                SpotlightANEContext.createCallback(completionHandler));
        if (ret is ANEError) throw ret as ANEError;
    }

    public static function get spotlightId():String {
        var ret:* = SpotlightANEContext.context.call("getSpotlightId");
        if (ret is ANEError) throw ret as ANEError;
        return ret as String;
    }

    /** Dispose of associated native objects */
    public function dispose():void {
        var ret:* = SpotlightANEContext.context.call("disposeIndex", id);
        if (ret is ANEError) throw ret as ANEError;
    }

}
}