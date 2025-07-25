/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;

gTestfile = 'regress-6359.js';

/**
 *  File Name:          regress-6359.js
 *  Reference:          ** replace with bugzilla URL or document reference **
 *  Description:        ** replace with description of test **
 *  Author:             ** replace with your e-mail address **
 */

// var SECTION = "js1_2";       // provide a document reference (ie, ECMA section)
// var VERSION = "ECMA_2"; // Version of JavaScript or ECMA
// var TITLE   = "Regression test for bugzilla # 6359";       // Provide ECMA section title or a description
var BUGNUMBER = "http://bugzilla.mozilla.org/show_bug.cgi?id=6359";     // Provide URL to bugsplat or bugzilla report


/*
 * Calls to Assert.expectEq here. Assert.expectEq is a function that is defined
 * in shell.js and takes three arguments:
 * - a string representation of what is being tested
 * - the expected result
 * - the actual result
 *
 * For example, a test might look like this:
 *
 * var zip = /[\d]{5}$/;
 *
 * Assert.expectEq(
 * "zip = /[\d]{5}$/; \"PO Box 12345 Boston, MA 02134\".match(zip)",   // description of the test
 *  "02134",                                                           // expected result
 *  "PO Box 12345 Boston, MA 02134".match(zip) );                      // actual result
 *
 */

Assert.expectEq( '/(a*)b\1+/("baaac").length',
         2,
         /(a*)b\1+/("baaac").length );

Assert.expectEq( '/(a*)b\1+/("baaac")[0]',
         "b",
         /(a*)b\1+/("baaac")[0]);

Assert.expectEq( '/(a*)b\1+/("baaac")[1]',
         "",
         /(a*)b\1+/("baaac")[1]);


// displays results.