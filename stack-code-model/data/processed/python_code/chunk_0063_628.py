/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2014. Nicolas Siver (http://siver.im)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
 * documentation files (the "Software"), to deal in the Software without restriction, including without
 * limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions
 * of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
 * TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
 * CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

package im.siver.library.utils {

    import flash.display.DisplayObject;
    import flash.display.Sprite;
    import flash.text.Font;
    import flash.text.TextField;

    public class FontEnum extends Sprite {
        public function FontEnum() {
            var len:uint = this.numChildren;
            var i:uint;
            var object:DisplayObject;

            for (i; i < len; ++i) {
                object = this.getChildAt(i);
                if (object is TextField) {
                    trace("Font: " + TextField(object).getTextFormat().font);
                }
            }
        }

        public static function enumerateFonts():Array {
            var fonts:Array = Font.enumerateFonts();
            var i:int;
            var len:int = fonts.length;
            var font:Font;
            var stringList:Array = [];

            for (i; i < len; ++i) {
                font = fonts[i];

                stringList.push(new FontDescription(font));
            }

            return stringList;
        }
    }
}

import flash.text.Font;

internal class FontDescription extends Object {

    public var font:Font;

    public function FontDescription($font:Font) {
        this.font = $font;
    }

    public function toString():String {
        var desc:String = "";
        desc += "Font {";
        desc += "Name: " + font.fontName + ", ";
        desc += "Style: " + font.fontStyle + ", ";
        desc += "Type: " + font.fontName + "}";
        return desc;
    }
}