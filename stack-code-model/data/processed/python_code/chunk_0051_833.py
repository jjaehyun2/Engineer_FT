/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;
import com.adobe.test.Utils;
//     var SECTION = "expression-004";
//     var VERSION = "JS1_4";
//     var TITLE   = "Property Accessors";

    var testcases = getTestCases();
    
function getTestCases() {
    var array = new Array();
    var item = 0;

    var OBJECT = new Property( "null", null, "null", 0 );

    var result    = "Failed";
    var exception = "No exception thrown";
    var expect    = "Passed";

    try {
        result = OBJECT.value.toString();
    } catch ( e ) {
        result = expect;
        exception = e.toString();
    }

    array[item++] = Assert.expectEq(
     // //    SECTION,
        "Get the toString value of an object whose value is null "+
        "(threw " + Utils.typeError(exception) +": null has no properties)",
        expect,
        result );

    return array;
}

function Property( object, value, string, number ) {
    this.object = object;
    this.string = String(value);
    this.number = Number(value);
    this.value = value;
}