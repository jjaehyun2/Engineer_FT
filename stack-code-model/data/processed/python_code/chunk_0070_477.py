package com.codeazur.as3swf.data.abc.exporters.js.builders.debug
{

	import com.codeazur.as3swf.data.abc.ABC;
	import com.codeazur.as3swf.data.abc.bytecode.attributes.ABCOpcodeAttribute;
	import com.codeazur.as3swf.data.abc.bytecode.attributes.ABCOpcodeDebugAttribute;
	import com.codeazur.as3swf.data.abc.exporters.builders.IABCDebugBuilder;
	import com.codeazur.as3swf.data.abc.exporters.js.ABCJavascriptExporter;
	import com.codeazur.as3swf.data.abc.exporters.js.builders.JSNameBuilder;
	import com.codeazur.as3swf.data.abc.exporters.js.builders.JSTokenKind;
	import com.codeazur.as3swf.data.abc.exporters.js.builders.expressions.JSThisExpression;
	import com.codeazur.as3swf.data.abc.io.IABCWriteable;
	import flash.utils.ByteArray;



	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public class JSDebugBuilder implements IABCDebugBuilder {
		
		public static const METHOD_NAME:String = "debug";
		
		public var _attribute:ABCOpcodeAttribute;
		
		public function JSDebugBuilder() {}
		
		public static function create(attribute:ABCOpcodeAttribute):JSDebugBuilder {
			const builder:JSDebugBuilder = new JSDebugBuilder();
			builder.attribute = attribute;
			return builder; 
		}

		public function write(data : ByteArray) : void {
			if(attribute is ABCOpcodeDebugAttribute) {
				const debug:ABCOpcodeDebugAttribute = ABCOpcodeDebugAttribute(attribute);
				
				JSNameBuilder.create(new <IABCWriteable>[JSThisExpression.create()]).write(data);
				JSTokenKind.DOT.write(data);
				
				data.writeUTF(ABCJavascriptExporter.PREFIX + METHOD_NAME);
				
				JSTokenKind.LEFT_PARENTHESES.write(data);
				
				data.writeUTF(debug.attributes.join(","));
				
				JSTokenKind.RIGHT_PARENTHESES.write(data);
			} else {
				throw new Error();
			}
		}
		
		public function get name():String { return "JSDebugBuilder"; }
		public function get attribute() : ABCOpcodeAttribute { return _attribute; }
		public function set attribute(value : ABCOpcodeAttribute) : void { _attribute = value; }
		
		public function toString(indent:uint=0):String {
			return ABC.toStringCommon(name, indent);
		}
	}
}