/**
 * com.sevenson.math.display.mathml.MRow
 * 
 * 
 * @author Andrew Sevenson
 * @version 1.0
*/

package com.sevenson.math.display.mathml
{
	import flash.display.Sprite;
	import com.sevenson.math.display.mathml.*;
	
	/**
	 * The MRow class
	 */
	public class MRow extends MathMLBaseSprite
	{
		
		
		/**
		 * Creates a new instance of the MRow class
		 */
		public function MRow ($node:XML)
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
		private function buildContent(node_xml:XMLList):void {
			// set up an array to hold each of the lements created
			var item_array:Array = new Array();
			// loop through all of the children, parsing each node and generating clips
			var len:int = node_xml.length();
			for(var i:int=0; i<len; i++) {
				// parse out each item
				var s:Sprite = MathML.parseMathMLNode(node_xml[i]);
				item_array.push(s);
				addChild(s);
				// position next to the last
				if (i > 0) {
					s.x = item_array[i - 1].x + item_array[i - 1].alignWidth;
				}
				if(s is MathMLBaseSprite) {
					s.x += MathMLBaseSprite(s).xoffset;
				}				
				
			}
			//
			var totalheight:Number = height;
			
			// position vertically?
			for(i=0; i<item_array.length; i++) {
				//trace("@ " + item_array[i].yoffset);
				item_array[i].y = (totalheight*0.5) - (item_array[i].alignHeight*0.5) + item_array[i].yoffset;
			}
			
		}
		
		// PROTECTED FUNCTIONS
		// ------------------------------------------------------------------------------------------
		
		
		
		// EVENT HANDLERS
		// ------------------------------------------------------------------------------------------
		
		
		// GETTERS & SETTERS
		// ------------------------------------------------------------------------------------------
		
		
	}
}