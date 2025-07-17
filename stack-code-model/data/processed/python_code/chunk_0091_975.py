package com.sixfootsoftware.pitstop {

    import org.flixel.FlxSprite;

    public class Car extends FlxSprite {

        private var precedes:Vector.<Car> = new Vector.<Car>();
        private var occupied:Boolean = false;

        public function Car() {
            super(0, 289);
            this.loadGraphic(AssetRegistry.PitStop, true, false, 959, 216);
            this.addAnimation("1", [14], 1, false);
            this.addAnimation("2", [12], 1, false);
            this.addAnimation("3", [10], 1, false);
            this.addAnimation("4", [1], 1, false);
            this.addAnimation("5", [4], 1, false);
            this.addAnimation("6", [2], 1, false);
            this.addAnimation("7", [0], 1, false);
            this.addAnimation("8", [6], 1, false);
            this.kill();
        }

        public function addSuccessor(car:Car):Car {
            precedes.push(car);
            return this;
        }

        public function setOccupied(occupied:Boolean):Car {
            this.occupied = occupied;
            if (occupied) {
                revive();
            } else {
                kill();
            }
            return this;
        }

        public function isOccupied():Boolean {
            return occupied;
        }

        public function canMove():Boolean {
            if (!occupied) {
                return false;
            }
            return !successorOccupied();
        }

        private function successorOccupied():Boolean {
            for each(var car:Car in precedes) {
                if (car.isOccupied()) {
                    return true;
                }
            }
            return false;
        }

        public function hasNoSuccessors():Boolean {
            return precedes.length == 0;
        }

        override public function preUpdate():void {
            super.preUpdate();
        }

        public function move():Boolean {
            if (precedes[precedes.length - 1].precedes.length > 0 && precedes[precedes.length - 1].precedes[0] is PitCar
                    && !precedes[precedes.length - 1].precedes[0].isOccupied()) {
                precedes[precedes.length - 1].setOccupied(true);
                this.setOccupied(false);
                return true;
            }
            var seed:int = 0;
            do {
                seed = int(Math.random() * precedes.length);
                if (!precedes[seed].isOccupied()) {
                    precedes[seed].setOccupied(true);
                    this.setOccupied(false);
                    break;
                }
            } while (true);
            return true;
        }
    }
}