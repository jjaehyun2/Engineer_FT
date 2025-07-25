/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import flash.system.*;
import avmplus.System;
import com.adobe.test.Assert;
import com.adobe.test.Utils;

var CODE_OLD = 1115; // _ is not a constructor.
var CODE_NEW = 1007; // Instantiation attempted on a non-constructor.
var playerType:String = Capabilities.playerType;
var CODE;

if (System.swfVersion >= 11) {
     CODE = CODE_NEW;
} else {
    if ((playerType == 'AVMPlus') && (System.getRunmode().indexOf('jit') != -1)) {
        CODE = CODE_NEW;
    } else {
        CODE = CODE_OLD;
    }
}

//-----------------------------------------------------------
//-----------------------------------------------------------

try {
        var z = "no error";
        var OBJECT = new Object();
        var o = new OBJECT();
} catch (err) {
        z = err.toString();
} finally {
        Assert.expectEq("[Object] Runtime Error", "TypeError: Error #" + CODE, Utils.typeError(z));
}

try {
        var z = "no error";
        var OBJECT = null;
        var o = new OBJECT();
} catch (err) {
        z = err.toString();
} finally {
        Assert.expectEq("[null] Runtime Error", "TypeError: Error #" + CODE, Utils.typeError(z));
}

try {
        var z = "no error";
        var OBJECT;
        var o = new OBJECT();
} catch (err) {
        z = err.toString();
} finally {
        Assert.expectEq("[undefined] Runtime Error", "TypeError: Error #" + CODE, Utils.typeError(z));
}

//-----------------------------------------------------------
//-----------------------------------------------------------