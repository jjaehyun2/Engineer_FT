/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


/*
 * Date: 07 July 2001
 *
 * SUMMARY: Regression test for Bugzilla bug 89474
 * See http://bugzilla.mozilla.org/show_bug.cgi?id=89474
 *
 * This test used to crash the JS shell. This was discovered
 * by Darren DeRidder <darren.deridder@icarusproject.com
 */
//-----------------------------------------------------------------------------
var gTestfile = 'regress-89474.js';
var BUGNUMBER = 89474;
var summary = "Testing the JS shell doesn't crash on it.item()";
var cnTest = 'it.item()';


//-----------------------------------------------------------------------------
addtestcases();
//-----------------------------------------------------------------------------


function addtestcases()
{

  //printBugNumber(BUGNUMBER);
  //printStatus (summary);

  tryThis(cnTest); // Just testing that we don't crash on this

  Assert.expectEq('', 'No Crash', 'No Crash');


}


function tryThis(sEval)
{
  try
  {
    eval(sEval);
  }
  catch(e)
  {
    // If we get here, we didn't crash.
  }
}