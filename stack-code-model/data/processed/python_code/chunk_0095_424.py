/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-330812.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 330812;
var summary = 'Making Array(1<<29).sort() less problematic';
var actual = 'No Crash';
var expect = 'No Crash';

//printBugNumber(BUGNUMBER);
//printStatus (summary);


//printStatus('This test passes if the browser does not hang or crash');
//printStatus('This test expects exit code 0 or 3 to indicate out of memory');

try
{
  var result = Array(1 << 29).sort();
}
catch(ex)
{
  // handle changed 1.9 branch behavior. see bug 422348
  expect = 'InternalError: allocation size overflow';
  actual = ex + '';
}

Assert.expectEq(summary, expect, actual);