/**
 * User: Dave Long
 * Date: 25/06/13
 * Time: 21:54
 */
package com.sixfootsoftware.pitstop {
    import org.flixel.FlxSprite;

    public class ScoreText extends FlxSprite {
        public function ScoreText() {
            super( 757, 56 );
            this.loadGraphic( AssetRegistry.ScoreText );
            this.kill();
        }
    }
}