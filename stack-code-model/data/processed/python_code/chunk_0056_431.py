/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;


var gTestfile = 'regress-466747.js';
//-----------------------------------------------------------------------------
var BUGNUMBER = 466747;
var summary = 'TM: Do not assert: fp->slots + fp->script->nfixed + ' +
  'js_ReconstructStackDepth(cx, fp->script, fp->regs->pc) == fp->regs->sp';
var actual = '';
var expect = '';


//-----------------------------------------------------------------------------
addtestcases();
//-----------------------------------------------------------------------------

function addtestcases()
{

  //printBugNumber(BUGNUMBER);
  //printStatus (summary);

  if (typeof window == 'undefined')
  {
    expect = actual = 'Test skipped: browser only';
    Assert.expectEq(summary, expect, actual);
  }
  else
  {
    gDelayTestDriverEnd = true;



    function newScriptWithLoop(m)
    {
      var ns = document.createElement("script");
      var nt = document.createTextNode("for (var q = 0; q < " + m + "; ++q) { }");
      ns.appendChild(nt);
      return ns;
    }

    function boom()
    {
      var div = document.createElement("div");
      div.appendChild(newScriptWithLoop(7));
      div.appendChild(newScriptWithLoop(1));
      document.body.appendChild(div);



      Assert.expectEq(summary, expect, actual);
      gDelayTestDriverEnd = false;
      jsTestDriverEnd();
    }

    window.addEventListener('load', boom, false);
  }


}