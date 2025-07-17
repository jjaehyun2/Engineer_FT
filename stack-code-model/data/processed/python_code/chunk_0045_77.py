/**
 * Created with IntelliJ IDEA.
 * User: dvlg
 * Date: 28/06/13
 * Time: 15:34
 * To change this template use File | Settings | File Templates.
 */
package com.sixfootsoftware.pitstop {
    import com.sixfootsoftware.engine.RefreshTimer;

    import org.flixel.FlxGroup;

    public class DemoControl extends FlxGroup {

        private var car:PitCar;
        private var leftArrowDisplay:LeftArrowDisplay = new LeftArrowDisplay();
        private var rightArrowDisplay:RightArrowDisplay = new RightArrowDisplay();
        private var refreshTimer:RefreshTimer = new RefreshTimer(500, 500);

        public function DemoControl() {
            add(leftArrowDisplay);
            add(rightArrowDisplay);
            kill();
        }

        public function setPitGridCar(car:PitCar):void {
            this.car = car;
        }

        override public function revive():void {
            callAll("revive");
            super.revive();
        }

        private function release():void {
            if ( !car.isWheelDone() && refreshTimer.isReadyForUpdate() ) {
                if ( !car.isWheelOff() ) {
                    car.loosenWheel();
                }
                if ( !car.isWheelOn() ) {
                    car.tightenWheel();
                }
            }
            if ( car.isOccupied() && car.isWheelDone() ) {
                car.release();
            }
        }

        override public function update():void {
            release();
            super.preUpdate();
        }
    }

}