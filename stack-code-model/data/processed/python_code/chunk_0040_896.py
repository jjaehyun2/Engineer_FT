/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
 
 

import FinalPublicDynamicClassMethodAndProp.*;
import com.adobe.test.Assert;

// var SECTION = "Definitions";           // provide a document reference (ie, ECMA section)
// var VERSION = "AS3";                   // Version of JavaScript or ECMA
// var TITLE   = "Access Class Properties & Methods";  // Provide ECMA section title or a description
var BUGNUMBER = "";




var arr = new Array(1,2,3);

var Obj = new AccFinPubDynClassMAndP();

var d = new Date();

var f = new Function();

var str = "Test";

var ob = new Object();


// ********************************************
// access default method
//
// ********************************************

Assert.expectEq( "*** Access default method of a class ***", 1, 1 );
Assert.expectEq( "Obj.setArray(arr), Obj.getArray()", arr, Obj.testGetSetArray(arr) );


// ********************************************
// access private method
//
// ********************************************

// TODO: Need to modify the test to only create the date as Date(0) and just check the year
// Assert.expectEq( "*** Access private method of a class ***", 1, 1 );
// Assert.expectEq( "Obj.setPrivDate(date), Obj.getPrivDate()", d, Obj.testGetSetPrivDate(d) );


// ********************************************
// access public method
//
// ********************************************

Assert.expectEq( "*** Access public method of a class ***", 1, 1 );
Assert.expectEq( "Obj.setPubBoolean(b), Obj.getPubBoolean()", true, (Obj.setPubBoolean(true), Obj.getPubBoolean()) );


// ********************************************
// access static method
//
// ********************************************

Assert.expectEq( "*** Access static method of a class ***", 1, 1 );
Assert.expectEq( "Obj.setStatFunction(f), Obj.getStatFunction()", f, Obj.testGetSetStatFunction(f) );

// ********************************************
// access private static method
// ********************************************

Assert.expectEq( "*** Access private static method of a class ***", 1, 1 );
Assert.expectEq( "Obj.setPrivStatString(s), Obj.getPrivStatString", str, Obj.testGetSetPrivStatString(str) );


// ********************************************
// access public static method
// ********************************************

Assert.expectEq( "*** Access public static method of a class ***", 1, 1 );
Assert.expectEq( "AccFinPubDynClassMAndP.setPubStatObject(ob), AccFinPubDynClassMAndP.getPubStatObject()", ob,
    (AccFinPubDynClassMAndP.setPubStatObject(ob), AccFinPubDynClassMAndP.getPubStatObject()) );


// ********************************************
// access final method
// ********************************************

Assert.expectEq( "*** Access final method of a class ***", 1, 1 );
Assert.expectEq( "Obj.setFinNumber(10), Obj.getFinNumber()", 10, Obj.testGetSetFinNumber(10) );


// ********************************************
// access public final method
// ********************************************

Assert.expectEq( "*** Access public final method of a class ***", 1, 1 );
Assert.expectEq( "Obj.setPubFinArray(arr), Obj.getPubFinArray()", arr, (Obj.setPubFinArray(arr), Obj.getPubFinArray()) );


// ********************************************
// access public property
// ********************************************

Assert.expectEq( "*** Access public property of a class ***", 1, 1 );
Assert.expectEq( "Obj.pubBoolean = true, Obj.pubBoolean", true, (Obj.pubBoolean = true, Obj.pubBoolean) );

// ********************************************
// access public static property
// ********************************************

Assert.expectEq( "*** Access public satic property of a class ***", 1, 1 );
Assert.expectEq( "AccFinPubDynClassMAndP.pubStatObject = ob, AccFinPubDynClassMAndP.pubStatObject", ob, (AccFinPubDynClassMAndP.pubStatObject = ob, AccFinPubDynClassMAndP.pubStatObject) );


// ********************************************
// access public final property
// ********************************************

Assert.expectEq( "*** Access public final property of a class ***", 1, 1 );
Assert.expectEq( "Obj.pubFinArray = arr, Obj.pubFinArray", arr, (Obj.pubFinArray = arr, Obj.pubFinArray) );



              // displays results.