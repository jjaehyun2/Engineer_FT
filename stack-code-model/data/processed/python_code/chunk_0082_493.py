/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;

//     var SECTION = "e11_2_3_5_n";
//     var VERSION = "ECMA_1";
//     var TITLE   = "Function Calls";


    var testcases = getTestCases();


function getTestCases() {
    var array = new Array();
    var item = 0;
    
    array[item++] = Assert.expectEq(  "true.valueOf()", true, true.valueOf() );
    
    return array;
}