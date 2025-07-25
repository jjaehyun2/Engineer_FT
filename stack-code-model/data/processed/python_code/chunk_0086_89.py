/* ***** BEGIN LICENSE BLOCK *****
 * Version: MPL 1.1/GPL 2.0/LGPL 2.1
 *
 * The contents of this file are subject to the Mozilla Public License Version
 * 1.1 (the "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 * http://www.mozilla.org/MPL/
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 * for the specific language governing rights and limitations under the
 * License.
 *
 * The Original Code is [Open Source Virtual Machine.].
 *
 * The Initial Developer of the Original Code is
 * Adobe System Incorporated.
 * Portions created by the Initial Developer are Copyright (C) 2005-2006
 * the Initial Developer. All Rights Reserved.
 *
 * Contributor(s):
 *   Adobe AS3 Team
 *
 * Alternatively, the contents of this file may be used under the terms of
 * either the GNU General Public License Version 2 or later (the "GPL"), or
 * the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
 * in which case the provisions of the GPL or the LGPL are applicable instead
 * of those above. If you wish to allow use of your version of this file only
 * under the terms of either the GPL or the LGPL, and not to allow others to
 * use your version of this file under the terms of the MPL, indicate your
 * decision by deleting the provisions above and replace them with the notice
 * and other provisions required by the GPL or the LGPL. If you do not delete
 * the provisions above, a recipient may use your version of this file under
 * the terms of any one of the MPL, the GPL or the LGPL.
 *
 * ***** END LICENSE BLOCK ***** */

var SECTION = "Definitions\const";       			// provide a document reference (ie, ECMA section)
var VERSION = "ActionScript 3.0";  			// Version of JavaScript or ECMA
var TITLE   = "conditional initialization inside class constructor";       // Provide ECMA section title or a description
var BUGNUMBER = "";

class MagicBall
{
    const num1:Number;
    
    function MagicBall(count:Number)
    {
        for (i=0; i<count; i++)
        {
            num1 ++;
        }
    }
    
    function getNumber():Number
    {
        return num1;
    }
}

startTest();

var thisError:String = "no error";
try
{
    var b:MagicBall = new MagicBall(3);
}
catch(err)
{
    thisError = err.toString();
}
finally
{
    AddTestCase("for loop for initializing const variable", "ReferenceError: Error #1074", referenceError(thisError));
}

test();