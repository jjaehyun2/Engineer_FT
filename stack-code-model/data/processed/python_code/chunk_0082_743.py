/*
 *	Temple Library for ActionScript 3.0
 *	Copyright © MediaMonks B.V.
 *	All rights reserved.
 *	
 *	Redistribution and use in source and binary forms, with or without
 *	modification, are permitted provided that the following conditions are met:
 *	1. Redistributions of source code must retain the above copyright
 *	   notice, this list of conditions and the following disclaimer.
 *	2. Redistributions in binary form must reproduce the above copyright
 *	   notice, this list of conditions and the following disclaimer in the
 *	   documentation and/or other materials provided with the distribution.
 *	3. All advertising materials mentioning features or use of this software
 *	   must display the following acknowledgement:
 *	   This product includes software developed by MediaMonks B.V.
 *	4. Neither the name of MediaMonks B.V. nor the
 *	   names of its contributors may be used to endorse or promote products
 *	   derived from this software without specific prior written permission.
 *	
 *	THIS SOFTWARE IS PROVIDED BY MEDIAMONKS B.V. ''AS IS'' AND ANY
 *	EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 *	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *	DISCLAIMED. IN NO EVENT SHALL MEDIAMONKS B.V. BE LIABLE FOR ANY
 *	DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 *	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 *	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 *	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *	
 *	
 *	Note: This license does not apply to 3rd party classes inside the Temple
 *	repository with their own license!
 */

package temple.codecomponents.scroll 
{
	import temple.codecomponents.buttons.CodeButton;
	import temple.codecomponents.graphics.CodeBackground;
	import temple.common.enum.Direction;
	import temple.common.enum.Orientation;
	import temple.ui.scroll.IScrollPane;
	import temple.ui.scroll.ScrollBar;
	import temple.ui.scroll.ScrollEvent;

	import flash.display.InteractiveObject;
	import flash.events.MouseEvent;

	/**
	 * @author Thijs Broerse
	 */
	public class CodeScrollBar extends ScrollBar 
	{
		public function CodeScrollBar(orientation:String = Orientation.VERTICAL, size:Number = 160, autoHide:Boolean = true, scrollPane:IScrollPane = null, thickness:Number = 14)
		{
			construct::codeScrollBar(orientation, size, autoHide, scrollPane, thickness);
		}
		
		/**
		 * @private
		 */
		override construct function scrollBar():void
		{
			liquidBehavior.adjustRelated = true;
			addEventListener(ScrollEvent.SCROLL, handleScroll);
			addEventListener(MouseEvent.MOUSE_WHEEL, handleMouseWheel);

			toStringProps.push("orientation");
		}

		/**
		 * @private
		 */
		construct function codeScrollBar(orientation:String, size:Number, autoHide:Boolean, scrollPane:IScrollPane, thickness:Number):void
		{
			this.orientation = orientation;
			
			switch (orientation)
			{
				case Orientation.HORIZONTAL:
				{
					width = size;
					break;
				}
				case Orientation.VERTICAL:
				{
					height = size;
					break;
				}
			}
			
			this.autoHide = autoHide;
			
			createUI(thickness);
			
			this.scrollPane = scrollPane;
		}


		private function createUI(thickness:Number):void 
		{
			track = addChild(new CodeBackground(thickness, thickness)) as InteractiveObject;
			if (orientation == Orientation.VERTICAL)
			{
				button = addChild(new CodeButton(thickness, thickness)) as InteractiveObject;
				upButton = addChild(new CodeScrollButton(Orientation.VERTICAL, Direction.DESCENDING, thickness, thickness)) as InteractiveObject;
				downButton = addChild(new CodeScrollButton(Orientation.VERTICAL, Direction.ASCENDING, thickness, thickness)) as InteractiveObject;
			}
			else
			{
				button = addChild(new CodeButton(thickness, thickness)) as InteractiveObject;
				leftButton = addChild(new CodeScrollButton(Orientation.HORIZONTAL, Direction.DESCENDING, thickness, thickness)) as InteractiveObject;
				rightButton = addChild(new CodeScrollButton(Orientation.HORIZONTAL, Direction.ASCENDING, thickness, thickness)) as InteractiveObject;
			}
			CodeButton(button).outOnDragOut = false;
			autoSizeButton = true;
			minimalButtonSize = 20;
		}
	}
}