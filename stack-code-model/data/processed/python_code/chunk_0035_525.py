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
/** An object representing a person in the context of search results. */
public class Person {
    private var _displayName:String;
    private var _handles:Vector.<String>;
    private var _handleIdentifier:String;
    private var _contactIdentifier:String;

    /**
     * @param displayName optional display name for displaying this recipient
     * @param handles An array of contact handles, e.g. phone numbers
     * @param handleIdentifier A ContactKey to identify the type of of handle, e.g. ContactKey.phoneNumbers
     */
    public function Person(displayName:String, handles:Vector.<String>, handleIdentifier:String) {
        this._displayName = displayName;
        this._handles = handles;
        this._handleIdentifier = handleIdentifier;
    }
    /** An optional display name for displaying this recipient */
    public function get displayName():String {
        return _displayName;
    }
    /** An array of contact handles, e.g. phone numbers */
    public function get handles():Vector.<String> {
        return _handles;
    }
    /** A ContactKey to identify the type of of handle, e.g. ContactKey.phoneNumbers */
    public function get handleIdentifier():String {
        return _handleIdentifier;
    }
    /** If the property has already been resolved, the identifier for the Contact */
    public function get contactIdentifier():String {
        return _contactIdentifier;
    }

    public function set contactIdentifier(value:String):void {
        _contactIdentifier = value;
    }
}
}