/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
/*
 * Internal Class InternalClass
 * Class methods
 *
 */

package InternalClassImpDefIntname{

    internal class InternalClass implements DefaultInt{
        
        public function deffunc():String{
            return"PASSED";
        }
        
    }


    public class InternalClassAccesor{
            var c:InternalClass = new InternalClass();
        var i:DefaultInt = c;
        public function accdeffunc(){return i.deffunc();}
                
       }
    
}