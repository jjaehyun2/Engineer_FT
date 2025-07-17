package view.image.title
{

    import flash.display.*;
    import flash.events.Event;

    import view.image.BaseImage;

    /**
     * Loading表示クラス
     *
     */


    public class Loading extends BaseImage
    {

        // HP表示元SWF
        //[Embed(source="../../../../data/image/titel_bg.swf")]
        [Embed(source="../../../../data/image/title/loading.swf")]
        private var _Source:Class;
        private static const SCALE:Number = 1.0;
        private static const X:int = 0;
        private static const Y:int = 0;


        /**
         * コンストラクタ
         *
         */
        public function Loading()
        {
            super();
        }

        override protected function swfinit(event: Event): void 
        {
            super.swfinit(event);
            initializePos();
        }

        override protected function get Source():Class
        {
            return _Source;
        }

        public function initializePos():void
        {
            scaleX = SCALE;
            scaleY = SCALE;
            x = X;
            y = Y;
            alpha = 1.0;
        }



    }

}