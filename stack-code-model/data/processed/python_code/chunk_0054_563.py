/**
 * Copyright (c) 2010 Johnson Center for Simulation at Pine Technical College
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

package quickb2.physics.ai.controllers 
{
	import quickb2.input.qb2I_Keyboard;
	import quickb2.math.general.*;
	import flash.display.*;
	import flash.ui.*;
	import quickb2.input.qb2I_Keyboard;
	import TopDown.objects.*;
	
	/**
	 * ...
	 * @author Doug Koellmer
	 */
	public class qb2I_KeyboardCarController extends qb2I_KeyboardController
	{
		public var turnRate:Number = .1;
		
		private var _leftRight:Number = 0;
		
		public const keysBrake:Vector.<uint>     = new Vector.<uint>();
		public const keysShiftUp:Vector.<uint>   = new Vector.<uint>();
		public const keysShiftDown:Vector.<uint> = new Vector.<uint>();
		
		public function qb2I_KeyboardCarController(keyboard:qb2I_Keyboard)
		{
			super(keyboard);
			
			keysBrake.push(Keyboard.SPACE);
			keysShiftUp.push(221);
			keysShiftDown.push(219);
		}
		
		protected override function activated():void
		{
			if ( host is qb2CarBody )
			{
				brainPort.open = true;
				super.activated();
			}
			else
			{
				brainPort.open = false;
			}
		}
		
		protected override function deactivated():void
		{
			super.deactivated();
			_leftRight = 0;
		}
		
		protected override function update():void
		{
			super.update();
			
			brainPort.clear();
			
			var brakeDown:Boolean   = getKeyboard().isKeyDown(keysBrake);
			var forwardDown:Boolean = getKeyboard().isKeyDown(keysForward);
			var backDown:Boolean    = getKeyboard().isKeyDown(keysBack);
			var leftDown:Boolean    = getKeyboard().isKeyDown(keysLeft);
			var rightDown:Boolean   = getKeyboard().isKeyDown(keyqb2I_ght);
			
			var forwardBack:Number = 0;
			var brake:Number = brakeDown ? 1 : 0;
			
			if ( forwardDown && !backDown )  forwardBack = 1;
			else if ( !forwardDown && backDown )  forwardBack = -1;
		
			if ( leftDown || rightDown )
			{
				if ( leftDown  )
				{
					if ( _leftRight > 0 )  _leftRight = 0;
					_leftRight -= turnRate;
				}
				if ( rightDown )
				{
					if ( _leftRight < 0 )  _leftRight = 0;
					_leftRight += turnRate;
				}
				
				_leftRight = qb2U_Math.constrain(_leftRight, -1, 1);
			}
			else
			{
				_leftRight = 0;
			}
			
			brainPort.NUMBER_PORT_1 = forwardBack;
			brainPort.NUMBER_PORT_2 = _leftRight * (host as qb2CarBody).maxTurnAngle;
			brainPort.NUMBER_PORT_3 = brake;
		}
		
		protected override function keyEvent(keyCode:uint, down:Boolean):void
		{
			super.keyEvent(keyCode, down);
		}
	}
}