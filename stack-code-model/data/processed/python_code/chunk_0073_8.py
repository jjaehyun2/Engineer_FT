/**
 * User: Dave Long
 * Date: 29/06/13
 * Time: 14:35
 */
package com.sixfootsoftware.pitstop {
    public class LeftArrowDisplay extends ArrowDisplay {
        public function LeftArrowDisplay() {
            super();
            addAnimation("enabled", [0, 3], 5, true);
            addAnimation("disabled", [0], 1, true);
            play("disabled");
        }

    }
}