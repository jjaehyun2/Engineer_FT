/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


/*
 *
 * Date:    19 April 2003
 * SUMMARY: Testing nested function scope capture
 *
 * See http://bugzilla.mozilla.org/show_bug.cgi?id=202678
 *
 */
//-----------------------------------------------------------------------------
var gTestfile = 'regress-202678-001.js';
var UBound = 0;
var BUGNUMBER = 202678;
var summary = 'Testing nested function scope capture';
var status = '';
var statusitems = [];
var actual = '';
var actualvalues = [];
var expect= '';
var expectedvalues = [];
var self = this;


function myFunc()
{
  var hidden = 'aaa';
  insideFunc();

  if (!self.runOnce)
  {
    var hidden = 'bbb';
    self.outSideFunc = insideFunc;
    self.runOnce = true;
  }
  else
  {
    var hidden = 'ccc';
  }


  function insideFunc()
  {
    actual = hidden;
  }
}



//status = inSection(1);
myFunc();  // this sets |actual|
expect = 'aaa';
addThis();

//status = inSection(2);
outSideFunc();  // sets |actual|
expect = 'bbb';
addThis();

//status = inSection(3);
myFunc();      // sets |actual|
expect = 'aaa';
addThis();

//status = inSection(4);
outSideFunc();  // sets |actual|
expect = 'bbb'; // NOT 'ccc'
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
//printStatus(summary);

  for (var i=0; i<UBound; i++)
  {
    Assert.expectEq(statusitems[i], expectedvalues[i], actualvalues[i]);
  }


}