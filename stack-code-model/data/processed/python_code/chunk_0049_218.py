﻿/* -*- Mode: js; js-indent-level: 2; indent-tabs-mode: nil; tab-width: 2 -*- */
/* vim: set shiftwidth=2 tabstop=2 autoindent cindent expandtab: */
/*
 * Copyright 2013 Mozilla Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package avm1lib {
  public class AS2Broadcaster {
    public static function initialize(obj) {
      obj._listeners = [];
      obj.broadcastMessage = _broadcastMessage;
      obj.addListener = _addListener;
      obj.removeListener = _removeListener;
    }
  }
}

function _broadcastMessage(eventName) {
  var args = Array.prototype.slice.call(arguments, 1);
  for (var i = 0; i < this._listeners.length; i++) {
    var listener = this._listeners[i];
    if (!(eventName in listener)) {
      continue;
    }
    listener[eventName].apply(listener, args);
  }
}
function _addListener(listener) {
  if (this._broadcastEventsRegistrationNeeded) {
    this._broadcastEventsRegistrationNeeded = false;
    for (var i = 0; i < this._broadcastEvents.length; i++) {
      (function (subject, eventName) {
        subject[eventName] = function () {
          _broadcastMessage.apply(subject, [eventName].concat(arguments));
        };
      })(this, this._broadcastEvents[i]);
    }
  }
  this._listeners.push(listener);
}
function _removeListener(listener) {
  var i = this._listeners.indexOf(listener);
  if (i < 0) {
    return;
  }
  this._listeners.splice(i, 1);
}