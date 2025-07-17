package com.codeazur.as3swf.data.abc.bytecode
{
	import com.codeazur.as3swf.data.abc.ABCData;
	import com.codeazur.as3swf.data.abc.bytecode.attributes.ABCOpcodeAttribute;
	import com.codeazur.as3swf.data.abc.bytecode.attributes.ABCOpcodeAttributeFactory;

	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public class ABCOpcodeFactory {

		public static function create(abcData : ABCData, kind : uint) : ABCOpcode {
			const kindType:ABCOpcodeKind = ABCOpcodeKind.getType(kind);
			if(!kindType) {
				throw new Error('Invalid kind type (recieved=' + kind + ')');
			}
			const attribute:ABCOpcodeAttribute = ABCOpcodeAttributeFactory.create(abcData, kindType);
			const opcode:ABCOpcode = ABCOpcode.create(abcData, kindType, attribute);
			opcode.alchemyOpcode = ABCOpcodeKind.isAlchemyOpcode(kindType);
			return opcode;
		}
	}
}