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
package org.libspark.betweenas3.core.tweens.decorators
{
	import org.libspark.as3unit.assert.*;
	import org.libspark.as3unit.test;
	import org.libspark.betweenas3.core.tweens.TestTween;
	
	use namespace test;
	
	/**
	 * @author	yossy:beinteractive
	 */
	public class DelayedTweenTest
	{
		test function delay():void
		{
			var t:TestTween = new TestTween(2, null);
			var d:DelayedTween = new DelayedTween(t, 1, 3);
			
			assertEquals(6, d.duration);
			
			d.update(0);
			
			assertEquals(-1, t.t);
			
			d.update(1);
			
			assertEquals(0, t.t);
			
			d.update(2);
			
			assertEquals(1, t.t);
			
			d.update(3);
			
			assertEquals(2, t.t);
			
			d.update(4);
			
			assertEquals(3, t.t);
			
			d.update(6);
			
			assertEquals(5, t.t);
			
			d.update(8);
			
			assertEquals(7, t.t);
		}
	}
}