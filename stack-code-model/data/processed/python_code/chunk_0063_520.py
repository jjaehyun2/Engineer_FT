package com.github.mortido.sqcity.ui.buttons
{
    import com.github.mortido.sqcity.ui.*;

    import flash.display.SimpleButton;
    import flash.display.Sprite;
    import flash.text.TextField;
    import flash.text.TextFormat;
    import flash.text.TextFormatAlign;

    public class TextButton extends SimpleButton
    {
        public function TextButton(text:String, width:Number, height:Number, textColor:uint = 0x000000, backgroundColor:uint = 0xcccccc, textSize:Number = 15)
        {
            var up:Sprite = new Sprite();
            var over:Sprite = new Sprite();
            var down:Sprite = new Sprite();

            var upText:TextField = new TextField();
            var overText:TextField = new TextField();
            var downText:TextField = new TextField();

            var textFormat:TextFormat = new TextFormat();
            textFormat.align = TextFormatAlign.CENTER;
            textFormat.size = textSize;
            textFormat.leading = 0;
            textFormat.font = "_sans";
            textFormat.color = textColor;
            textFormat.bold = true;

            upText.defaultTextFormat = downText.defaultTextFormat = overText.defaultTextFormat = textFormat;
            upText.text = downText.text = overText.text = text;
            upText.height = downText.height = overText.height = height;
            upText.width = downText.width = overText.width = width;
            upText.y = downText.y = overText.y = Math.round((height - upText.textHeight) / 3);

            up.graphics.beginFill(backgroundColor);
            up.graphics.drawRect(0, 0, width, height);
            up.graphics.endFill();

            over.graphics.beginFill(backgroundColor);
            over.graphics.drawRect(0, 0, width, height);
            over.graphics.endFill();

            down.graphics.beginFill(backgroundColor);
            down.graphics.drawRect(0, 0, width, height);
            down.graphics.endFill();

            up.addChild(upText);
            over.addChild(overText);
            down.addChild(downText);

            over.filters = VisualEffects.HOVERED_BUTTON_FILTERS;
            down.filters = VisualEffects.PRESSED_BUTTON_FILTERS;

            super(up, over, down, up);
        }
    }
}