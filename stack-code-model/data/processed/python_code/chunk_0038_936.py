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

final class FinExtDynamicImplDefDefPub extends DynamicClass implements DefaultIntDef, DefaultInt {

    // ****************************************
    // define a default definition from
    // default interface as a default method
    // ****************************************

     public  function iGetBoolean() : Boolean { return this.boolean; }
        public function iGetNumber1() : Number { return 5; }
	public function testGetBoolean(flag:Boolean):Boolean {

	  setBoolean(flag);
	  return iGetBoolean();
	}


    // ****************************************
    // define a public defintion from
    // default interface as a default method
    // ****************************************

        public function iGetPubBoolean(): Boolean {return false;}


    // ****************************************
    // define a default definition from
    // default interface 2 as a public method
    // ****************************************

    public function iGetNumber() : Number { return this.number; }
        
	public function testGetSetNumber( num:Number ) : Number {

	  setNumber(num);
	  return iGetNumber();
	}


    // ****************************************
    // define a public defintion from
    // default interface 2 as a default method
    // ****************************************

   
    public function iGetPubNumber() : Number { return 5; }

    // ************************************
    // access public method of parent
    // from default method of sub class
    // ************************************

    function subGetArray() : Array { return this.getPubArray(); }
    function subSetArray(a:Array) { this.setPubArray(a); }

    public function testGetSubArray(a:Array) : Array {
        this.subSetArray(a);
        return this.subGetArray();
    }


    // ************************************
    // access public method of parent
    // from public method of sub class
    // ************************************

    public function pubSubGetArray() : Array { return this.getPubArray(); }
    public function pubSubSetArray(a:Array) { this.setPubArray(a); }

    // ************************************
    // access public method of parent
    // from private method of sub class
    // ************************************

    private function privSubGetArray() : Array { return this.getPubArray(); }
    private function privSubSetArray(a:Array) { this.setPubArray(a); }

    // function to test above from test scripts
    public function testPrivSubArray(a:Array) : Array {
        this.privSubSetArray(a);
        return this.privSubGetArray();
    }

  }

 	// Create an instance of the final class in the package.
  	// This object will be used for accessing the methods created
  	// within the sub class given above.
  	var FINEXTDCLASS = new FinExtDynamicImplDefDefPub();

  	// Create a series of public functions that call the methods.
  	// The same names can be used as used in the class; because we are now
  	// outside of the class definition.

  	// The default method of the sub class.
  	public function setPubArray( a:Array )  { return FINEXTDCLASS.setPubArray( a ); }
  	public function setPubBoolean( a:Boolean )  { return FINEXTDCLASS.setPubBoolean( a ); }
  	public function setPubDate( a:Date )  { return FINEXTDCLASS.setPubDate( a ); }
  	public function setPubFunction( a:Function )  { return FINEXTDCLASS.setPubFunction( a ); }
  	public function setPubNumber( a:Number )  { return FINEXTDCLASS.setPubNumber( a ); }
  	public function setPubString( a:String )  { return FINEXTDCLASS.setPubString( a ); }
  	public function setPubObject( a:Object )  { return FINEXTDCLASS.setPubObject( a ); }

  	// The dynamic method of the sub class.
  	public function testGetSetBoolean( a:Array )  { FINEXTDCLASS.testGetSetBoolean( a ); }
  	public function testPubGetSetBoolean( a:Array )  { FINEXTDCLASS.testPubGetSetBoolean( a ); }


  	// The public method of the sub class.
  	public function testGetSubArray( a:Array )  { return FINEXTDCLASS.testGetSubArray( a ); }
  	public function pubSubSetArray( a:Array )  { return FINEXTDCLASS.pubSubSetArray( a ); }
  	public function pubSubGetArray()  { return FINEXTDCLASS.pubSubGetArray(  ); }

  	// The private method of the sub class. Only one is used as we need to call only the
  	// test function, which in turn calls the actual private methods, as within the class
  	// we can access the private methods; but not outside of the class.
  	public function testPrivSubArray( a:Array ) : Array  { return FINEXTDCLASS.testPrivSubArray( a ); }

  	// The default property being accessed by the different method attributes.
  	// The default method attribute.
  	public function pubSubSetDPArray( a:Array ) { return FINEXTDCLASS.pubSubSetDPArray(a); }
  	public function testSubGetDPArray(a:Array) : Array { return FINEXTDCLASS.testSubGetDPArray(a); }


  	// the private static method attribute
  	public function testPrivSubGetDPArray(a:Array) : Array { return FINEXTDCLASS.testPrivSubGetDPArray(a); }

public class accFinExtDynamicImplDefDefPub{
	private var obj:FinExtDynamicImplDefDefPub = new FinExtDynamicImplDefDefPub();
                var i:DefaultInt=obj;
                var j:DefaultIntDef=obj;
      public function acciGetPubBoolean() : Boolean {return obj.iGetPubBoolean();}
      public function acciGetPubNumber() : Number { return obj.iGetPubNumber(); }
      public function acciiGetNumber1(): Number{ return i.iGetNumber1();}
      public function accjiGetNumber1(): Number{ return obj.DefaultIntDef::iGetNumber1();}

}

}