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
import com.tuarua.SpotlightANEContext;
import com.tuarua.fre.ANEError;

/** A search query object manages the criteria to apply when searching app content that you have previously
 * indexed using the Core Spotlight APIs.
 * See https://developer.apple.com/documentation/corespotlight/cssearchquery
 * */
public class SearchQuery {
    private var id:String;

    /**
     * @param queryString a formatted query string See https://developer.apple.com/documentation/corespotlight/cssearchquery
     * @param attributes an array of attribute names that correspond to properties defined by SearchableItemAttributeSet
     */
    public function SearchQuery(queryString:String, attributes:Vector.<String> = null) {
        id = SpotlightANEContext.context.call("createGUID") as String;
        var ret:* = SpotlightANEContext.context.call("initQuery", id, queryString, attributes);
        if (ret is ANEError) throw ret as ANEError;
    }

    /** Asynchronously queries the index for items that match the query object’s specifications. */
    public function start(completionHandler:Function):void {
        var ret:* = SpotlightANEContext.context.call("startQuery", id,
                SpotlightANEContext.createCallback(completionHandler));
        if (ret is ANEError) throw ret as ANEError;
    }

    /** Cancels a query operation. */
    public function cancel():void {
        var ret:* = SpotlightANEContext.context.call("cancelQuery", id);
        if (ret is ANEError) throw ret as ANEError;
    }

    public function dispose():void {
        var ret:* = SpotlightANEContext.context.call("disposeQuery", id);
        if (ret is ANEError) throw ret as ANEError;
    }
}
}