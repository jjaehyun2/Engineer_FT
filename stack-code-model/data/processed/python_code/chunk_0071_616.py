/**
 * Created by vizoli on 4/8/16.
 */
package ageofai.game.event
{
    import flash.events.Event;

    public class GameEvent extends Event
    {
        public static const INIT_GAME:String = "GameEvent.initGame";
        public static const TICK:String = "GameEvent.tick";

        public function GameEvent( type:String, bubbles:Boolean = false, cancelable:Boolean = false )
        {
            super( type, bubbles, cancelable );
        }

        public override function clone():Event
        {
            var event:GameEvent = new GameEvent( type );

            return event;
        }
    }
}