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

package flash.events {
[native(cls='TextEventClass')]
public class TextEvent extends Event {
  public static const LINK:String = "link";
  public static const TEXT_INPUT:String = "textInput";


  public function TextEvent(type:String, bubbles:Boolean = false, cancelable:Boolean = false,
                            text:String = "")
  {
    super(type, bubbles, cancelable);
    this.text = text;
  }

  public native function get text():String;
  public native function set text(value:String):void;

  public override native function clone():Event;
  public override native function toString():String;
}
}