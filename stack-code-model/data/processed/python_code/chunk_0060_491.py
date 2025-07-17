/*
 * Copyright (c) 2014 Frédéric Thomas
 *
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * User: Frederic THOMAS Date: 14/06/2014 Time: 20:47
 */
package com.doublefx.as3.thread {
import com.doublefx.as3.thread.event.ThreadFaultEvent;
import com.doublefx.as3.thread.event.ThreadResultEvent;
import com.doublefx.as3.thread.namespace.thread_diagnostic;

import flash.system.MessageChannelState;
import flash.system.WorkerState;

import org.flexunit.assertThat;
import org.flexunit.asserts.assertEquals;
import org.flexunit.asserts.assertNotNull;
import org.flexunit.asserts.fail;
import org.flexunit.async.Async;

import workers.SimpleWorkerWithNoArgs;

use namespace thread_diagnostic;

public class SimpleThreadTestWithNoArgs extends ThreadTestBase {

    [Before]
    override public function setUp():void {
        _thread = new Thread(SimpleWorkerWithNoArgs, "simpleRunnable", false, null, loaderInfo);
    }

    [Test(description="Verify the name of the Thread")]
    override public function testName():void {
        assertEquals("Should be equal to 'simpleRunnable'", _thread.name, "simpleRunnable");
    }

    [Test(description="Verify the state of the Thread before the start method has been called")]
    override public function testStateBeforeStart():void {
        assertEquals("Should be 'new'", _thread.state, WorkerState.NEW);
    }

    [Test(description="Verify dependencies")]
    override public function testDependenciesExistence():void {
        assertNotNull("Should not be null", Thread(_thread).collectedDependencies);
    }

    [Test(description="Verify dependencies content")]
    public function testDependenciesContent():void {
        const dependencies:Vector.<String> = Vector.<String>(
                "mx.core.DebuggableWorker,com.doublefx.as3.thread.api.CrossThreadDispatcher,com.doublefx.as3.thread.api.IWorker,workers.SimpleWorkerWithNoArgs,com.doublefx.as3.thread.api.Runnable,com.doublefx.as3.thread.api.IProperty,com.doublefx.as3.thread.api.SharableData,com.doublefx.as3.thread.api.IDataProducer,com.doublefx.as3.thread.util.AsynchronousDataManager,com.doublefx.as3.thread.util.Closure,com.doublefx.as3.thread.util.DecodedMessage,com.doublefx.as3.thread.event.ThreadFaultEvent,com.doublefx.as3.thread.event.ThreadResultEvent,com.doublefx.as3.thread.event.ThreadProgressEvent,com.doublefx.as3.thread.event.ThreadActionRequestEvent,com.doublefx.as3.thread.event.ThreadActionResponseEvent,com.doublefx.as3.thread.error.NotImplementedRunnableError,com.doublefx.as3.thread.error.IllegalStateError,com.doublefx.as3.thread.error.UnsupportedOperationError,com.doublefx.as3.thread.util.ClassAlias".split(",")
        );

        assertThat(Thread(_thread).collectedDependencies, arrayExact(dependencies));
    }

    [Test(description="Verify the Runnable class name")]
    override public function testRunnableClassName():void {
        assertEquals(Thread(_thread).runnableClassName, "workers.SimpleWorkerWithNoArgs");
    }

    [Test(description="Verify the Worker has been created")]
    override public function testWorkerExistence():void {
        assertNotNull("Should Not be null", Thread(_thread).worker);
    }

    [Test(description="Verify the incoming message channel has been created")]
    override public function testIncomingMessageChannelExistence():void {
        assertNotNull("Should Not be null", Thread(_thread).incomingChannel);
    }

    [Test(description="Verify the incoming message channel state")]
    public function testIncomingMessageChannelState():void {
        assertEquals("Should be opened", Thread(_thread).incomingChannel.state, MessageChannelState.OPEN);
    }

    [Test(description="Verify the outgoing message channel has been created")]
    override public function testOutgoingMessageChannelExistence():void {
        assertNotNull("Should Not be null", Thread(_thread).outgoingChannel);
    }

    [Test(description="Verify the outgoing message channel state")]
    public function testOutgoingMessageChannelState():void {
        assertEquals("Should be opened", Thread(_thread).outgoingChannel.state, MessageChannelState.OPEN);
    }

    [Test(async, description="Verify the Runnable 'run' method can be call with valide primitive values")]
    public function testStartThreadWithValidValues():void {
        _thread.addEventListener(ThreadResultEvent.RESULT, Async.asyncHandler(this, thread_resultHandler, 2000, null, thread_faultHandler), false, 0, true);
        _thread.addEventListener(ThreadFaultEvent.FAULT, thread_faultHandler);
        _thread.start();
    }

    protected function thread_resultHandler(event:ThreadResultEvent, passThroughData:Object = null):void {
        testStateRunning();
        assertEquals(event.result, 3);
    }

    protected function thread_faultHandler(event:ThreadFaultEvent, passThroughData:Object = null):void {
        testStateRunning();
        fail(event.fault.message);
    }
}
}