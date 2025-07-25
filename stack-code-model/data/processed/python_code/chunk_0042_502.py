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
  
  dynamic class DynExtDynamicClassFinInner extends DynamicClass {

    // ************************************
    // access final method of parent
    // from default method of sub class
    // ************************************

    function subGetArray() : Array { return this.getFinArray(); }
    function subSetArray(a:Array) { this.setFinArray(a); }

    // function to test above from test scripts
    public function testSubArray(a:Array) : Array {
        this.subSetArray(a);
        return this.subGetArray();
    }

    // ************************************
    // access final method of parent
    // from public method of sub class
    // ************************************

    public function pubSubGetArray() : Array { return this.getFinArray(); }
    public function pubSubSetArray(a:Array) { this.setFinArray(a); }

    // ************************************
    // access final method of parent
    // from private method of sub class
    // ************************************

    private function privSubGetArray() : Array { return this.getFinArray(); }
    private function privSubSetArray(a:Array) { this.setFinArray(a); }

    // function to test above from test scripts
    public function testPrivSubArray(a:Array) : Array {
        this.privSubSetArray(a);
        return this.privSubGetArray();
    }

    // ************************************
    // access final method of parent
    // from final method of sub class
    // ************************************

    final function finSubGetArray() : Array { return this.getFinArray(); }
    final function finSubSetArray(a:Array) { this.setFinArray(a); }

    // function to test above from test scripts
    public function testFinSubArray(a:Array) : Array {
        this.finSubSetArray(a);
        return this.finSubGetArray();
    }
    
    // ************************************
    // access final method of parent
    // from private final method of sub class
    // ************************************

    private final function finPrivSubGetArray() : Array { return this.getFinArray(); }
    private final function finPrivSubSetArray(a:Array) { this.setFinArray(a); }

    // function to test above from test scripts
    public function testPrivFinSubArray(a:Array) : Array {
        this.finPrivSubSetArray(a);
        return this.finPrivSubGetArray();
    }
    
    virtual function virSubGetArray() : Array { return this.getFinArray(); }
    virtual function virSubSetArray(a:Array) { this.setFinArray(a); }

    // function to test above from test scripts
    public function testVirSubArray(a:Array) : Array {
        this.virSubSetArray(a);
        return this.virSubGetArray();
    }    

    // ***************************************
    // access final property from 
    // default method of sub class
    // ***************************************

    function subGetDPArray() : Array { return finArray; }
    function subSetDPArray(a:Array) { finArray = a; }
    // function to test above from test scripts
    public function testSubGetDPArray(a:Array) : Array {
        this.subSetDPArray(a);
        return this.subGetDPArray();
    }

   
    // ***************************************
    // access final property from
    // public method of sub class
    // ***************************************

    public function pubSubGetDPArray() : Array { return this.finArray; }
    public function pubSubSetDPArray(a:Array) { this.finArray = a; }

    // ***************************************
    // access final property from
    // private method of sub class
    // ***************************************
 
    private function privSubGetDPArray() : Array { return this.finArray; }
    private function privSubSetDPArray(a:Array) { this.finArray = a; }
    // function to test above from test scripts
    public function testPrivSubGetDPArray(a:Array) : Array {
        this.finSubSetDPArray(a);
        return this.finSubGetDPArray();
    }

    // ***************************************
    // access final property from 
    // final method of sub class
    // ***************************************

    final function finSubGetDPArray() : Array { return finArray; }
    final function finSubSetDPArray(a:Array) { finArray = a; }
    // function to test above from test scripts
    public function testFinSubGetDPArray(a:Array) : Array {
        this.finSubSetDPArray(a);
        return this.finSubGetDPArray();
    }
    
    // ***************************************
    // access final property from 
    // private virtual method of sub class
    // ***************************************

    public virtual function privVirSubGetDPArray() : Array { return finArray; }
    public virtual function privVirSubSetDPArray(a:Array) { finArray = a; }
    // function to test above from test scripts
    public function testPrivVirSubGetDPArray(a:Array) : Array {
        this.privVirSubSetDPArray(a);
        return this.privVirSubGetDPArray();
    }    

  }
  public class DynExtDynamicClassFin extends DynExtDynamicClassFinInner  {}
}