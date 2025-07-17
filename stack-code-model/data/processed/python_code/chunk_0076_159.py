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

package com.tuarua.spotlight {
/** Index errors returned by Core Spotlight.*/
public class IndexError extends Error {
    /** The indexer was unavailable*/
    public static const indexUnavailableError:int = -1000;
    /** The SearchableItem is invalid for some reason */
    public static const invalidItemError:int = -1001;
    /** The provided clientState was not valid for some reason */
    public static const invalidClientStateError:int = -1002;
    /** There was an error trying to communicate with the remote process */
    public static const remoteConnectionError:int = -1003;
    /** Quota for bundle was exceeded */
    public static const quotaExceeded:int = -1004;
    /** Indexing isn't supported on this device */
    public static const indexingUnsupported:int = -1005;

    public function IndexError(message:* = "", id:* = 0) {
        super(message, id);
    }
}
}