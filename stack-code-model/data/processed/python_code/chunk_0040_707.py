/**
 * Copyright arithma ( http://wonderfl.net/user/arithma )
 * MIT License ( http://www.opensource.org/licenses/mit-license.php )
 * Downloaded from: http://wonderfl.net/c/uFjq
 */

package 
{
    import flash.display.MovieClip;
    import flash.display.Sprite;
    import flash.events.Event;
    import flash.geom.Point;
    
    /**
     * ...
     * @author ...
     */
    public class Main extends Sprite 
    {
        public const N:int = 400;
        public var points:Array;
        
        public function Main():void 
        {
            if (stage) init();
            else addEventListener(Event.ADDED_TO_STAGE, init);
        }
        
        private function init(e:Event = null):void 
        {
            removeEventListener(Event.ADDED_TO_STAGE, init);
            // entry point
            
            points = new Array();
            
            for (var i:int = 0; i < N; i++) {
                var arrw:MovieClip = new MovieClip();
                arrw.x = Math.random() * stage.stageWidth;
                arrw.y = Math.random() * stage.stageHeight;
                arrw.graphics.beginFill(Math.random() * 0xFFFFFF);
                arrw.graphics.moveTo( -Math.sin(Math.PI / 10)*10, (.5 - Math.cos(Math.PI / 10)) * 10);
                arrw.graphics.lineTo( +Math.sin(Math.PI / 10)*10, (.5 - Math.cos(Math.PI / 10)) * 10);
                arrw.graphics.lineTo( 0, .5 * 10);
                arrw.graphics.endFill();
                arrw.rotation = Math.atan2(arrw.vy, arrw.vx) * 180 / Math.PI - 90;
                addChild(arrw);
                points.push(arrw);
            }
            
            addEventListener(Event.ENTER_FRAME, frame);
        }
        
        private function frame(e:Event = null):void {
            for each(var arrw:MovieClip in points) {
                var vx:Number = 0;
                var vy:Number = 0;
                for each(var other:MovieClip in points) {
                    if (other != arrw) {
                        var dist2:Number =    (arrw.x - other.x) * (arrw.x - other.x) +
                                            (arrw.y - other.y) * (arrw.y - other.y);
                                            
                        var dist:Number = Math.sqrt(dist2);
                        vx += 1 * (Math.exp(-dist*.05)) * (other.x - arrw.x) / dist;
                        vy += 1 * (Math.exp(-dist*.05)) * (other.y - arrw.y) / dist;
                        
                        vx += -20 * (Math.exp(-dist2*.005)) * (other.x - arrw.x) / dist;
                        vy += -20 * (Math.exp(-dist2*.005)) * (other.y - arrw.y) / dist;
                        
                        vx -= .15 * (Math.exp( -dist2 * .001)) * (other.y - arrw.y);
                        vy += .15 * (Math.exp( -dist2 * .001)) * (other.x - arrw.x);
                    }
                }
                arrw.x += vx;
                arrw.y += vy;
                arrw.rotation = Math.atan2(vy, vx) * 180 / Math.PI - 90;
            }
        }
        
    }
    
}