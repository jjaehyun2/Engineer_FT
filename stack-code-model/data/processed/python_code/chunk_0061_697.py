/* ***** BEGIN LICENSE BLOCK *****
 * Version: MPL 1.1/GPL 2.0/LGPL 2.1
 *
 * The contents of this file are subject to the Mozilla Public License Version
 * 1.1 (the "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 * http://www.mozilla.org/MPL/
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 * for the specific language governing rights and limitations under the
 * License.
 *
 * The Original Code is [Open Source Virtual Machine.].
 *
 * The Initial Developer of the Original Code is
 * Adobe System Incorporated.
 * Portions created by the Initial Developer are Copyright (C) 2004-2006
 * the Initial Developer. All Rights Reserved.
 *
 * Contributor(s):
 *   Adobe AS3 Team
 *
 * Alternatively, the contents of this file may be used under the terms of
 * either the GNU General Public License Version 2 or later (the "GPL"), or
 * the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
 * in which case the provisions of the GPL or the LGPL are applicable instead
 * of those above. If you wish to allow use of your version of this file only
 * under the terms of either the GPL or the LGPL, and not to allow others to
 * use your version of this file under the terms of the MPL, indicate your
 * decision by deleting the provisions above and replace them with the notice
 * and other provisions required by the GPL or the LGPL. If you do not delete
 * the provisions above, a recipient may use your version of this file under
 * the terms of any one of the MPL, the GPL or the LGPL.
 *
 * ***** END LICENSE BLOCK ***** */


import DefaultClass.*;

var SECTION = "Definitions";       			// provide a document reference (ie, ECMA section)
var VERSION = "AS3";  					// Version of JavaScript or ECMA
var TITLE   = "Public Class Extends Default Class";      // Provide ECMA section title or a description
var BUGNUMBER = "";

startTest();                // leave this alone

/**
 * Calls to AddTestCase here. AddTestCase is a function that is defined
 * in shell.js and takes three arguments:
 * - a string representation of what is being tested
 * - the expected result
 * - the actual result
 *
 * For example, a test might look like this:
 *
 * var helloWorld = "Hello World";
 *
 * AddTestCase(
 * "var helloWorld = 'Hello World'",   // description of the test
 *  "Hello World",                     // expected result
 *  helloWorld );                      // actual result
 *
 */

var EXTDCLASS = new DynExtDefaultClassPub();
var arr = new Array(10, 15, 20, 25, 30);
  
// *******************************************
//  access public method of parent class from 
//  outside of class
// *******************************************

AddTestCase( "*** Access from outside of class ***", 1, 1 );
AddTestCase( "EXTDCLASS.setPubArray(arr), EXTDCLASS.getPubArray", arr, (EXTDCLASS.setPubArray(arr), EXTDCLASS.getPubArray()) );


// ********************************************
// access public method from a default
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from default method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testSubArray(arr)", arr, (EXTDCLASS.testSubArray(arr)) );


// ********************************************
// access public method from a public 
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from public method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.pubSubSetArray(arr), EXTDCLASS.pubSubGetArray()", arr, (EXTDCLASS.pubSubSetArray(arr), EXTDCLASS.pubSubGetArray()) );


// ********************************************
// access public method from a private 
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from private method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPrivSubArray(arr)", arr, EXTDCLASS.testPrivSubArray(arr) );


// ********************************************
// access public method from a final 
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from final method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testFinSubArray(arr)", arr, (EXTDCLASS.testFinSubArray(arr)) );

// ********************************************
// access public method from a final 
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from final method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPubFinSubArray(arr)", arr, (EXTDCLASS.testPubFinSubArray(arr)) );

// ********************************************
// access public method from a final 
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from final method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPrivFinSubArray(arr)", arr, (EXTDCLASS.testPrivFinSubArray(arr)) );

// ********************************************
// access public method from a virtual 
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from virtual method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testVirSubArray(arr)", arr, (EXTDCLASS.testVirSubArray(arr)) );

// ********************************************
// access public method from a public virtual 
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from public virtual method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPubVirSubArray(arr)", arr, (EXTDCLASS.testPubVirSubArray(arr)) );

// ********************************************
// access public method from a private virtual 
// method of a sub class
//
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public method from private virtual method of sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPrivVirSubArray(arr)", arr, (EXTDCLASS.testPrivVirSubArray(arr)) );



// ********************************************
// access public property from outside
// the class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from outside the class ***", 1, 1 );
AddTestCase( "EXTDCLASS.pubArray = arr", arr, (EXTDCLASS.pubArray = arr, EXTDCLASS.pubArray) );


// ********************************************
// access public property from 
// default method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from default method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testSubDPArray(arr)", arr, (EXTDCLASS.testSubDPArray(arr)) );


// ********************************************
// access public property from 
// public method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from public method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.pubSubSetDPArray(arr), EXTDCLASS.pubSubGetDPArray()", arr, (EXTDCLASS.pubSubSetDPArray(arr), EXTDCLASS.pubSubGetDPArray()) );


// ********************************************
// access public property from 
// private method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from private method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPrivDPArray(arr)", arr, (EXTDCLASS.testPrivDPArray(arr)) );


// ********************************************
// access public property from 
// final method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from final method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testFinDPArray(arr)", arr, (EXTDCLASS.testFinDPArray(arr)) );

// ********************************************
// access public property from 
// public final method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from public final method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPubFinDPArray(arr)", arr, (EXTDCLASS.testPubFinDPArray(arr)) );

// ********************************************
// access public property from 
// private final method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from private final method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPrivFinDPArray(arr)", arr, (EXTDCLASS.testPrivFinDPArray(arr)) );

// ********************************************
// access public property from 
// virtual method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from final method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testVirDPArray(arr)", arr, (EXTDCLASS.testVirDPArray(arr)) );

// ********************************************
// access public property from 
// public virtual method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from public final method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPubVirDPArray(arr)", arr, (EXTDCLASS.testPubVirDPArray(arr)) );

// ********************************************
// access public property from 
// private virtual method in sub class
// ********************************************

EXTDCLASS = new DynExtDefaultClassPub();
AddTestCase( "*** Access public property from private final method in sub class ***", 1, 1 );
AddTestCase( "EXTDCLASS.testPrivVirDPArray(arr)", arr, (EXTDCLASS.testPrivVirDPArray(arr)) );


test();       // leave this alone.  this executes the test cases and
              // displays results.