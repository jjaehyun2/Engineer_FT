package com.finegamedesign.subtletea
{
    public class Model
    {
        internal static var levelScores:Array = [];
        internal static var score:int = 0;

        internal var highScore:int;
        internal var level:int;
        internal var levelScore:int = 0;
        internal var selected:Object = {x: -1, y: -1};
        internal var target:Object = {x: -1, y: -1, alpha: 1.0};
        internal var trial:int = 0;
        internal var trialMax:int = 10;
        private var bounds:Object = {
            topLeft: {x: 0, y: 0},
            bottomRight: {x: 100, y: 100}};
        private var distance:int;
        private var now:int;
        private var complete:Boolean;
        private var elapsed:Number;
        private var milliseconds:int;
        private var previousTime:int;
        private var populateTime:int;
        private var startTime:int;
        private var waitTime:int;

        public function Model()
        {
            score = 0;
            highScore = 0;
            levelScores = [];
        }

        internal function setBounds(rectangle:Object, targetRectangle:Object, margin:int = 20):void
        {
            bounds.topLeft.x = Math.ceil(rectangle.topLeft.x + targetRectangle.width + margin);
            bounds.topLeft.y = Math.ceil(rectangle.topLeft.y + targetRectangle.height + margin);
            bounds.bottomRight.x = Math.floor(rectangle.bottomRight.x - targetRectangle.width - margin);
            bounds.bottomRight.y = Math.floor(rectangle.bottomRight.y - targetRectangle.height - margin);
            
            bounds.width = bounds.bottomRight.x - bounds.topLeft.x;
            bounds.height = bounds.bottomRight.y - bounds.topLeft.y;
        }

        /**
         * Might be nice to shuffle bins and roll jitter in bin.
         */
        private static function randomlyPlace(target:Object, bounds:Object):void
        {
            target.x = Math.round(Math.random() * bounds.width + bounds.topLeft.x);
            target.y = Math.round(Math.random() * bounds.height + bounds.topLeft.y);
        }

        internal function populate(level:int):void
        {
            complete = trialMax <= trial;
            if (!complete) {
                this.level = level;
                if (null == levelScores[level]) {
                    levelScores[level] = 0;
                    levelScore = 0;
                }
                populateTime = now;
                waitTime = -1;
                startTime = -1;
                trial++;
            }
        }

        private function mayPlaceNow():void
        {
            if (-1 == startTime) {
                if (-1 == waitTime) {
                    var waitMin:int = 1000;
                    var waitMax:int = 8000;
                    waitTime = (waitMax - waitMin) * Math.random() + waitMin;
                }
                var wait:int = now - populateTime;
                if (waitTime <= wait) {
                    randomlyPlace(target, bounds);
                    startTime = now;
                }
                else {
                    clear();
                }
            }
        }

        internal function clear():void
        {
            target.x = -bounds.topLeft.x;
            target.y = bounds.topLeft.y;
            target.alpha = 0.0;
        }

        internal function update(now:int):int
        {
            previousTime = 0 <= this.now ? this.now : now;
            this.now = now;
            elapsed = this.now - previousTime;
            levelScore += judge();
            mayPlaceNow();
            milliseconds = now - startTime;
            target.alpha = updateOpacity();
            updateScore();
            return win();
        }

        /**
         * Fade in:  Slow at high level and high trial.
         */
        private function updateOpacity():Number
        {
            var perMillisecond:Number = 0.01;
            perMillisecond /= level * level * level;
            perMillisecond /= trial;
            var opacity:Number = milliseconds * perMillisecond;
            opacity = Math.min(1.0, opacity);
            return opacity;
        }

        internal function judge():int
        {
            var points:int = 0;
            if (0 <= selected.x) {
                var max:int = 100;
                var perDistance:Number = -1.0;
                distance = getDistance(selected, target);
                points = Math.round(0.5 * max + distance * perDistance);

                var perMillisecond:Number = -0.01;
                points += Math.round(0.5 * max + milliseconds * perMillisecond);
                points *= level;
                points = Math.max(0, points);
                selected.x = -1;
                selected.y = -1;
                populate(level);
            }
            return points;
        }

        internal function select(x:int, y:int):void
        {
            selected.x = x;
            selected.y = y;
            trace("Model.select: " + x + ", " + y);
        }

        internal static function getDistance(pointA:Object, pointB:Object):Number
        {
            return Math.pow(pointA.x - pointB.x, 2)
                 + Math.pow(pointA.y - pointB.y, 2);
        }

        /**
         * @return  0 continue, 1: win, -1: lose.
         */
        private function win():int
        {
            var winning:int = 0;
            if (complete) {
                winning = 1;
            }
            return winning;
        }

        private function updateScore():int
        {
            if (levelScores[level] < levelScore) {
                levelScores[level] = levelScore;
            }
            var sum:int = 0;
            for each (var n:int in levelScores) {
                sum += n;
            }
            score = sum;
            return sum;
        }
    }
}