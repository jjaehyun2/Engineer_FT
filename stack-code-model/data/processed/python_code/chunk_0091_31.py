﻿package com.codeazur.as3swf.data.actions.swf5
{
	import com.codeazur.as3swf.data.actions.*;
	
	public class ActionBitLShift extends Action implements IAction
	{
		public static const CODE:uint = 0x63;
		
		public function ActionBitLShift(code:uint, length:uint) {
			super(code, length);
		}
		
		public function toString(indent:uint = 0):String {
			return "[ActionBitLShift]";
		}
	}
}