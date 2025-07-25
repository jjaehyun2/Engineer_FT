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
package OverrideFunctionName {

	public class TestNameObjBase {
    	// constructor
    	public function TestNameObjBase() {}

    	// not the constructor but looks like it
    	public function testNameObj() { return null; }

    	public function a1 () { return null; }
    	public function a_1 () { return null; }
    	public function _a1 () { return null; }
    	public function __a1 () { return null; }
    	public function _a1_ () { return null; }
    	public function __a1__ () { return null; }
    	public function $a1 () { return null; }
    	public function a$1 () { return null; }
    	public function a1$ () { return null; }
    	public function A1 () { return null; }
    	public function cases () { return null; }
    	public function Cases () { return null; }
    	public function abcdefghijklmnopqrstuvwxyz0123456789$_ () { return null; }
	}

	public class TestNameObj extends TestNameObjBase {
    	// constructor
    	public function TestNameObj() {}

    	// not the constructor but looks like it
    	override public function testNameObj() { return "not the constructor" }

    	override public function a1 () { return "a1"; }
    	override public function a_1 () { return "a_1"; }
    	override public function _a1 () { return "_a1"; }
    	override public function __a1 () { return "__a1"; }
    	override public function _a1_ () { return "_a1_"; }
    	override public function __a1__ () { return "__a1__"; }
    	override public function $a1 () { return "$a1"; }
    	override public function a$1 () { return "a$1"; }
    	override public function a1$ () { return "a1$"; }
    	override public function A1 () { return "A1"; }
    	override public function cases () { return "cases"; }
    	override public function Cases () { return "Cases"; }
    	override public function abcdefghijklmnopqrstuvwxyz0123456789$_ () { return "all"; }
	}

}