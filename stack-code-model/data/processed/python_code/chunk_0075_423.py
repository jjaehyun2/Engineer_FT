/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;
//     var SECTION = "15.7.3.6-4";
//     var VERSION = "ECMA_1";
//     var TITLE   = "Number.POSITIVE_INFINITY";


    var testcases = getTestCases();

function getTestCases() {
    var array = new Array();
    var item = 0;

    string = '';
    for ( prop in Number ) { string += ( prop == 'POSITIVE_INFINITY' ) ? prop : ''; }

    array[item++] = Assert.expectEq(
                    //SECTION,
                    "var string = ''; for ( prop in Number ) { string += ( prop == 'POSITIVE_INFINITY' ) ? prop : '' } string;",
                    "",
                    string
                    );

    return ( array );
}