﻿package nid.xfl.compiler.swf.data.actions.swf4
{
	import nid.xfl.compiler.swf.data.actions.*;
	
	public class ActionAdd extends Action implements IAction
	{
		public static const CODE:uint = 0x0a;
		
		public function ActionAdd(code:uint, length:uint) {
			super(code, length);
		}
		
		override public function toString(indent:uint = 0):String {
			return "[ActionAdd]";
		}
	}
}