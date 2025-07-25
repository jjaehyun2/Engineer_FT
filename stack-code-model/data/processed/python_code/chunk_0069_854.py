/**
 * This code is part of the Bumpslide Library maintained by David Knape
 * Fork me at http://github.com/tkdave/bumpslide_as3
 * 
 * Copyright (c) 2010 by Bumpslide, Inc. 
 * http://www.bumpslide.com/
 *
 * This code is released under the open-source MIT license.
 * See LICENSE.txt for full license terms.
 * More info at http://www.opensource.org/licenses/mit-license.php
 */
package com.bumpslide.ui.skin.defaults
{

	import com.bumpslide.ui.ISkinnable;
	import com.bumpslide.ui.Label;
	import com.bumpslide.ui.Box;
	import com.bumpslide.ui.Component;
	import com.bumpslide.ui.PixelIcon;
	import com.bumpslide.util.Align;
	import com.bumpslide.util.DisplayUtil;


	/**
	 * Button with a checkbox on it 
	 *
	 * @author David Knape
	 */
	public class DefaultCheckboxSkin extends DefaultButtonSkin
	{
		public var checkBox:Box;
		public var check:Component;

		
		override public function initHostComponent( host_component:ISkinnable ):void
		{
			super.initHostComponent( host_component );
			
			// hide the background (make it like the hit area)
			background.alpha = 0;
			
			checkBox = add( Box, Style.INPUT_BACKGROUND_PROPS );
			
			//checkBox = addChild( new Box( 0xcccccc, 16, 16, 0, 0, 0, 0 ) ) as Box;
			//checkBox.filters = [ Style.BEVEL_FILTER_INSET ];

			//addChild( check = new PixelIcon( [ '*   *', ' * *', '  * ', ' * *', '*   *' ] ) );
			addChild( check = new Label( 'X', Style.BUTTON_TEXT_FORMAT ) );
			
			_off();
		}


		override protected function draw():void
		{
			super.draw();
			if(!checkBox)  return;
			checkBox.width = checkBox.height = background.height;

			Align.center( check, checkBox.width );
			Align.middle( check, checkBox.height );
		}


		override public function _off():void
		{
			checkBox.borderColor = Style.INPUT_BORDER;
			checkBox.backgroundColor = Style.INPUT_BACKGROUND;
			DisplayUtil.colorize( check, Style.BUTTON_LABEL );
			check.visible = false;
		}


		override public function _over():void
		{
			checkBox.borderColor = Style.INPUT_FOCUS_BORDER;
			checkBox.backgroundColor = Style.INPUT_FOCUS_BACKGROUND;
			check.visible = true;
			DisplayUtil.colorize( check, Style.BUTTON_LABEL_OVER );
		}


		override public function _selected():void
		{
			checkBox.borderColor = Style.INPUT_FOCUS_BORDER;
			checkBox.backgroundColor = Style.INPUT_BACKGROUND;
			check.visible = true;
			DisplayUtil.colorize( check, Style.BUTTON_LABEL );
		}


		override public function _down():void
		{
			checkBox.borderColor = Style.INPUT_FOCUS_BORDER;
			checkBox.backgroundColor = Style.INPUT_BACKGROUND;
			check.visible = true;
			DisplayUtil.colorize( check, Style.BUTTON_LABEL );
		}
	}
}