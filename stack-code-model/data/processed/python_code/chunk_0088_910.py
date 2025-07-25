/*
 * Copyright (c) 2018 Marcel Piestansky
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.marpies.ane.facebook.events {

    import com.marpies.ane.facebook.data.BasicUserProfile;

    import flash.events.Event;

    /**
     * Dispatched once the basic user profile becomes available.
     * Listen to this event during Facebook initialization and/or login methods.
     */
    public class AIRFacebookBasicUserProfileEvent extends Event {

        public static const PROFILE_READY:String = "profileReady";

        private var mBasicUserProfile:BasicUserProfile;

        public function AIRFacebookBasicUserProfileEvent( type:String, bubbles:Boolean = false, cancelable:Boolean = false ) {
            super( type, bubbles, cancelable );
        }

        /**
         *
         *
         * Getters / Setters
         *
         *
         */

        /**
         * Returns basic user profile.
         */
        public function get basicUserProfile():BasicUserProfile {
            return mBasicUserProfile;
        }

        /**
         * @private
         */
        ns_airfacebook_internal function set basicUserProfile( value:BasicUserProfile ):void {
            mBasicUserProfile = value;
        }

    }

}