/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;

gTestfile = 'plus.js';

/**
   Filename:     plus.js
   Description:  'Tests regular expressions containing +'

   Author:       Nick Lerissa
   Date:         March 10, 1998
*/

// var SECTION = 'As described in Netscape doc "Whats new in JavaScript 1.2"';
// var VERSION = 'no version';
// var TITLE   = 'RegExp: +';


// 'abcdddddefg'.match(new RegExp('d+'))
Assert.expectEq (  "'abcdddddefg'.match(new RegExp('d+'))",
           String(["ddddd"]), String('abcdddddefg'.match(new RegExp('d+'))));

// 'abcdefg'.match(new RegExp('o+'))
Assert.expectEq (  "'abcdefg'.match(new RegExp('o+'))",
           null, 'abcdefg'.match(new RegExp('o+')));

// 'abcdefg'.match(new RegExp('d+'))
Assert.expectEq (  "'abcdefg'.match(new RegExp('d+'))",
           String(['d']), String('abcdefg'.match(new RegExp('d+'))));

// 'abbbbbbbc'.match(new RegExp('(b+)(b+)(b+)'))
Assert.expectEq (  "'abbbbbbbc'.match(new RegExp('(b+)(b+)(b+)'))",
           String(["bbbbbbb","bbbbb","b","b"]), String('abbbbbbbc'.match(new RegExp('(b+)(b+)(b+)'))));

// 'abbbbbbbc'.match(new RegExp('(b+)(b*)'))
Assert.expectEq (  "'abbbbbbbc'.match(new RegExp('(b+)(b*)'))",
           String(["bbbbbbb","bbbbbbb",""]), String('abbbbbbbc'.match(new RegExp('(b+)(b*)'))));

// 'abbbbbbbc'.match(new RegExp('b*b+'))
Assert.expectEq (  "'abbbbbbbc'.match(new RegExp('b*b+'))",
           String(['bbbbbbb']), String('abbbbbbbc'.match(new RegExp('b*b+'))));

// 'abbbbbbbc'.match(/(b+)(b*)/)
Assert.expectEq (  "'abbbbbbbc'.match(/(b+)(b*)/)",
           String(["bbbbbbb","bbbbbbb",""]), String('abbbbbbbc'.match(/(b+)(b*)/)));

// 'abbbbbbbc'.match(new RegExp('b*b+'))
Assert.expectEq (  "'abbbbbbbc'.match(/b*b+/)",
           String(['bbbbbbb']), String('abbbbbbbc'.match(/b*b+/)));