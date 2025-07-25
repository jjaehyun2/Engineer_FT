/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


/*
 * Date: 2001-07-16
 *
 * SUMMARY:  Testing visiblity of variables from within a with block.
 * See http://bugzilla.mozilla.org/show_bug.cgi?id=90325
 */
//-----------------------------------------------------------------------------
var gTestfile = 'scope-004.js';
var UBound = 0;
var BUGNUMBER = 90325;
var summary = 'Testing visiblity of variables from within a with block';
var status = '';
var statusitems = [];
var actual = '';
var actualvalues = [];
var expect= '';
var expectedvalues = [];

// (compare local definitions which follow) -
var A = 'global A';
var B = 'global B';
var C = 'global C';
var D = 'global D';

// an object with 'C' and 'D' properties -
var objTEST = new Object();
objTEST.C = C;
objTEST.D = D;


status = 'Section 1 of test';
with (new Object())
{
  actual = A;
  expect = 'global A';
}
addThis();


status = 'Section 2 of test';
with (Function)
{
  actual = B;
  expect = 'global B';
}
addThis();


status = 'Section 3 of test';
with (this)
{
  actual = C;
  expect = 'global C';
}
addThis();


status = 'Section 4 of test';
localA();
addThis();

status = 'Section 5 of test';
localB();
addThis();

status = 'Section 6 of test';
localC();
addThis();

status = 'Section 7 of test';
localC(new Object());
addThis();

status = 'Section 8 of test';
localC.apply(new Object());
addThis();

status = 'Section 9 of test';
localC.apply(new Object(), [objTEST]);
addThis();

status = 'Section 10 of test';
localC.apply(objTEST, [objTEST]);
addThis();

status = 'Section 11 of test';
localD(new Object());
addThis();

status = 'Section 12 of test';
localD.apply(new Object(), [objTEST]);
addThis();

status = 'Section 13 of test';
localD.apply(objTEST, [objTEST]);
addThis();



//-------------------------------------------------------------------------------------------------
addtestcases();
//-------------------------------------------------------------------------------------------------



// contains a with(new Object()) block -
function localA()
{
  var A = 'local A';

  with(new Object())
  {
    actual = A;
    expect = 'local A';
  }
}


// contains a with(Number) block -
function localB()
{
  var B = 'local B';

  with(Number)
  {
    actual = B;
    expect = 'local B';
  }
}


// contains a with(this) block -
function localC(obj)
{
  var C = 'local C';

  with(this)
  {
    actual = C;
  }

  if ('C' in this)
    expect = this.C;
  else
    expect = 'local C';
}


// contains a with(obj) block -
function localD(obj)
{
  var D = 'local D';

  with(obj)
  {
    actual = D;
  }

  if ('D' in obj)
    expect = obj.D;
  else
    expect = 'local D';
}


function addThis()
{
  statusitems[UBound] = status;
  actualvalues[UBound] = actual;
  expectedvalues[UBound] = expect;
  UBound++;
}


function addtestcases()
{

 

  for (var i = 0; i < UBound; i++)
  {
    Assert.expectEq(statusitems[i], expectedvalues[i], actualvalues[i]);
  }


}