/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import DefClassImpPublicIntpubname.*;
import com.adobe.test.Assert;
// var SECTION = "Definitions";       // provide a document reference (ie, Actionscript section)
// var VERSION = "AS3";        // Version of ECMAScript or ActionScript
// var TITLE   = "Default class implements public interface";       // Provide ECMA section title or a description
var BUGNUMBER = "";



///////////////////////////////////////////////////////////////
// add your tests here
  

var obj:DefaultClassAccesor = new DefaultClassAccesor();

//Default class implements a default interface with a public name interface method
Assert.expectEq("Default class implements a public interface with a public name interface method", "PASSED",obj.accdeffunc());

////////////////////////////////////////////////////////////////

//}

              // displays results.