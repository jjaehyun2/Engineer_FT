/**
 * com.sevenson.math.display.mathml.MSqrt
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
	 * The MSqrt class
	 */
	public class MSqrt extends MRoot
	{
		
		// vars

		
		/**
		 * Creates a new instance of the MSqrt class
		 */
		public function MSqrt ($node:XML)
		{
			//
			super($node);
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
		// this should build the required content
		override protected function buildContent(node_xml:XMLList):void {
			// check that there is enough nodes
			var len:int = node_xml.length();
			if(len!=1) {
				throw new Error("MSQRT was given incorrect number of properties:\n" + node_xml);
				return;
			}
			//
			var tmp:XML = <mn></mn>
			//
			renderRootLayout(node_xml[0], tmp);
			
		}			
		
		override protected function verticallyPositionElements($base:Sprite, $power:Sprite, $radical:Sprite):void {
			// position it
			if ($power && $power.parent) $power.parent.removeChild($power);
			//$radical.y  = $base.y = _linethickness + ($power.y + $power.height) - ($base.height * 0.5);
			
		}		
		
		// EVENT HANDLERS
		// ------------------------------------------------------------------------------------------
		
		
		// GETTERS & SETTERS
		// ------------------------------------------------------------------------------------------
		
		
	}
}