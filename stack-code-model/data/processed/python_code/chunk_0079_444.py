/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-452742-01.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 452742;
var summary = 'Do not do overzealous eval inside function optimization in BindNameToSlot';
var actual = '';
var expect = '';


//-----------------------------------------------------------------------------
addtestcases();
//-----------------------------------------------------------------------------

function addtestcases()
{

  //printBugNumber(BUGNUMBER);
  //printStatus (summary);
 
  expect = actual = 'No Error';

  var obj = { x: -100 };

  function a(x)
  {
    var orig_x = x;
    var orig_obj_x = obj.x;

    with (obj) { x = x + 10; }

    if (x !== orig_x)
      throw "Unexpected mutation of x: " + x;
    if (obj.x !== orig_obj_x + 10)
      throw "Unexpected mutation of obj.x: " + obj.x;
  }

  try
  {
    a(0);
  }
  catch(ex)
  {
    actual = ex + '';
  }
  Assert.expectEq(summary, expect, actual);


}