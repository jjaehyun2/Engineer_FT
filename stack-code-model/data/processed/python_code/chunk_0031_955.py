/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

import DefaultClass.*;
import com.adobe.test.Assert;


// var SECTION = "Definitions";                                // provide a document reference (ie, ECMA section)
// var VERSION = "AS 3.0";                                 // Version of JavaScript or ECMA
// var TITLE   = "Override default function in final class extending default class";       // Provide ECMA section title or a description
var BUGNUMBER = "";



var CLASSDEFN = new FinExtDefaultOverRideDefault();
var myNum = 55;

Assert.expectEq( "CLASSDEFN.setGetNumber(myNum)", 75, CLASSDEFN.setGetNumber(myNum) );
Assert.expectEq( "CLASSDEFN.orSet", "PASSED", CLASSDEFN.orSet );
Assert.expectEq( "CLASSDEFN.orGet", "PASSED", CLASSDEFN.orGet );


            // This function is for executing the test case and then
            // displaying the result on to the console or the LOG file.