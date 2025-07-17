/**
 * User: dvlg
 * Date: 04/07/13
 * Time: 14:28
 */
package com.sixfootsoftware.engine {
    import org.flixel.FlxSprite;

    public interface MenuItem {
        function clicked():Boolean;

        function getSprite():FlxSprite;
    }
}