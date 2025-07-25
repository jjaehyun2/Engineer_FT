/* Copyright 2018 Tua Rua Ltd.

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

package com.tuarua.mlane.models {
import flash.display.BitmapData;

public class MobileNetInput {
    public var image:BitmapData;

    public function MobileNetInput(image:BitmapData) {
        this.image = image;
    }

    /** @private */
    public function getProperties():Array { //used in ANE
        return ["image"];
    }
}
}