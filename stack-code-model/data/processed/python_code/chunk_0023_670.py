package com.sixfootsoftware.pitstop {
    public class PlayerPitstopCalculator implements Calculator {
	
        private var pitstop:Number = 0;
        private var lastPitstop:Number = 0;

        public function calculatePitstop( elapsed:Number ):void {
			pitstop = int( elapsed / 10 );
        }

        public function getCalculatorResult():Number {
            lastPitstop = pitstop;
            return pitstop;
        }

        public function updated():Boolean {
            return lastPitstop != pitstop;
        }
    }
}