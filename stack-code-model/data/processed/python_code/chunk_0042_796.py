/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;
/*
 * Date: 26 November 2000
 *
 *
 * SUMMARY: Passing (RegExp object, flag) to RegExp() function.
 * This test arose from Bugzilla bug 61266. The ECMA3 section is:
 *
 * 15.10.3 The RegExp Constructor Called as a Function
 *
 *   15.10.3.1 RegExp(pattern, flags)
 *
 *   If pattern is an object R whose [[Class]] property is "RegExp"
 *   and flags is undefined, then return R unchanged.  Otherwise
 *   call the RegExp constructor (section 15.10.4.1),  passing it the
 *   pattern and flags arguments and return  the object constructed
 *   by that constructor.
 *
 *
 * The current test will check the first scenario outlined above:
 *
 *   "pattern" is itself a RegExp object R
 *   "flags" is undefined
 *
 * The flags parameter will be undefined in the sense of not being
 * provided. We check that RegExp(R) returns R  -
 */
//-------------------------------------------------------------------------------------------------

// var SECTION = "e15_10_3_1_1";
// var VERSION = "";
// var TITLE   = "Passing (RegExp object,flag) to RegExp() function";
// var bug = "61266";

var testcases = getTestCases();

function getTestCases() {
    var array = new Array();
    var item = 0;

    var i = -1; var j = -1; var s = ''; var f = '';
    var obj = {}; var status = ''; var actual = ''; var expect = '';
    var patterns = new Array();
    var flags = new Array();
    var cnSUCCESS = 'RegExp() returned the supplied RegExp object';
    var cnFAILURE =  'RegExp() did NOT return the supplied RegExp object';

    // various regular expressions to try -
    patterns[0] = '';
    patterns[1] = 'abc';
    patterns[2] = '(.*)(3-1)\s\w';
    patterns[3] = '(.*)(...)\\s\\w';
    patterns[4] = '[^A-Za-z0-9_]';
    patterns[5] = '[^\f\n\r\t\v](123.5)([4 - 8]$)';

    // various flags to try -
    flags[0] = 'i';
    flags[1] = 'g';
    flags[2] = 'm';
    flags[3] = undefined;

    for (i in patterns)
    {
        s = patterns[i];
        for (j in flags)
        {
            f = flags[j];
            status = getStatus(s, f);
            obj = new RegExp(s, f);

            actual = (obj == RegExp(obj))? cnSUCCESS : cnFAILURE;
            expect = cnSUCCESS;
            array[item++] = Assert.expectEq( status, expect, actual);
        }
    }


    var statprefix = 'RegExp(new RegExp(';
    var comma =  ', ';
    var singlequote = "'";
    var closeparens = '))';

    function getStatus(regexp, flag)
    {
      return (statprefix  +  quote(regexp) +  comma  +   flag  +  closeparens);
    }

    function quote(text)
    {
      return (singlequote  +  text  + singlequote);
    }

    return array;
}