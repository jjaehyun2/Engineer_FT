/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */


import StaticPropertyPackage.*;
import com.adobe.test.Assert;
import com.adobe.test.Utils;

// var SECTION = "Definitions";       // provide a document reference (ie, ECMA section)
// var VERSION = "AS3";  // Version of JavaScript or ECMA
// var TITLE   = "Access static method of base class";       // Provide ECMA section title or a description
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

var obj:AccStatPropViaSubClass = new AccStatPropViaSubClass();

// ********************************************
// Try to access a static property (in a namespace)
// of the base class via a reference to the subclass
// ********************************************
var thisError = "no exception thrown";
try{
    var date = obj.ns1::date;
} catch (e1) {
    thisError = e1.toString();
} finally {
    Assert.expectEq( "access static property in namespace of base class using subclass",
                Utils.REFERENCEERROR+1069,
                Utils.referenceError( thisError) );
}

// ********************************************
// Try to access a static property of the base
// class via a reference to the subclass
// ********************************************
thisError = "no exception thrown";
try{
    var str = obj.string;
} catch (e2) {
    thisError = e2.toString();
} finally {
    Assert.expectEq( "access static property of base class using subclass",
                Utils.REFERENCEERROR+1069,
                Utils.referenceError( thisError) );
}

// ********************************************
// Try to access the static property of the base
// class from an instance method in the subclass
// using "this.foo"
// ********************************************
var thisError = "no exception thrown";
try{
    var str = obj.getString();
} catch (e3) {
    thisError = e3.toString();
} finally {
    Assert.expectEq( "access static property of base class in subclass with this.foo",
                Utils.REFERENCEERROR+1069,
                Utils.referenceError( thisError) );
}

              // displays results.