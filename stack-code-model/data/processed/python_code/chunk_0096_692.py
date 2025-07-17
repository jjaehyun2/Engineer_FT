package com.codeazur.as3swf.data.abc.exporters.js.builders
{
	import flash.utils.ByteArray;
	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public class JSLiteralKind {
		
		
		public static const ARRAY:JSLiteralKind = new JSLiteralKind();
		public static const OBJECT:JSLiteralKind = new JSLiteralKind();
				
		public function JSLiteralKind() {}
		
		public function write(data:ByteArray):void {
			switch(this) {
				case ARRAY:
					JSTokenKind.LEFT_SQUARE_BRACKET.write(data);
					JSTokenKind.RIGHT_SQUARE_BRACKET.write(data);
					break;
					
				case OBJECT:
					JSTokenKind.LEFT_CURLY_BRACKET.write(data);
					JSTokenKind.RIGHT_CURLY_BRACKET.write(data);
					break;
			}
		}
	}
}