/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


/*
 *
 * Date:    27 Sep 2003
 * SUMMARY: Calling a local function from global scope
 * See http://bugzilla.mozilla.org/show_bug.cgi?id=220362
 *
 */
//-----------------------------------------------------------------------------
var gTestfile = 'regress-220362.js';
var UBound = 0;
var BUGNUMBER = 220362;
var summary = 'Calling a local function from global scope';
var status = '';
var statusitems = [];
var actual = '';
var actualvalues = [];
var expect= '';
var expectedvalues = [];


// creates a local function and calls it immediately
function a()
{
  var x = 'A';
  var f = function() {return x;};
  return f();
}

// creates and returns a local function
function b()
{
  var x = 'B';
  var f = function() {return x;};
  return f;
}


//status = inSection(1);
actual = a();
expect = 'A';
addThis();

//status = inSection(2);
var f = b();
actual = f();
expect = 'B';
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