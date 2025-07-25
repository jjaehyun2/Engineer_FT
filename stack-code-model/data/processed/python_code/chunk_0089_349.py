/*
Copyright 2009, Matthew Eernisse (mde@fleegix.org) and Slide, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
*/

package org.windmill.events {
  import flash.events.FocusEvent;
  import flash.display.InteractiveObject;
  
  public class WMFocusEvent extends FocusEvent {
    public function WMFocusEvent(type:String,
        bubbles:Boolean = true, cancelable:Boolean = false,
        relatedObject:InteractiveObject = null,
        shiftKey:Boolean = false, keyCode:uint = 0) {
      super(type, bubbles, cancelable, relatedObject,
          shiftKey, keyCode);
    }
  }
}