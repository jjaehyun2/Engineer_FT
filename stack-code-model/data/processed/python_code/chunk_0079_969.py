/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-238881.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 238881;
var summary = 'const propagation for switch too aggressive';
var actual = '';
var expect = '';

//printBugNumber(BUGNUMBER);
//printStatus (summary);

const C=42;
function f(C,x)
{
  switch(x)
  {
  case C:
    return 1;
  default:
    return 0;
  }
}

actual = f(44,42);
expect = 0;
 
Assert.expectEq(summary, expect, actual);