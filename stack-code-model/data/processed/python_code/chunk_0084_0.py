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


package P {
 
     public namespace nsPublic    	
     
     internal namespace nsInternal
     
        

	public class Game{

           protected namespace nsProtected        
           private namespace nsPrivate
             nsPublic function whoplay(){return "Steve"}  //public namespace
	     nsPrivate function whoplay(){return "Joe"}   //private namespace
             nsInternal function whoplay(){return "Luis"}   //internal namespace
  	     nsProtected function whoplay(){return "Peter"}   //protected namespace

             public function accprivwhoplay(){return nsPrivate::whoplay()} //public function to access nsPrivate function
             public function accintwhoplay(){return nsInternal::whoplay()} //public function to access nsInternal function
             public function accprotwhoplay(){return nsProtected::whoplay()} //public function to access nsProtected function
        
     }
 }

 
var SECTION = "Directives";       // provide a document reference (ie, Actionscript section)
var VERSION = "AS 3.0";        // Version of ECMAScript or ActionScript 
var TITLE   = "Public_Private_Internal_Protected_Namespace as function attribute";       // Provide ECMA section title or a description
var BUGNUMBER = "";

startTest();                // leave this alone





import P.*;

var game = new Game();

AddTestCase( "(Public Namespace function) Who is going to play = 'Steve'", "Steve", game.nsPublic::whoplay());
AddTestCase( "(Private Namespace function) Who is going to play = 'Joe'", "Joe", game.accprivwhoplay());
AddTestCase( "(Internal Namespace function) Who is going to play = 'Luis'", "Luis", game.accintwhoplay());
AddTestCase( "(Protected Namespace function) Who is going to play = 'Peter'", "Peter", game.accprotwhoplay());


test();       // leave this alone.  this executes the test cases and
              // displays results.