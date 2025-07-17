package interfaces.skin.phone
{
    import interfaces.component.ValueButton;
    import interfaces.container.MenuView;
    import interfaces.skin.AbstractSkin;

    import mx.controls.Spacer;
    import spark.components.Label;

    public class MenuSkin extends AbstractSkin
    {
        /**
         *  @copy spark.skins.spark.ApplicationSkin#hostComponent
         */
        public var hostComponent:MenuView;

        //[Embed(source="logo.png")]
        public var img_logo:Class;
        public var txt_caption:Label;
        public var txt_info:Label;
        public var btn_startQuiz:ValueButton;
        public var btn_showAbout:ValueButton;

        public function MenuSkin()
        {
            super();
        }

        override protected function createChildren():void
        {
            super.createChildren();

            var space1:Spacer = new Spacer();
            space1.height = 10;
            content.addElement(space1);
/*
            var img:BitmapImage = new BitmapImage();
            img.source = new img_logo();
            img.width = 100;
            img.smooth = true;
            img.smoothingQuality = BitmapSmoothingQuality.HIGH;
            img.fillMode = BitmapFillMode.SCALE;
            img.scaleMode = ScaleMode.LETTERBOX;
            content.addElement(img);
*/
            var space2:Spacer = new Spacer();
            space2.percentHeight = 100;
            content.addElement(space2);

            txt_caption = new Label();
            txt_caption.id = "txt_caption";
            content.addElement(txt_caption);

            txt_info = new Label();
            txt_info.id = "txt_info";
            content.addElement(txt_info);

            btn_startQuiz = new ValueButton();
            btn_startQuiz.id = "btn_startQuiz";
            content.addElement(btn_startQuiz);

            btn_showAbout = new ValueButton();
            btn_showAbout.id = "btn_showAbout";
            content.addElement(btn_showAbout);

        }

        override protected function layoutContents(unscaledWidth:Number, unscaledHeight:Number):void
        {
            super.layoutContents(unscaledWidth, unscaledHeight);

            txt_caption.percentWidth = 100;
            txt_info.percentWidth = 100;
            btn_startQuiz.percentWidth = 100;
            btn_showAbout.percentWidth = 100;
        }
    }
}