/**
 * com.sevenson.math.display.mathml.MFenced
 * 
 * 
 * @author Andrew Sevenson
 * @version 1.0
*/

package com.sevenson.math.display.mathml
{
	import flash.display.Sprite;
	import com.sevenson.math.display.mathml.*;
	import flash.text.TextField;
	
	/**
	 * The MFenced class
	 */
	public class MFenced extends MathMLBaseSprite
	{
		
		// vars
		private var _open:String = "(";
		private var _close:String = ")";
		private var _separators:String = ',';
		
		private var _gutteroffsetinternal:Number = -4;		
		
		
		/**
		 * Creates a new instance of the MFenced class
		 */
		public function MFenced ($node:XML)
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
			// set up an array to hold each of the lements created
			var $item_array:Array = new Array();
			// loop through all of the children, parsing each node and generating clips
			var $len:int = $node.length();
			for(var $i:int=0; $i<$len; $i++) {
				// put in the required divider
				if($i>0 && _separators!="") {
					var $sep:Number = $i-1;
					if($sep>_separators.length-1) { $sep=_separators.length-1; }
					var $tf:TextField = MathML.generateTextField();
					$tf.htmlText = _separators.charAt($sep);
					addChild($tf);
					$item_array.push($tf);
				}
				// parse out each item
				var $s:Sprite = MathML.parseMathMLNode($node[$i]);
				$item_array.push($s);
				addChild($s);
			}

			//
			var $totalheight:Number = height;
			
			// put in the open fence
			var $openfence:Sprite = new Sprite();
			var $opentf:TextField = MathML.generateTextField();
			$opentf.htmlText = _open;
			$openfence.addChild($opentf);
			addChild($openfence);
			$openfence.height = $totalheight;
			
			
			// position 
			for($i=0; $i<$item_array.length; $i++) {
				// vertically
				$item_array[$i].y = ($totalheight/2) - ($item_array[$i].height/2);
				if($item_array[$i] is MathMLBaseSprite) { $item_array[$i].y += $item_array[$i].yoffset; }
				//
				if($i>0) {
					var w:Number = $item_array[$i-1].width;
					if($item_array[$i-1] is MathMLBaseSprite) { w = $item_array[$i-1].alignWidth; }
					$item_array[$i].x = $item_array[$i-1].x + w;
				} else {
					$item_array[$i].x = $openfence.width + _gutteroffsetinternal;
				}
				
				//
				if($item_array[$i-1] is MathMLBaseSprite) {
					$item_array[$i].x += $item_array[$i-1].xoffset;
				}
			}
			
			// put in the close fence		
			var $closefence:Sprite = new Sprite();
			var $closetf:TextField = MathML.generateTextField();
			$closetf.htmlText = _close;
			$closefence.addChild($closetf);
			addChild($closefence);
			$closefence.height = $totalheight;
			//
			$closefence.x = width + _gutteroffsetinternal;
			
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
			if($xml.@open!=undefined) {
				_open = String($xml.@open);
			}
			//
			if($xml.@close!=undefined) {
				_close = String($xml.@close);
			}
			//
			if($xml.@separators!=undefined) {
				_separators = String($xml.@separators);
			}
		}			
		
		// EVENT HANDLERS
		// ------------------------------------------------------------------------------------------
		
		
		// GETTERS & SETTERS
		// ------------------------------------------------------------------------------------------
		
		
		
	}
}