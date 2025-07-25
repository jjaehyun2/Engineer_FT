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

 Additional Terms
 No part, or derivative of this Air Native Extensions's code is permitted
 to be sold as the basis of a commercially packaged Air Native Extension which
 undertakes the same purpose as this software. That is an ARKit wrapper for iOS.
 All Rights Reserved. Tua Rua Ltd.
 */

package com.tuarua.arkit {

public class Configuration {
    private var _worldAlignment:int = WorldAlignment.gravity;
    private var _isLightEstimationEnabled:Boolean = true;
    private var _frameSemantics:Vector.<uint> = new Vector.<uint>();
    public function Configuration() {
    }

    /** Determines how the coordinate system should be aligned with the world.
     * @default WorldAlignment.gravity */
    public function get worldAlignment():int {
        return _worldAlignment;
    }

    public function set worldAlignment(value:int):void {
        _worldAlignment = value;
    }

    /** Enable or disable light estimation.
     * @default true */
    public function get isLightEstimationEnabled():Boolean {
        return _isLightEstimationEnabled;
    }

    public function set isLightEstimationEnabled(value:Boolean):void {
        _isLightEstimationEnabled = value;
    }

    /** The set of active semantics on the frame. */
    public function get frameSemantics():Vector.<uint> {
        return _frameSemantics;
    }

    public function set frameSemantics(value:Vector.<uint>):void {
        _frameSemantics = value;
    }
}
}