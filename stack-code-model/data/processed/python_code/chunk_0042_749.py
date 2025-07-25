﻿/*
 * BetweenAS3
 * 
 * Licensed under the MIT License
 * 
 * Copyright (c) 2009 BeInteractive! (www.be-interactive.org) and
 *                    Spark project  (www.libspark.org)
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
 * 
 */
package org.libspark.betweenas3.tickers
{
	import flash.utils.getTimer;
	import org.libspark.as3unit.assert.*;
	import org.libspark.as3unit.test;
	
	use namespace test;
	
	/**
	 * @author	yossy:beinteractive
	 */
	public class EnterFrameTickerTest
	{
		test function update():void
		{
			var l01:MockTickerListener = new MockTickerListener(1);
			var l02:MockTickerListener = new MockTickerListener(1);
			var l03:MockTickerListener = new MockTickerListener(2);
			var l04:MockTickerListener = new MockTickerListener(3);
			var l05:MockTickerListener = new MockTickerListener(5);
			var l06:MockTickerListener = new MockTickerListener(8);
			var l07:MockTickerListener = new MockTickerListener(13);
			var l08:MockTickerListener = new MockTickerListener(21);
			var l09:MockTickerListener = new MockTickerListener(34);
			var l10:MockTickerListener = new MockTickerListener(55);
			var l11:MockTickerListener = new MockTickerListener(89);
			var l12:MockTickerListener = new MockTickerListener(144);
			var l13:MockTickerListener = new MockTickerListener(233);
			var l14:MockTickerListener = new MockTickerListener(377);
			var l15:MockTickerListener = new MockTickerListener(610);
			var l16:MockTickerListener = new MockTickerListener(987);
			var l17:MockTickerListener = new MockTickerListener(1597);
			var l18:MockTickerListener = new MockTickerListener(2584);
			var l19:MockTickerListener = new MockTickerListener(4181);
			var l20:MockTickerListener = new MockTickerListener(6765);
			var l21:MockTickerListener = new MockTickerListener(10946);
			var l22:MockTickerListener = new MockTickerListener(17711);
			var l23:MockTickerListener = new MockTickerListener(28657);
			var l24:MockTickerListener = new MockTickerListener(46368);
			
			var ticker:EnterFrameTicker = new EnterFrameTicker();
			
			ticker.addTickerListener(l01);
			ticker.addTickerListener(l02);
			ticker.addTickerListener(l03);
			ticker.addTickerListener(l04);
			ticker.addTickerListener(l05);
			ticker.addTickerListener(l06);
			ticker.addTickerListener(l07);
			ticker.addTickerListener(l08);
			ticker.addTickerListener(l09);
			ticker.addTickerListener(l10);
			ticker.addTickerListener(l11);
			ticker.addTickerListener(l12);
			ticker.addTickerListener(l13);
			ticker.addTickerListener(l14);
			ticker.addTickerListener(l15);
			ticker.addTickerListener(l16);
			ticker.addTickerListener(l17);
			ticker.addTickerListener(l18);
			ticker.addTickerListener(l19);
			ticker.addTickerListener(l20);
			ticker.addTickerListener(l21);
			ticker.addTickerListener(l22);
			ticker.addTickerListener(l23);
			ticker.addTickerListener(l24);
			
			for (var i:uint = 1; i < 50000; ++i) {
				ticker.update(null);
			}
			
			assertEquals(1, l01.c);
			assertEquals(1, l02.c);
			assertEquals(2, l03.c);
			assertEquals(3, l04.c);
			assertEquals(5, l05.c);
			assertEquals(8, l06.c);
			assertEquals(13, l07.c);
			assertEquals(21, l08.c);
			assertEquals(34, l09.c);
			assertEquals(55, l10.c);
			assertEquals(89, l11.c);
			assertEquals(144, l12.c);
			assertEquals(233, l13.c);
			assertEquals(377, l14.c);
			assertEquals(610, l15.c);
			assertEquals(987, l16.c);
			assertEquals(1597, l17.c);
			assertEquals(2584, l18.c);
			assertEquals(4181, l19.c);
			assertEquals(6765, l20.c);
			assertEquals(10946, l21.c);
			assertEquals(17711, l22.c);
			assertEquals(28657, l23.c);
			assertEquals(46368, l24.c);
		}
		
		/**
		test function speed():void
		{
			var i:uint;
			var ticker:EnterFrameTicker = new EnterFrameTicker();
			
			for (i = 0; i < 8000; ++i) {
				ticker.addTickerListener(new MockTickerListener(600));
			}
			
			var t:uint = getTimer();
			
			for (i = 0; i < 600; ++i) {
				ticker.update(null);
			}
			
			trace('time<' + (getTimer() - t) + '>');
		}
		/**/
		
		test function addListenerInTick():void
		{
			var ticker:EnterFrameTicker = new EnterFrameTicker();
			
			var l3:MockTickerListener = new MockTickerListener(5);
			var l2:MockTickerListener = new MockTickerListener(5);
			var l1:AddingListenerTickerListener = new AddingListenerTickerListener(5, ticker, l3);
			
			ticker.addTickerListener(l1);
			ticker.addTickerListener(l2);
			
			ticker.update(null);
			ticker.update(null);
			
			assertEquals(2, l1.c);
			assertEquals(2, l2.c);
			assertEquals(1, l3.c);
		}
		
		// http://www.libspark.org/ticket/108
		test function issue108():void
		{
			var ticker:EnterFrameTicker = new EnterFrameTicker();
			
			var l8:MockTickerListener = new MockTickerListener(2);
			var l7:MockTickerListener = new MockTickerListener(2);
			var l6:MockTickerListener = new MockTickerListener(2);
			var l5:MockTickerListener = new MockTickerListener(2);
			var l4:MockTickerListener = new MockTickerListener(2);
			var l3:MockTickerListener = new MockTickerListener(2);
			var l2_2:MockTickerListener = new MockTickerListener(2);
			var l2_1:AddingListenerTickerListener = new AddingListenerTickerListener(1, ticker, l2_2);
			var l1:MockTickerListener = new MockTickerListener(1);
			
			ticker.addTickerListener(l8);
			ticker.addTickerListener(l7);
			ticker.addTickerListener(l6);
			ticker.addTickerListener(l5);
			ticker.addTickerListener(l4);
			ticker.addTickerListener(l3);
			ticker.addTickerListener(l2_1);
			ticker.addTickerListener(l1);
			
			ticker.update(null);
			ticker.update(null);
			ticker.update(null);
			ticker.update(null);
			
			assertEquals(1, l1.c);
			assertEquals(1, l2_1.c);
			assertEquals(2, l2_2.c);
			assertEquals(2, l3.c);
			assertEquals(2, l4.c);
			assertEquals(2, l5.c);
			assertEquals(2, l6.c);
			assertEquals(2, l7.c);
			assertEquals(2, l8.c);
		}
		
		test function iterationOrder():void
		{
			var l01:LoggingTickerListener = new LoggingTickerListener('A', 1);
			var l02:LoggingTickerListener = new LoggingTickerListener('B', 2);
			var l03:LoggingTickerListener = new LoggingTickerListener('C', 3);
			var l04:LoggingTickerListener = new LoggingTickerListener('D', 4);
			var l05:LoggingTickerListener = new LoggingTickerListener('E', 5);
			var l06:LoggingTickerListener = new LoggingTickerListener('F', 6);
			var l07:LoggingTickerListener = new LoggingTickerListener('G', 7);
			var l08:LoggingTickerListener = new LoggingTickerListener('H', 8);
			
			var ticker:EnterFrameTicker = new EnterFrameTicker();
			
			ticker.addTickerListener(l01);
			ticker.addTickerListener(l02);
			ticker.addTickerListener(l03);
			ticker.addTickerListener(l04);
			ticker.addTickerListener(l05);
			ticker.addTickerListener(l06);
			ticker.addTickerListener(l07);
			ticker.addTickerListener(l08);
			
			Static.log = '';
			
			for (var i:uint = 1; i < 10; ++i) {
				ticker.update(null);
			}
			
			var log:String = '';
			log += 'A1 B1 C1 D1 E1 F1 G1 H1 ';
			log += 'B2 C2 D2 E2 F2 G2 H2 ';
			log += 'C3 D3 E3 F3 G3 H3 ';
			log += 'D4 E4 F4 G4 H4 ';
			log += 'E5 F5 G5 H5 ';
			log += 'F6 G6 H6 ';
			log += 'G7 H7 ';
			log += 'H8 ';
			
			assertEquals(log, Static.log);
		}
		
		test function insertAfterDelete():void
		{
			var ticker:EnterFrameTicker = new EnterFrameTicker();
			
			var l1:MockTickerListener = new MockTickerListener(1);
			var l2:MockTickerListener = new MockTickerListener(1);
			var l3:AddingListenerTickerListener = new AddingListenerTickerListener(2, ticker, l1, 1);
			
			ticker.addTickerListener(l3);
			ticker.addTickerListener(l2);
			
			ticker.update(null);
			ticker.update(null);
			ticker.update(null);
			
			assertEquals(1, l1.c);
			assertEquals(1, l2.c);
			assertEquals(2, l3.c);
		}
	}
}

import org.libspark.betweenas3.core.ticker.TickerListener;
import org.libspark.betweenas3.core.ticker.ITicker;

internal class Static
{
	public static var log:String;
}

internal class MockTickerListener extends TickerListener
{
	public function MockTickerListener(n:uint)
	{
		this.n = n;
		this.c = 0;
	}
	
	public var n:uint;
	public var c:uint;
	
	override public function tick(time:Number):Boolean
	{
		return ++c == n;
	}
}

internal class AddingListenerTickerListener extends MockTickerListener
{
	public function AddingListenerTickerListener(n:uint, ticker:ITicker, listener:TickerListener, n2:uint = 0)
	{
		super(n);
		
		this.ticker = ticker;
		this.listener = listener;
		this.n2 = n2;
	}
	
	public var ticker:ITicker;
	public var listener:TickerListener;
	public var n2:uint;
	
	override public function tick(time:Number):Boolean
	{
		if (c == n2) {
			ticker.addTickerListener(listener);
		}
		return super.tick(time);
	}
}

internal class LoggingTickerListener extends TickerListener
{
	public function LoggingTickerListener(name:String, n:uint)
	{
		this.name = name;
		this.n = n;
		this.c = 0;
	}
	
	public var name:String;
	public var n:uint;
	public var c:uint;
	
	override public function tick(time:Number):Boolean
	{
		++c;
		
		Static.log += name + c + ' ';
		
		return c == n;
	}
}