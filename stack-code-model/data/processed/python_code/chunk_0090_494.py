/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.ui.themes {
    import flash.display.Bitmap;
    import flash.display.Graphics;
    import flash.display.Shape;
    import flash.text.Font;
    import flash.text.TextFormat;

    public interface ITheme {

        //function drawPanel()

        function drawCorneredBackground(width:Number, height:Number):Shape;

        function createBitmapLabel(value:String, fontSize:int, fontColor:uint, fontName:String = "default", backgroundColor:uint = 0, backgroundAlpha:Number = 0):Bitmap;

        function init():void;

        function drawButtonBackground(graphics:Graphics, _width:Number, _height:Number, BUTTON_STATE_NORMAL:uint):void;

        function getDefaultTextFormat():TextFormat;

        function registerFont(fontName:String, fontClass:Class):Font;

        function getStyleGroup(groupName:String):StyleGroup;

        function getFont(fontName:String):String;
    }
}