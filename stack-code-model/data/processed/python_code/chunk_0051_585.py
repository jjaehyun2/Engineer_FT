/*
 *  Copyright 2018 Tua Rua Ltd.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

package com.tuarua.firebase.firestore {
public class DocumentSnapshot {
    /** The ID of the document for which this <code>DocumentSnapshot</code> contains data. */
    public var id:String;
    public var data:*;
    /** True if the document exists. */
    public var exists:Boolean = false;
    /** Metadata about this snapshot concerning its source and if it has local modifications. */
    public var metadata:SnapshotMetadata;

    public function DocumentSnapshot(id:String, data:*, exists:Boolean, metadata:SnapshotMetadata) {
        this.id = id;
        this.data = data;
        this.exists = exists;
        this.metadata = metadata;
    }

}
}