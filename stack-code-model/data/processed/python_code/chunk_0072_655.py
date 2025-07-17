/**
 * com.sevenson.math.display.mathml.MSup
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
	 * The MSup class
	 */
	public class MSup extends MSubSup
	{
		
		// vars
		
		/**
		 * Creates a new instance of the MSup class
		 */
		public function MSup ($node:XML)
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
		
		// this should build the required content
		override protected function buildContent(node_xml:XMLList):void {
			// check that there is enough nodes
			var len:int = node_xml.length();
			if(len!=2) {
				throw new Error("MSup was given incorrect number of properties:\n" + node_xml);
				return;
			}
			
			//
			var tmp:XML = <mn></mn>
			//
			renderSubSupLayout(node_xml[0], tmp, node_xml[1]);
			
		}		
		
		// EVENT HANDLERS
		// ------------------------------------------------------------------------------------------
		
		
		// GETTERS & SETTERS
		// ------------------------------------------------------------------------------------------
		

		
	}
}