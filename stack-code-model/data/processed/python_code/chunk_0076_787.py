﻿package swf.data.actions.swf4
{
	import swf.data.actions.*;

	class ActionGetVariable extends Action implements IAction
	{
		public static inline var CODE:Int = 0x1c;

		public function ActionGetVariable(code:Int, length:Int, pos:Int) {
			super(code, length, pos);
		}

		override public function toString(indent:Int = 0):String {
			return "[ActionGetVariable]";
		}
	}
}