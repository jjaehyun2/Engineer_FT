﻿package com.codeazur.as3swf.factories
{
	import com.codeazur.as3swf.data.actions.*;
	import com.codeazur.as3swf.data.actions.swf3.*;
	import com.codeazur.as3swf.data.actions.swf4.*;
	import com.codeazur.as3swf.data.actions.swf5.*;
	import com.codeazur.as3swf.data.actions.swf6.*;
	import com.codeazur.as3swf.data.actions.swf7.*;
	
	public class SWFActionFactory
	{
		public static function create(code:uint, length:uint):IAction
		{
			switch(code)
			{
				/* 0x04 */ case ActionNextFrame.CODE: 		return new ActionNextFrame(code, length);
				/* 0x05 */ case ActionPreviousFrame.CODE: 	return new ActionPreviousFrame(code, length);
				/* 0x06 */ case ActionPlay.CODE: 			return new ActionPlay(code, length);
				/* 0x07 */ case ActionStop.CODE: 			return new ActionStop(code, length);
				/* 0x08 */ case ActionToggleQuality.CODE: 	return new ActionToggleQuality(code, length);
				/* 0x09 */ case ActionStopSounds.CODE: 		return new ActionStopSounds(code, length);
				/* 0x0a */ case ActionAdd.CODE: 			return new ActionAdd(code, length);
				/* 0x0b */ case ActionSubtract.CODE: 		return new ActionSubtract(code, length);
				/* 0x0c */ case ActionMultiply.CODE: 		return new ActionMultiply(code, length);
				/* 0x0d */ case ActionDivide.CODE: 			return new ActionDivide(code, length);
				/* 0x0e */ case ActionEquals.CODE: 			return new ActionEquals(code, length);
				/* 0x0f */ case ActionLess.CODE: 			return new ActionLess(code, length);
				/* 0x10 */ case ActionAnd.CODE: 			return new ActionAnd(code, length);
				/* 0x11 */ case ActionOr.CODE: 				return new ActionOr(code, length);
				/* 0x12 */ case ActionNot.CODE: 			return new ActionNot(code, length);
				/* 0x13 */ case ActionStringEquals.CODE: 	return new ActionStringEquals(code, length);
				/* 0x14 */ case ActionStringLength.CODE: 	return new ActionStringLength(code, length);
				/* 0x15 */ case ActionStringExtract.CODE: 	return new ActionStringExtract(code, length);
				/* 0x17 */ case ActionPop.CODE: 			return new ActionPop(code, length);
				/* 0x18 */ case ActionToInteger.CODE: 		return new ActionToInteger(code, length);
				/* 0x1c */ case ActionGetVariable.CODE: 	return new ActionGetVariable(code, length);
				/* 0x1d */ case ActionSetVariable.CODE: 	return new ActionSetVariable(code, length);
				/* 0x20 */ case ActionSetTarget2.CODE: 		return new ActionSetTarget2(code, length);
				/* 0x21 */ case ActionStringAdd.CODE: 		return new ActionStringAdd(code, length);
				/* 0x22 */ case ActionGetProperty.CODE: 	return new ActionGetProperty(code, length);
				/* 0x23 */ case ActionSetProperty.CODE: 	return new ActionSetProperty(code, length);
				/* 0x24 */ case ActionCloneSprite.CODE: 	return new ActionCloneSprite(code, length);
				/* 0x25 */ case ActionRemoveSprite.CODE: 	return new ActionRemoveSprite(code, length);
				/* 0x26 */ case ActionTrace.CODE: 			return new ActionTrace(code, length);
				/* 0x27 */ case ActionStartDrag.CODE: 		return new ActionStartDrag(code, length);
				/* 0x28 */ case ActionEndDrag.CODE: 		return new ActionEndDrag(code, length);
				/* 0x29 */ case ActionStringLess.CODE: 		return new ActionStringLess(code, length);
				/* 0x2a */ case ActionThrow.CODE: 			return new ActionThrow(code, length);
				/* 0x2b */ case ActionCastOp.CODE: 			return new ActionCastOp(code, length);
				/* 0x2c */ case ActionImplementsOp.CODE: 	return new ActionImplementsOp(code, length);
				/* 0x30 */ case ActionRandomNumber.CODE: 	return new ActionRandomNumber(code, length);
				/* 0x31 */ case ActionMBStringLength.CODE: 	return new ActionMBStringLength(code, length);
				/* 0x32 */ case ActionCharToAscii.CODE: 	return new ActionCharToAscii(code, length);
				/* 0x33 */ case ActionAsciiToChar.CODE: 	return new ActionAsciiToChar(code, length);
				/* 0x34 */ case ActionGetTime.CODE: 		return new ActionGetTime(code, length);
				/* 0x35 */ case ActionMBStringExtract.CODE: return new ActionMBStringExtract(code, length);
				/* 0x36 */ case ActionMBCharToAscii.CODE: 	return new ActionMBCharToAscii(code, length);
				/* 0x37 */ case ActionMBAsciiToChar.CODE: 	return new ActionMBAsciiToChar(code, length);
				/* 0x3a */ case ActionDelete.CODE: 			return new ActionDelete(code, length);
				/* 0x3b */ case ActionDelete2.CODE: 		return new ActionDelete2(code, length);
				/* 0x3c */ case ActionDefineLocal.CODE: 	return new ActionDefineLocal(code, length);
				/* 0x3d */ case ActionCallFunction.CODE: 	return new ActionCallFunction(code, length);
				/* 0x3e */ case ActionReturn.CODE: 			return new ActionReturn(code, length);
				/* 0x3f */ case ActionModulo.CODE: 			return new ActionModulo(code, length);
				/* 0x40 */ case ActionNewObject.CODE: 		return new ActionNewObject(code, length);
				/* 0x41 */ case ActionDefineLocal2.CODE: 	return new ActionDefineLocal2(code, length);
				/* 0x42 */ case ActionInitArray.CODE: 		return new ActionInitArray(code, length);
				/* 0x43 */ case ActionInitObject.CODE: 		return new ActionInitObject(code, length);
				/* 0x44 */ case ActionTypeOf.CODE: 			return new ActionTypeOf(code, length);
				/* 0x45 */ case ActionTargetPath.CODE: 		return new ActionTargetPath(code, length);
				/* 0x46 */ case ActionEnumerate.CODE: 		return new ActionEnumerate(code, length);
				/* 0x47 */ case ActionAdd2.CODE: 			return new ActionAdd2(code, length);
				/* 0x48 */ case ActionLess2.CODE: 			return new ActionLess2(code, length);
				/* 0x49 */ case ActionEquals2.CODE: 		return new ActionEquals2(code, length);
				/* 0x4a */ case ActionToNumber.CODE: 		return new ActionToNumber(code, length);
				/* 0x4b */ case ActionToString.CODE: 		return new ActionToString(code, length);
				/* 0x4c */ case ActionPushDuplicate.CODE: 	return new ActionPushDuplicate(code, length);
				/* 0x4d */ case ActionStackSwap.CODE: 		return new ActionStackSwap(code, length);
				/* 0x4e */ case ActionGetMember.CODE: 		return new ActionGetMember(code, length);
				/* 0x4f */ case ActionSetMember.CODE: 		return new ActionSetMember(code, length);
				/* 0x50 */ case ActionIncrement.CODE: 		return new ActionIncrement(code, length);
				/* 0x51 */ case ActionDecrement.CODE: 		return new ActionDecrement(code, length);
				/* 0x52 */ case ActionCallMethod.CODE: 		return new ActionCallMethod(code, length);
				/* 0x53 */ case ActionNewMethod.CODE: 		return new ActionNewMethod(code, length);
				/* 0x54 */ case ActionInstanceOf.CODE: 		return new ActionInstanceOf(code, length);
				/* 0x55 */ case ActionEnumerate2.CODE: 		return new ActionEnumerate2(code, length);
				/* 0x60 */ case ActionBitAnd.CODE: 			return new ActionBitAnd(code, length);
				/* 0x61 */ case ActionBitOr.CODE: 			return new ActionBitOr(code, length);
				/* 0x62 */ case ActionBitXor.CODE: 			return new ActionBitXor(code, length);
				/* 0x63 */ case ActionBitLShift.CODE: 		return new ActionBitLShift(code, length);
				/* 0x64 */ case ActionBitRShift.CODE: 		return new ActionBitRShift(code, length);
				/* 0x65 */ case ActionBitURShift.CODE: 		return new ActionBitURShift(code, length);
				/* 0x66 */ case ActionStrictEquals.CODE: 	return new ActionStrictEquals(code, length);
				/* 0x67 */ case ActionGreater.CODE: 		return new ActionGreater(code, length);
				/* 0x68 */ case ActionStringGreater.CODE: 	return new ActionStringGreater(code, length);
				/* 0x69 */ case ActionExtends.CODE: 		return new ActionExtends(code, length);
				/* 0x81 */ case ActionGotoFrame.CODE: 		return new ActionGotoFrame(code, length);
				/* 0x83 */ case ActionGetURL.CODE: 			return new ActionGetURL(code, length);
				/* 0x87 */ case ActionStoreRegister.CODE: 	return new ActionStoreRegister(code, length);
				/* 0x88 */ case ActionConstantPool.CODE: 	return new ActionConstantPool(code, length);
				/* 0x8a */ case ActionWaitForFrame.CODE: 	return new ActionWaitForFrame(code, length);
				/* 0x8b */ case ActionSetTarget.CODE: 		return new ActionSetTarget(code, length);
				/* 0x8c */ case ActionGotoLabel.CODE: 		return new ActionGotoLabel(code, length);
				/* 0x8d */ case ActionWaitForFrame2.CODE: 	return new ActionWaitForFrame2(code, length);
				/* 0x8e */ case ActionDefineFunction2.CODE: return new ActionDefineFunction2(code, length);
				/* 0x8f */ case ActionTry.CODE: 			return new ActionTry(code, length);
				/* 0x94 */ case ActionWith.CODE: 			return new ActionWith(code, length);
				/* 0x96 */ case ActionPush.CODE: 			return new ActionPush(code, length);
				/* 0x99 */ case ActionJump.CODE: 			return new ActionJump(code, length);
				/* 0x9a */ case ActionGetURL2.CODE: 		return new ActionGetURL2(code, length);
				/* 0x9b */ case ActionDefineFunction.CODE: 	return new ActionDefineFunction(code, length);
				/* 0x9d */ case ActionIf.CODE: 				return new ActionIf(code, length);
				/* 0x9e */ case ActionCall.CODE: 			return new ActionCall(code, length);
				/* 0x9f */ case ActionGotoFrame2.CODE: 		return new ActionGotoFrame2(code, length);
						   default: 						return new ActionUnknown(code, length);
			}
		}
	}
}