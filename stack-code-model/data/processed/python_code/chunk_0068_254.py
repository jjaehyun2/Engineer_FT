/*
 * Copyright 2014 Mozilla Foundation
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

package flash.display {
import flash.errors.IllegalOperationError;
import flash.events.Event;
import flash.events.EventDispatcher;
import flash.events.UncaughtErrorEvents;
import flash.system.ApplicationDomain;
import flash.utils.ByteArray;

[native(cls='LoaderInfoClass')]
public class LoaderInfo extends EventDispatcher {
  public static native function getLoaderInfoByDefinition(object:Object):LoaderInfo;
  public function LoaderInfo() {}
  public native function get loaderURL():String;
  public native function get url():String;
  public native function get isURLInaccessible():Boolean;
  public native function get bytesLoaded():uint;
  public native function get bytesTotal():uint;
  public native function get applicationDomain():ApplicationDomain;
  public native function get swfVersion():uint;
  public native function get actionScriptVersion():uint;
  public native function get frameRate():Number;
  public function get parameters():Object {
    // Parameters have to be cloned, but our native implementation of _getArgs does that.
    return _getArgs();
  }
  public native function get width():int;;
  public native function get height():int;
  public native function get contentType():String;
  public native function get sharedEvents():EventDispatcher;
  public native function get parentSandboxBridge():Object;
  public native function set parentSandboxBridge(door:Object):void;
  public native function get childSandboxBridge():Object;
  public native function set childSandboxBridge(door:Object):void;
  public native function get sameDomain():Boolean;
  public native function get childAllowsParent():Boolean;
  public native function get parentAllowsChild():Boolean;
  public native function get loader():Loader;
  public native function get content():DisplayObject;
  public native function get bytes():ByteArray;
  public function get uncaughtErrorEvents():UncaughtErrorEvents {
    var events:UncaughtErrorEvents = _getUncaughtErrorEvents();
    if (!events) {
      events = new UncaughtErrorEvents();
      _setUncaughtErrorEvents(events);
    }
    return events;
  }
  private native function _getArgs():Object;
  private native function _getUncaughtErrorEvents():UncaughtErrorEvents;
  private native function _setUncaughtErrorEvents(value:UncaughtErrorEvents):void;
  public override function dispatchEvent(event:Event):Boolean {
    Error.throwError(IllegalOperationError, 2118);
    return false;
  }
}
}