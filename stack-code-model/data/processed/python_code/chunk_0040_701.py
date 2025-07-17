/**
 * <p>Original Author: toddanderson</p>
 * <p>Class File: ITargetScrollAdaptor.as</p>
 * <p>Version: 0.3</p>
 *
 * <p>Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:</p>
 *
 * <p>The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.</p>
 *
 * <p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.</p>
 *
 * <p>Licensed under The MIT License</p>
 * <p>Redistributions of files must retain the above copyright notice.</p>
 */
package com.custardbelly.as3flobile.controls.viewport.adaptor
{
	import com.custardbelly.as3flobile.controls.viewport.context.IScrollViewportStrategy;
	import com.custardbelly.as3flobile.model.IDisposable;
	
	import flash.display.DisplayObject;
	import flash.geom.Point;

	/**
	 * ITargetScrollAdaptor is an optional adaptor for a scroll target that is used to determine the scroll position to a specified target position. 
	 * @author toddanderson
	 */
	public interface ITargetScrollAdaptor extends IDisposable
	{
		/**
		 * Starts scroll animation toward a given target position. 
		 * @param targetPosition Point The target position.
		 * @param currentPosition Point The current position of scroll target display.
		 * @param content DisplayObject The scroll target display.
		 * @param delegate IScrollViewportStrategy The underlying delegate strategy. Mainly used to access signals.
		 */
		function scrollToPosition( targetPosition:Point, currentPosition:Point, content:DisplayObject, delegate:IScrollViewportStrategy ):void;
		/**
		 * Stops the scroll animation.
		 */
		function stop():void;
	}
}