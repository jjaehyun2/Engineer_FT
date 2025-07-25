/* 
 * Copyright (c) 2008 Allurent, Inc.
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without restriction,
 * including without limitation the rights to use, copy, modify,
 * merge, publish, distribute, sublicense, and/or sell copies of the
 * Software, and to permit persons to whom the Software is furnished
 * to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
 * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
 * OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
package com.allurent.coverage.model
{
    import flash.events.EventDispatcher;
    
    /**
     * Model of a package in the application for coverage purposes. 
     */
    public class PackageModel extends SegmentModel
    {
        /**
         * Construct a new PackageModel. 
         */
        public function PackageModel()
        {
        }
        
        override public function createChild(element:CoverageElement):SegmentModel
        {
            return new ClassModel();
        }
        
        override public function createChildFromXml(childXml:XML):SegmentModel
        {
            return new ClassModel();
        }
        
        override public function get displayName():String
        {
            return (name == "") ? "[top level]" : name;
        }

        override protected function createXmlElement():XML
        {
            return <package/>;
        }
    }
}