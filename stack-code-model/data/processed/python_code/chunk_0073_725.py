/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-452495.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 452495;
var summary = 'Do not crash with JIT: @ TraceRecorder::getThis';
var actual = 'No Crash';
var expect = 'No Crash';

//printBugNumber(BUGNUMBER);
//printStatus (summary);



for (var j = 0; j < 4; ++j) { try { new 1(this); } catch(e) { } }



Assert.expectEq(summary, expect, actual);