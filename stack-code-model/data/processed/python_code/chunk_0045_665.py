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
 * Portions created by the Initial Developer are Copyright (C) 2004-2006
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


package DynamicClass {

import DynamicClass.*;

dynamic class DynExtDynImplDefDefInner extends DynamicClass implements DefaultIntDef, DefaultInt {

    // ****************************************
    // define a default definition from
    // default interface as a default method
    // ****************************************

    public function iGetBoolean() : Boolean { return this.boolean; }

	public function testGetSetBoolean( flag:Boolean ) : Boolean {

	  setBoolean(flag);
	  return iGetBoolean();
	}


    // ****************************************
    // define a public defintion from
    // default interface as a default method
    // ****************************************

    public function iGetPubBoolean() : Boolean { return this.pubBoolean; }

	public function testPubGetSetBoolean( flag:Boolean ) : Boolean {

	  setPubBoolean(flag);
	  return iGetPubBoolean();
	}


    // ****************************************
    // define a default defintion from
    // default interface 2 as a default method
    // ****************************************

    public function iGetNumber() : Number { return this.number; }

	public function testGetSetNumber( num:Number ) : Number {

	  setNumber(num);
	  return iGetNumber();
	}


    // ****************************************
    // define a public definition from
    // default interface 2 as a default method
    // ****************************************

    public function iGetPubNumber() : Number { return this.pubNumber; }

	public function testPubGetSetNumber( num:Number ) : Number {

	  setPubNumber(num);
	  return iGetPubNumber();
	}


    // ************************************
    // access default method of parent
    // from default method of sub class
    // ************************************

    function subGetArray() : Array { return this.getArray(); }
    function subSetArray(a:Array) { this.setArray(a); }

    public function testGetSubArray(a:Array) : Array {
        this.subSetArray(a);
        return this.subGetArray();
    }


    // ************************************
    // access default method of parent
    // from public method of sub class
    // ************************************

    public function pubSubGetArray() : Array { return this.getArray(); }
    public function pubSubSetArray(a:Array) { this.setArray(a); }

    // ************************************
    // access default method of parent
    // from private method of sub class
    // ************************************

    private function privSubGetArray() : Array { return this.getArray(); }
    private function privSubSetArray(a:Array) { this.setArray(a); }

    // function to test above from test scripts
    public function testPrivSubArray(a:Array) : Array {
        this.privSubSetArray(a);
        return this.privSubGetArray();
    }

    // ***************************************
    // access default property from
    // default method of sub class
    // ***************************************

    function subGetDPArray() : Array { return array; }
    function subSetDPArray(a:Array) { array = a; }

    public function testSubGetDPArray(a:Array) : Array {
        this.subSetDPArray(a);
        return this.subGetDPArray();
    }


    // ***************************************
    // access default property from
    // public method of sub class
    // ***************************************

    public function pubSubGetDPArray() : Array { return this.array; }
    public function pubSubSetDPArray(a:Array) { this.array = a; }

    // ***************************************
    // access default property from
    // private method of sub class
    // ***************************************

    private function privSubGetDPArray() : Array { return this.array; }
    private function privSubSetDPArray(a:Array) { this.array = a; }

    public function testPrivSubGetDPArray(a:Array) : Array {
        this.privSubSetDPArray(a);
        return this.privSubGetDPArray();
    }
 }

public class DynExtDynamicImplDefDef extends DynExtDynImplDefDefInner {}


}