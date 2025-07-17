/**
 * User: dvlg
 * Date: 04/07/13
 * Time: 14:40
 */
package com.sixfootsoftware.pitstop {
    import com.sixfootsoftware.engine.MenuItem;

    import org.flixel.FlxG;

    import org.flixel.FlxSprite;

    public class LeaderboardMenuItem implements MenuItem {

        private var sprite:FlxSprite = new FlxSprite();

        public function clicked():Boolean {
            if ( FlxG.mouse.justReleased() ) {
                if ( sprite.overlapsPoint( FlxG.mouse.getScreenPosition())) {
                    return true;
                }
            }
            return false;
        }

        public function getSprite():FlxSprite {
            return sprite;
        }
    }
}