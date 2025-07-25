/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */


// var SECTION = "Definitions";       // provide a document reference (ie, ECMA section)
// var VERSION = "Clean AS2";  // Version of JavaScript or ECMA
// var TITLE   = "Extend Public Class Implement Default interface";       // Provide ECMA section title or a description
var BUGNUMBER = "";


/**
 * Calls to Assert.expectEq here. Assert.expectEq is a function that is defined
 * in shell.js and takes three arguments:
 * - a string representation of what is being tested
 * - the expected result
 * - the actual result
 *
 * For example, a test might look like this:
 *
 * var helloWorld = "Hello World";
 *
 * Assert.expectEq(
 * "var helloWorld = 'Hello World'",   // description of the test
 *  "Hello World",                     // expected result
 *  helloWorld );                      // actual result
 *
 */

import  PublicClass.*;

import com.adobe.test.Assert;
var obj = new accFinExtPublicImplDefDefPub();

Assert.expectEq( "*** public method implemented interface ***", 1, 1 );
Assert.expectEq( "iGetPubBoolean", false, obj.acciGetPubBoolean() );

Assert.expectEq( "*** public method implemented interface ***", 2, 2 );
Assert.expectEq( "iGetPubNumber", 5 , obj.acciGetPubNumber() );
Assert.expectEq( "iiGetNumber1", 5 , obj.acciiGetNumber1() );
Assert.expectEq( "jiGetNumber1", 5 , obj.accjiGetNumber1() );
//*******************************************
// Default Methods and Default properties
//
// call a defualt Method of an object that
// inherited it from it's parent class
//*******************************************

var arr = new Array(1, 2, 3);
var date = new Date(0);
var func = function() {};
var num = new Number();
var obj = new Object();
var str = new String("test");

Assert.expectEq( "*** Default Methods and Default properites of extended class ***", 1, 1 );
Assert.expectEq( "testGetSubArray(arr)", arr, testGetSubArray(arr) );

//*******************************************
// public Methods and public properties
//
// call a public Method of an object that
// inherited it from it's parent class
//*******************************************

arr = new Array(1, 2, 3);
date = new Date(0);
func = function() {}
num = new Number();
obj = new Object();
str = new String("test");

var EXTDCLASS = new PublicClass();

// ********************************************
// access default method from a default
// method of a sub class
//
// ********************************************
//print(testGetSubArray(arr));
Assert.expectEq( "*** Access default method from default method of sub class ***", 1, 1 );
Assert.expectEq( "testGetSubArray(arr)", arr, testGetSubArray(arr) );

// <TODO>  fill in the rest of the cases here


// ********************************************
// access default method from a public
// method of a sub class
//
// ********************************************

Assert.expectEq( "*** Access default method from public method of sub class ***", 1, 1 );
Assert.expectEq( "pubSubSetArray(arr), pubSubGetArray()", arr, (pubSubSetArray(arr), pubSubGetArray()) );

// <TODO>  fill in the rest of the cases here

// ********************************************
// access default method from a private
// method of a sub class
//
// ********************************************

Assert.expectEq( "*** Access default method from private method of sub class ***", 1, 1 );
Assert.expectEq( "testPrivSubArray(arr)", arr, testPrivSubArray(arr) );

// <TODO>  fill in the rest of the cases here


              // displays results.