/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-233483-2.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 233483;
var summary = 'Don\'t crash with null properties - Browser only';
var actual = 'No Crash';
var expect = 'No Crash';

//printBugNumber(BUGNUMBER);
//printStatus (summary);

if (typeof document == 'undefined')
{
  Assert.expectEq(summary, expect, actual);
}
else
{
  // delay test driver end
  gDelayTestDriverEnd = true;

  actual = 'Crash';
  window.onload = onLoad;
}

function onLoad()
{
  var a = new Array();
  var pe;
  var x;
  var s;

  setform();

  for (pe=document.getElementById("test"); pe; pe=pe.parentNode)
  {
    a[a.length] = pe;
  }

  // can't document.write since this is in after load fires
  s = a.toString();

  actual = 'No Crash';

  Assert.expectEq(summary, expect, actual);

  gDelayTestDriverEnd = false;
  jsTestDriverEnd();
}

function setform()
{
  var form  = document.body.appendChild(document.createElement('form'));
  var table = form.appendChild(document.createElement('table'));
  var tbody = table.appendChild(document.createElement('tbody'));
  var tr    = tbody.appendChild(document.createElement('tr'));
  var td    = tr.appendChild(document.createElement('td'))
    var input = td.appendChild(document.createElement('input'));

  input.setAttribute('id', 'test');
  input.setAttribute('value', '1232');

}