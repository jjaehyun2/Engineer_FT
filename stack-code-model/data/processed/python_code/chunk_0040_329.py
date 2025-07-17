/**
 * User: Dave Long
 * Date: 06/08/13
 * Time: 19:17
 */
package com.sixfootsoftware.engine.utils {
    public class StringOperations {
        public static function zeroPad(str:String, width:int):String {
            while( str.length < width )
                str="0" + str;
            return str;
        }
    }
}