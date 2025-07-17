/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.ui.components {
    import flash.events.Event;

    public class BorderBackground extends ComponentBase {

        private var _backgroundEnabled:Boolean = false;
        private var _backgroundColor:uint;
        private var _backgroundAlpha:Number = 1;

        private var _borderEnabled:Boolean = false;
        private var _borderColor:uint;
        private var _borderAlpha:Number = 1;

        private var _redrawOnNextFrame:Boolean = false;
        public var drawFunction:Function = null;

        private var _tintDuration:int = 10;

        public function BorderBackground(_width:Number, _height:Number) {
            super(_width, _height);
            initHandler = draw;
        }

        protected function draw(baseColor:uint = 1):void {
            if(baseColor == 1) {
                baseColor = backgroundColor;
            }
            if(drawFunction == null) {
                graphics.clear();
                if (_borderEnabled) {
                    graphics.lineStyle(1, borderColor, borderAlpha);
                }
                if (_backgroundEnabled) {
                    graphics.beginFill(baseColor, backgroundAlpha);
                }
                graphics.drawRect(0, 0, _width, _height);
                if (_backgroundEnabled) {
                    graphics.endFill();
                }
            } else {
                drawFunction(this);
            }
        }

        public function get backgroundColor():uint {
            return _backgroundColor;
        }

        public function set backgroundColor(value:uint):void {
            _backgroundColor = value;
            _backgroundEnabled = true;
            redrawOnNextFrame = true;
        }

        public function get backgroundAlpha():Number {
            return _backgroundAlpha;
        }

        public function set backgroundAlpha(value:Number):void {
            _backgroundAlpha = value;
            _backgroundEnabled = true;
            redrawOnNextFrame = true;
        }

        public function get borderColor():uint {
            return _borderColor;
        }

        public function set borderColor(value:uint):void {
            _borderColor = value;
            _borderEnabled = true;
            redrawOnNextFrame = true;
        }

        public function get borderAlpha():Number {
            return _borderAlpha;
        }

        public function set borderAlpha(value:Number):void {
            _borderAlpha = value;
            _borderEnabled = true;
            redrawOnNextFrame = true;
        }

        protected function get redrawOnNextFrame():Boolean {
            return _redrawOnNextFrame;
        }

        protected function set redrawOnNextFrame(value:Boolean):void {
            _redrawOnNextFrame = value;
            draw();
        }

        public function setTemporaryTint(color:uint, duration:int = 8):void {
            if(!hasEventListener(Event.ENTER_FRAME)) {
                _tintDuration = duration;
                draw(color);
                addEventListener(Event.ENTER_FRAME, checkTintDuration);
            }
        }

        private function checkTintDuration(event:Event):void {
            if(_tintDuration > 0) {
                _tintDuration--;
            } else {
                draw();
                removeEventListener(Event.ENTER_FRAME, checkTintDuration);
            }
        }
    }
}