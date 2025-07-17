/**
 * com.sevenson.math.display.mathml.MSubSup
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
	 * The MSubSup class
	 */
	public class MSubSup extends MathMLBaseSprite
	{
		
		// vars
		private var _alignheight:Number;
		private var _gutteroffsetinternal:Number = -4;
		
		private var $temp:String;
		
		/**
		 * Creates a new instance of the MSubSup class
		 */
		public function MSubSup ($node:XML)
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
		
		
		// this should build the required content
		protected function buildContent(node_xml:XMLList):void {
			// check that there is enough nodes
			var len:int = node_xml.length();
			if(len!=3) {
				throw new Error("MSubSup was given incorrect number of properties:\n" + node_xml);
				return;
			}
			//
			renderSubSupLayout(node_xml[0], node_xml[1], node_xml[2]);
			
		}		
		
		
		// this will render out the given text
		protected function renderSubSupLayout(basenode:XML, subnode:XML, supnode:XML):void {
			// parse the base
			var base:Sprite = MathML.parseMathMLNode(basenode);
			addChild(base);
			//
			_alignheight = base.height;
			
			// parse the sub
			var sub:Sprite = MathML.parseMathMLNode(subnode);
			addChild(sub);
			sub.scaleX = sub.scaleY = MathML.subSupScale
			
			// parse the sup
			var sup:Sprite = MathML.parseMathMLNode(supnode);
			addChild(sup);
			sup.scaleX = sup.scaleY = MathML.subSupScale;;
			
			// position it
			//base.y = sup.height * 0.4;
			sup.x = (base.x + base.width) + _gutteroffsetinternal;
			sup.y = -(sup.height * 0.3);
			sub.x = (base.x + base.width) + _gutteroffsetinternal;
			sub.y = (base.y + base.height) - (sub.height * 0.7);
			
	$temp = base.width + " " + sub.width + " " + sup.width;
			
		}
		
		// EVENT HANDLERS
		// ------------------------------------------------------------------------------------------
		
		
		// GETTERS & SETTERS
		// ------------------------------------------------------------------------------------------
		
		/**
		 * Returns the height that should be used to align this item
		 */
		override public function get alignHeight():Number {
			return _alignheight;
		}
		
		
		
	}
}