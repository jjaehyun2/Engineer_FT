/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.view {
    import com.bytesfromouterspace.stockbrokers.controller.SoundRandomGeneratorController;
    import com.bytesfromouterspace.stockbrokers.model.SoundRandomGeneratorModel;
    import com.bytesfromouterspace.stockbrokers.model.StockShareModel;

    import flash.display.Graphics;
    import flash.display.Shape;

    import flash.display.Sprite;
    import flash.events.Event;
    import flash.events.TimerEvent;
    import flash.media.SoundMixer;
    import flash.utils.ByteArray;
    import flash.utils.Timer;

    public class SoundRandomGeneratorView extends Sprite {

        protected var model:SoundRandomGeneratorModel;
        protected var controller:SoundRandomGeneratorController;

        protected var shareHolder:Sprite;
        protected var shares:Vector.<StockShareModel>;
        protected var numShares:int = 10;

        public function SoundRandomGeneratorView(model:SoundRandomGeneratorModel, controller:SoundRandomGeneratorController) {
            this.model = model;
            this.controller = controller;
            this.model.addEventListener(Event.CHANGE, onModelChanged);
            addEventListener(Event.ADDED_TO_STAGE, draw);
        }

        private function onModelChanged(event:Event):void {

        }

        private function draw(event:Event):void {
            trace("SGR Add");
            removeEventListener(Event.ADDED_TO_STAGE, draw);
            start();
        }

        public function start():void {
            controller.start();
        }

        private function onTimer(event:TimerEvent):void {
            for(var i:int = 0; i < shares.length; i++) {
                shares[i].update(model._nextAudioSample);
            }
        }




    }
}