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
package testpublicClassInitializer{

public class testClassInitializers{

        public static var j:Number=1;
        public static var k:Number=0;
        public static var l:Number=0;
        public static var m:Number=0;
        for (j=1;j<2;j++)
                         {
                          k=j;
                         }
        if(j>10){
                l=11;
                }
        else
            {
            l=j;
            }


public static var p:Number=10;
public static var q:Number=5;
public static var r:Number=p/q;

do{
  m=m+1
  }while(m<2);
}
public class testClassInitializersWrap{
public function MyNumber1():Number{
                                 return testClassInitializers.k;
                                }
public function MyNumber2():Number{
                                 return testClassInitializers.l;
                                }
public function MyNumber3():Number{
                                 return testClassInitializers.m;
                                  }
                                      }

}