package com.codeazur.as3swf.data.abc.bytecode.traits
{
	import flash.utils.Dictionary;
	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public class ABCTraitInfoFlags {
		
		private static const _types:Dictionary = new Dictionary();
		
		public static const FINAL:ABCTraitInfoFlags = new ABCTraitInfoFlags(0x01);
		public static const OVERRIDE:ABCTraitInfoFlags = new ABCTraitInfoFlags(0x02);
		public static const METADATA:ABCTraitInfoFlags = new ABCTraitInfoFlags(0x04);

		private var _type:uint;

		public function ABCTraitInfoFlags(type:uint) {
			_type = type;
			_types[this] = type; 
		}
		
		public static function isType(flag:uint, type:ABCTraitInfoFlags):Boolean {
			return ((flag >> 4) & type._type) != 0; 
		}
		
		public function get type():uint { return _type; }
	}
}