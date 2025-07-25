/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-292215.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 292215;
var summary = 'Set arguments';
var actual = '';
var expect = '00012';

//printBugNumber(BUGNUMBER);
//printStatus (summary);
 

function zeroArguments () {
  arguments[1] = '0';
  actual += arguments[1];
}

function oneArgument (x) {
  arguments[1] = '1';
  actual += arguments[1];
}

function twoArguments (x,y) {
  arguments[1] = '2';
  actual += arguments[1];
}

zeroArguments();
zeroArguments(1);
zeroArguments('a', 'b');
oneArgument();
twoArguments();

Assert.expectEq(summary, expect, actual);