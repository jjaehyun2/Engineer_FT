/**
 * User: Dave Long
 * Date: 29/06/13
 * Time: 14:29
 */
package com.sixfootsoftware.pitstop {

    import org.flixel.FlxSprite;

    public class ArrowDisplay extends FlxSprite {

        private var _playingAnimation:Boolean = false;

        public function ArrowDisplay(x:int = 71, y:int = 400) {
            super(x, y);
            this.loadGraphic(AssetRegistry.Arrows, true, false, 108, 110);
            kill();
        }

        public function get playingAnimation():Boolean {
            return _playingAnimation;
        }

        public function set playingAnimation(value:Boolean):void {
            if (value) {
                play("enabled");
            } else {
                play("disabled");
            }
            _playingAnimation = value;
        }
    }
}