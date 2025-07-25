/* -*- Mode: C++; c-basic-offset: 4; indent-tabs-mode: nil; tab-width: 4 -*- */
/* vi: set ts=4 sw=4 expandtab: (add to ~/.vimrc: set modeline modelines=5) */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

import flash.utils.ByteArray;

var DESC = "Read aligned bigEndian short from ByteArray, store in local with type int.";
include "driver.as"

function bytearray_read_short(iter: int, a: ByteArray): int
{
    var tmp1:int;
    var tmp2:int;
    var tmp3:int;
    var tmp4:int;
    var tmp5:int;
    for ( var i:int = 0 ; i < iter ; i++ ) {
        a.position = 0;
        for ( var j:int = 0 ; j < 1000 ; j++ ) {
            tmp1 = a.readShort();
            tmp2 = a.readShort();
            tmp3 = a.readShort();
            tmp4 = a.readShort();
            tmp5 = a.readShort();
        }
    }
    return tmp1+tmp2+tmp3+tmp4+tmp5;
}

var bai: ByteArray = new ByteArray();
(function () {
    for ( var i=0 ; i < 5000 ; i++ )
        bai.writeShort(i);
 })();
TEST(function () { bytearray_read_short(1000, bai); }, "bytearray-read-short-1");