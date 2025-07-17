/**
 * <p>Original Author: toddanderson</p>
 * <p>Class File: DividerSkin.as</p>
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
package com.custardbelly.as3flobile.skin
{
	import com.custardbelly.as3flobile.controls.shape.Divider;
	
	import flash.display.Graphics;

	/**
	 * DividerSkin is the base skin class for a divider display. 
	 * @author toddanderson
	 */
	public class DividerSkin extends Skin
	{
		/**
		 * Constructor.
		 */
		public function DividerSkin() { super(); }
		
		/**
		 * @inherit
		 */
		override protected function clearDisplay():void
		{
			super.clearDisplay();
			var background:Graphics = ( _target as Divider ).background;
			background.clear();
		}
		
		/**
		 * @private
		 * 
		 * Updates the background display of the target Divider. 
		 * @param display Graphics
		 * @param width int
		 * @param height int
		 */
		protected function updateBackground( display:Graphics, width:int, height:int ):void
		{
			display.clear();
			display.beginFill( 0xAAAAAA );
			display.drawRect( 0, 0, width, height );
			display.endFill();
		}
		
		/**
		 * @inherit
		 */
		override public function updateDisplay(width:int, height:int):void
		{
			super.updateDisplay( width, height );
			
			var background:Graphics = ( _target as Divider ).background;
			updateBackground( background, width, height );
		}
	}
}