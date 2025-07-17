/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.ui.components {
    import com.bytesfromouterspace.stockbrokers.ui.*;
    import com.bytesfromouterspace.stockbrokers.ui.themes.ITheme;

    public interface IThemedComponent {
        function set theme(value:ITheme):void;
        function get theme():ITheme;
        function updateTheme():void;
    }
}