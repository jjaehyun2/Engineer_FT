/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


/*
 *
 * Date:    30 Sep 2003
 * SUMMARY: Testing concatenation of string + number
 * See http://bugzilla.mozilla.org/show_bug.cgi?id=39309
 *
 */
//-----------------------------------------------------------------------------
var gTestfile = 'regress-39309.js';
var UBound = 0;
var BUGNUMBER = 39309;
var summary = 'Testing concatenation of string + number';
var status = '';
var statusitems = [];
var actual = '';
var actualvalues = [];
var expect= '';
var expectedvalues = [];


function f(textProp, len)
{
  var i = 0;
  while (++i <= len)
  {
    var name = textProp + i;
    actual = name;
  }
}


//status = inSection(1);
f('text', 1);  // sets |actual|
expect = 'text1';
addThis();

//status = inSection(2);
f('text', 100);  // sets |actual|
expect = 'text100';
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