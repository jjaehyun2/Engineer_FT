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

package temple.codecomponents.style 
{
	import flash.text.StyleSheet;
	import flash.filters.DropShadowFilter;
	import flash.filters.BevelFilter;
	import flash.filters.GlowFilter;
	import flash.text.TextFormat;

	/**
	 * This class defines the design of the CodeComponents.
	 * 
	 * <p>It's possible to alter this property to change the look of the CodeComponents. This must be done before you
	 * create the components.</p>
	 * 
	 * @author Thijs Broerse
	 */
	public final class CodeStyle 
	{
		/**
		 * Text
		 */
		public static const textFormat:TextFormat = new TextFormat();
		public static var textColor:uint = 0x000000;
		public static var CSS:String = 
		<css><![CDATA[
			a
			{
				text-decoration: underline;
			}
			h1
			{
				font-size: 20px;
			}
		]]>
		</css>;
		public static const styleSheet:StyleSheet = new StyleSheet();
		
		/**
		 * Background properties
		 */
		public static var backgroundColor:uint = 0xffffff;
		public static var backgroundAlpha:Number = .9;
		public static const backgroundFilters:Array = [new DropShadowFilter(2, 45, 0, 1, 2, 2, .5, 1, true)];
		
		/**
		 * Button
		 */
		public static var buttonColor:uint = 0x999999;
		public static var buttonAlpha:Number = 1;
		public static const buttonFilters:Array = [new BevelFilter(1, 45, 0xffffff, 1, 0x000000, 1, 1, 1, 1, 1)];
		public static var buttonOverstateColor:uint = 0xeeeeee;
		public static var buttonOverstateAlpha:Number = 1;
		public static const buttonDownFilters:Array = [new BevelFilter(1, 225, 0xffffff, 1, 0x000000, 1, 1, 1, 1, 1)];
		public static var buttonDownstateColor:uint = 0xaaaaaa;
		public static var buttonDownstateAlpha:Number = 1;
		public static var buttonSelectstateColor:uint = 0xeeeeee;
		public static var buttonSelectstateAlpha:Number = .5;
		
		/**
		 * Focus
		 */
		public static var focusColor:uint = 0xffffff;
		public static var focusAlpha:Number = .5;
		public static var focusThickness:Number = 2;
		public static const focusFilters:Array = [new GlowFilter(focusColor, focusAlpha, 2 * focusThickness, 2 * focusThickness, 2, 1, false, true)];

		/**
		 * Error
		 */
		public static var errorColor:uint = 0xff0000;
		public static var errorAlpha:Number = .5;
		public static var errorThickness:Number = 2;
		public static const errorFilters:Array = [new GlowFilter(errorColor, errorAlpha, 2 * errorThickness, 2 * errorThickness, 2, 1, false, true)];
		
		/**
		 * Icons
		 */
		public static var iconColor:uint = 0x000000;
		public static var iconAlpha:Number = .5;
		public static const iconFilters:Array = [new DropShadowFilter(1, 45, 0, 1, 2, 2)];
		
		/**
		 * List
		 */
		public static var listItemSelectstateColor:uint = 0x888888;
		public static var listItemSelectstateAlpha:Number = .5;
		public static var listItemOverstateColor:uint = 0x888888;
		public static var listItemOverstateAlpha:Number = .2;
		
		/**
		 * ComboBox
		 */
		public static const comboBoxListFilter:Array = [new DropShadowFilter(4, 45, 9, 1, 4, 4, .6)];
		
		/**
		 * ToolTip
		 */
		public static var toolTipBackgroundColor:uint = 0xFFFFFF;
		public static var toolTipBackgroundAlpha:Number = .8;
		public static var toolTipBorderColor:uint = 0x000000;
		public static var toolTipBorderAlpha:Number = 1;
		public static var toolTipTextColor:uint = 0x000000;
		public static const toolTipTextFormat:TextFormat = new TextFormat();
		public static const toolTipFilters:Array = [new DropShadowFilter(4, 45, 9, 1, 4, 4, .2)];
		
		/**
		 * Window
		 */
		public static var windowBackgroundColor:uint = 0xdddddd;
		public static var windowBackgroundAlpha:Number = .9;
		public static const windowFilters:Array = [new DropShadowFilter(4, 45, 0, 1, 8, 8, .3)];
		public static var windowBorderBackgroundColor:uint = 0x999999;
		public static var windowBorderBackgroundAlpha:Number = 1;
		public static const windowBorderFilters:Array = [new BevelFilter(1, 45, 0xffffff, 1, 0x000000, 1, 1, 1, 1, 1)];
		

		private static function init():void 
		{
			styleSheet.parseCSS(CSS);
			
			textFormat.font = "_sans";
			textFormat.size = 11;
			textFormat.leftMargin = textFormat.rightMargin = 4;
			textFormat.color = textColor;

			toolTipTextFormat.font = "_sans";
			toolTipTextFormat.size = 10;
			toolTipTextFormat.leftMargin = toolTipTextFormat.rightMargin = 0;
		}
		
		init();
	}
}