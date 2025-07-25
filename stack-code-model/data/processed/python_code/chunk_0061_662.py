/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


/*
 *
 * Date:    10 December 2001
 * SUMMARY: Regression test for bug 114493
 * See http://bugzilla.mozilla.org/show_bug.cgi?id=114493
 *
 * Rhino crashed on this code. It should produce a syntax error, not a crash.
 * Note that "3"[5] === undefined, and Rhino correctly gave an error if you
 * tried to use the call operator on |undefined|:
 *
 *      js> undefined();
 *      js: TypeError: undefined is not a function.
 *
 * However, Rhino CRASHED if you tried to do "3"[5]().
 *
 * Rhino would NOT crash if you tried "3"[0]() or "3"[5]. Only array indices
 * that were out of bounds, followed by the call operator, would crash.
 *
 */
//-----------------------------------------------------------------------------
var gTestfile = 'regress-114493.js';
var UBound = 0;
var BUGNUMBER = 114493;
var summary = 'Regression test for bug 114493';
var status = '';
var statusitems = [];
var actual = '';
var actualvalues = [];
var expect= '';
var expectedvalues = [];
var sEval = '';


//status = inSection(1);
actual = 'Program execution did NOT fall into catch-block';
expect = 'Program execution fell into into catch-block';
try
{
  sEval = '"3"[5]()';
  eval(sEval);
}
catch(e)
{
  actual = expect;
}
addThis();



//-----------------------------------------------------------------------------
addtestcases();
//-----------------------------------------------------------------------------


function addThis()
{
  statusitems[UBound] = status;
  actualvalues[UBound] = actual;
  expectedvalues[UBound] = expect;
  UBound++;
}


function addtestcases()
{

  //printBugNumber(BUGNUMBER);
  //printStatus (summary);

  for (var i = 0; i < UBound; i++)
  {
    Assert.expectEq(statusitems[i], expectedvalues[i], actualvalues[i]);
  }


}