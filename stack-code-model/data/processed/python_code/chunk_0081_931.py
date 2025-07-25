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

package flash.text.engine {
import flash.events.EventDispatcher;

[native(cls='TextElementClass')]
public final class TextElement extends ContentElement {
  public function TextElement(text: String = null, elementFormat: ElementFormat = null,
                              eventMirror: EventDispatcher = null, textRotation: String = "rotate0")
  {
    super(elementFormat, eventMirror, textRotation);
    this.text = text;
  }
  public native function set text(value: String): void;
  public native function replaceText(beginIndex: int, endIndex: int, newText: String): void;
}
}