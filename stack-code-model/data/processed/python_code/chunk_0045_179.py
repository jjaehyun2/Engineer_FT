/**
 *  Starling Builder
 *  Copyright 2015 SGN Inc. All Rights Reserved.
 *
 *  This program is free software. You can redistribute and/or modify it in
 *  accordance with the terms of the accompanying license agreement.
 */
package starlingbuilder.demo2
{
    import flash.utils.Dictionary;

    import starling.display.DisplayObject;
    import starling.text.BitmapFont;
    import starling.text.TextField;

    import starlingbuilder.engine.localization.DefaultLocalizationHandler;

    /**
     * Default implementation of ILocalizationHandler
     *
     * @see ILocalizationHandler
     */
    public class LocalizationHandler extends DefaultLocalizationHandler
    {
        /**
         * Constructor
         */
        public function LocalizationHandler()
        {
            super();
        }

        /**
         * @inheritDoc
         */
        override public function localize(object:DisplayObject, text:String, paramsDict:Dictionary, locale:String):void
        {
            var textField:TextField = object as TextField;
            if (textField)
            {
                if (locale == "cn_ZH" && textField.format.font == BitmapFont.MINI)
                    textField.format.font = "_sans";
                else if (textField.format.font == "_sans")
                    textField.format.font = BitmapFont.MINI;
            }

            super.localize(object, text, paramsDict, locale);
        }
    }
}