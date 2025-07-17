/*
 * =BEGIN MIT LICENSE
 * 
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 Andras Csizmadia
 * http://www.vpmedia.hu
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
 * =END MIT LICENSE
 *
 */

package {
import com.docmet.extensions.CryptoPPExtension;

import flash.display.Shape;
import flash.display.Sprite;
import flash.display.StageAlign;
import flash.display.StageScaleMode;
import flash.events.Event;
import flash.filesystem.StorageVolume;
import flash.filesystem.StorageVolumeInfo;
import flash.text.TextField;
import flash.text.TextFormat;
import flash.utils.getTimer;

/**
 * ANE Tester Client Document Class
 */
public class Main extends Sprite {

    /**
     * @private
     */
    private var extension:CryptoPPExtension;

    /**
     * @private
     */
    private var messageLabel:TextField;

    //----------------------------------
    //  Constructor
    //----------------------------------

    /**
     * Constructor
     */
    public function Main() {
        addEventListener(Event.ADDED_TO_STAGE, onAdded, false, 0, true);
    }

    /**
     * @private
     */
    private function onRemoved(event:Event):void {
        if (extension)
            extension.dispose();
    }

    /**
     * @private
     */
    private function onAdded(event:Event):void {
        removeEventListener(Event.ADDED_TO_STAGE, onAdded);
        addEventListener(Event.REMOVED_FROM_STAGE, onRemoved, false, 0, true);

        stage.scaleMode = StageScaleMode.NO_SCALE;
        stage.align = StageAlign.TOP_LEFT;

        const sw:uint = stage.fullScreenWidth;
        const sh:uint = stage.fullScreenHeight;

        var bg:Shape = new Shape();
        bg.graphics.beginFill(0x333333);
        bg.graphics.drawRect(0, 0, sw, sh);
        bg.graphics.endFill();
        addChild(bg);

        // create log text field
        messageLabel = new TextField();
        messageLabel.width = sw;
        messageLabel.height = sh;
        messageLabel.multiline = true;
        messageLabel.wordWrap = true;
        messageLabel.defaultTextFormat = new TextFormat("Arial", 10, 0xFFFFFF);
        addChild(messageLabel);

        // create native extension context
        extension = new CryptoPPExtension();
        extension.setLogger(function (message:String):void {
            message = "ANE::" + message;
            log(message);
        });

        extension.callNative(CryptoPPExtension.EXT_SHA_512, "HelloWorld");
    }

    /**
     * @private
     */
    private function log(message:String):void {
        const msg:String = getTimer() + " :: " + message;
        trace(this, msg);
        messageLabel.text += msg + "\n";
        messageLabel.scrollV = messageLabel.maxScrollV;
    }

    // EOC
}

//EOP

}