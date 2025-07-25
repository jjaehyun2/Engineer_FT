/*
 Copyright (c) 2009 by contributors:

 * Richard R. Masters

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
*/

package org.svgweb.smil
{
    public class OffsetTimeSpec extends TimeSpec
    {
        protected var timeSpecString:String;
        protected var offset:Number;

        public function OffsetTimeSpec(timeSpecString:String, offset:Number):void {
            this.timeSpecString = timeSpecString;
            this.offset = offset;
        }

        public function getOffset():Number {
            return offset;
        }

    }
}