/*
 Copyright (c) 2012 Josh Tynjala

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 */
package feathers.layout
{
	/**
	 * Used by layout algorithms for determining the bounds in which to position
	 * and size items.
	 */
	public class ViewPortBounds
	{
		public function ViewPortBounds()
		{
		}

		public var x:Number = 0;
		public var y:Number = 0;
		public var explicitWidth:Number = NaN;
		public var explicitHeight:Number = NaN;
		public var minWidth:Number = 0;
		public var minHeight:Number = 0;
		public var maxWidth:Number = Number.POSITIVE_INFINITY;
		public var maxHeight:Number = Number.POSITIVE_INFINITY;
	}
}