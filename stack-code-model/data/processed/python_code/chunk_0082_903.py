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
/**
 Enum constants for indicating the mode of environment texturing to run.
 */
public final class EnvironmentTexturing {
    /** No texture information is gathered. */
    public static const none:int = 0;
    /** Texture information is gathered for the environment.
     Environment textures will be generated for AREnvironmentProbes added to the session. */
    public static const manual:int = 1;
    /** Texture information is gathered for the environment and probes automatically placed in the scene. */
    public static const automatic:int = 2;
}
}