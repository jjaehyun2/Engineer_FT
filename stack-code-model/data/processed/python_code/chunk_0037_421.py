/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package DynamicClass{

/**
 * The 'import' statements should be the first
 * non-comment line in a file.
 *
 * These lines have to be commented out.
 * The compiler requires only the parent Class to be imported and not the Subclass folder.
 * Hence change in the import statements required.
 *  import Definitions.Classes.Simple;
 *  import Definitions.Classes.Ext.FinExtDynamicClass;
 */
import DynamicClass.*;
import com.adobe.test.Assert;



// var SECTION = "Definitions\Ext";                // provide a document reference (ie, ECMA section)
// var VERSION = "AS3";                    // Version of JavaScript or ECMA
// var TITLE   = "Final Class Extends Dynamic Class Default Methods";      // Provide ECMA section title or a description
//var BUGNUMBER = "";


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

/**
 * The 'import' statements should be the first
 * non-comment line in a file.
 * import Definitions.Classes.Simple;
 * import Definitions.Classes.Ext.FinExtDynamicClass;
 *
 */


// Can't create an instance because it's not public
// Hence commenting out the lines where the class is initialized.
// var EXTDCLASS = new FinExtDynamicClass();


// Create an array variable which will define the test array to be used
// for the given output.
var arr = new Array(1, 2, 3);


// access default method from outside of the class
Assert.expectEq( "*** Access the default method from outside of the class ***", 1, 1 );
//Assert.expectEq( "setArray(arr), getArray()", arr, ( setArray( arr ), getArray() ) );


// access default method from a default method of a sub class
Assert.expectEq( "*** Access default method from default method of sub class ***", 1, 1 );
Assert.expectEq( "subSetArray( arr ), subGetArray()", arr, ( subSetArray( arr ), subGetArray() ) );


// access default method from a dynamic method of a sub class
Assert.expectEq( "*** Acess default method from dynamic method of sub class ***", 1, 1 );
Assert.expectEq( "dynSubSetArray( arr ), dynSubGetArray()", arr, ( dynSubSetArray( arr ), dynSubGetArray()) );


// access default method from a public method of a sub class
Assert.expectEq( "*** Access default method from public method of sub class ***", 1, 1 );
Assert.expectEq( "pubSubSetArray( arr ), pubSubGetArray()", arr, ( pubSubSetArray( arr ), pubSubGetArray()) );


// access default method from a private method of a sub class
Assert.expectEq( "*** Access default method from private method of sub class ***", 1, 1 );
Assert.expectEq( "testPrivSubArray( arr )", arr, testPrivSubArray( arr ) );


// access default method from a static method of a sub class
Assert.expectEq( "*** Access default method from static method of sub class ***", 1, 1 );
Assert.expectEq( "*** Static Method cannot access any other methods except static methods of the parent class ***", 1, 1 );
// Assert.expectEq( "statSubSetArray( arr ), statSubGetArray()", arr, ( statSubSetArray( arr ), statSubGetArray() ) );


// access default method from a final method of a sub class
Assert.expectEq( "*** Access default method from final method of sub class ***", 1, 1 );
Assert.expectEq( "finSubSetArray( arr ), finSubGetArray()", arr, ( finSubSetArray( arr ), finSubGetArray() ) );


// access default method from a virtual method of a sub class
Assert.expectEq( "*** Access default method from virtual method of sub class ***", 1, 1 );
Assert.expectEq( "virSubSetArray( arr ), virSubSetArray()", arr, ( virSubSetArray( arr ), virSubGetArray() ) );


// access default method from a public dynamic method of a sub class
Assert.expectEq( "*** Acess default method from public dynamic method of sub class ***", 1, 1 );
Assert.expectEq( "pubDynSubSetArray( arr ), pubDynSubGetArray()", arr, ( pubDynSubSetArray( arr ), pubDynSubGetArray()) );


// access default method from a public static method of a sub class
Assert.expectEq( "*** Access default method from public static method of sub class ***", 1, 1 );
Assert.expectEq( "*** Static Method cannot access any other methods except static methods of the parent class ***", 1, 1 );
// Assert.expectEq( "pubStatSubSetArray( arr ), pubStatSubGetArray()", arr, ( pubStatSubSetArray( arr ), pubStatSubGetArray() ) );


// access default method from a public final method of a sub class
Assert.expectEq( "*** Access default method from public final method of sub class ***", 1, 1 );
Assert.expectEq( "pubFinSubSetArray( arr ), pubFinSubGetArray()", arr, ( pubFinSubSetArray( arr ), pubFinSubGetArray() ) );


// access default method from a public virtual method of a sub class
Assert.expectEq( "*** Access default method from public virtual method of sub class ***", 1, 1 );
Assert.expectEq( "pubVirSubSetArray( arr ), pubVirSubSetArray()", arr, ( pubVirSubSetArray( arr ), pubVirSubGetArray() ) );


// access default method from a final private method of a sub class
Assert.expectEq( "*** Access default method from final private method of sub class ***", 1, 1 );
Assert.expectEq( "testPrivFinSubArray( arr )", arr, testPrivFinSubArray( arr ) );


// access default method from a final static method of a sub class
Assert.expectEq( "*** Access default method from final static method of sub class ***", 1, 1 );
Assert.expectEq( "*** Static Method cannot access any other methods except static methods of the parent class ***", 1, 1 );
// Assert.expectEq( "finStatSubSetArray( arr ), finStatSubGetArray()", arr, ( finStatSubSetArray( arr ), finStatSubGetArray() ) );


// access default method from a private static method of a sub class
Assert.expectEq( "*** Access default method from private static method of sub class ***", 1, 1 );
Assert.expectEq( "*** Static Method cannot access any other methods except static methods of the parent class ***", 1, 1 );
// Assert.expectEq( "testPrivStatSubArray( arr )", arr, testPrivStatSubArray( arr ) );


// access default method from a private virtual method of a sub class
Assert.expectEq( "*** Access default method from private virtual method of sub class ***", 1, 1 );
Assert.expectEq( "testPrivVirSubArray( arr )", arr, testPrivVirSubArray( arr ) );



// access default property from outside the class
Assert.expectEq( "*** Access default property from outside the class ***", 1, 1 );
Assert.expectEq( "array = arr", arr, (array = arr, array) );


// access default property from a default method of a sub class
Assert.expectEq( "*** Access default property from default method of sub class ***", 1, 1 );
Assert.expectEq( "subSetDPArray( arr ), subGetDPArray()", arr, ( subSetDPArray( arr ), subGetDPArray() ) );


// access default property from a dynamic method of a sub class
Assert.expectEq( "*** Access default property from dynamic method of sub class ***", 1, 1 );
Assert.expectEq( "dynSubSetDPArray( arr ), dynSubGetDPArray()", arr, ( dynSubSetDPArray( arr ), dynSubGetDPArray() ) );


// access default property from a public method of a sub class
Assert.expectEq( "*** Access default property from public method of sub class ***", 1, 1 );
Assert.expectEq( "pubSubSetDPArray( arr ), pubSubGetDPArray()", arr, ( pubSubSetDPArray( arr ), pubSubGetDPArray() ) );


// access default property from a private method of a sub class
Assert.expectEq( "*** Access default property from private method of sub class ***", 1, 1 );
Assert.expectEq( "testPrivSubDPArray( arr )", arr, testPrivSubDPArray( arr ) );


// access default property from a static method of a sub class
Assert.expectEq( "*** Access default property from static method of sub class ***", 1, 1 );
Assert.expectEq( "statSubSetDPArray( arr ), statSubGetDPArray()", arr, ( statSubSetDPArray( arr ), statSubGetDPArray() ) );


// access default property from a final method of a sub class
Assert.expectEq( "*** Access default property from final method of sub class ***", 1, 1 );
Assert.expectEq( "finSubSetDPArray( arr ), finSubGetDPArray()", arr, ( finSubSetDPArray( arr ), finSubGetDPArray() ) );


// access default property from a private virtual method of a sub class
Assert.expectEq( "*** Access default property from private virtual method of sub class ***", 1, 1 );
Assert.expectEq( "virSubSetDPArray( arr ), virSubGetDPArray()", arr, ( virSubSetDPArray( arr ), virSubGetDPArray() ) );


// access default property from a public static method of a sub class
Assert.expectEq( "*** Access default property from public static method of sub class ***", 1, 1 );
Assert.expectEq( "pubStatSubSetDPArray( arr ), pubStatSubGetDPArray()", arr, ( pubStatSubSetDPArray( arr ), pubStatSubGetDPArray() ) );


// access default property from a private static method of a sub class
Assert.expectEq( "*** Access default property from private static method of sub class ***", 1, 1 );
Assert.expectEq( "testPrivStatSubDPArray( arr )", arr, testPrivStatSubDPArray( arr ) );


// ********************************************
// Class Prototype Testing
// ********************************************

//Add new property to parent through prototype object, verify child inherits it
var child = new FinExtDynamicClass();
DynamicClassInner.prototype.fakeProp = 100;
Assert.expectEq("*** Add new property to parent prototype object, verify child class inherits it ***", 100, child.fakeProp);

//Try overriding parent property through prototype object, verify child object has correct value
DynamicClassInner.prototype.pObj = 2;
child = new FinExtDynamicClass();
Assert.expectEq("*** Try overriding parent property through prototype object, verify child object has correct value ***", 1, child.pObj);

            // This function is for executing the test case and then
            // displaying the result on to the console or the LOG file.
}