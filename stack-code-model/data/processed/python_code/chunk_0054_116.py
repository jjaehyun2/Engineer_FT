/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */


package PublicClassImpPublicInt{

use namespace ns;

    public class PublicClass implements PublicInt{
        
        public function deffunc():String{                  //Default method
            return"PASSED";
        }

        public function getdeffunc():String{return deffunc();}
        // access default function deffunc


        public function pubFunc():Boolean{         //Public method
                return true;
        }
            
        ns function nsFunc(a="test"):int{          //Namespace method
            return a.length;
        }
        
        public function getnsFunc(a="test"):int{return ns::nsFunc(a);}
        // access default function nsFunc

       }
}