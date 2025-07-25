/* -*- Mode: C++; c-basic-offset: 4; indent-tabs-mode: nil; tab-width: 4 -*- */
/* vi: set ts=4 sw=4 expandtab: (add to ~/.vimrc: set modeline modelines=5) */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

import flash.utils.ByteArray;

var DESC = "Write long string as length-prefixed UTF to pre-sized ByteArray";
include "driver.as"

function bytearray_write_utf(iter: int): uint
{
    const s1:String = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us...";
    const s2:String = "Ja vi elsker dette landet som det stiger frem furet vaerbitt over vannet med de tusen hjem elsker elsker det og tenker paa vaar far og mor og den saganatt som senker senker droemme paa vaar jord";
    const lim:int = 1000;
    var ba1: ByteArray = new ByteArray();
    ba1.length = (s1.length+2)*lim;
    var ba2: ByteArray = new ByteArray();
    ba2.length = (s2.length+2)*lim;
    for ( var i:int = 0 ; i < iter ; i++ ) {
        ba1.position = 0;
        ba2.position = 0;
        for ( var j:int = 0 ; j < lim ; j++ ) {
            ba1.writeUTF(s1);
            ba2.writeUTF(s2);
        }
        if (ba1.length != (s1.length+2)*lim || ba1.position != ba1.length)
            throw "Error writing " + s1 + ": " + ba1.length + ", " + ba1.position;
        if (ba2.length != (s2.length+2)*lim || ba2.position != ba2.length)
            throw "Error writing " + s2 + ": " + ba2.length + ", " + ba2.position;
    }
    return ba1.length + ba2.length;
}

TEST(function () { bytearray_write_utf(100); }, "bytearray-write-utf-2");