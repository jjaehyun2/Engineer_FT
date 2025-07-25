/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;

gTestfile = 'new-001.js';

/**
   File Name:          new-001.js
   Section:
   Description:

   http://scopus.mcom.com/bugsplat/show_bug.cgi?id=76103

   Author:             christine@netscape.com
   Date:               12 november 1997
*/
// var SECTION = "new-001";
// var VERSION = "JS1_3";
// var TITLE   = "new-001";
var BUGNUMBER="31567";


function Test_One (x) {
  this.v = x+1;
  return x*2
    }

function Test_Two( x, y ) {
  this.v = x;
  return y;
}

Assert.expectEq(
    
  "Test_One(18)",
  36,
  Test_One(18) );

Assert.expectEq(
    
  "new Test_One(18)",
  "[object Object]",
  new Test_One(18) +"" );

Assert.expectEq(
    
  "new Test_One(18).v",
  19,
  new Test_One(18).v );

Assert.expectEq(
    
  "Test_Two(2,7)",
  7,
  Test_Two(2,7) );

Assert.expectEq(
    
  "new Test_Two(2,7)",
  "[object Object]",
  new Test_Two(2,7) +"" );

Assert.expectEq(
    
  "new Test_Two(2,7).v",
  2,
  new Test_Two(2,7).v );