package view.image.raid
{

    import flash.display.*;
    import flash.events.Event;
    import flash.geom.*;
    import flash.utils.*;

    import mx.core.UIComponent;

    import org.libspark.betweenas3.BetweenAS3;
    import org.libspark.betweenas3.tweens.ITween;
    import org.libspark.thread.Thread;
    import org.libspark.thread.utils.*;
    import org.libspark.thread.threads.between.BeTweenAS3Thread;

    import view.image.BaseImage;
    import view.image.game.HPGauge;
    import controller.*;

    /**
     * HPゲージ表示クラス
     *
     */

    public class BossMiniHPGauge extends HPGauge
    {
        private static const _X:int = 6;
        private static const _Y:int = 39;

        private static const _W:int = 117;
        private static const _H:int = 3;

        /**
         * コンストラクタ
         *
         */
        public function BossMiniHPGauge()
        {
            super();
            addChild(_gauge);
            x = _X;
            y = _Y;
        }

        override protected function initGauge():void
        {
            _gauge.graphics.clear();
            _gauge.graphics.lineStyle(0, 0x000000,0);
            _gauge.graphics.beginFill(0x000000);
            _gauge.graphics.drawRect(0,0,_W,_H);
            _gauge.transform.colorTransform = _color;
        }


    }

}