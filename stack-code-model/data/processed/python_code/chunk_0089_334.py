/**
 * com.sevenson.math.display.mathml.MFrac
 * 
 * 
 * @author Andrew Sevenson
 * @version 1.0
*/

package com.sevenson.math.display.mathml
{
	import flash.display.Sprite;
	import com.sevenson.math.display.mathml.*;
	import flash.geom.Rectangle;
	import flash.display.LineScaleMode;
	import flash.display.CapsStyle;
	
	/**
	 * The MFrac class
	 */
	public class MFrac extends MathMLBaseSprite
	{
		
		// vars
		private var _linethickness:Number = 1;
		private var _gutteroffsetexternal:Number = 3;
		
		/**
		 * Creates a new instance of the MFrac class
		 */
		public function MFrac ($node:XML)
		{
			//
			super($node);
			//
			buildContent($node.child('*'));
		}
		
		
		// STATIC PUBLIC FUNCTIONS
		// ------------------------------------------------------------------------------------------
		
		
		// STATIC PRIVATE FUNCTIONS
		// ------------------------------------------------------------------------------------------
		
		
		// PUBLIC FUNCTIONS
		// ------------------------------------------------------------------------------------------

		
		
		// PRIVATE FUNCTIONS
		// ------------------------------------------------------------------------------------------
		
		/**
		 * This will build this item based on the $node passed in
		 * @param	$node
		 */
		private function buildContent($node:XMLList):void {
			// check that there is enough nodes
			var len:int = $node.length();
			if(len!=2) {
				throw new Error("MFRAC was given incorrect number of properties:\n" + $node);
				return;
			}
			
			//
			
			// parse the two halves...
			var numerator:Sprite = MathML.parseMathMLNode($node[0]);
			addChild(numerator);
			
			var denominator:Sprite = MathML.parseMathMLNode($node[1]);
			addChild(denominator);
			
			// draw in the line
			var tempwidths:Array = [numerator.width, denominator.width]
			tempwidths.sort(Array.NUMERIC | Array.DESCENDING);
			var line:Sprite = new Sprite();
			if(_linethickness>0) {
				//trace(">>> " + _linethickness);
				line.graphics.lineStyle(_linethickness,  int(MathML.currentTextFormat.color), 1, false, LineScaleMode.NONE, CapsStyle.NONE);
				line.graphics.lineTo(tempwidths[0],0);
				addChild(line);
			}
			// position everything
			var nrect:Rectangle = numerator.getRect(numerator);
			var drect:Rectangle = denominator.getRect(denominator);
			
			// vertically
			line.y = (numerator.y + numerator.height + _linethickness) + nrect.top;;
			denominator.y = (line.y + _linethickness) - drect.top;

			// horizontally
			if(numerator.width>denominator.width) {
				denominator.x = (numerator.width/2) - (denominator.width/2);
			} else {
				numerator.x = (denominator.width/2) - (numerator.width/2);
			}
			
			// apply the internal offsets
			denominator.x += _gutteroffsetexternal;
			numerator.x += _gutteroffsetexternal;
			line.x += _gutteroffsetexternal;
			
			// apply the offsets, etc...
			numerator.y += (numerator as MathMLBaseSprite).yoffset;
			numerator.x += (numerator as MathMLBaseSprite).xoffset;

			denominator.y += (denominator as MathMLBaseSprite).yoffset;
			denominator.x += (denominator as MathMLBaseSprite).xoffset;			

			line.y += (denominator as MathMLBaseSprite).yoffset;
			line.x += (denominator as MathMLBaseSprite).xoffset;			
			
			
		}		
		
		
		// PROTECTED FUNCTIONS
		// ------------------------------------------------------------------------------------------
		
		/**
		 * Parses the attributes from the passed in xml
		 * @param	$xml
		 */
		override protected function parseAttributes($xml:XML):void {
			//
			super.parseAttributes($xml)
			//
			if($xml.@linethickness!=undefined) {
				_linethickness = Number($xml.@linethickness);
				if(_linethickness<0) { _linethickness =0; }
			}
		}			
		
		// EVENT HANDLERS
		// ------------------------------------------------------------------------------------------
		
		
		// GETTERS & SETTERS
		// ------------------------------------------------------------------------------------------
		
		/**
		 * Returns the width that should be used to align this item
		 */
		override public function get alignWidth():Number {
			return width + (_gutteroffsetexternal*2);
		}
		
	}
}