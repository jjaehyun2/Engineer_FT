/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


// var SECTION = "Directives\const";                   // provide a document reference (ie, ECMA section)
// var VERSION = "ActionScript 3.0";               // Version of JavaScript or ECMA
// var TITLE   = "using const inside a class without methods";     // Provide ECMA section title or a description
var BUGNUMBER = "";




/*===========================================================================*/

// Test case for checking the CONST keyword.

class MyConstClass {

    // Using 'const' only in place of 'var' is not an error.
    const myVar = 10;
}

var Obj = new MyConstClass();

Assert.expectEq("class MyConstClass { const myVar = 10; }; var Obj = new MyConstClass(); Obj.myVar;", 10, Obj.myVar );


            // This function is for executing the test case and then
            // displaying the result on to the console or the LOG file.