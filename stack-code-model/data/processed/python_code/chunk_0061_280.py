/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;

gTestfile = 'general1.js';

/**
   Filename:     general1.js
   Description:  'This tests out some of the functionality on methods on the Array objects'

   Author:       Nick Lerissa
   Date:         Fri Feb 13 09:58:28 PST 1998
*/

// var SECTION = 'As described in Netscape doc "Whats new in JavaScript 1.2"';
// var VERSION = 'no version';
// var TITLE = 'String:push,unshift,shift';


var array1 = [];

var testcases = [];
var index = 0;

array1.push(123);            //array1 = [123]
array1.push("dog");          //array1 = [123,dog]
array1.push(-99);            //array1 = [123,dog,-99]
array1.push("cat");          //array1 = [123,dog,-99,cat]
Assert.expectEq(  "array1.pop()", array1.pop(),'cat');
//array1 = [123,dog,-99]
array1.push("mouse");        //array1 = [123,dog,-99,mouse]
Assert.expectEq(  "array1.shift()", array1.shift(),123);
//array1 = [dog,-99,mouse]
array1.unshift(96);          //array1 = [96,dog,-99,mouse]
Assert.expectEq(  "state of array", String([96,"dog",-99,"mouse"]), String(array1));
Assert.expectEq(  "array1.length", array1.length,4);
array1.shift();              //array1 = [dog,-99,mouse]
array1.shift();              //array1 = [-99,mouse]
array1.shift();              //array1 = [mouse]
Assert.expectEq(  "array1.shift()", array1.shift(),"mouse");
Assert.expectEq(  "array1.shift()", "undefined", String(array1.shift()));