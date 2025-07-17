/**
 * com.sevenson.math.display.mathml.MSpace
 * 
 * 
 * @author Andrew Sevenson
 * @version 1.0
*/

package com.sevenson.math.display.mathml
{
	import flash.display.Sprite;
	import flash.geom.Rectangle;
	import com.sevenson.math.display.mathml.*;
	import flash.text.TextField;
	
	/**
	 * The MSpace class
	 */
	public class MSpace extends MathMLBaseSprite
	{
		
		// vars
		private var _width:Number = 0;
		private var _height:Number = 0;
		private var _depth:Number = 0;
		
		private var _alignheight:Number = 0;		
		
		
		/**
		 * Creates a new instance of the MSpace class
		 */
		public function MSpace ($node:XML)
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
		

		
		// PROTECTED FUNCTIONS
		// ------------------------------------------------------------------------------------------
		
		/**
		 * This will build this item based on the $node passed in
		 * @param	$node
		 */
		protected function buildContent(node_xml:XMLList):void {
			//
			if(String(tf)==""){ return; }
			// create a text field to use as a reference
			var tf:TextField = MathML.generateTextField();
			tf.htmlText = "A";
			
			// the base line of the text boxes...
			var baseline:Number = tf.height;
			//
			var topbottom:Array = new Array();
			topbottom[0] = baseline - _height;
			topbottom[1] = baseline + _depth;
			topbottom.sort(Array.NUMERIC);
			//
			if(topbottom[0]==topbottom[1]) { topbottom[0]-0.1;}
			
			//
			var leftright:Array = new Array();
			leftright[0] = 0;
			leftright[1] = _width;
			leftright.sort(Array.NUMERIC);
			
			trace(leftright[0] + " " + topbottom[0] +  " " + leftright[1] + " " +topbottom[1]);
			// figure out a draw width (needs to be at least something)
			if(leftright[0]==leftright[1]) { leftright[0] -= 0.01; }
			
			// draw an ivisible box to the required size
			graphics.beginFill(0x000000,1);
			graphics.lineStyle(0,0x000000,0);
			graphics.drawRect(leftright[0],topbottom[0],leftright[1]-leftright[0],topbottom[1]-topbottom[0]);
			
			//
			tf = null;
		}
		
		
		//
		override protected function parseAttributes(node_xml:XML):void {
			//
			if(node_xml.@width!=undefined) {
				_width = Number(node_xml.@width);
			}
			//
			if(node_xml.@depth!=undefined) {
				_depth = Number(node_xml.@depth);
			}
			//
			if(node_xml.@height!=undefined) {
				_height = Number(node_xml.@height);
			}			
			//
			super.parseAttributes(node_xml);
		}		
		
		
		// EVENT HANDLERS
		// ------------------------------------------------------------------------------------------
		
		
		// GETTERS & SETTERS
		// ------------------------------------------------------------------------------------------
		
		//
		override public function get alignHeight():Number {
			var rect:Rectangle = getRect(this);
			return rect.height + rect.top;
		}	
		
	}
}