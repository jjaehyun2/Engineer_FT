/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import avmplus.*;
import com.adobe.test.Assert;


/*
 * Date: 14 October 2001
 *
 * SUMMARY: Regression test for Bugzilla bug 104584
 * See http://bugzilla.mozilla.org/show_bug.cgi?id=104584
 *
 * Testing that we don't crash on this code. The idea is to
 * call F,G WITHOUT providing an argument. This caused a crash
 * on the second call to obj.toString() or print(obj) below -
 */

//-----------------------------------------------------------------------------
var gTestfile = 'regress-104584.js';
var BUGNUMBER = 104584;
var summary = "Testing that we don't crash on this code -";

//printBugNumber(BUGNUMBER);
//printStatus (summary);

F();
G();

Assert.expectEq('', 'No Crash', 'No Crash');

function F(obj)
{
  if(!obj)
    obj = {};
  obj.toString();
  System.forceFullCollection();
  obj.toString();
}


function G(obj)
{
  if(!obj)
    obj = {};
  print(obj);
  System.forceFullCollection();
  print(obj);
}