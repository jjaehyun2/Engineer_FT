﻿/*
 * ActionScript Thread Library
 * 
 * Licensed under the MIT License
 * 
 * Copyright (c) 2008 BeInteractive! (www.be-interactive.org) and
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
package org.libspark.thread.utils
{
	import flash.events.IEventDispatcher;
	
	/**
	 * 仕事が進行し、 <code>total</code> プロパティか <code>current</code> プロパティか <code>percent</code> プロパティの
	 * いずれかが更新されると送出されます.
	 * 
	 * @eventType	org.libspark.thread.utils.events.ProgressEvent.UPDATE
	 * @see	#total
	 * @see	#current
	 * @see	#percent
	 */
	[Event(name="update", type="org.libspark.thread.utils.events.ProgressEvent")]
	
	/**
	 * 仕事が開始されると送出されます.
	 * 
	 * @eventType	org.libspark.thread.utils.events.ProgressEvent.START
	 * @see	#isStarted
	 */
	[Event(name="start", type="org.libspark.thread.utils.events.ProgressEvent")]
	
	/**
	 * 仕事が完了すると送出されます.
	 * 
	 * @eventType	org.libspark.thread.utils.events.ProgressEvent.COMPLETED
	 * @see	#isCompleted
	 */
	[Event(name="completed", type="org.libspark.thread.utils.events.ProgressEvent")]
	
	/**
	 * 仕事が失敗すると送出されます.
	 * 
	 * @eventType	org.libspark.thread.utils.events.ProgressEvent.FAILED
	 * @see	#isFailed
	 */
	[Event(name="failed", type="org.libspark.thread.utils.events.ProgressEvent")]
	
	/**
	 * 仕事がキャンセルされると送出されます.
	 * 
	 * @eventType	org.libspark.thread.utils.events.ProgressEvent.CANCELED
	 * @see	#isCanceled
	 */
	[Event(name="canceled", type="org.libspark.thread.utils.events.ProgressEvent")]
	
	/**
	 * IProgress インターフェイスは、進捗状況を表現します.
	 * 
	 * @author	yossy:beinteractive
	 */
	public interface IProgress extends IEventDispatcher
	{
		/**
		 * 仕事量の合計を返します.
		 * 
		 * <p>仕事量の合計が未知である場合、 0 を返します。</p>
		 */
		function get total():Number;
		
		/**
		 * 現在までに完了している仕事量を返します.
		 */
		function get current():Number;
		
		/**
		 * 仕事量の合計に対する、現在までに完了している仕事量の割合を、0 ～ 1.0 の範囲で返します.
		 */
		function get percent():Number;
		
		/**
		 * 仕事が開始されていれば true、そうでなければ false を返します.
		 * 
		 * <p>このプロパティは、仕事が完了したり、失敗やキャンセルされた場合でも false になることはありません。</p>
		 */
		function get isStarted():Boolean;
		
		/**
		 * 仕事が完了していれば true、そうでなければ false を返します.
		 */
		function get isCompleted():Boolean;
		
		/**
		 * 仕事が失敗していれば true、そうでなければ false を返します.
		 * 
		 * <p>このプロパティが true であるときに、 <code>isCompleted</code> プロパティが true になることはありません。</p>
		 * 
		 * @see	#isCompleted
		 */
		function get isFailed():Boolean;
		
		/**
		 * 仕事がキャンセルされた場合に true、そうでない場合に false を返します.
		 * 
		 * <p>このプロパティが true であるときに、 <code>isCompleted</code> プロパティが true になることはありません。</p>
		 * 
		 * @see	#isCompleted
		 */
		function get isCanceled():Boolean;
	}
}