/**
 * <p>Original Author: toddanderson</p>
 * <p>Class File: IScrollViewportStrategy.as</p>
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
package com.custardbelly.as3flobile.controls.viewport.context
{
	import com.custardbelly.as3flobile.controls.viewport.IScrollViewport;
	import com.custardbelly.as3flobile.controls.viewport.adaptor.ITargetScrollAdaptor;
	import com.custardbelly.as3flobile.model.IDisposable;
	
	import flash.geom.Point;
	
	import org.osflash.signals.Signal;

	/**
	 * IScrollViewportStrategy is the strategy used to animate the scrolling of a viewport. 
	 * @author toddanderson
	 */
	public interface IScrollViewportStrategy extends IDisposable
	{
		/**
		 * Begins a mediated animation sequence with a target IScrollViewport. 
		 * @param viewport IScrollViewport
		 */
		function mediate( viewport:IScrollViewport ):void;
		/**
		 * Ends a mediated animation sequence.
		 */
		function unmediate():void;
		
		/**
		 * Resets any initial values for mediation.
		 */
		function reset():void;
		/**
		 * Starts the scrolling animation session. 
		 * @param point Point The coordinate point at which to start.
		 */
		function start( point:Point ):void;
		/**
		 * Moves the scrolling area. 
		 * @param point Point The coorrdinate point to which to move.
		 */
		function move( point:Point ):void;
		/**
		 * Ends the scrolling animation session. 
		 * @param point Point The corrdinate point at which to end.
		 */
		function end( point:Point ):void;
		
		/**
		 * Returns signal reference of start of scroll. 
		 * @return DeluxeSignal
		 */
		function get scrollStart():Signal;
		/**
		 * Returns signal reference of end of scroll. 
		 * @return DeluxeSignal
		 */
		function get scrollEnd():Signal;
		/**
		 * Returns signal reference of change in scroll. 
		 * @return DeluxeSignal
		 */
		function get scrollChange():Signal;
		
		/**
		 * Accessor/Modifier for the coordinate position of the top/left corner of content within the viewport. 
		 * @return Point
		 */
		function get position():Point;
		function set position( value:Point ):void;
		
		/**
		 * Accessor/Modifier for the target scroll adaptor.
		 * The ITargetScrollAdaptor assumes behaviour of scrolling to a target position.
		 * Scrolling within this strategy is mainly loose scrolling based on user gestures.
		 * When a defined position within the viewport is requested, this adaptor takes over control of seeking to that coordinate.  
		 * @return ITargetScrollAdaptor
		 */
		function get targetScrollAdaptor():ITargetScrollAdaptor;
		function set targetScrollAdaptor(value:ITargetScrollAdaptor):void;
	}
}