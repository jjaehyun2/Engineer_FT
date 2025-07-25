/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-271716-n.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 271716;
var summary = 'Don\'t Crash on infinite loop creating new Arrays';
var actual = 'Crash';
var expect = 'No Crash';

//printBugNumber(BUGNUMBER);
//printStatus (summary);
 
try
{
  a = new Array();
  while (1) a = new Array(a);
  actual = 'No Crash';
}
catch(e)
{
  actual = 'No Crash';
}

Assert.expectEq(summary, expect, actual);