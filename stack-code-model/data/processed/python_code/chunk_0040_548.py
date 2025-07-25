/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;

//     var SECTION = "15.6.4.2-2";
//     var VERSION = "ECMA_1";
//     var TITLE   = "Boolean.prototype.toString()"

    var testcases = getTestCases();

function getTestCases() {
    var array = new Array();
    var item = 0;

    tostr=Boolean.prototype.toString;
    Boolean.prototype.toString=tostr;
    x=new Boolean();
    array[item++] = Assert.expectEq(   
                                    "tostr=Boolean.prototype.toString; Boolean.prototype.toString=tostr;x=new Boolean();x.toString()",
                                    "false",
                                    x.toString());

    tostr=Boolean.prototype.toString;
    Boolean.prototype.toString=tostr;
    x=new Boolean(true);
    array[item++] = Assert.expectEq(   
                                    "tostr=Boolean.prototype.toString; Boolean.prototype.toString=tostr;x=new Boolean(true);x.toString()",
                                    "true",
                                    x.toString());

    tostr = Boolean.prototype.toString;
    Boolean.prototype.toString=tostr;
    x=new Boolean(false);
    array[item++] = Assert.expectEq( 
                                    "tostr=Boolean.prototype.toString; Boolean.prototype.toString=tostr;x=new Boolean(false);x.toString()",
                                    "false",
                                    x.toString());
    return (array);

}