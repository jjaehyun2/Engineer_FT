/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
/*
 * Public Class PublicClass
 * Class methods
 *
 */

package PublicClassImpInternalIntname{


    public class PublicClass implements InternalInt{
        
        public function deffunc():String{
            return"PASSED";
        }


            public function accdeffunc(){return InternalInt::deffunc();}
            
       }
}