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
 * User: Frederic THOMAS Date: 14/06/2014 Time: 15:13
 */
package com.doublefx.as3.thread.event {
import flash.events.Event;

[RemoteClass(alias="com.doublefx.as3.thread.event.ThreadProgressEvent")]
public class ThreadProgressEvent extends Event {
    public static const PROGRESS:String = "progress";

    private var _current:uint;
    private var _total:uint;

    public function ThreadProgressEvent(current:uint = 0, total:uint = 100, bubbles:Boolean = false, cancelable:Boolean = false) {
        super(PROGRESS, bubbles, cancelable);
        _current = current;
        _total = total;
    }

    public function get current():uint {
        return _current;
    }

    public function get total():uint {
        return _total;
    }

    public function set current(value:uint):void {
        _current = value;
    }

    public function set total(value:uint):void {
        _total = value;
    }

    public override function clone():Event {
        var evt:ThreadProgressEvent = new ThreadProgressEvent(_current, _total, this.bubbles, this.cancelable);
        return evt;
    }
}
}