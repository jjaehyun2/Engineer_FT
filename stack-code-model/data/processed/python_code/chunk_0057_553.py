/**
 *  Copyright (c) 2007 Allurent, Inc.
 *  http://code.google.com/p/visualflexunit/
 *  
 *  Permission is hereby granted, free of charge, to any person obtaining
 *  a copy of this software and associated documentation files (the
 *  "Software"), to deal in the Software without restriction, including
 *  without limitation the rights to use, copy, modify, merge, publish,
 *  distribute, sublicense, and/or sell copies of the Software, and to
 *  permit persons to whom the Software is furnished to do so, subject to
 *  the following conditions:
 *  
 *  The above copyright notice and this permission notice shall be
 *  included in all copies or substantial portions of the Software.
 *  
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 *  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 *  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 *  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 *  LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 *  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 *  WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

package com.allurent.flexunit2.vfu.utils
{
    public class ObjectUtil
    {
        import mx.utils.ObjectUtil;

        public static function getInstanceType(instance:Object, fullyQuald:Boolean = false) : String {
            var name:String;
            if (instance is String)
            {
                name = "String";
            }
            else
            {
                var i:Object = mx.utils.ObjectUtil.getClassInfo(instance);
                name = i.name;
            }
            if (!fullyQuald)
            {
                if (name.indexOf("::") != -1)
                {
                    name = StringUtil.getCharsAfterSubstring(name, "::");
                }
            }
            return name;
        }

        public static function getPropCount(obj:Object):int
        {
            var cnt:int = 0;
            for (var i:Object in obj)
            {
                cnt++;
            }
            return cnt;
        }
    }
}