/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.ui.themes {
    import flash.display.Bitmap;
    import flash.display.BitmapData;
    import flash.display.Graphics;
    import flash.display.Shape;
    import flash.display.Sprite;
    import flash.text.Font;
    import flash.text.TextField;
    import flash.text.TextFormat;
    import flash.utils.Dictionary;

    public class DefaultTheme implements ITheme {

        [Embed(source="/assets/fonts/pixelart.ttf",
                fontName = "PixelArt",
                mimeType = "application/x-font",
                advancedAntiAliasing="true",
                embedAsCFF="false")]
        private var _artFont:Class;
        private var defaultFont:Font;

        [Embed(source="/assets/fonts/visitor1.ttf",
                fontName = "Visitor1",
                mimeType = "application/x-font",
                advancedAntiAliasing="true",
                embedAsCFF="false")]
        private var _vis1Font:Class;

        [Embed(source="/assets/fonts/visitor2.ttf",
                fontName = "Visitor2",
                mimeType = "application/x-font",
                advancedAntiAliasing="true",
                embedAsCFF="false")]
        private var _vis2Font:Class;

        [Embed(source="/assets/fonts/04b08.ttf",
                fontName = "04b08",
                mimeType = "application/x-font",
                advancedAntiAliasing="true",
                embedAsCFF="false")]
        private var _04b08Font:Class;

        [Embed(source="/assets/fonts/type_writer.ttf",
                fontName = "type_writer",
                mimeType = "application/x-font",
                advancedAntiAliasing="true",
                embedAsCFF="false")]
        private var _type_writerFont:Class;

        [Embed(source="/assets/fonts/victor-pixel.ttf",
                fontName = "victor-pixel",
                mimeType = "application/x-font",
                advancedAntiAliasing="true",
                embedAsCFF="false")]
        private var _victor_pixel_writerFont:Class;

        private var _fonts:Dictionary;

        public var borderColor:uint = 0x41C6F3;
        public var backgroundColor:uint = 0x017EC1;

        public var outerCornerRadius:int = 16;
        public var innerCornerRadius:int = 6;

        protected var _textField:TextField;
        protected var _textFormat:TextFormat;
        protected var _defaultTextColor:uint = 0xFFFFFF;
        protected var contentSprite:Sprite;

        protected var _styles:Dictionary;

        public function DefaultTheme() {
            contentSprite = new Sprite();
            contentSprite.graphics.beginFill(0x00CC00,0.5);
            contentSprite.graphics.drawRect(0,0,100,100);
            contentSprite.graphics.endFill();
            defaultFont = registerFont("default", _artFont);
            registerFont("visitor1", _vis1Font);
            registerFont("visitor2", _vis2Font);
            registerFont("04b08", _04b08Font);
            registerFont("type_writer", _type_writerFont);
            registerFont("victor_pixel", _victor_pixel_writerFont);
            _textField = new TextField();
            _textField.width = 200;
            _textField.height = 50;
            _textField.wordWrap = false;
            _textField.autoSize = "left";
            _textField.embedFonts = true;
            _textFormat = new TextFormat(defaultFont.fontName, 10, _defaultTextColor);
            _textField.defaultTextFormat = _textFormat;
            contentSprite.addChild(_textField);
        }

        public function drawCorneredBackground(width:Number, height:Number):Shape {
            var shape:Shape = new Shape();
            shape.graphics.lineStyle(1, borderColor, 1, false, "none");
            shape.graphics.beginFill(backgroundColor, 0.8);
            shape.graphics.moveTo(innerCornerRadius, 0);
            shape.graphics.lineTo(width - outerCornerRadius, 0);
            shape.graphics.lineTo(width, outerCornerRadius);
            shape.graphics.lineTo(width, height - innerCornerRadius);
            shape.graphics.lineTo(width - innerCornerRadius, height);
            shape.graphics.lineTo(innerCornerRadius, height);
            shape.graphics.lineTo(0, height - innerCornerRadius);
            shape.graphics.lineTo(0, innerCornerRadius);
            shape.graphics.lineTo(innerCornerRadius, 0);
            shape.graphics.endFill();
            return shape;
        }

        public function drawPath(pathDefinition:String, graphics:Graphics):void {

        }

        public function createBitmapLabel(value:String, fontSize:int, fontColor:uint, fontName:String = "default", backgroundColor:uint = 0, backgroundAlpha:Number = 0):Bitmap {
            //_textField.width = 200;
            //_textField.height = 50;
            _textFormat.font = getFont(fontName);
            _textField.wordWrap = false;
            _textField.text = value;
            _textFormat.color = fontColor;
            _textFormat.size = fontSize;
            _textField.setTextFormat(_textFormat);
            var bmpData:BitmapData = new BitmapData(_textField.textWidth + 5,
                    _textField.textHeight + 5,
                    backgroundAlpha == 0,
                    backgroundAlpha == 0 ? 0 : backgroundColor
            );
            bmpData.draw(_textField);
            return new Bitmap(bmpData, "auto", true);
        }

        public function init():void {
            _styles = new Dictionary();
            _styles["stockView"] = new StyleGroup("stockView", {
                borderColor: borderColor,
                backgroundColor: backgroundColor,
                backgroundAlpha: 1,
                titleBackgroundColor: 0,
                titleBackgroundAlpha: 0.3,
                titleColor: 0xFFFFFF,
                contentBackgroundColor: 0xFFFFFF,
                contentBackgroundAlpha: 0.4
            });
        }

        public function drawButtonBackground(graphics:Graphics, _width:Number, _height:Number, BUTTON_STATE_NORMAL:uint):void {
            //graphics.lineStyle(1, buttonBackground)
        }

        public function getDefaultTextFormat():TextFormat {
            return new TextFormat(defaultFont.fontName, 10, _defaultTextColor);
        }

        public function getStyleGroup(groupName:String):StyleGroup {
            if(groupName) {
                if(_styles[groupName] != null) {
                    return _styles[groupName];
                }
            }
            return new StyleGroup("", null);
        }

        public function registerFont(fontName:String, fontClass:Class):Font {
            if(_fonts == null) {
                _fonts = new Dictionary();
            }
            var fnt:Font = new fontClass() as Font;
            Font.registerFont(fontClass);
            _fonts[fontName] = fnt;
            return fnt;
        }

        public function getFont(fontName:String):String {
            if(_fonts && _fonts[fontName]) {
                return _fonts[fontName].fontName;
            }
            return "_typewriter";
        }
    }
}