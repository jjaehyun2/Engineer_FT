/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-140852.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 140852;
var summary = 'String(number) = xxxx:0000 for some numbers';
var actual = '';
var expect = '';


//printBugNumber(BUGNUMBER);
//printStatus (summary);

var value;
 
value = 99999999999;
expect = '99999999999';
actual = value.toString();
Assert.expectEq(summary, expect, actual);

value = 100000000000;
expect = '100000000000';
actual = value.toString();
Assert.expectEq(summary, expect, actual);

value = 426067200000;
expect = '426067200000';
actual = value.toString();
Assert.expectEq(summary, expect, actual);