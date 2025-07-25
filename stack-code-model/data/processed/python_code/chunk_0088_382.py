﻿package com.codeazur.as3swf.data.actions.swf4
{
	import com.codeazur.as3swf.data.actions.*;
	
	public class ActionNot extends Action implements IAction
	{
		public static const CODE:uint = 0x12;
		
		public function ActionNot(code:uint, length:uint) {
			super(code, length);
		}
		
		public function toString(indent:uint = 0):String {
			return "[ActionNot]";
		}
	}
}