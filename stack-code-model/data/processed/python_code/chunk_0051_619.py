package elements {
    import flash.utils.*;
    import elements.BaseClip;

    public class FootBot extends BaseClip {
        private var animation;
        private var interval;
        private var explosion;
        public var health = 100;

        public function FootBot(newX:Number, newY:Number, walking:Boolean = true) {
            x = newX;
            y = newY;

            animation = addChild(new FootBot_walk());
            animation.stop();
            if (walking){
                walk();
            }
        }

        private function walk(){
            animation.play();
            interval = setInterval(function(){
                x += 25;
                var event_out = new CustomEvent(CustomEvent.ON_MOVE);
                //event_out.x = x;
                //event_out.y = y;
                dispatchEvent(event_out);
            }, 167);
        }

        public function beginDeath(){
            clearInterval(interval);
            animation.stop();
            
            explosion = addChild(new Explosion());
            removeChild(animation);
            dispatchEvent(new CustomEvent(CustomEvent.ON_DIE));
        }

        public function handler_ON_SHOOT(event){
            if(event.x == x){
                health -= 25;
                //trace(health);
                if(health <= 0){
                    beginDeath();
                }
            }
        }

        public function doDie(callback) {
            setTimeout(callback, 500);
        }
    }
}