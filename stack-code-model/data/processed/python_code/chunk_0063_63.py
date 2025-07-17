/**
 * <p>Original Author: toddanderson</p>
 * <p>Class File: BaseToggleSwitchContext.as</p>
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
package com.custardbelly.as3flobile.controls.toggle.context
{
	import com.custardbelly.as3flobile.controls.slider.context.BaseSliderContext;
	import com.custardbelly.as3flobile.controls.slider.context.ISliderStrategy;
	import com.custardbelly.as3flobile.controls.toggle.IToggleSwitch;
	
	/**
	 * BaseToggleSwitchContext is a base context to manage a IToggleSwitch based on a strategy. 
	 * @author toddanderson
	 */
	public class BaseToggleSwitchContext extends BaseSliderContext implements IToggleSwitchContext
	{
		protected var _toggleStrategy:IToggleSwitchStrategy;
		
		/**
		 * Constructor. 
		 * @param strategy IToggleSwitchStrategy
		 */
		public function BaseToggleSwitchContext( strategy:ISliderStrategy )
		{
			super( strategy );
			_toggleStrategy = ( strategy as IToggleSwitchStrategy );
		}
		
		/**
		 * @copy IToggleSwitchContext#updateSelectedIndex()
		 */
		public function updateSelectedIndex( value:uint ):void
		{
			if( _isActive && _toggleStrategy != null )
			{
				_toggleStrategy.selectIndex( value );
			}
		}
	}
}