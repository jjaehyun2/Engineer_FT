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

package temple.ui.labels 
{
	import temple.core.display.IDisplayObject;

	/**
	 * @author Thijs Broerse
	 */
	public interface ILabelContainer extends ITextFieldLabel, IDisplayObject
	{
		/**
		 * Space between the left side of the TextField and the left border of the container.
		 * If NaN property is not used
		 */
		function get paddingLeft():Number;

		/**
		 * @inheritDoc
		 */
		function set paddingLeft(value:Number):void
		
		/**
		 * Space between the right side of the TextField and the right border of the container.
		 * If NaN property is not used
		 */
		function get paddingRight():Number;

		/**
		 * @inheritDoc
		 */
		function set paddingRight(value:Number):void
		
		/**
		 * Space between the top of the TextField and the top of the container.
		 * If NaN property is not used
		 */
		function get paddingTop():Number;

		/**
		 * @inheritDoc
		 */
		function set paddingTop(value:Number):void
		
		/**
		 * Space between the bottom side of the TextField and the bottom of the container.
		 * If NaN property is not used
		 */
		function get paddingBottom():Number;

		/**
		 * @inheritDoc
		 */
		function set paddingBottom(value:Number):void
		
		/**
		 * Property to set paddingLeft, paddingRight, paddingTop and paddingBottom at once.
		 * If paddingLeft, paddingRight, paddingTop and paddingBottom are not equal, NaN will be returned
		 */
		function get padding():Number;

		/**
		 * @inheritDoc
		 */
		function set padding(value:Number):void
	}
}