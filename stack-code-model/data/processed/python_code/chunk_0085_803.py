﻿package com.codeazur.as3swf.data.actions.swf6
{
	import com.codeazur.as3swf.data.actions.*;
	
	public class ActionStringGreater extends Action implements IAction
	{
		public static const CODE:uint = 0x68;
		
		public function ActionStringGreater(code:uint, length:uint) {
			super(code, length);
		}
		
		public function toString(indent:uint = 0):String {
			return "[ActionStringGreater]";
		}
	}
}