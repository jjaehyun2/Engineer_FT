/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-451884.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 451884;
var summary = 'Do not crash [@ QuoteString]';
var actual = 'No Crash';
var expect = 'No Crash';


//-----------------------------------------------------------------------------
addtestcases();
//-----------------------------------------------------------------------------

function addtestcases()
{

  //printBugNumber(BUGNUMBER);
  //printStatus (summary);

  try
  {
    (function(k){eval("k.y")})();
  }
  catch(ex)
  {
  }

  Assert.expectEq(summary, expect, actual);


}