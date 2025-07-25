﻿package format.swf.data.actions.swf7
{
	import format.swf.data.actions.*;
	
	class ActionThrow extends Action implements IAction
	{
		public static inline var CODE:Int = 0x2a;
		
		public function ActionThrow(code:Int, length:Int, pos:Int) {
			super(code, length, pos);
		}
		
		override public function toString(indent:Int = 0):String {
			return "[ActionThrow]";
		}
	}
}