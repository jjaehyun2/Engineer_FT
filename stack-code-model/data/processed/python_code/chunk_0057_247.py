/* -*- c-basic-offset: 4; indent-tabs-mode: nil; tab-width: 4 -*- */
/* vi: set ts=4 sw=4 expandtab: (add to ~/.vimrc: set modeline modelines=5) */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;

// var SECTION = "4.4.16.15";
// var VERSION = "AS3";
// var TITLE   = "Math and geometric methods public function reciprocal(arg:float4):float4";


var flt4:float4 = new float4(1f);
Assert.expectEq("float4.reciprocal() returns a float4", "float4", getQualifiedClassName(float4.reciprocal(flt4)));
Assert.expectEq("float4.reciprocal() length is 1", 1, float4.reciprocal.length);

var flt_recip:float = float.reciprocal(1f);
AddStrictTestCase("float4.reciprocal(1f, 1f, 1f, 1f)", new float4(flt_recip), float4.reciprocal(flt4));